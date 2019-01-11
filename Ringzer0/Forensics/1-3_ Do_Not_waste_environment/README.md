# 1 / 3 Do not waste the environment

__SOLUTION__

So again we have an unknown file. We again try `xxd` or `strings` along with `grep` but this time you'll notice that you are getting too many match which are not actually our flag.

So we try a new trick
```bash

➜ strings 5bd2510a83e82d271b7bf7fa4e0970d1 | grep -i "F L A G"
F l a g -=66d7724d872da91af56907aea0f6bfb8
F l a g -=66d7724d872da91af56907aea0f6bfb8
F l a g -=66d7724d872da91af56907aea0f6bfb8
F l a g -=66d7724d872da91af56907aea0f6bfb8
F l a g -=66d7724d872da91af56907aea0f6bfb8
F l a g - 66d772
F l a g -=66d7724d872da91af56907aea0f6bfb8
F l a g -=66d7724d872da91af56907aea0f6bfb8
F l a g -=66d7724d872da91af56907aea0f6bfb8
F l a g -=66d7724d872da91af56907aea0f6bfb8
F l a g -=66d7724d872da91af56907aea0f6bfb8
F l a g -=66d7724d872da91af56907aea0f6bfb8
F l a g -=66d7724d872da91af56907aea0f6bfb8
F l a g -=66d7724d872da91af56907aea0f6bfb8
```

FLAG - `Flag-66d7724d872da91af56907aea0f6bfb8`
