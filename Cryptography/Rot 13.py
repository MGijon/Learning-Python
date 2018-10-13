ALPH_LENG = 26
KEY = 13

def getMessage():
    return input('Text your message to hide/reveal:\n')

def printMessage(mOut):
    print(mOut)

def algorithmROT13(mIn):
    mOut = ''
    for l in mIn:
        if l.isalpha():                 # letters

            s = ord(l)
            s += KEY
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
        else:                           # other simbols

            mOut += l

    return mOut


printMessage(algorithmROT13(getMessage()))