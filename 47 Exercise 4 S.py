import random
import string

def get_random_str(length=3):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

word = input("Enter message: ")
words = word.split(" ")
coding = input("1 for Coding or 0 for Decoding: ")
coding = True if coding == "1" else False
nwords = []

if coding:
    for word in words:
        if len(word) >= 3:
            r1 = get_random_str()
            r2 = get_random_str()
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print("  ".join(nwords))
else:
    for word in words:
        if len(word) >= 3 and len(word) > 6:  
            stnew = word[3:-3]  
            stnew = stnew[-1] + stnew[:-1]  
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print("  ".join(nwords))
