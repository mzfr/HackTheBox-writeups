# File Recovery

__PROBLEM__

We are given an archive.

__SOLUTION__

After unzip the archive we find a directory called [`flag`](flag/) a [`private.pem`](flag/private.pem) and [`flag.enc`](flag/flag.enc).

So basically this a simple RSA problem. Actually there is no problem, to decrypt any encrypted message/file all we neew is the private key which is given to us.

So we can decrypt it using a program called openssl.
```bash
➜ openssl rsautl -decrypt -in flag.enc -out plain.txt -inkey private.pem
```

This will give you a file called [`plain.txt`](flag/plain.txt)

FLAG - `FLAG-vOAM5ZcReMNzJqOfxLauakHx`
