import numpy as np
f=10**6
empty_block = []

def len_seg(i):
    l = 1/f*np.sqrt(i*6*1.602*10**-19*100*np.sin(np.pi/4)/(2*1.992*10**-26))
    return(l)
 
summe = 0
for i in np.arange(1,21):
    x = len_seg(i)
    empty_block.append(x)
    summe += x

print(empty_block)
print(summe)