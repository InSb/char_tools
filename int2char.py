'''Receive a sequence of Unicode integers, than convert them into characters.
'''
import sys

def int2char(start, end):
    for i in range(start, end+1):
        yield chr(i)

if __name__ == '__main__':
    start, end = int(sys.argv[1], base=16), int(sys.argv[2], base=16)
    char_generator = int2char(start, end)
    for c in char_generator:
        print(c, end='')
    print()
