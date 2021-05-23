import numpy as np
import random
# from tqdm import tqdm


tdict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 
         'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 
         'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 
         's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23,
         'y': 24, 'z': 25, ' ': 26}




ivd = {v: k for k, v in tdict.items()}

def ktov(l):
    word = ""
    for elt in l:
        value = tdict[(elt)]
        word += str(value)
    return word

def vtok(l):
    numlist = []
    for letter in l:
        numlist.append(ivd[letter])
    return "".join(numlist)



with open("sampleEnglish.txt") as f:
    sample = []
    for line in f:
        sample.append(list(line.lower().rstrip()))
        sample = [item for sublist in sample for item in sublist]
    
P = np.zeros((len(tdict), len(tdict)))


for i in range(len(sample)):
    try:
        a = tdict[sample[i]]
        b = tdict[sample[i+1]]
    except:
        continue
    
    P[a,b] += 1
    
rowtotal = np.zeros((len(tdict),1))
Q = np.zeros((len(tdict),1))
for i in range(len(tdict)):
    rowtotal[i] = np.sum(P[i,:])
    if rowtotal[i] != 0:
        P[i,:] = P[i,:]/rowtotal[i]

Q = rowtotal/np.sum(rowtotal)

lP = -(np.log(P))


for (x,y), value in np.ndenumerate(lP):
    if lP[x,y] == float('+inf'):
        lP[x,y] = 20


def Plf(flist):
    Plf = 0
    for i in range(len(flist)-1):
        Plf = Plf + lP[flist[i],flist[i+1]]
    return Plf
    
def swap(d): 
    key1, key2 = random.sample(list(d), 2)
    e = d.copy()
    e[key1], e[key2] = d[key2], d[key1]
    return e
    

with open("code.txt") as f:
    coded = []
    for line in f:
        coded.append(list(line.lower().rstrip()))
        coded = [item for sublist in coded for item in sublist]
    for i in range(len(coded)):
        coded[i] = tdict[coded[i]]
    print(coded)
    
    
    fdict = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 
         7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 
         13: 13, 14: 14, 15: 15, 16: 16, 17: 17, 18: 18, 
         19: 19, 20: 20, 21: 21, 22: 22, 23: 23, 24: 24,
         25: 25, 26: 26}
    

    decoded = list(map(fdict.get,coded))
    lp = Plf(decoded)
    
    smallestlp = lp
    de = decoded
    
    for j in range(int(1e7)):
        fdictStar = swap(fdict)
        decodedStar = list(map(fdictStar.get,coded))
        lpStar = Plf(decodedStar)
        if (lpStar <= lp) or (random.random() < np.exp((lp-lpStar))):
            fdict, decoded, lp = fdictStar, decodedStar, lpStar
            if lp < smallestlp:
                smallestlp, de = lp, decoded
                
            
            
        
        if j % 10000 == 0:
            print(vtok(decoded),lp, '\n')
            
            
            