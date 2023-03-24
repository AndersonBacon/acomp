from itertools import permutations  

from functools import reduce
def sortString(str): 
    return reduce(lambda a, b : a + b, sorted(str)) 
   
str = str(input("Digite a string: "))
print(sortString(str))

p = permutations(sortString(str))  
for j in list(p):  
    print(j) 