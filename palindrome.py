# test = "racecar"

# Solution 1 - compare fist and last letter
# def palindrome(y):
#     y = str(y)
#     if y[0] == y[-1]:
#         print True
#     else:
#         print False
#
# palindrome(test)

# # Solution 2 - Reverse string
# def palindrome(y):
#     z = y[::-1]
#     if y == z:
#         print True
#     else:
#         print False
#
# palindrome(test)

# # Solution 3 - Slice and switch
# def palindrome(y):
#     n = len(y)
#     part_1 = y[:n//2]
#     part_2 = y[n-n//2:]
#     reverse_part_2 = part_2[::-1]
#     if part_1 == reverse_part_2:
#         print True
#     else:
#         print False
#
# palindrome(test)