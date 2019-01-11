# SysAdmin part 2

__PROBLEM__

Find architect password

User: morpheus
Password: VNZDDLq2x9qXCzVdABbR1HOtz

ssh morpheus@challenges.ringzer0team.com -p 10148

__SOLUTION__

So this time we have to find architect password. I tried to look more into `ps` but found nothing related to architect. So I got out of the `home/` directory and found other directories:
```bash
backup  bin  boot  dev  etc  home  lib  lib64  media  mnt  nohup.out  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```
First I tried `tmp` but nothing then I went to `etc/` and tried `grep -i arch *`, this command basically find the word `arch`, `-i` ignores the case meaning it will look for `arch` or `ARCH` and `*` meaning in every file. This command gives us:

```bash
morpheus@lxc-sysadmin:/etc$ grep -s -i arch *
deluser.conf:# exclude these filesystem types when searching for files of a user to backup
fstab:#//TheMAtrix/phone  /media/Matrix  cifs  username=architect,password=$(base64 -d "RkxBRy0yMzJmOTliNDE3OGJkYzdmZWY3ZWIxZjBmNzg4MzFmOQ=="),iocharset=utf8,sec=ntlm  0  0
group:challenger:x:1000:morpheus,trinity,architect,oracle,neo,cypher
group:architect:x:1003:
inputrc:# alternate mappings for "page up" and "page down" to search the history
inputrc:# "\e[5~": history-search-backward
inputrc:# "\e[6~": history-search-forward
mime.types:application/java-archive                     jar
mime.types:application/vnd.android.package-archive                                              apk
nanorc:## Do backwards searches by default.
nanorc:## Do case-sensitive searches by default.
nanorc:## Remember the used search/replace strings for the next session.
nanorc:## searches.  They cannot contain blank characters.  The former set must
nanorc:## Do extended regular expression searches by default.
passwd:architect:x:1002:1003::/home/architect:/bin/bash
securetty:# Chase Research AT/PCI-Fast serial card
services:search         2010/tcp        ndtp
services:asp            27374/tcp                       # Address Search Protocol
subgid:architect:231072:65536
subuid:architect:231072:65536
```

We see an interesting base64 string decode it and you'll have the password
```bash
➜ echo "RkxBRy0yMzJmOTliNDE3OGJkYzdmZWY3ZWIxZjBmNzg4MzFmOQ==" | base64 -d
FLAG-232f99b4178bdc7fef7eb1f0f78831f9
```

FLAG - `FLAG-232f99b4178bdc7fef7eb1f0f78831f9`
