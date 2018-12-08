# Encrypted Zip

__PROBLEM__

wierd.zip and flag.zip apparently have the same password. We also found a unzipped version of wierd.txt

__SOLUTION__

I used [fcrackzip](https://github.com/hyc/fcrackzip) along with our lovely [`rockyou.txt`](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=2ahUKEwjjqPK-v5DfAhXaWysKHTBXB-gQFjAAegQIBxAB&url=https%3A%2F%2Fgithub.com%2Fbrannondorsey%2Fnaive-hashcat%2Freleases%2Fdownload%2Fdata%2Frockyou.txt&usg=AOvVaw3snAERl1mU6Ccr4WFEazBd). It took around a second to crack the password.

password was `testtest`.

Using that password you can extract the `flag.zip` file and you'll have it.

FLAG - `FLAG-Mk5N1z6PDbcw6alA1G8ixz85`
