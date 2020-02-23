# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:48:19 2020

@author: thors
"""


#%%
#exercise 5.1

#str.format
print('file_{:>03} : {:0.2f}, {:0.2e}, {:0.2e}'.format(2,123.4567,10000,12345.67))
#f-string
vals = [2,123.4567,10000,12345.67]
print(f'file_%03i : %0.2f, %0.2e, %0.2e'%(2,123.4567,10000,12345.67))

#%%
#exercise 5.2
def iterableFunct(valList):
    length = len(valList)
    val=""
    cnt=0
    for x in valList:
        cnt += 1
        if cnt < len(valList):
            val += str(x)
            val += ","
        else:
            val += str(x)
    print(f'The {len(valList)} numbers are: {val}' ) 
iterableFunct([6,7,8,9])

#%%
#exercise 5.3
def iterableFunct(valList):
    length = len(valList)
    val=""
    cnt=0
    for x in range(len(valList)):
        if x < len(valList)-1:
            val += str(valList[x])
            val += ","
        else:
            val += str(valList[x])
    print(f'The {len(valList)} numbers are: {val}' ) 
iterableFunct([6,7,8,9])

#%%
#exercise 5.4
def fString(ListA):
    print(f''.join(f'{x} ' for x in ListA))
fString((4,30,2017,2,27))

#%%
#exercise 5.5
def fStringFormat(fruit1,weight1,fruit2,weight2):
    print(f'The weight of an {fruit1} is {weight1} and the weight of a {fruit2} is {weight2} and the total weight is {weight1 + weight2:0.1f}')

fStringFormat('orange',1.3,'lemon',1.1)

#%%
#exercise 5.6
def fStringWeightChange(listA, width):
    print(f''.join(f'{x:>{width}}' for x in listA))

fStringWeightChange([1,2,3,4,5], 3)

#%%
#exercise 5.7

