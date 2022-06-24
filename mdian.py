test_list = [3, 7, 9, 9, 10, 20]
  
# printing list
print("The original list : " + str(test_list))
  
# Median of list
# Using loop + "~" operator
test_list.sort()
mid = len(test_list) // 2
res = (test_list[mid] + test_list[~mid]) / 2
  
# Printing result
print("Median of list is : " + str(res))
