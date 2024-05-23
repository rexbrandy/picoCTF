import string

alphabet = string.ascii_lowercase
alphabet += '0123456789_'

fp = open('message2.txt', 'r')
numbers = fp.read().strip().split(' ')

flag = ''

for n in numbers:
    n = int(n)
    position =  pow(n, -1, 41)
    flag += alphabet[position-1]

print(flag)
