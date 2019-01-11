# Dinosaure Survive

__SOLUTION__

We are given a random file. So first thing I did was
```bash
➜ file 0b02119984a7cee0ba83d55425b9491f.E01
0b02119984a7cee0ba83d55425b9491f.E01: EWF/Expert Witness/EnCase image file format
```
Doesn't tell anything or I should say anything that I am aware about. So I tried to extract everything that I could from the given file.

```
➜ binwalk -e 0b02119984a7cee0ba83d55425b9491f.E01
```

This will give us lot of files. So I searched in those extracted files.

```
➜ grep -i flag *
Binary file 601FD matches
Binary file DB405 matches
Binary file DD3F1 matches
```

There are 3 files that may have some `flag` string in them. So let's start with the bottom one
```
➜ xxd DD3F1 | grep flag

00000e20: 666c 6167 2d36 6239 3665 3231 3262 3366  flag-6b96e212b3f
00002d50: 666c 6167 2d36 6239 3665 3231 3262 3366  flag-6b96e212b3f
00002dc0: 2e00 7400 7800 7400 666c 6167 2d36 6239  ..t.x.t.flag-6b9
```

this doesn't give us the whole flag but to view the whole flag I did `xxd DD3F1` and manually copied the flag.

FLAG - `flag-6b96e212b3f85968db654f7892f06122`

