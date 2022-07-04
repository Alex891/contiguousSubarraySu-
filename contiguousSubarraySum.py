# Write a function that finds the contiguous subarray (containing at least one number) which has the largest 
# sum within an array read in input to the function. The function should return the sub-array and the corresponding sum. 
# Which is the complexity of your solution? Can you do a solution with linear complexity? Write a unit test for the function.

from sys import maxsize
import numpy as np



def contiguousSubarraySum(in_array, test_id):
    '''
    
    :param in_array: input array
    :param test_id: test identifier

    The function take in input the array and print the 
    contiguous sub-array on the screen with the maximum sum and the related elements within it.

    Time Complexity: O(n) - where n is the size of the array.
    
    '''   
    print("\nInput array: {}".format(in_array)) 
    array_size = len(in_array)
    global_max = -maxsize - 1
    curr_max = 0
    start_index = 0
    end_index = 0
    curr_start_index = 0
 
    for i in range(array_size):
 
        curr_max += in_array[i]
 
        if global_max < curr_max:
            global_max = curr_max
            
            #we keep the indices whenever we get the maximum sum.
            start_index = curr_start_index
            end_index = i
        
        #When the sum of the subarray becomes less than zero we start with a new sum over a new interval.
        if curr_max < 0:
            curr_max = 0
            curr_start_index = i+1
    
    print("Maximum contiguous sum for test {} is: {}, contiguous subarray: {}.".format(test_id, global_max, in_array[start_index:end_index+1]))




#Test the solution
test_id = 0
for i in range(3):
    in_array= np.random.randint(-10,10,8)
    test_id += 1
    contiguousSubarraySum(in_array, test_id=test_id)


#Other tests
in_array = [8, 1, 5, -6, -2, -1]
test_id += 1
contiguousSubarraySum(in_array, test_id=test_id)


in_array = [-8, -1, -5, -6, -2, -1]
test_id += 1
contiguousSubarraySum(in_array, test_id=test_id)



