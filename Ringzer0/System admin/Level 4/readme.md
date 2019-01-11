# SysAdmin part 4

__PROBLEM__

Get access to the oracle account.

User: morpheus
Password: VNZDDLq2x9qXCzVdABbR1HOtz

ssh morpheus@challenges.ringzer0team.com -p 10146

__SOLUTION__

This we need access to oracle's account. I started with normal grep like `grep 'oracle' -R /` which gave permission denied and stuff so I did `grep 'oracle' -R / 2>/dev/null`. This will also give you lot of outputs but you'll notice in the end
```bash
....
/usr/lib/x86_64-linux-gnu/perl/5.22/DB_File.pm:The official web site for Berkeley DB is F<http://www.oracle.com/technology/products/berkeley-db/db/index.html>.
/usr/lib/x86_64-linux-gnu/perl/5.22/DB_File.pm:F<http://www.oracle.com/technology/products/berkeley-db/db/index.html>) regarding the license:
/usr/lib/x86_64-linux-gnu/perl/5.22.1/DB_File.pm:The official web site for Berkeley DB is F<http://www.oracle.com/technology/products/berkeley-db/db/index.html>.
/usr/lib/x86_64-linux-gnu/perl/5.22.1/DB_File.pm:F<http://www.oracle.com/technology/products/berkeley-db/db/index.html>) regarding the license:
Binary file /backup/c074fa6ec17bb35e168366c43cf4cd19 matches
Binary file /bin/udevadm matches
Binary file /bin/systemd matches
```

And if you'll do `cat /backup/c074fa6ec17bb35e168366c43cf4cd19` again you will get lot's of output but you'll notice a RSA private key in there.
```
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAqBIMY0jPs4dvQqsyHreYccCOIMFrBy+el5Td8TNc8pQqINNr
WSefxANe4b0EaAZofvZbBGrHipyB6X+FgugXYqwB0uem06uTGnIdHAZyHV6IE9f/
hLCm+9nWOJfUvPNFbMaIizvzMVhO6GTGyxJ8zh/ASQXYBHSzyOxkmqDLB7zFteyJ
F7hv6s6W20TmpjhMQtOC0mYwn64ZCsVi2d1c7tFiw37cOutT1LfZaaAUBIwdpvL6
BFjqpNkxzwm105eFTDt4WZNKOZ9nOns18MHBHFOXk8WgAxC6gqtE2gr7cTBZsbwv
jXrte8oTtAWCv3YHSECH91NzE3DKVktCwr1bjQIDAQABAoIBAQCdefu9c1WZY4bu
MrYNbf0aaE9Dhbcgzo+Me+HQxE2MxSMMCsyEhsn9wSK/5Hkidw6mF3KEmwBIcgiP
nfqdA5YV0BENahw4LITyvIVl4uw9dHuQDEzQKSzswdkkwa6FNHOSThtWSl+9ln6o
5PQXBkWGZN2oDh+vXSGvWz+QWqSho8vufmTtYntfFPAfVfcyp8BtiUgKQh069uGg
XKnehmkrHoW9gQ2Lo0uaFWcTIGm1vsgBd7L4cfb98jDB63H+Lhf4UPYv4WmH2rrj
bnk5lAU71JK4QsPnnOx1PA685p2e5mEfh0LKRKq9Fx3+umbGPJGvgcjobtXaW9OT
mpaz6ZPBAoGBAM+diN8s/osQdi8odS9+HUWVZBa9Z2Dn0X2IlSxWK9u/UclhjYgP
i2KXEY0wRV+ZiXURmrFNVxgA/EJ9BOgptSZNmi9fEdfnVB4L11T7HFny/J8u3sXt
dn0OqHmf5ZEPtV7m0bK0jtznTgTTuBI9yXvRgHO2HQPCshdP7GIgt++lAoGBAM89
Pd7HyMYnh0ancCTICkVIIWF6Ylf20BKz4Zwy9tYASCxY3iFllBdOXw/UgCnmJseQ
73Dcimi5OEyUckOp7xX4HTwidFVbxfNeC0ZfsPbd22qSDcw5orpQMoDy3iP+bPJh
SgwtusqotGjm0jTpnhqRV5x6rchzkMYwF8/WkvfJAoGBAMeem6yh0XiaclfzWYE5
jCGMezjWEeD949IEkhGYJQFbmeK79l49O/KmeAy9veYmdSDntUoGp9f/kozHMgGb
oH5cnQQxL7HczWc6UWd3LhJabIUNhsreAFBL2Ldgg1UPun6uBjACJV7G06AWhWSc
ne58SDp5frpP5/Y8NXdAKDq1AoGAYCSFQ4lj96n29CxRtn6nZSTld5eTcEOsnECf
dhuesAFJemlwBAZgAb/2Eh3/p3CCpSr0KmPmQldLaxujNwjrRkHpLjC9z6vX1ePX
TzqtmpmqZXKEvC4w9EaoZ3JE5GXwnTHNbID6m3JQ4CnVc36+Po0XHB096jTTAV7m
bSGa5SECgYBE2IuW1pk2pOZ+FDtKltWHk8KK89QmGsFf2YnVZ/FsAkPnayeTkmMz
AWxRP/W/Uj5ypw7KjprQee31hkisBG/ZPBvQdjAvxF7m4usuEN2Nkb0FTIjZHYbD
iPOmPHIUlwwL8UVzDQUzXhegSB4GUeP/06T/eM5PPB8SX0ZaHIw1wQ==
-----END RSA PRIVATE KEY-----
```

Put it in a file and do the `chmod 600 file`. Basically this is private key for oracle's account and using this key we will ssh in his account.

Now disconnect from the server and connect again using following command:
```bash
ssh oracle@challenges.ringzer0team.com -p 10146 -i keyz
```

Here `keyz` is the name of the file which holds the private key. Also do not forget to `chmod` the file before using it or else you'll get error.

Now we are in oracle's account:

```bash
Last login: Thu Jan 10 22:11:20 2019 from 77.87.48.26
oracle@lxc-sysadmin:~$ ls
encflag.txt.enc  flag.txt
oracle@lxc-sysadmin:~$ cat flag.txt
RkxBRy1kMzI1ZTczOGZhN2Q4N2Q0ZjU2MDdjMzAyYjM3ZGIyMA==
oracle@lxc-sysadmin:~$ echo "RkxBRy1kMzI1ZTczOGZhN2Q4N2Q0ZjU2MDdjMzAyYjM3ZGIyMA==" | base64 -d
FLAG-d325e738fa7d87d4f5607c302b37db20oracle@lxc-sysadmin:~$
```

FLAG - `FLAG-d325e738fa7d87d4f5607c302b37db20`
