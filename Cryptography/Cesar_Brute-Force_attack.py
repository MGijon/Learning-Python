ALPH_LENG = 26

def getMessage():
    return input('Text your message to hide/reveal:\n')


def algorithmCesar_BruteForce_attack(mIn):

    mIn = ' ' + mIn
    for i in range(0, ALPH_LENG + 1):

        mOut = ''
        for ll in mIn:
            if ll.isalpha():  # letters

                s = ord(ll)
                s += -i

                if ll.isupper():
                    if s > ord('Z'):
                        s -= ALPH_LENG
                    elif s < ord('A'):
                        s += ALPH_LENG
                elif ll.islower():
                    if s > ord('z'):
                        s -= ALPH_LENG
                    elif s < ord('a'):
                        s += ALPH_LENG

                mOut += chr(s)
            else:  # other simbols

                mOut += ll

        print("If the key is " + str(i) + " the original message is:\n")
        print("\b" + mOut )




algorithmCesar_BruteForce_attack(getMessage())         