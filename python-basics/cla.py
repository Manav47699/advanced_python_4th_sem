# cla = command line argumnet -> giving input directly from the terminal without asking for input

import sys

# print (sys.argv)   # this gives a list -> ['command_line_argument.py', 'hello', '123']

n = int(sys.argv[1])
for i in range(1, 11):
    print(f'{n}*{i} = {n*i}')


