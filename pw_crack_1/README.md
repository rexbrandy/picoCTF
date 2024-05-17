# PW Crack 1
Here is the link to the [challenge](https://play.picoctf.org/practice/challenge/245)

This challenge is a basic reverse engineering challenge where we must review a python file to find the password to decrypt the code.

In this challenge we are given 2 files: 
  `level1.flag.txt.enc` : This is the encrypted flag code.
  `level1.py` : This is the python code we must reverse engineer to decrypt the provided code.

If we run at `level1.py` we will see this:

```
> python3 level1.py
Please enter correct password for flag: 
```

And if we open the file we will see this subroutine that prints the prompt and awaits the password.

```
def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "691d"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")
```

the if statemant on line 3 of this sub is checking if the inputted password is equal to `691d`. After reviewing the code it's quite simple, we run the script and input the prompt and we will see this.

```
> python3 level1.py 
Please enter correct password for flag: 691d
Welcome back... your flag, user:
picoCTF{#################}
```

