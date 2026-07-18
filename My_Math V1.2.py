#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 11:54:40 2025

Goblin Lab 2 (My Math Lib)
13/10/2025

Kumbi Mandigora

No external (FUNCTIONS)
"""


#%% Task 1 (Custom Stats Library)

import math as m
import numpy as np

# Test Data
test_data = [-9999, 1, 2, 3, 4, 5]
test_data_clean = [1, 2, 3, 4, 5]

# Invalid Values
 
inv_f=float(input("Enter invalid value (Start here-float): "))


#Functions

# Sum
def my_sum(data):
    """Outputs sum of operand
    """
    
    # Initialise Variable
    total=0
    
    # Iterate through container
    
   
    for value in data:
        
        # Increment according to value
        total+=float(value)
       
    # Return container     
    return total

# Length
def my_len(data):
    """Outputs the number of values in a container
    """
    
    # Initialise Counter
    total=0
    
    # Iterate through container
    for value in data:
        
        # Increment Counter 
        total+=1
     
    # Return Container    
    return total

# Average 

def my_avg(data):
    """Outputs container average
    """
    
    # Sum
    dSum=my_sum(data)
    
    # Len
    dLen=my_len(data)
    
    # Processing
    avg=dSum/dLen
    
    # Return Average
    return avg

# Minimum

def my_min(data):
    """Outputs the minimum value in the container
    """
    
    # Index first values
    first=data[0]

    # Iterate through container
    for value in data:
           
        # Selects for smallest value
        if value<first:
                 
            # Reassign smaller value
            first = value
            
    return first

# Maximum

def my_max(data):
    """Outputs the maximum value in the container
    """
    
    # Index first values
    first=data[0]

    # Iterate through container
    for value in data:
        
        # Selects for smallest value
        if value>first:
            
            # Reassign smaller value
            first = value
            
    return first
        
# Standard Deviation(Population)

def my_std(data):
    """Outputs the standard deviation of a container (Population)
    """
    
    # Average 
    aStd=my_avg(data)
    
    # Container Size
    lStd=my_len(data)
    
    # Varience Container 
    varCont=[]
    
    # Iterate through container 
    for value in data:
        
           # Variance
           var=value-aStd
        
           # Variance(Squared)
           var2=var**2
        
           # Appended to empty list
           varCont.append(var2)
    
    # Sum of Variance 
    sumVar=my_sum(varCont)
    
    # Variance/Length of Container    
    std=sumVar/lStd
    
    # 
    std=m.sqrt(std)
    
    return(std)
        
# Standard Deviation(Sample)

def my_std_sample(data):
    """Outputs the standard deviation of a container (Sample)
    """
    
    # Average 
    aStd=my_avg(data)
    
    # Container Size
    lStd=my_len(data)
    
    # Variance Container 
    varCont=[]
    
    # Iterate through container 
    for value in data:
     
        # Variance
        var=value-aStd
        
        # Variance(Squared)
        var2=var**2
        
        # Appended to empty list
        varCont.append(var2)
    
    # Sum of Variance 
    sumVar=my_sum(varCont)
    
    # Variance/Length of Container    
    std=sumVar/(lStd-1)
    
    # 
    std=m.sqrt(std)
    
    return(std)


# Variance(Population)
def my_var_pop(data):
    """Outputs the variance of a container (Population)
    """
    
    # Average
    mVar=my_avg(data)
    
    # Length
    lVar=my_len(data)
    
    # Variance Container
    varCont=[]
    
    # Iterate through data
    for value in data:
    
        var=value-mVar
        var2=var**2
        varCont.append(var2)
    
    # Sum Variance Squared
    sumVar=my_sum(varCont)
    
    var=sumVar/lVar
    
    return var

# Variance(Sample)
def my_var_sample(data):
    """Outputs the variance of a container (Sample)
    """
    
    # Average
    mVar=my_avg(data)
    
    # Length
    lVar=my_len(data)
    
    # Variance Container
    varCont=[]
    
    # Iterate through data
    for value in data:
        
        var=value-mVar
        var2=var**2
        varCont.append(var2)
    
    # Sum Variance Squared
    sumVar=my_sum(varCont)
    
    var=sumVar/(lVar-1)
    
    return var

    
        
# Option (A)

        
# Sum- NaN
def my_nansum(data):
    """NaN- Outputs sum of operand
    """
    
    # Initialise Variable
    total=0
    
    # Iterate through container
    for value in data:
        
        # Skips Nan values or denoted floats
        if (value!=value) or value == inv_f:  
                   continue
      
        else:
   
            # Sum of valid values
            total+=float(value)
       
    # Return container     
    return total

# Length- NaN
def my_nanlen(data):
    """NaN- Outputs the number of values in a container
    """

    # Initialise Counter
    total=0
    
    # Iterate through container
    for value in data:
        
        # Skips Nan values or denoted floats
        if (value!=value) or value == inv_f:   
           continue
      
        else:
            
            # Increment Counter 
            total+=1
     
    # Return Container    
    return total

# Average- NaN

def my_nanavg(data):
    """NaN- Outputs container average
    """
    
    # Sum
    dSum=my_nansum(data)
    
    # Len
    dLen=my_nanlen(data)
    
    # Processing
    
    if (dSum and dLen) != 0:
        
        avg=dSum/dLen
    
    
    # Return Average
    return avg

# Minimum- NaN

def my_nanmin(data):
    """NaN- Outputs the minimum value in the container
    """
    
    # Initialise first to None
    first=None

    # Find the first valid value for starting point 
    for value in data:
        
        # Check if valid values exist 
          
        if first is None:
        
            return None
    
        # Checks for Nan values or denoted floats
        elif value is not((value!=value) or value == inv_f):  
                  
            # Reassign First
            first=value 
          
    
        # Compare valid values 

        elif value < first:
            
            # Reassign First Value
            first = value   
    
      
            
    return first

# Maximum- NaN

def my_nanmax(data):
    """NaN- Outputs the maximum value in the container
    """
    
     
    # Initialise first to None
    first=None

    # Find the first valid value for starting point 
    for value in data:
        
        # Check if valid values exist 
          
        if first is None:
        
            return None
    
        # Checks for Nan values or denoted floats
        elif value is not((value!=value) or value == inv_f):  
                  
            # Reassign First
            first=value 
          
    
        # Compare valid values 

        elif value > first:
            
            # Reassign First Value
            first = value   
    

    return first
        
# Standard Deviation(Population)- NaN

def my_nanstd(data):
    """NaN- Outputs the standard deviation of a container (Population)
    
    """
    
    # Average 
    aStd=my_nanavg(data)
    
    # Container Size
    lStd=my_nanlen(data)
    
    # Varience Container 
    varCont=[]           # Contains no invalid values
    
    # Iterate through container 
    for value in data:
        
        
        
        # Skip invalid values 
        if value is not ((value!=value) or value == inv_f):  
                  
            continue  
       
        # Process as usual
        else:
            
        
            # Variance
            var=value-aStd
        
            # Variance(Squared)
            var2=var**2
        
            # Appended to empty list
            varCont.append(var2)
    
    # Sum of Variance 
    sumVar=my_nansum(varCont)
    
    # Variance/Length of Container    
    std=sumVar/lStd
    
    # 
    std=m.sqrt(std)
    
    return(std)
        

# Standard Deviation(Sample)- Nan

def my_nanstd_sample(data):
    """NaN- Outputs the standard deviation of a container- NaN Values (Sample)
    
    """
    
    # Average 
    aStd=my_nanavg(data)
    
    # Container Size
    lStd=my_nanlen(data)
    
    # Varience Container 
    varCont=[]          # Contains no invalid values
    
    # Iterate through container 
    for value in data:
        
        # Skip invalid values 
       if value is not ((value != value) or value == inv_f):  
                  
            continue  
       
        # Process as usual
    else:       
        
            # Variance
            var=value-aStd
        
            # Variance(Squared)
            var2=var**2
        
            # Appended to empty list
            varCont.append(var2)
    
    # Sum of Variance 
    sumVar=my_nansum(varCont)
    
    # Variance/Length of Container    
    std=sumVar/(lStd-1)
    
    # 
    std=m.sqrt(std)
    
    return(std)
        



# Variance(Population)- NaN
def my_nanvar_pop(data):
    """NaN- Outputs the variance of a container (Population)
    """
    
    # Average
    mVar=my_nanavg(data)
    
    # Length
    lVar=my_nanlen(data)
    
    # Variance Container
    varCont=[]          # Contains no invalid values
    
    # Iterate through data
    for value in data:
         
        # Skip invalid values 
       if value is not ((value != value) or value == inv_f):  
                  
            continue
       
        # Process as usual
       else:
            var=value-mVar
            var2=var**2
            varCont.append(var2)
    
    # Sum Variance Squared
    sumVar=my_nansum(varCont)
    
    var=sumVar/lVar
    
    return var

# Variance(Sample)- NaN
def my_nanvar_sample(data):
    """NaN- Outputs the variance of a container (Sample)
    """
    
    # Average
    mVar=my_nanavg(data)
    
    # Length
    lVar=my_nanlen(data)
    
    # Variance Container
    varCont=[]          # Contains no invalid values
    
    # Iterate through data
    for value in data:
        
        # Skip invalid values 
       if value is not ((value != value) or value == inv_f):  
                  
            continue  
       
       
        # Process as usual
       else:
        
            var=value-mVar
            var2=var**2
            varCont.append(var2)
    
    # Sum Variance Squared
    sumVar=my_nansum(varCont)
    
    var=sumVar/(lVar-1)
    
    return var

         
        
# Option (B)
"""
Replaces the Nan values/missing values with either the mean or median of the dataset
(Replaces invalid values with the mean)
"""

# Nan- Sum (Mean)
def my_nanmean_sum(data):
    """NaN- Outputs sum of operand(Replaces invalid values with the mean)
    """
    
    # Initialise Total
    total=0
    
    # Mean skipping the invalid values
    mean=my_nanavg(data)
    
    # Iterate through container 
    for value in data:
        
        # Check for mean
       if value is not ((value != value) or value == inv_f):  
                  
            # Overwrite value with mean
            value=mean
            
            #Increment Total
            total+=value
            
       else:
            
            #Increment Total
            total+=value
            
    return total

# Nan- Length (Mean)
def my_nanmean_len(data):
    """NaN- Outputs the number of values in a container(Replaces invalid values with the mean)
    """
    
    # Initialise Counter
    counter=0
    
    # Iterate through container
    for value in data:
        
        # Skips Invalid values
       if value is not ((value != value) or value == inv_f):  
            
            # Continue Incrementation
            counter+=1
            
       else:
            
            # Increment Total 
            counter+=1
     
    # Return Container    
    return counter


# NaN- Average(Mean) 
def my_nanmean_avg(data):
    """NaN- Outputs container average(Replaces invalid values with the mean)
    """
    
    # Processing
    mean=my_nanmean_sum(data)/my_nanmean_len(data)
    
    # Return Average
    return mean

# Nan- Minimum

 # Begin Naming convention changes here
print("Begin Naming convention changes here line 649")

def my_nanmin_mean(data):
    """NaN- Outputs the minimum value in the container(Replaces invalid values with the mean)
    """
    
    # Index first values
    initial=data[0]
    
    # Mean
    mean=my_nanmean_avg(data)

    # Iterate through container
    for value in data:
          
        # Check for invalid value
       if value is not ((value != value) or value == inv_f):
            
            # Overwrite value w/ mean
            initial=mean
            
            
        # Selects for smallest value
       if value<initial:
            
            # Overwrite initial with smaller value
            initial = value
            
    return initial

# Nan- Maximum

def my_nanmax_mean(data):
    """NaN- Outputs the maximum value in the container(Replaces invalid values with the mean)
    """
    
    # Index first values
    initial=data[0]

    # Mean
    mean=my_nanmean_avg(data)

    # Iterate through container
    for value in data:
          
        # Check for invalid value
       if value is not ((value != value) or value == inv_f):
            
            # Overwrite value with mean
            initial=mean
            
        # Selects for largest value
       if value>initial:
            
            # Overwrite initial with larger value
            initial = value
  

    return initial
        
# Nan- Standard Deviation(Population)

def my_nanstd_mean(data):
    """NaN- Outputs the standard deviation (Population) of a container. 
    
    (Replaces invalid values with the mean)
    """
    
    # Mean (Clean)
    mean=my_nanmean_avg(data)

    # Cleaned Data
    cleanData=[]
    
    # Varience Container (No Invalid Values)
    varCont=[]
                
    # Iterate through container
    for value in cleanData:
            
            # Variance
            var=value-mean
        
            # Variance(Squared)
            var2=var**2
        
            # Appended to empty list
            varCont.append(var2)
    
    # Sum Variance 
    std=m.sqrt(my_nanmean_sum(varCont)/my_nanmean_len(data))
    
    return(std)
        
# Nan- Standard Deviation(Sample)


# Stopped Cleaning here 17/06/26
print("Continue Update here")

def my_nanstd_sample_mean(data):
    """NaN- Outputs the standard deviation(Sample) of a container.
    
    (Replaces invalid values with the mean)
    """
    # Mean (Clean)
    mean=my_nanmean_avg(data)
    
    # Container Size (Clean)
    length=my_nanmean_len(data)
    
    # Cleaned Data
    cleanData=[]
    
    # Varience Container 
    varCont=[]
    
    # Iterate through data
    for value in data:
        
        # Check if Data is vaild
        if (isinstance(value, float) and m.isnan(value)) or value == -9999:
            
            # Append mean
            cleanData.append(mean)
            
        else:
            
            # Append Value 
            cleanData.append(value)
    
                
    
    # Iterate through container(Clean)
    for value in cleanData:
           
        # Variance
        var=value-mean
        
        # Variance(Squared)
        var2=var**2
        
        # Appended to empty list
        varCont.append(var2)
    
    # Sum of Variance 
    sumVar=my_nanmean_sum(varCont)
    
    # Variance/Length of Container    
    std=sumVar/(length-1)
    
    # 
    std=m.sqrt(std)
    
    return(std)


# Nan- Variance(Population)
def my_nanvar_pop_mean(data):
    """NaN- Outputs the variance(Population) of a container.
    
    (Replaces invalid values with the mean)
    """
    # Length
    length=my_nanmean_len(data)
    
    # Variance Container (No Invalid Values)
    varCont=[]
    
    # Mean (Clean)
    mean=my_nanmean_avg(data)
    
    # Container Size (Clean)
    length=my_nanmean_len(data)
    
    # Cleaned Data
    cleanData=[]
    
    # Varience Container (No Invalid Values)
    varCont=[]
    
    
    # Iterate through data
    for value in data:
        
        # Check if Data is vaild
        if (isinstance(value, float) and m.isnan(value)) or value == -9999:
            
            # Append mean
            cleanData.append(mean)
            
        else:
            
            # Append Value 
            cleanData.append(value)
    
                
    
    # Iterate through container(Clean)
    for value in cleanData:
    
        # Variance
        var=value-mean
        
        # Variance(Squared)
        var2=var**2
        
        # Appended to empty list
        varCont.append(var2)
        
    # Sum Variance Squared
    sumVar=my_nanmean_sum(varCont)
    
    var=sumVar/length
    
    return var

# Nan- Variance(Sample)
def my_nanvar_sample_mean(data):
    """NaN- Outputs the variance(Sample) of a container.
    
    (Replaces invalid values with the mean)
    """
    
    # Length
    length=my_nanmean_len(data)
    
    # Variance Container (No Invalid Values)
    varCont=[]
    
    # Mean (Clean)
    mean=my_nanmean_avg(data)
    
    # Container Size (Clean)
    length=my_nanmean_len(data)
    
    # Cleaned Data
    cleanData=[]
    
    # Varience Container (No Invalid Values)
    varCont=[]
    
    
    # Iterate through data
    for value in data:
        
        # Check if Data is vaild
        if (isinstance(value, float) and m.isnan(value)) or value == -9999:
            
            # Append mean
            cleanData.append(mean)
            
        else:
            
            # Append Value 
            cleanData.append(value)
    
                
    
    # Iterate through container(Clean)
    for value in cleanData:
    
        # Variance
        var=value-mean
        
        # Variance(Squared)
        var2=var**2
        
        # Appended to empty list
        varCont.append(var2)
    
    # Sum Variance Squared
    sumVar=my_nanmean_sum(varCont)
    
    var=sumVar/(length-1)
    
    return var



# Option C- Median

test_data = [-9999, 1, 2, 3, 4, 5]
test_data_clean = [1, 2, 3, 4, 5]

    # NanSum (Median)
def my_nansum_median(data):
    """NaN- Outputs sum of the operand (Replaces invalid values with the Median)
    """
        
    # Sort Data
    sort=sorted(data)
    
    # Initialise Variable
    total=0
        
    # Container length skipping the invalid values
    length=my_nanlen(sort)
                    
    # Iterate through container
    for value in data:
            
        # Skips Invalid values
        if  (isinstance(value, float) and m.isnan(value) or value == -9999):
                
            # Even
            if length%2==0:
                    
                # Median
                median=(length+(length+1))/2
                
                #Increment replacement value
                total+=float(value)
                   
            # Odd
            elif length%2==1:
                    
                # Median
                median=(length+1)/2
                
                #Increment replacement value
                total+=float(value)
                
        else:
                
            
            # Increment according to value
            total+=float(value)
           
    # Return container     
    return total




# NanLength (Median)
def my_nanlen_median(data):
    """NaN- Outputs the number of values in a container(Replaces invalid values with the Median)
    """
    
    # Initialise Counter
    counter=0
    
    # Mean 
    length=my_nanlen(data)
    
    # Iterate through container
    for value in data:
        
        # Skips Invalid values
        if (isinstance(value, float) and m.isnan(value)) or value == -9999 :
            
            # Even
            if length%2==0:
                
                # Median
                median=(length+(length+1))/2
               
                # Replace invalid(median) 
                i=data[int(median)]
           
            # Odd
            elif length%2==1:
                
                # Median
                median=(length+1)/2
                
                # Replace invalid(median) 
                i=data[int(median)]
            
            # Continue Incrementation
            counter+=1
            
        else:
            
            # Increment Counter 
            counter+=1
     
    # Return Container    
    return counter

# NanAverage(Median) 
def my_nanavg_median(data):
    """NaN= Outputs container average(Replaces invalid values with the median)
    """
    
    # Sum
    dSum=my_nansum_median(data)
    
    # Len
    dLen=my_nanlen_median(data)
    
    # Processing
    avg=dSum/dLen
    
    # Return Average
    return avg

# NanMinimum

def my_nanmin_median(data):
    """NaN-Outputs the minimum value in the container(Replaces invalid values with the median)
    """
    
    # Index first values
    initial=data[0]
    
    # Mean
    length=my_nanlen(data)

    # Iterate through container
    for value in data:
          
        # Skips Invalid values
        if (isinstance(value, float) and m.isnan(value)) or value == -9999 :
            
            # Even
            if length%2==0:
                
                # Median
                median=(length+(length+1))/2
               
                # Replace invalid(median) 
                value=data[median]
           
            # Odd
            elif length%2==1:
                
                # Median
                median=(length+1)/2
                
                # Replace invalid(median) 
                value=data[int(median)]
            
        # Selects for smallest value
        if value<initial:
            
            # Reassign smaller value
            initial = value
            
    return initial


def my_nanmax_median(data):
    """NaN- Outputs the maximum value in the container(Replaces invalid values with the median)
    """
    # Sorted Data
    sort=sorted(data)
    
    # Index first values
    initial=sort[0]

    # Length of container
    length=my_nanlen(sort)
    
    # Median
    if length % 2 == 1:
       
        # Odd length: take middle element
        
        middle= length//2       # Integer Division
        
        median = sort[int(middle)]
        
  
    elif length % 2 ==0:
        
        # Even length: average the two middle elements
        
        median = (sort[int(length/2) - 1] + sort[int(length/2)]) / 2

    # Iterate through container
    for value in data:
        
       # Skips Invalid values
       if (isinstance(value, float) and m.isnan(value)) or value == -9999 :
            
            initial=median
            
        # Process as usual
       else:

            # Selects for larger value
            if value>initial:
            
                # Reassign larger value
                initial =value
            
    return initial


      
# NanStandard Deviation(Population)

def my_nanstd_median(data):
    """Outputs the standard deviation of a container (Population)
    -(Replaces invalid values with the median)
    """
    
    # Average
    aStd=my_nanavg_median(data)
    
    # Container Size
    lStd=my_nanlen_median(data)
    
    # Varience Container 
    varCont=[]
    
    # Iterate through container 
    for i in data:
            
            # Variance
            var=i-aStd
        
            # Variance(Squared)
            var2=var**2
        
            # Appended to empty list
            varCont.append(var2)
    
    # Sum of Variance 
    sumVar=my_sum(varCont)
    
    # Variance/Length of Container    
    std=sumVar/lStd
    
    std=m.sqrt(std)
    
    return(std)
        
# NanStandard Deviation(Sample)

def my_nanstd_sample_median(data):
    """Outputs the standard deviation of a container (Sample)(Replaces invalid values with the median)
    """
    
    # Average 
    aStd=my_nanavg_median(data)
    
    # Container Size
    lStd=my_nanlen_median(data)
    
    # Variance Container 
    varCont=[]
    
    # Iterate through container 
    for i in data:
        
           # Variance
           var=i-aStd
        
           # Variance(Squared)
           var2=var**2
        
           # Appended to empty list
           varCont.append(var2)
    
    # Sum of Variance 
    sumVar=my_sum(varCont)
    
    # Variance/Length of Container    
    std=sumVar/(lStd-1)
    
    # 
    std=m.sqrt(std)
    
    return(std)


# NanVariance(Population)
def my_nanvar_pop_median(data):
    """Outputs the variance of a container (Population)(Replaces invalid values with the median)
    """
    
    # Average
    mVar=my_nanavg_median(data)
    
    # Length
    lVar=my_nanlen_median(data)
    
    # Variance Container
    varCont=[]
    
    # Iterate through data
    for i in data:

            var=i-mVar
            var2=var**2
            varCont.append(var2)
    
    # Sum Variance Squared
    sumVar=my_sum(varCont)
    
    var=sumVar/lVar
    
    return var

# NanVariance(Sample)
def my_nanvar_sample_median(data):
    """Outputs the variance of a container (Sample)(Replaces invalid values with the median)
    """
    
    # Average
    mVar=my_nanavg_median(data)
    
    # Length
    lVar=my_nanlen_median(data)
    
    # Variance Container
    varCont=[]
    
    # Iterate through data
    for i in data:
  
            var=i-mVar
            var2=var**2
            varCont.append(var2)
    
    # Sum Variance Squared
    sumVar=my_sum(varCont)
    
    var=sumVar/(lVar-1)
    
    return var
    
# This runs ONLY when you execute this file directly

if __name__ == "__main__":
    print("Testing my_math()...")
    test_data = [-9999, 1, 2, 3, 4, 5]
    test_data_clean = [1, 2, 3, 4, 5]
    
    # For fair comparison, convert -9999 to np.nan for NumPy nan functions
    test_data_numpy = [np.nan if x == -9999 else x for x in test_data]
    
    print("=" * 60)
    print("--- Regular functions (clean data) ---")
    print("=" * 60)
    print(f"Sum - My: {my_sum(test_data_clean)}, NumPy: {np.sum(test_data_clean)}")
    print(f"Average - My: {my_avg(test_data_clean):.2f}, NumPy: {np.mean(test_data_clean):.2f}")
    print(f"Min - My: {my_min(test_data_clean)}, NumPy: {np.min(test_data_clean)}")
    print(f"Max - My: {my_max(test_data_clean)}, NumPy: {np.max(test_data_clean)}")
    print(f"Std (Population) - My: {my_std(test_data_clean):.2f}, NumPy: {np.std(test_data_clean):.2f}")
    print(f"Std (Sample) - My: {my_std_sample(test_data_clean):.2f}, NumPy: {np.std(test_data_clean, ddof=1):.2f}")
    print(f"Variance (Population) - My: {my_var_pop(test_data_clean):.2f}, NumPy: {np.var(test_data_clean):.2f}")
    print(f"Variance (Sample) - My: {my_var_sample(test_data_clean):.2f}, NumPy: {np.var(test_data_clean, ddof=1):.2f}")
    
    print("\n" + "=" * 60)
    print("--- Option A: NaN functions - Skip invalid values ---")
    print("=" * 60)
    print(f"Sum - My: {my_nansum(test_data)}, NumPy: {np.nansum(test_data_numpy)}")
    print(f"Average - My: {my_nanavg(test_data):.2f}, NumPy: {np.nanmean(test_data_numpy):.2f}")
    print(f"Min - My: {my_nanmin(test_data)}, NumPy: {np.nanmin(test_data_numpy)}")
    print(f"Max - My: {my_nanmax(test_data)}, NumPy: {np.nanmax(test_data_numpy)}")
    print(f"Std (Population) - My: {my_nanstd(test_data):.2f}, NumPy: {np.nanstd(test_data_numpy):.2f}")
    print(f"Std (Sample) - My: {my_nanstd_sample(test_data):.2f}, NumPy: {np.nanstd(test_data_numpy, ddof=1):.2f}")
    print(f"Variance (Population) - My: {my_nanvar_pop(test_data):.2f}, NumPy: {np.nanvar(test_data_numpy):.2f}")
    print(f"Variance (Sample) - My: {my_nanvar_sample(test_data):.2f}, NumPy: {np.nanvar(test_data_numpy, ddof=1):.2f}")
    
    print("\n" + "=" * 60)
    print("--- Option B: Replace invalid values with MEAN ---")
    print("=" * 60)
    print(f"Sum - My: {my_nanmean_sum(test_data):.2f}")
    print(f"Mean - My: {my_nanmean_avg(test_data):.2f}")
    print(f"Min - My: {my_nanmin_mean(test_data):.2f}")
    print(f"Max - My: {my_nanmax_mean(test_data):.2f}")
    print(f"Std (Population) - My: {my_nanstd_mean(test_data):.2f}")
    print(f"Std (Sample) - My: {my_nanstd_sample_mean(test_data):.2f}")
    print(f"Variance (Population) - My: {my_nanvar_pop_mean(test_data):.2f}")
    print(f"Variance (Sample) - My: {my_nanvar_sample_mean(test_data):.2f}")
    
    print("\n" + "=" * 60)
    print("--- Option C: Replace invalid values with MEDIAN ---")
    print("=" * 60)
    print(f"Sum - My: {my_nansum_median(test_data):.2f}")
    print(f"Average - My: {my_nanavg_median(test_data):.2f}")
    print(f"Min - My: {my_nanmin_median(test_data):.2f}")
    print(f"Max - My: {my_nanmax_median(test_data):.2f}")
    print(f"Std (Population) - My: {my_nanstd_median(test_data):.2f}")
    print(f"Std (Sample) - My: {my_nanstd_sample_median(test_data):.2f}")
    print(f"Variance (Population) - My: {my_nanvar_pop_median(test_data):.2f}")
    print(f"Variance (Sample) - My: {my_nanvar_sample_median(test_data):.2f}")
    
    print("\n" + "=" * 60)
    print("Summary: test_data = [-9999, 1, 2, 3, 4, 5]")
    print("Expected mean (without -9999): 3.0")
    print("Expected median (without -9999): 3.0")
    print("=" * 60)

#%% Notes

print("17/06/26- Streamlined functions up until my_nan_std_sample_mean:"+ 
      "I still need to finish streamlining the functions beofre updating the"+ 
      "naming conventions")

#%% Reference List
"""
[1] https://datatest.readthedocs.io/en/latest/how-to/nan-values.html
"""

