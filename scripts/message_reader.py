fp = open('message.txt', 'r')
numbers = fp.read().strip().split(' ')
 
for n in numbers:
    n = int(n)
    n = n % 37

    if n < 26:
        print(chr(n+97).upper(), end='')
    elif n < 36:
        print(n-26, end='') 
    elif n == 36:
        print('_',end='')

