# Hide my ass in my home

__SOLUTION__

After extracting we get lots of file. so first thing to start with
```bash
➜ grep -i flag .*
grep: .gnome2: Is a directory
Binary file .me.swp matches
grep: .mozilla: Is a directory
```
So there is a binary file.
```bash
➜ cat .me.swp
b0VIM 7.2|�S
U3210#"! Utpad��������Flag-1s4g76jk89ffull of full and sunfull and i'm beautifull
```

FLAG - `Flag-1s4g76jk89f`
