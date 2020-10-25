## Password Generator with Python

We use passwords everywhere, and to improve security we must use strong passwords. And we can do that with Python. 
Python string and random modules are used to generate passwords.

### Code

```
import string
from random import *
char = string.ascii_letters + string.punctuation + string.digits 
passwordGenerator = "".join(choice(char) for x in range(randint(8,16)))
print(passwordGenerator)
```

### Understanding the Code

```
import string
from random import *
```
This is used to import the string and random modules to our code.

```
char = string.ascii_letters + string.punctuation + string.digits 
```

**string.ascii_letters** is used to concatenate the leeters(uppercase and lowercase).
**string.digits** It will use '0123456789'.
**string.punctuation** String of ASCII characters which are considered punctuation characters in the C
locale.

These three will be concatenated to produce a strong password.

And finally we can see some outputs like this:
```
vT3w}j@$@FW"h-H!
F<dH)&}*
=9"SCL#eXR3$A,D*
_5/k^SiG.=? 
```
