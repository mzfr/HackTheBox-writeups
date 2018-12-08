# Meat Loaf

__PROBLEM__

RingZer0 Team delicious meat loaf.

This is the official RingZer0 Team meat loaf recipe.

Ingredients.
111 tablespoons lard
19 g ripe tomatoes
104 teaspoons tomato sauce
73 g beans
87 eggs
59 g dijon mustard
97 potatoes
84 ml aberlour single malt
110 g bananas
10 g chopped olives
100 ml water
7 ml vanilla extract
117 cups oil
curcuma
salt
ground pepper
116 g goat cheese
108 pickles
13 teaspoons sugar

Cooking time: 3 hours.

Method.
Put goat cheese into the mixing bowl.
Put potatoes into the mixing bowl.
Put dijon mustard into the 2nd mixing bowl.
Add chopped olives to the 2nd mixing bowl.
Fold chopped olives into the 2nd mixing bowl.
Put chopped olives into the mixing bowl.
Clean the 2nd mixing bowl.
Put goat cheese into the mixing bowl.
Put bananas into the mixing bowl.
Put water into the mixing bowl.
Put pickles into the mixing bowl.
Put oil into the mixing bowl.
Put lard into the mixing bowl.
Put eggs into the mixing bowl.
Put beans into the mixing bowl.
Put aberlour single malt into the mixing bowl.
Put goat cheese into the 2nd mixing bowl.
Put aberlour single malt into the 2nd mixing bowl.
Add sugar to the 2nd mixing bowl.
Put tomato sauce into the 2nd mixing bowl.
Liquefy contents of the 2nd mixing bowl.
Pour contents of the 2nd mixing bowl into the 3rd baking dish.
Stir for 15 minutes.
Liquefy contents of the mixing bowl.
Pour contents of the mixing bowl into the baking dish.
Refrigerate for 3 hours.

__SOLUTION__

At first look it seemed okay to me and I thought those numbers in ingredient is our key so I did

```python
>>> d = [111,19,104,73,87,59,97,84,110,10,100,7,117,116,108,13]

>>> for i in d:
       print(chr(i))
```
But I got some random strings. So after googling I found out that there is actually a programming language called [`chef`](https://esolangs.org/wiki/chef)

This is really funny though. Then I use an [interpreter](https://metacpan.org/release/WERNERMP/Acme-Chef-1.03) to run the code

```perl
use Acme::Chef;

open my $fh, '<', "recipe.txt";
read $fh, my $code_string, -s $fh;
close $fh;

my $compiled = Acme::Chef->compile($code_string);
print $compiled->execute();
```

```bash
➜ perl chef.pl
IWouldntEatThat
```

FLAG - `IWouldntEatThat`
