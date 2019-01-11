# Public key recovery

__PROBLEM__

```
-----BEGIN RSA PRIVATE KEY-----
MIICXgIBAAKBgQDwkrxVrZ+KCl1cX27SHDI7EfgnFJZ0qTHUD6uEeSoZsiVkcu0/
XOPbz1RtpK7xxpKMSnH6uDc5On1IEw3A127wW4Y3Lqqwcuhgypd3Sf/bH3z4tC25
eqr5gA1sCwSaEw+yBxdnElBNOXxOQsST7aZGDyIUtmpouI1IXqxjrDx2SQIDAQAB
AoGBAOwd6PFitnpiz90w4XEhMX/elCOvRjh8M6bCNoKP9W1A9whO8GJHRnDgXio6
/2XXktBU5OfCVJk7uei6or4J9BvXRxQpn1GvOYRwwQa9E54GS0Yu1XxTPtnBlqKZ
KRbmVNpv7eZyZfYG+V+/f53cgu6M4U3SE+9VTlggfZ8iSqGBAkEA/XvFz7Nb7mIC
qzQpNmpKeN4PBVRJBXqHTj0FcqQ5POZTX6scgE3LrxVKSICmm6ungenPXQrdEQ27
yNQsfASFGQJBAPL2JsjakvTVUIe2JyP99CxF5WuK2e0y6N2sU3n9t0lde9DRFs1r
mhbIyIGZ0fIkuwZSOqVGb0K4W1KWypCd8LECQQCRKIIc8R9iIepZVGONb8z57mA3
sw6l/obhfPxTrEvC3js8e+a0atiLiOujHVlLqD8inFxNcd0q2OyCk05uLsBxAkEA
vWkRC3z7HExAn8xt7y1Ickt7c7+n7bfGuyphWbVmcpeis0SOVk8QrbqSNhdJCVGB
TIhGmBq1GnrHFzffa6b1wQJAR7d8hFRtp7uFx5GFFEpFIJvs/SlnXPvOIBmzBvjU
yGglag8za2A8ArHZwA1jXcFPawuJEmeZWo+5/MWp0j+yzQ==
-----END RSA PRIVATE KEY-----
```

__SOLUTION__

So we are given a Private key. We can simply generate Public key from the given private key using openssl.

Just save the given private key in a file called `id_rsa` and run the following command:

```bash
➜ openssl rsa -in id_rsa -pubout
writing RSA key
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDwkrxVrZ+KCl1cX27SHDI7Efgn
FJZ0qTHUD6uEeSoZsiVkcu0/XOPbz1RtpK7xxpKMSnH6uDc5On1IEw3A127wW4Y3
Lqqwcuhgypd3Sf/bH3z4tC25eqr5gA1sCwSaEw+yBxdnElBNOXxOQsST7aZGDyIU
tmpouI1IXqxjrDx2SQIDAQAB
-----END PUBLIC KEY-----
```

Now we have the public key but in question it ask for md5 of the key. This caused me a bit of problem. If you'll try to give the above key to any md5 generator as it is then you won't get the right md5 hash. Instead you have to give it in form of a single string i.e without any `\n`(newline character).

```python
import hashlib
>>> s  = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDwkrxVrZ+KCl1cX27SHDI7EfgnFJZ0qTHUD6uEeSoZsiVkcu0/XOPbz1RtpK7xxpKMSnH6uDc5On1IEw3A127wW4Y3Lqqwcuhgypd3Sf/bH3z4tC25eqr5gA1sCwSaEw+yBxdnElBNOXxOQ sST7aZGDyIUtmpouI1IXqxjrDx2SQIDAQAB"

>>> hashlib.md5(s.encode('utf-8')).hexdigest()
'42f51df8b6a2bafa824c179a38066e5d'
```

Submitting the md5 will give you the flag.

FLAG - `FLAG-9869O2dQ43d1r116kfD0Sj5n`
