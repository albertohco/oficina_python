#! /usr/bin/env python3

'''
#Comandos para fazer testes:
python -m doctest rf.py -v

>>> main([])
Please provide words to search,

>>> main(['cruzeiro']) # doctest: +NORMALIZE_WHITESPACE
U+20A2 N{CRUZEIRO SIGN} CRUZEIRO SIGN

>>> search(['cat'])
U+20A2 N{CRUZEIRO SIGN} CRUZEIRO SIGN

'''
import sys
import unicodedata

def search(query: list[str], first=32, last = sys.maxunicode ) -> None:
    query = ' '.join(query).replace('-',' ').split()
    query = {word.upper() for word in query}
    for code in range(32,  +1):
        char = chr(code)
        name = unicodedata.name(char, None)
        if name is None:
            pass
        name = name.replace('-',' ')
        name = set(name.split())
        if query <= name:
            print(f'U+{code:04X}\t{char}\t{unicodedata.name(char)}')

def main(args: list[str]) -> None:
    if args:
        search(args)
    else:
        print('Please provide words to search, ')

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
   