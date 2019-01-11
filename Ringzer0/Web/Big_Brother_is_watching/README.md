# Big Brother is watching

__PROBLEM__

```
 Even Google cannot find this one
```

__SOLUTION__

Since it says that `Google cannot find this one`, it will have something to do with `Robots.txt` file because that is the file used by "Websites" to disallow specific URL to be crawled by.

So we head over to `https://ringzer0ctf.com/robots.txt` and finds out that
```
User-agent: *
Disallow: /16bfff59f7e8343a2643bdc2ee76b2dc/
```

There is a specific URL that is disallowed.
When we visit that URL(`https://ringzer0ctf.com//16bfff59f7e8343a2643bdc2ee76b2dc/`) we see

```
FLAG-G5swO95w0c7R5fq0sa85nVs5dK49O04i
```

