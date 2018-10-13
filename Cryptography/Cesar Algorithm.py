ALPH_LENG = 26


mIn = 'Lorem Ipsum'
mOut = ''
key =  1

# encrypt: key = key
# decrypt: key = -key
for l in mIn:
    if l.isalpha():             # letters

        s = ord(l)
        s += key
        if l.isupper():
            if s > ord('Z'):
                s -= ALPH_LENG
            elif s < ord('A'):
                s += ALPH_LENG
        elif l.islower():
            if s > ord('z'):
                s -= ALPH_LENG
            elif s < ord('a'):
                s += ALPH_LENG

        mOut += chr(s)
    else:                       # add other simbols

        mOut += l


print(mOut)


