
import numpy as np

obsVals = [1,40,31,40,57,88]
simVals = [-13,79,71,81,104,42]

#%%
# 1. Given two 1-d arrays of simulated values and observed values, Write a Python function to calculate the mean error, 
#    coefficient of determination, and nash coefficient. Not allowed to use loops.
def mean_Error(obsVals,simVals):
    obsArr = np.array(obsVals)
    simArr = np.array(simVals)
    return np.nanmean(simArr - obsArr)

def coeff_Determination(obsVals, simVals):
    obsArr = np.array(obsVals)
    simArr = np.array(simVals)
    n = obsArr.size
    return (np.nansum((obsArr - np.nanmean(obsArr)) * (simArr - np.nanmean(simArr))) **2) / \
            (np.nansum((obsArr - np.nanmean(obsArr)) **2) * np.nansum((simArr - np.nanmean(simArr)) **2))

def coeff_Nash(obsVals, simVals):
    obsArr = np.array(obsVals)
    simArr = np.array(simVals)
    return 1 - (np.nansum((obsArr - simArr) **2) / np.nansum((obsArr - np.nanmean(obsArr)) **2))

print(mean_Error(obsVals, simVals)) 
print(coeff_Determination(obsVals, simVals))    
print(coeff_Nash(obsVals, simVals))
    

#%%
# 2. Given `x` and `y`, write a Python function to perform linear regression which returns `a`, `c` and `sum of square errors`
#    where `ax + c = y`
def linear_Regression(x, y):
    non_nan = ~ (np.isnan(x) | np.isnan(y))
    x = np.array(x)[non_nan]
    y = np.array(y)[non_nan]
    sumX = x.sum()
    sumXsq = (x **2).sum()
    sumY = y.sum()
    sumXY = (x * y).sum()
    n= x.size
    c = (sumY * sumXsq - sumX * sumXY) / (n * (sumXsq) - (sumX) **2)
    a = (n * sumXY - sumX * sumY) / (n * sumXsq - sumX **2)
    sumsqErr = np.nansum((y - np.nanmean(y)) **2) - np.nansum(((a * x + c) - np.nanmean(y)) **2)    
    return a, c, sumsqErr

x = obsVals
y = simVals

print(linear_Regression(x, y))

#%%
# 3. Eestimate the mean precipitation on different land use types.
    
landuse = np.random.randint(1, 5, [5, 5])
precip = np.random.random([5, 5])
    
print('landuse\n', landuse)
print('landuse\n', precip)


#%%
# 4. We have two array. The first array is the distribution of irrigated land. 
    
#   The second array is the precipitation.
landuse = np.random.randint(0,1,[6,6])
precip = np.random.random([6,6])
        
print('landuse\n', landuse)
print('precip\n', precip)
#   A. Create a function to create the buffer zones of varied distances to the irrigated land.
     
#   B. Calculate the mean precipitation in the buffer zones of different distance to the irrigated land.


#%%
# 5. Write a Python function to find the nearest point of a list of given points. You are not allowed to use any type of loops.
#       e. g. points = [(3, 4), (1, 2), (7, 8), (9, 4), (6, 5), (8, 7), (4, 7)]

#       Hint: using numpy to create a N x N array which contain the distances between each ith an jth point pair; where N is the
#             numer of points."

