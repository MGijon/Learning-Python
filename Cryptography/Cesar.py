ALPH_LENG = 26

def getMessage():
    return input('Text your message to hide/reveal:\n')

def getKey():
    return int(input('Text your secret key:\n'))

def getMode():
    return input('\'encrypt\' or \'e\' to encrypt a message,\n\'decrypt\' or \'d\' to decrypt a message\n')

def printMessage(mOut):
    print(mOut)

def algorithmCesar(mIn, key, mode):

    if mode in 'decrypt d'.split():
        key = - key

    mOut = ''
    for l in mIn:
        if l.isalpha():                 # letters

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
        else:                           # other simbols

            mOut += l

    return mOut

mode = getMode()
message = getMessage()
key = getKey()

printMessage(algorithmCesar(message, key, mode))