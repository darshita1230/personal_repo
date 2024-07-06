Array operations (Search, insert, delete)
# Example 1: Basic operations
my_list = [1, 2, 3]
my_list.append(4)            # [1, 2, 3, 4]
my_list.extend([5, 6])       # [1, 2, 3, 4, 5, 6]
my_list.insert(2, 'a')       # [1, 2, 'a', 3, 4, 5, 6]
my_list.remove('a')          # [1, 2, 3, 4, 5, 6]
removed_element = my_list.pop(3)  # [1, 2, 3, 5, 6], removed_element is 4
index_of_element = my_list.index(5)  # 3

# Example 2: List comprehensions
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]


# Maximum and minimum in an array
# Second largest in array
# Sum of array elements
# Reverse an Array

arr = [1, 2, 10, 3, 4, 5, 9, 20, 20]
arr.sort()
print(arr[0], arr[-1], arr[-2])
print(sum(arr))
arr.reverse()
print(arr)
#reverse fn
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l = 0
h = len(nums) - 1
while l < h:
    nums[l], nums[h] = nums[h] , nums[l]
    l += 1
    h -= 1
print(nums)

#binary search
l = 0
h = len(nums) - 1
t = 7
while l <= h:
    mid = l + (h-l)//2
    if nums[mid] == t:
        print(mid)
    else if nums[mid] > t:
        h = mid - 1
    else if nums[mid] < t:
        l = mid + 1
