import random

wordlist = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]
numbers = [i for i in range(0, 10)]
num = False
pas = ''

pass_length = int(input('input length pass: '))

if pass_length < 1:
    print('too few')

choice = input('should there be any numbers (y/n)?: ')

if choice.lower() == "y":
    num = True

if num:
    wordlist += numbers

for _ in range(pass_length):
    pas += wordlist[random.randint(0, len(wordlist) - 1)]

print(pas)
