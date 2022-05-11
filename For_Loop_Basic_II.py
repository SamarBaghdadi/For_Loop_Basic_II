# Biggie Size - Given a list, write a function that changes all positive numbers 
# in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, 
# but whose values are now [-1, "big", "big", -5]

def biggie_size(A):
    for i in range(len(A)):
        if A[i]>=0:
            A[i]="big"

    return A


# Count Positives - Given a list of numbers, create a function to replace the last value with 
# the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(A):
    pos=0
    for element in A:
        if element >0:
            pos=pos+1
    if len(A) ==0:
        return False
    else:
        A[len(A)-1]=pos

    return A

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sum_total(A):
    sum=0
    for element in A:
        sum= sum+element

    return sum


# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5
def average(A):
    if len(A)==0:
        return False
    else:
        avg=0
    for element in A:
        avg=avg+element
    avg=avg/len(A)
    return avg

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def length(A):
    return len(A)

# Minimum - Create a function that takes a list of numbers and returns the minimum value
# in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(A):
    if len(A)==0:
        return False
    else:
        min=A[0]
        for element in A:
            if element<min:
                min=element
    return min

# Maximum - Create a function that takes a list and returns the maximum value in the list. 
# If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum(A):
    if len(A)==0:
        return False
    else:
        max=A[0]
        for element in A:
            if element>max:
                max=element
    return max



# Ultimate Analysis - Create a function that takes a list and returns a dictionary that 
# has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(A):
    if len(A)==0:
        return False
    else:
        new_dict={}
        new_dict["sumTotal"]=sum_total(A)
        new_dict["average"]=average(A)
        new_dict["minimum"]=minimum(A)
        new_dict["maximum"]=maximum(A)
        new_dict["length"]=length(A)
    
    return new_dict

# Reverse List - Create a function that takes a list and return that list with values reversed. 
# Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(A):
    if len(A)==0:
        return False
    else:
        for i in range(int(len(A)/2)):
            print (i)
            v_int=A[i]
            A[i]=A[len(A)-1-i]
            A[len(A)-i-1]=v_int
    return A

