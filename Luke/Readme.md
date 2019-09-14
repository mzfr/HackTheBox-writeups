# Luke

<h1 align="center">
  <br>
  <a href="https://www.hackthebox.eu/home/machines/profile/190"><img src="images/img.png" alt="Luke"></a>
  <br>
</h1>

<h4 align="center"> Author: H4d3s</h4>

***

__Machine IP__: 10.10.10.137

__Starting On__: `Wed Jul 17 12:55:44 IST 2019`

***

## NMAP

![](images/nmap.png)

There are quite a few ports open. FTP allows anonymous login so I think it would be nice if we start with that.

***

## FTP

I logged into FTP and found a file name `for_Chihiro.txt` in a folder named `webapp`.

![](images/ftp.png)

and it had the following message

![](images/note.png)

Okay so this mean somewhere the source of the website is present.
Also now we know that there are two user `Chihiro` and `Derry`.

Let's move on to all the HTTP ports

***

## HTTP


#### Port 80

Website on the port 80 was pretty simple and there wasn't anything in the source of the page.

![](images/website-80.png)

I ran `dirsearch` on the website and found some directories:

![](images/dirsearch.png)

There wasn't anything interesting in any of those files except `config.php`

I found a username and password in config.php

![](images/config.png)

```php
$dbHost = 'localhost';
$dbUsername = 'root';
$dbPassword  = 'Zk6heYCyv6ZE9Xcg';
$db = "login";

$conn = new mysqli($dbHost, $dbUsername, $dbPassword,$db) or die("Connect failed: %s\n". $conn -> error);
```
I tried to use those logins on `/login.php` and `/management/` but it didn't work on any of those. So I decided to move on with the remaining two ports.

***

#### Port 8000

![](images/website-8000.png)

It's a login page. I didn't even knew what ajenti was so I googled it and found out

```
An admin's tool for a more civilized age, providing you with a fast and secure way to manage a remote Linux box at any time using everyday tools like a web terminal, text editor, file manager and others.
```

This could be `vulnerable` to something. So I used `searchsploit` and found an exploit for it.

![](images/searchsploit.png)

But since this exploit need a way to make directory I couldn't use it.

**Moving on to port `3000`**

***

#### Port 3000

![](images/website-3000.png)

It's an API which requires auth token. I decided to use the `password` I found in `config.php` and it gave 200 but still had a `Invalid token error`

![](images/invalid.png)

After reading some forum comments I realized I was doing it all wrong. The `Zk6heYCyv6ZE9Xcg` is not the token but the password. So that means I need to get token first using `Zk6heYCyv6ZE9Xcg` with some different username.

I read this [medium](https://medium.com/@nieldw/using-curl-to-authenticate-with-jwt-bearer-tokens-55b7fac506bd) article that showed me how to use `curl` for sending token and username etc.

Since I need to find more information through this API I decided to run `dirsearch` on it to see if I can find some directories that might give something away.

![](images/dir-3000.png)

So we can use `http://10.10.10.137:3000/login` to find our token but we still need to bruteforce the `username`. I started using all the username I've found till now but none of them worked.

![](images/failure.png)

But I got the token with `admin:Zk6heYCyv6ZE9Xcg`

![](images/token.png)

```json
{
  "success": true,
  "message": "Authentication successful!",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiaWF0IjoxNTYzMzUzNTA3LCJleHAiOjE1NjM0Mzk5MDd9.6KHbS8q0UbOyMbIdR2974jzztEUf-kdYeHQtz-4_Rg0"
}
```

I assigned the token to a variable in my shell so I don't have to paste long stuff again and again.

![](images/assign.png)

Now we can look into all the directories we found on this port.

On `/users` I got a some users with their ID along with their roles.

![](images/users.png)

```json
[
  {
    "ID": "1",
    "name": "Admin",
    "Role": "Superuser"
  },
  {
    "ID": "2",
    "name": "Derry",
    "Role": "Web Admin"
  },
  {
    "ID": "3",
    "name": "Yuri",
    "Role": "Beta Tester"
  },
  {
    "ID": "4",
    "name": "Dory",
    "Role": "Supporter"
  }
]
```
and on `users/admin` I got some credentials.

![](images/admin-pass.png)

```json
{
  "name": "Admin",
  "password": "WX5b7)>/rp$U)FW"
}
```

So till now We have 3 portal to try these credentials on.

*  Port 80 - `/login`
*  Port 80 - `/management/`
*  Port 8000 - `/`

I tried those credentials but none of them worked. So after thinking a bit I realized something. When we visted the `users/Admin` we got password for `Admin` but what if we try other user names maybe we can get password for them as well.

![](images/passwords.png)

```bash
➜ http http://10.10.10.137:3000/users/Derry $TOKEN | jq .
{
  "name": "Derry",
  "password": "rZ86wwLvx7jUxtch"
}

~
➜ http http://10.10.10.137:3000/users/Dory $TOKEN | jq .
{
  "name": "Dory",
  "password": "5y:!xa=ybfe)/QD"
}

~
➜ http http://10.10.10.137:3000/users/Yuri $TOKEN | jq .
{
  "name": "Yuri",
  "password": "bet@tester87"
}
```

🎉🎉🎉🎉🎉🎉

Now we can use `Derry's` credential because he's the `Web Admin`.

First I visted the `management/` and got some different page URLs

![](images/management.png)

If we open the `config.json` we can see some information related to `ajenti` running on port `8000`

![](images/config-json.png)

We can see credentials `root:KpMasng6S5EtTy9Z`. We can use these on the port `8000` to login.

***

I logged in on http://10.10.10.137:8000/ using the `root:KpMasng6S5EtTy9Z` and got a simple dashboard.

![](images/dashboard.png)


In the lower left side we can see option for `Terminal` click on it and make a new terminal.

When I ran the `whomai` command I was screaming like a crazy person.

![](images/whoami.png)

Now we can just get user and root hash 😜😜😜

![](images/user-root.png)

***

It was kinda good box not too difficult but neither too easy. I really liked the API usage part.

Thanks to H4d3s for making this box.

***
Thanks for reading, Feedback is always appreciated.

Follow me [@0xmzfr](https://twitter.com/0xmzfr) for more “Writeups”.
