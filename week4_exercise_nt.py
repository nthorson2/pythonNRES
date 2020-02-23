# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 15:58:36 2020

@author: thors
"""

#%% print values in range 1-6 excluding 3 & 6 ex4.1
def printNums(min,max,ex1,ex2):
    i = min
    for i in range(max):
        if i != ex1:
            if i != ex2:
                print(i)
            else: continue
        else: continue   
printNums(0,6,3,6)
          
#%% check user password validity ex4.2
def checkPassword(String):
    import sys

    print()

    upCnt = 0           #number of upper case characters in string
    lowCnt = 0          #number of lower case characters in string
    numCnt = 0          #number of numeric values in string
    charCnt = 0         #number of special characters in string

    
    if len(String)<6 or len(String)>16:
        print("password length must be between 6-16 characters")
        sys.exit()  
    else:
        for i in String:
            if ord(i)>=65 and ord(i)<=90:
                upCnt = upCnt + 1
    
            if ord(i)>=97 and ord(i)<=122:
                lowCnt = lowCnt + 1
            
            if ord(i)>=48 and ord(i)<=57:
                numCnt = numCnt + 1
                
            if ord(i) == 35 or ord(i) == 36 or ord(i) == 64:
                charCnt = charCnt + 1
                
    if upCnt>0 and lowCnt>0 and numCnt>0 and charCnt>0:
        print("password accepted!")
    else:
        if upCnt <= 0:
            print("- password must contain at least one upper case letter")
            sys.exit()
        if lowCnt <= 0:
            print("- password must contain at least one lower case letter")
            sys.exit()
        if numCnt <= 0:
            print("- password must contain at least one numeric integer value between 0-9")
            sys.exit()
        if charCnt <=0:
            print("- password must contain at least one of the following special characters ($ # @)")
            sys.exit()
    
checkPassword("Tested#7")

#%% nested for loop mimicking a pattern ex4.3
cnt = 0
for i in range(10):
    string =""
    if i> 5:
        cnt = cnt + 1    
        for x in range(5):
            if x <= 4 - cnt:
                string = string + chr(127) + chr(42)
            else:
                string = string + chr(127) + chr(45)
    else:
        for x in range(i):
            string = string + chr(127) + chr(42)
    print(string)
    
#%% analysis across lists ex4.4
print("")
brandLIST = ["Ford", "Ford", "Chevy", "Chevy", "Honda", "Ford", "Honda", "Honda", "Ford", "Chevy"]
modelLIST = ["F150", "Escape", "Charger", "Charger", "Civic", "Escape", "CRV", "CRV", "F150", "Silverado"]
typeLIST = ["Pickup", "SUV", "Sedan", "Sedan", "Sedan", "SUV", "SUV", "SUV", "Pickup", "Pickup"]
accidentsLIST = [25, 79, 46, 90, 29, 88, 79, 93, 20, 11]

minAccIndex = None
minPickupIndex = None
minSuvIndex = None
minSedanIndex = None

fordPickupAcc = 0
fordSuvAcc = 0
chevySedanAcc = 0
hondaSedanAcc = 0
hondaSuvAcc = 0
chevyPickupAcc = 0

#safest overall
for i in range(len(accidentsLIST)):
    if i==0:
        minAccIndex = i
    else:
        if accidentsLIST[minAccIndex]>accidentsLIST[i]:
            minAccIndex=i
print("Safest Overall Vehicle: " + brandLIST[minAccIndex] + chr(127) + modelLIST[minAccIndex] + chr(127) + typeLIST[minAccIndex])

#safest Brand for each Type
print("")
for i in range(len(accidentsLIST)):
    if typeLIST[i]=="Pickup":
        if minPickupIndex == None:    
            minPickupIndex = i
        else:
            if accidentsLIST[minPickupIndex]>accidentsLIST[i]:
                minPickupIndex = i
    elif typeLIST[i]=="SUV":
        if minSuvIndex == None:    
            minSuvIndex = i
        else:
            if accidentsLIST[minSuvIndex]>accidentsLIST[i]:
                minSuvIndexIndex = i
    elif typeLIST[i]=="Sedan":
        if minSedanIndex == None:    
            minSedanIndex = i
        else:
            if accidentsLIST[minSedanIndex]>accidentsLIST[i]:
                minSedanIndex = i
print("Safest Pickeup: " + brandLIST[minPickupIndex])
print("Safest SUV: " + brandLIST[minSuvIndex])
print("Safest Sedan: " + brandLIST[minSedanIndex])

#Number of Accidents for each Brand and Type
print("")
for i in range(len(accidentsLIST)):
    vType= typeLIST[i]
    vBrand= brandLIST[i]
    vAcc= accidentsLIST[i]
    if vType=="Pickup" and vBrand=="Chevy":
        chevyPickupAcc = chevyPickupAcc + vAcc
    if vType == "Pickup" and vBrand=="Ford":
        fordPickupAcc = fordPickupAcc + vAcc
    if vType == "SUV" and vBrand=="Ford":
        fordSuvAcc = fordSuvAcc + vAcc
    if vType == "SUV" and vBrand=="Honda":
        hondaSuvAcc = hondaSuvAcc + vAcc
    if vType== "Sedan" and vBrand=="Chevy":
        chevySedanAcc = chevySedanAcc + vAcc
    if vType=="Sedan" and vBrand=="Honda":
        hondaSedanAcc = hondaSedanAcc + vAcc
        
print("Chevy Pickup Accidents per Year: ", chevyPickupAcc)
print("Ford Pickup Accidents per Year: ", fordPickupAcc)
print("Ford SUV Accidents per Year: ", fordSuvAcc)
print("Honda SUV Accidents per Year: ", hondaSuvAcc)
print("Chevy Sedan Accidents per Year: ", chevySedanAcc)
print("Honda Sedan Accidents per Year: ", hondaSedanAcc)

#%%  Temperature classification ex4.5
import statistics

temperatures = [-5.4, 1.0, -1.3, -4.8, 3.9, 0.1, -4.4, 4.0, -2.2, -3.9, 4.4, -2.5,
-4.6, 5.1, 2.1, -2.4, 1.9, -3.3, -4.8, 1.0, -0.8, -2.8, -0.1, -4.7, -5.6, 2.6,
-2.7, -4.6, 3.4, -0.4, -0.9, 3.1, 2.4, 1.6, 4.2, 3.5, 2.6, 3.1, 2.2, 1.8, 3.3,
1.6, 1.5, 4.7, 4.0, 3.6, 4.9, 4.8, 5.3, 5.6, 4.1, 3.7, 7.6, 6.9, 5.1, 6.4, 3.8,
4.0, 8.6, 4.1, 1.4, 8.9, 3.0, 1.6, 8.5, 4.7, 6.6, 8.1, 4.5, 4.8, 11.3, 4.7, 5.2,
11.5, 6.2, 2.9, 4.3, 2.8, 2.8, 6.3, 2.6, -0.0, 7.3, 3.4, 4.7, 9.3, 6.4, 5.4, 7.6,
5.2]

cold = []
slippery = []
comfortable = []
warm = []
data1 = []

print("")

for i in range(len(temperatures)):
    temp = temperatures[i]
    if temp < -2:
        cold.append(i)
    if temp >=-2 and temp < 2:
        slippery.append(i)
    if temp >= 2 and temp < 15:
        comfortable.append(i)
    if temp >= 15:
        warm.append(i)
# calculates mean of list values
def calcMean(tempList):
    if len(tempList)>0:
        for i in range(len(tempList)):
            data1.append(temperatures[tempList[i]])
            x = statistics.mean(data1)
    else: x = "N/A"
    return x    

print("Cold Mean: ", calcMean(cold))
print("Slippery Mean: ", calcMean(slippery))
print("Comfortable Mean: ", calcMean(comfortable))
print("Warm Mean: ", calcMean(warm))

#%% longest Sub-String of String without repeating characters ex4.6
def subLength(string):
    uniqueChar = []
    uniqueCharIndex = []
    maxStrLgth = 0
    maxStr = []
    index = 0
    i = 0
    maxString = ""
    
    while i < (len(string)-1):    
        for i, item in enumerate(string):
            if i>= index:
                if len(uniqueChar)==0:
                    uniqueChar.append(string[i])
                    if maxStrLgth==0:
                        maxStrLgth=len(uniqueChar)
                        maxStr=uniqueChar
                else:
                    for x in range(len(uniqueChar)):
                        if uniqueChar[x] == string[i]:
                            append = False
                            break
                        else:
                            append = True
                    if append == True:
                        uniqueChar.append(string[i])
                        uniqueCharIndex.append(i)
                        strLgth = len(uniqueChar)
                        if maxStrLgth < strLgth:
                            maxStrLgth = strLgth
                            maxStr = uniqueChar
                    else:
                        if  (len(string) - uniqueCharIndex[0]) > maxStrLgth:
                            index = i - (len(uniqueChar)-1)
                            i = i
                            uniqueChar= [] 
                            uniqueCharIndex = []
                        else: 
                            i = len(string)-1
                        break

    for z in maxStr:
        maxString = maxString + z
    
    answerString = "The answer is '" + maxString + "' with a length of " + str(maxStrLgth)
    return answerString
print(subLength("testedstringentry"))

#%% find all unique triplets ex4.7
def findTriplets(*args):
    uniqueValLST = [] #list of unique value sets that sum to 0
    test = len(args)
    
    for i in range(len(args)):
        for x in range(len(args)):
            for z in range(len(args)):
                if args[i] + args[x] + args[z] == 0:
                    valSet = str(args[i]) + chr(58) + str(args[x])+ chr(58) + str(args[z])
                    if len(uniqueValLST)==0:
                        uniqueValLST.append(valSet)
                    else:
                        for y in range(len(uniqueValLST)):
                            string = uniqueValLST[y]
                            stringLst = string.split(chr(58))
                            valSetLst = valSet.split(chr(58))
                            stringLst.sort()
                            valSetLst.sort()
                            if stringLst == valSetLst:
                                append = False
                                break
                            else:
                                append = True
                                
                        if append == True:
                            uniqueValLST.append(valSet)
                            
    return uniqueValLST
print(findTriplets(-1,0,1,2,-1,4))
