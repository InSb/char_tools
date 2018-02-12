'''Receive a sequence of Unicode integers, than convert them into characters.
example:
    > python ./int2char.py 4E00 4E0F
    一丁丂七丄丅丆万丈三上下丌不与丏
'''
import sys

def int2char(start, end):
    for i in range(start, end+1):
        yield chr(i)

if __name__ == '__main__':
    to_int = lambda a: int(a, base=16)
    start, end = (map(to_int, sys.argv[1:3]))   # argv 1 and 2
    char_generator = int2char(start, end)
    for c in char_generator:
        print(c, end='')
    print()
