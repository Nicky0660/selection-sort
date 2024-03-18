# selection_sort.py

# ________________________________________________________________________________________
# Mutates original arr to being sorted

# def selection_sort(arr):
#     arr.sort()
#     return arr

# print('expecting: [-1,0,1]')
# print('=>', selection_sort([0,1,-1]))

# ________________________________________________________________________________________
# Does not mutate original array

def selection_sort(arr):
    sortedArr = sorted(arr)
    return sortedArr

print('expecting: [-1, 0, 1]')
print('=>', selection_sort([0,1,-1]))

print('\n')

print('expecting:[]')
print('=>', selection_sort([]))

print('\n')

print('expecting: [1]')
print('=>', selection_sort([1]))

print('\n')

print('expecting: [-10, -8, -6, -4, -2, -1]')
print('=>', selection_sort([-6, -4, -10, -1, -8, -2]))

print('\n')

print('expecting: [1, 1, 2, 2, 3, 10]')
print('=>', selection_sort([3,10, 1,2,1,2]))

# BenchMark and print average runtime
import time
import random

def generate_random_array(size):
    return [random.randint(-10000, 10000) for _ in range(size)]

def benchmark_sorting_function(func, array_size, num_trials):
    test_array = generate_random_array(array_size)

    start_time = time.time()

    for _ in range(num_trials):
        _ = func(test_array.copy())

    end_time = time.time()

    average_runtime = ((end_time - start_time) / num_trials) * 1000
    return average_runtime

array_size = 1000
num_trials = 100

average_runtime = benchmark_sorting_function(selection_sort, array_size, num_trials)
print(f"Average runtime for sorting an array of size {array_size} over {num_trials} trials: {average_runtime} ms.")

# psuedocode

# Function selection_sort(arr)
#     - Create a variable 'sortedArr' and assign it the result of calling sorted(arr)
#     - Return 'sortedArr'

# Function generate_random_array(size)
#     - Initialize an empty list 'arr'
#     - Loop from 0 up to 'size':
#         - Append a random integer between -10000 and 10000 to 'arr'
#     - Return 'arr'

# Function benchmark_sorting_function(func, array_size, num_trials)
#     Inputs:
#         - func: the sorting function to be benchmarked
#         - array_size: the size of the array to sort in each trial
#         - num_trials: the number of trials to run

#     - Initialize 'test_array' by calling generate_random_array with 'array_size'
#     - Record the current time in 'start_time'
#     - Loop 'num_trials' times:
#         - Copy 'test_array' and apply 'func' to the copied array
#     - Record the current time in 'end_time'
#     - Calculate 'average_runtime' as (end_time - start_time) / num_trials, converted to milliseconds
#     - Return 'average_runtime'

# - Set 'array_size' to 1000 and 'num_trials' to 100
# - Call benchmark_sorting_function with selection_sort, 'array_size', and 'num_trials'
# - Print the 'average_runtime'
