# Words mean something?

__PROBLEM__

```
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam commodo risus lobortis diam molestie, varius vestibulum lacus condimentum. Phasellus fringilla, leo at ornare tristique, est elit lobortis dolor, a placerat tortor eros nec elit. Suspendisse feugiat, enim ac hendrerit malesuada, libero lectus rutrum tellus, ut faucibus sem odio non nunc. Vestibulum dignissim magna et felis laoreet viverra. Integer sodales tellus molestie suscipit feugiat. Praesent quis elit tristique nisl laoreet elementum eu nec felis. Fusce nunc enim, rhoncus at metus sed, accumsan accumsan augue. Nunc venenatis tempor mi sit amet tempus. Maecenas luctus lacus mi, id pretium magna feugiat eu. Aenean euismod ante at neque rhoncus, eget dapibus nisi lacinia. Aenean vulputate risus id velit interdum vulputate. Mauris id rhoncus dolor.
```

__SOLUTION__

No words doesn't mean anything. It's there for just umm nothing.

Start with checking out the `HEADERS` of the `REQUEST` and you'll see
```
Host: ringzer0ctf.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://ringzer0ctf.com/challenges
Connection: keep-alive
Cookie: flag=0; PHPSESSID=ngh45r2bqkhpgjjbhbshbvoc76
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
TE: Trailers
```

There is a `flag=0`. Just change it to `flag=1`. So now your request will look like

```
Host: ringzer0ctf.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://ringzer0ctf.com/challenges
Connection: keep-alive
Cookie: flag=1; PHPSESSID=ngh45r2bqkhpgjjbhbshbvoc76
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0, no-cache
TE: Trailers
Pragma: no-cache
```

And it will return you the flag.

FLAG - `FLAG-AnlAb6QxDpQvg1yn2bAhyOJw`
