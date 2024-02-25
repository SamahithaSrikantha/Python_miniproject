import random
import time

def linear_search(arr, target):
    """Linear search algorithm."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target, low=None, high=None):
    """Binary search algorithm."""
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1
    if high < low:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

if __name__ == '__main__':
    array_length = 10000
    sorted_array = sorted(random.sample(range(-3 * array_length, 3 * array_length), array_length))
    
    start = time.time()
    for target in sorted_array:
        linear_search(sorted_array, target)
    end = time.time()
    linear_avg_time = (end - start) / array_length
    print("Linear search time: ", linear_avg_time, "seconds")
    
    start = time.time()
    for target in sorted_array:
        binary_search(sorted_array, target)
    end = time.time()
    binary_avg_time = (end - start) / array_length
    print("Binary search time: ", binary_avg_time, "seconds")
