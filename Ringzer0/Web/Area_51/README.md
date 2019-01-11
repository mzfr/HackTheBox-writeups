# Area 51

__SOLUTION__

So when you load the challenge page you get

```
Access to this area is restricted using some secure .htaccess
```

So basically `.htaccess` is a fie used to change server configuration in apache. No problem !!

I Start with looking into the headers and found nothing fishy. So I try to change the `Request method`.
First I changed `GET` to `POST` but nothing and then I tried `PUT` and Boom

```
 AREA 51 The origin of the Area 51 name is unclear? Alien?
 FLAG-w4KRr557y626izv567758O52
```

FLAG - `FLAG-w4KRr557y626izv567758O52`

P.S - You can check out headers in `Networks` tab in `developers tool` of your browser.
