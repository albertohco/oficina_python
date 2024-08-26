#! /usr/bin/env python3

'''
#Comandos para fazer testes:
#python -m doctest rf.py -v

>>> main([])
Please provide words to search.

>>> main(['cruzeiro']) # doctest: +NORMALIZE_WHITESPACE
U+20A2      ₢       CRUZEIRO SIGN

>>> search(['cat'])  # doctest: +NORMALIZE_WHITESPACE
U+A2B6      ꊶ      YI SYLLABLE CAT
U+CC41      챁      HANGUL SYLLABLE CAT
U+101EC     𐇬       PHAISTOS DISC SIGN CAT
U+1F408     🐈      CAT
U+1F431     🐱      CAT FACE
U+1F638     😸      GRINNING CAT FACE WITH SMILING EYES
U+1F639     😹      CAT FACE WITH TEARS OF JOY
U+1F63A     😺      SMILING CAT FACE WITH OPEN MOUTH
U+1F63B     😻      SMILING CAT FACE WITH HEART-SHAPED EYES
U+1F63C     😼      CAT FACE WITH WRY SMILE
U+1F63D     😽      KISSING CAT FACE WITH CLOSED EYES
U+1F63E     😾      POUTING CAT FACE
U+1F63F     😿      CRYING CAT FACE
U+1F640     🙀      WEARY CAT FACE

>>> search(['cat', 'eyes'])  # doctest: +NORMALIZE_WHITESPACE
U+1F638	    😸	    GRINNING CAT FACE WITH SMILING EYES
U+1F63B	    😻	    SMILING CAT FACE WITH HEART-SHAPED EYES
U+1F63D	    😽	    KISSING CAT FACE WITH CLOSED EYES

'''
import sys
import unicodedata

def search(query: list[str], first=32, last=sys.maxunicode ) -> None:
    query = ' '.join(query).replace('-',' ').split()
    query = {word.upper() for word in query}
    for code in range(first, last + 1):
        char = chr(code)
        name = unicodedata.name(char, None)
        if name is None:
            continue
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
    main(sys.argv[1:])
   