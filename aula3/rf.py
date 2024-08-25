#! /usr/bin/env python3

'''
#Comandos para fazer testes:
#python -m doctest rf.py -v

>>> main([])
Please provide words to search.

>>> main(['cruzeiro']) # doctest: +NORMALIZE_WHITESPACE
U+20A2 N{CRUZEIRO SIGN} CRUZEIRO SIGN

>>> search(['cat'])  # doctest: +NORMALIZE_WHITESPACE
(41654, 'YI SYLLABLE CAT')
(52289, 'HANGUL SYLLABLE CAT')
(66028, 'PHAISTOS DISC SIGN CAT')
(128008, 'CAT')
(128049, 'CAT FACE')
(128568, 'GRINNING CAT FACE WITH SMILING EYES')
(128569, 'CAT FACE WITH TEARS OF JOY')
(128570, 'SMILING CAT FACE WITH OPEN MOUTH')
(128571, 'SMILING CAT FACE WITH HEART-SHAPED EYES')
(128572, 'CAT FACE WITH WRY SMILE')
(128573, 'KISSING CAT FACE WITH CLOSED EYES')
(128574, 'POUTING CAT FACE')
(128575, 'CRYING CAT FACE')
(128576, 'WEARY CAT FACE')

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
        print('Please provide words to search.')

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
   