# -*- coding: utf-8 -*-
'''Input a CJKV character, a sequence of variation selectors for Ideographic
variation sequences, and filename, it will append a file with variations of
the character.
example:
    > python ivd_test.py 0x9089 0xE0100 0xE011F tmp_file.txt
    (In tmp_file.txt:)
    === Ideographic Variations ===
    0X9089	邉
    with variation selectors:
    0XE0100	邉󠄀
    0XE0101	邉󠄁
    0XE0102	邉󠄂
    0XE0103	邉󠄃
    ...
    0XE011F	邉󠄟

'''
import sys

def iv_output(char_code, vselectors_seq, output_file):
    with open(output_file, mode='a', encoding='utf-8') as f:
        print('=== Ideographic Variations ===', file=f)
        print(format(char_code, '#X'), chr(char_code), sep='\t', file=f)
        print('with variation selectors:', file=f)
        for vselector in vselectors_seq:
            print(format(vselector, '#X')+'\t',
                  chr(char_code), chr(vselector), sep='',
                  file=f)
        print(file=f)

if __name__ == '__main__':
    to_int = lambda a: int(a, base=16)
    char_code = to_int(sys.argv[1])
    vselectors_seq = range(to_int(sys.argv[2]), to_int(sys.argv[3])+1)
    output_file = sys.argv[4]
    iv_output(char_code, vselectors_seq, output_file)
