#  PHP Fairy

__SOLUTION__

We are given a form and we don't have the password. Let's start with inspecting the source.

```php
<?php
$output = "";
if (isset($_GET['code'])) {
  $content = file_get_contents(__FILE__);
  $content = preg_replace('/FLAG\-[0-9a-zA-Z_?!.,]+/i', 'FLAG-XXXXXXXXXXXXXXXXXXXXXXX', $content);
  echo '<div class="code-highlight">';
  highlight_string($content);
  echo '</div>';
}

if (isset($_GET['pass'])) {
  if(!preg_match('/^[^\W_]+$/', $_GET['pass'])) {
    $output = "Don't hack me please :(";
  } else {

    $pass = md5("admin1674227342");
    if ((((((((($_GET['pass'] == $pass)))) && (((($pass !== $_GET['pass']))))) || ((((($pass == $_GET['pass'])))) && ((($_GET['pass'] !== $pass)))))))) { // Trolling u lisp masta
      if (strlen($pass) == strlen($_GET['pass'])) {
        $output = "<div class='alert alert-success'>FLAG-XXXXXXXXXXXXXXXXXXXXXXX</div>";
      } else {
        $output = "<div class='alert alert-danger'>Wrong password</div>";
      }
    } else {
      $output = "<div class='alert alert-danger'>Wrong password</div>";
    }
  }
}
?>
```

Well on the first go it seemed easy that all we need to do is the md5 of `admin1674227342` but when you try that as the password, you'll see all your hopes crashing down.
I am no wizard in PHP so I started googling stuff and after some looking I found `http://turbochaos.blogspot.com/2013/08/exploiting-exotic-bugs-php-type-juggling.html`. And realized that our hash also start with `0e` so basically that means we are comparing to `0's`.

So now we know that `0` is the password but if you'll notice that
```php
if (strlen($pass) == strlen($_GET['pass'])) {
    $output = "<div class='alert alert-success'>FLAG-XXXXXXXXXXXXXXXXXXXXXXX</div>";
```

It is comparing `lengths` so that means simply `0` won't do the job. We need 0's in length of the hash i.e `00000000000000000000000000000000`

FLAG - `FLAG-K7PY48gt02T1yvoO9jzP694FztgR1jIS`
