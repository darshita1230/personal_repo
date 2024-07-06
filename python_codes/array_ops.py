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
