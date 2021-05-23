import random

mycode = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 
         'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k', 'k': 'k', 'l': 'm', 
         'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 
         's': 't', 't': 'u', 'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y',
         'y': 'z', 'z': ' ', ' ': "a"}


def swap(d): 
    key1, key2 = random.sample(list(d), 2)
    e = d.copy()
    e[key1], e[key2] = d[key2], d[key1]
    return e



def ktov(l):
    word = ""
    for elt in l:
        try:
            value = mycode[(elt)]
            word += str(value)
        except:
            continue
    return word


for i in range(40):
    mycode = swap(mycode)
print(mycode, "\n")

message = 'the massive door turned over and over in its sleep until the little fox jumped'

m = []
m.append(list(message.lower().rstrip()))
m = [item for sublist in m for item in sublist]
    

codedtext = ktov(m)
print(message, "\n")
print(m, "\n")
print(codedtext)

with open("code.txt", "w") as f:
    f.write(codedtext)
