# Hey Chuck where is the flag?

__SOLUTION__

We are given a `.pcap` file. So we open it in wireshark and search for string `chuck`, since we are asking chuck. I didn't found anything there so I decided to export all the `HTTP` objects from the given PCAP file. You cn do that by going in `File>Export Object>HTTP`.

I exported in a folder called `export`. Now I used a tool called `ripgrep`
```bash
➜ rg flag
askldj3lkj234.php
1:Hey this is a flag FLAG-GehFMsqCeNvof5szVpB2Dmjx

askldj3lkj234(1).php
1:Hey this is a flag FLAG-GehFMsqCeNvof5szVpB2Dmjx

```
FLAG - `FLAG-GehFMsqCeNvof5szVpB2Dmjx`
