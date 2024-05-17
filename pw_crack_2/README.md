# PW Crack 2
Here is the link to the [challenge](https://play.picoctf.org/practice/challenge/246). This one is very similar to the challenge before.

This challenge is a basic reverse engineering challenge where we must review a python file to find the password to decrypt the code.

In this challenge we are given 2 files: 
  `level2.flag.txt.enc` : This is the encrypted flag code.
  `level2.py` : This is the python code we must reverse engineer to decrypt the provided code.

If we run at `level2.py` we will see this:

```
> python3 level2.py
Please enter correct password for flag: 
```

And if we open the file we will see this subroutine that prints the prompt and awaits the password.

```
def level_2_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == chr(0x33) + chr(0x39) + chr(0x63) + chr(0x65) ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")
```

the if statemant on line 3 of this sub is checking if the inputted password is equal to `chr(0x33) + chr(0x39) + chr(0x63) + chr(0x65)`. 
The chr() function returns the character that represents the specified unicode. To find out what these characters are we can open a python3 interpreter and do the following

```
> python3
Python 3.11.6 (main, Nov  2 2023, 04:51:19) [Clang 14.0.0 (clang-1400.0.29.202)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print(chr(0x33), chr(0x39), chr(0x63), chr(0x65))
3 9 c e
>>> print(chr(0x33)+chr(0x39)+chr(0x63)+chr(0x65))
39ce
```

After doing this we can see the password to the file is 39ce.

```
> python3 level2.py 
Please enter correct password for flag: 39ce
Welcome back... your flag, user:
picoCTF{#################}
```

