# I made a dd of Agent Smith usb key

__SOLUTION__

It says something about `I'm sure it contain the matrix password! Can you find it? `. Now we could have dig into the file but since this is a 1 pointer. Ther first thing I tried `➜ xxd 86b265d37d1fc10b721a2accae04a60d | grep FLAG` and BOOM
```
0000a400: 464c 4147 2d67 676d 676b 3035 3039 360a  FLAG-ggmgk05096.
```

FLAG - `FLAG-ggmgk05096`
