# Password Generator

Allows the user to generate a password with a length of x. The user can specify whether the  password must have uppercases, numbers or special characters.

## How to use it

Just change the global variables at the begining of the main.py file

Keep in mind that every value of these variables must be a string, otherwise it will raise an exception

``` py
# Example

LENGTH = "14" # must be at least 8
MUST_HAVE_UPPERCASES = "true"
MUST_HAVE_NUMBERS = "true"
MUST_HAVE_SPECIAL_CHARACTERS = "true"
```

## Default values

PasswordGenerator has default values, so if any PasswordGenerator "set" method is not called it will use the dafault values 

* LENGTH = "8"
* MUST_HAVE_UPPERCASES = "False"
* MUST_HAVE_NUMBERS = "False"
* MUST_HAVE_SPECIAL_CHARACTERS = "False"
