from itertools import combinations

class Solution:
    def maxLength(self, arr: List[str]) -> int:

# # generate all possible combinations of the strings in arr. For each combination, it concatenates the strings and checks if the concatenated string has all unique characters.
#         max_length = 0
#         # Generate all combinations of the array elements
#         for i in range(1,len(arr)+1):
#             for combo in combinations(arr,i):
#                 concat = ''.join(combo)
#                 if len(concat) == len(set(concat)):  # Check if all characters are unique
#                     max_length = max(max_length, len(concat))

#         return max_length

#Without creating combinations
        # Filtering duplicates
        arr = [ str for str in arr if len(str) == len(set(str))]

        # Helper function to check if characters are unique
        def isUnique(s1, s2):
            for char in s1:
                if char in s2:
                    return False
            return True
        # Backtracking function to try adding each string to the current combination
        def backtrack(index, current):
            max_length = len(current)

            for i in range(index, len(arr)):
                # if not set(arr[i]).intersection(set(current)):  # Check if characters are unique
                if isUnique(arr[i],current):
                    max_length = max(max_length, backtrack(i + 1, current + arr[i]))

            return max_length
        return backtrack(0, '')
   
        
