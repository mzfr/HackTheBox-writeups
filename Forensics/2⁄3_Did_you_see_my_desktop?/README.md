# 2 / 3 Did you see my desktop?

__SOLUTION__

Again we have a random file and we'll play with grep.
Grep-ing the flag will again result in lots of matches and also trying out the old trick will show you the old password.

Okay so since problem says something about the desktop we try to grep `desktop`but again lots of matches. So I tried `desktop/flag` and nothing but doing
```bash
➜ strings 5bd2510a83e82d271b7bf7fa4e0970d1 | grep -i flag/desktop
Visited: flag@file:///C:/Users/flag/Desktop/F$L%25A%5EG-.txt
:2014030920140310: flag@file:///C:/Users/flag/Desktop/F$L%25A%5EG-5bd2510a83e82d271b7bf7fa4e0970d1.txt
:2014030920140310: flag@file:///C:/Users/flag/Desktop/F$L%25A%5EG-5bd2510a83e82d271b7bf7fa4e0970d1.txt
Visited: flag@file:///C:/Users/flag/Desktop/F$L%25A%5EG-5bd2510a83e82d271b7bf7fa4e0970d1.txt
file:///C:/Users/flag/Desktop/F$L%25A%5EG-5bd2510a83e82d271b7bf7fa4e0970d1.txt
Visited: flag@file:///C:/Users/flag/Desktop/F$L%25A%5EG-5bd2510a83e82d271b7bf7fa4e0970d1.txt
nVisited: flag@file:///C:/Users/flag/Desktop/F$L%25A%5EG-5bd2510a83e82d271b7bf7fa4e0970d1.txt
:2014030920140310: flag@file:///C:/Users/flag/Desktop/F$L%25A%5EG-.txt
Visited: flag@file:///C:/Users/flag/Desktop/F$L%25A%5EG-5bd2510a83e82d271b7bf7fa4e0970d1.txt
Visited: flag@file:///C:/Users/flag/Desktop/F$L%25A%5EG-5bd2510a83e82d271b7bf7fa4e0970d1.txt
```

FLAG - `FLAG-5bd2510a83e82d271b7bf7fa4e0970d1`

