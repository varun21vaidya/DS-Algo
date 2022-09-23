# # summation of first N numbers @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#  # parameterized way: TC:O(n) SC:O(n)
# def summation(n, summ):
#     if n < 1:
#         print("parameterized sum is ", summ)
#         return
#     summation(n-1, summ+n)

# summation(3, 0)


# # functinal way: TC:O(n) SC:O(n)
# def summation(n):
#     if n < 1:
#         return 0
#     return n+summation(n-1)

# print("functional sum is ", summation(3))


# # factorial of N: TC:O(n) SC:O(n)
# def facto(n):
#     if n<2:
#         return 1
#     return n*facto(n-1)

# n=5
# print("factorial of",n,"is equal to" ,facto(n))


# # reverse an Array: @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# # USING LOOPS

# arr=[2, 5, 8, 12, 23]
# for i in range(len(arr)//2):
#     arr[i],arr[len(arr)-1-i]=arr[len(arr)-1-i],arr[i]
# print("using for loop", arr)


# arr=[2, 5, 8, 12, 23,45]
# i,j=0,len(arr)-1
# while i<j:
#     arr[i],arr[j]=arr[j],arr[i]
#     i+=1
#     j-=1
# print("using while",arr)


# # USING RECURSION


# # WITH NEW ARRAY
# def reverser(arr,newarr):
#     if len(arr)==0: return
#     newarr.append(arr[len(arr)-1])
#     reverser(arr[:len(arr)-1],newarr)
#     return newarr
# arr=[2, 5, 8, 12, 23]
# newArr=[]
# print("using recursion with new arr",reverser(arr,newArr))


# # WITHOUT NEW ARRAY (Standard Approach)
# def reverse_recursion(arr,i=0):
#     if i>=len(arr)//2: return
#     arr[i],arr[len(arr)-1-i]=arr[len(arr)-1-i],arr[i]
#     # print("iteration",i,arr)
#     reverse_recursion(arr,i+1)
#     return arr
# arr=[1,2,3,4,5,6]
# print("using recursion",reverse_recursion(arr))


# # String Palindrome @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def pali_check(st,i=0):
#     # if index goes beyond half that means its palindrome
#     if i>=len(st)//2: return True
#     if st[i]==st[len(st)-1-i]:
#         return pali_check(st,i+1)
#     else:
#         return False
# st= "NAYAN"
# st2="1251"
# print(st,pali_check(st))
# print(st2,pali_check(st2))


# Fibonacci Number @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def fibo(n):
#     if n<2:
#         return n
#     return fibo(n-1)+fibo(n-2)

# n=6
# print(n,"th fibonacci number is",fibo(n))

# now when there was single recursion call,
# Complexity was TC:O(n) SC:O(n)
# but as there are two recursion calls,
# these two will call two more recursion calls
# So complexity will be Exponential ie, TC:O(2^n) (well not exact but general)
# And as maximum height of recursive tree is n, SC:O(n)


# Print All Subsequences @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# subsequence: a contigeous | non-contigeous sequence which follows the order

# arr=[3,1,2]
# contigeous = [3,1,2,(3,1),(1,2),(3,1,2)] # these are also subarrays
# non-contigeous= [(3,2)]
# but all in all order has to be maintianed

# USING POWER SET ALGORITHM (ie. BIT MANIPULATION)  (IMP**)

# eg S='abc' --> "",a,b,c,ab,ac,bc,abc
# So if length of string is n, number of substrings generated are 2^n ***

# fundametal to check if bit is set or not
# suppose for number 4 --> 1 0 0 --> 0th bit=0, 1st bit =0, 2nd bit=1
# so to check if 2nd bit is set or not
# n & (1<<i), n=4 and i=2 for 2nd bit
# so if this gives non-zero number its set else its not set
# so if n & (i<<1)!=0  op=> set

# now for string of length n
# now for each number from 0 to 2^n -1 we will loop (2^n => (1<<n))
# and for each of that number we check if any of its bit is set or not
# if yes then add the value of that bit from original string

# eg for length of 3 ie abc where a=>0th bit, b=> 1st bit, c=>2nd bit
# 0 000 --> ""
# 1 001 --> a
# 2 010 --> b
# 3 011 --> ab
# 4 100 --> c
# 5 101 --> ac
# 6 110 --> bc
# 7 111 --> abc


# TC: O(2^n * n) SC: O(1)
# S="abc"
# n=len(S)
# for num in range((1<<n)):
#     sub=""
#     for i in range(n):
#         if num & (1<<i):
#             sub+=S[i]
#     print(sub)

# for GFG: https://practice.geeksforgeeks.org/problems/power-set4302/1

# TC: O(2^n * n) SC: O(n)
# def AllPossibleStrings(self, s):
#     # Code here
#     n=len(s)
#     res=[]
#     for num in range(1<<n): # (2^n => (1<<n)) TC:O(2^n)
#         sub=""
#         for i in range(n):                    TC: O(n)
#             if num & (1<<i):
#                 sub+=s[i]
#         res.append(sub)
#     return sorted(res)[1:]


# USING RECURSION*****

# arr=[3,1,2] give all its subsequences

# for recursion we will use 2 parameters
# index to iterate, result for each subsequence
# For recursion the main condition we will first check
# if index we are increasing with each recursion tree
# is equal or greater than length of arr then print the resultant arr
# then take next value and append in result and use recursion
# now we also need to take conditions without that Value
# so remove that value from result and again use recursion
# this will use recursion until reaches end of index and check all conditions
# ad print all the subsequences

# TC: O(2^n) the recursion tree will need 2^n outputs
# SC: O(n) due to recursion stack
# as height of recursion tree will be same as lenght of input arr

# def printSubsequence(ind, arr,res):

#     if ind>=len(arr):
#         print(res)
#         return

#     # take value and use recursion
#     res.append(arr[ind])
#     printSubsequence(ind+1,arr, res)

#     # remove value and use recursion
#     res.remove(arr[ind])
#     printSubsequence(ind+1,arr, res)

# # Function call
# arr=[3,1,2]
# printSubsequence(0,arr,[])


# # Printing Subsequences whose sum is K @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# def printKSubsequence(ind, arr,res,k):

#     if ind>=len(arr):
#         if sum(res)==k:
#             print(res)
#         return

#     # take value and use recursion
#     res.append(arr[ind])
#     printKSubsequence(ind+1,arr, res,k)

#     # remove value and use recursion
#     res.remove(arr[ind])
#     printKSubsequence(ind+1,arr, res,k)

# # Function call
# arr=[1,2,1]
# printKSubsequence(0,arr,[],2)


# # Printing Subsequences whose sum is K but Only 1 value @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# # so when we get a value we return true
# # and when we get that value from a recursion == true
# # we will return true else false

# # in this sum => (s) is calculated along the way, either method is ok

# def printKSubsequence(ind, arr, res, k, s):

#     if ind >= len(arr):
#         if s == k:
#             print(res)
#             return True
#         else:
#             return False

#     # take value and use recursion
#     res.append(arr[ind])
#     s += arr[ind]
#     if (printKSubsequence(ind+1, arr, res, k, s) == True):
#         return True

#     # remove value and use recursion
#     res.remove(arr[ind])
#     s -= arr[ind]
#     if (printKSubsequence(ind+1, arr, res, k, s) == True):
#         return True

#     return False


# # Function call
# arr = [1, 2, 1]
# printKSubsequence(0, arr, [], 2, 0)


# # Count number of Subsequences whose sum is K @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# # in this sum => (s) is calculated along the way

# # so for such problem where just count is enough
# # there is basic pattern

# # fn(){

# #     base case:
# #     true return 1
# #     false return 0

# #     call the left function
# #     l= f()

# #     call the right function
# #     r= f()

# #     return l+r
# # }

# # *******************************
# # (for multiple recursion calls, loop from 1 to n and before that s=0
# # and add the return values s+=f() and return s) USED FOR DP like N queens


# def printKSubsequence(ind, arr, k, s):

#     # s is sum variable like temp which we use to compare with
#     # k ie target sum

#     # if index reaches last element of array and if sum is equal to k
#     # return 1 which will increase the count cz we have found one subsequence
#     # if not return 0


#     # append one Element in sum and use recursion with increased index
#     # after adding this number if there is matched subsequence
#     # increase the count of left variable ie l

#     # after that remove that Element, and again use recursion to
#     # find another subsequence without that number
#     # if found it will increase count of right variable

#     # add both counts and return result


#     if ind >= len(arr):
#         if s == k:
#             return 1
#         else:
#             return 0

#     s += arr[ind]
#     l= printKSubsequence(ind+1, arr, k, s)

#     s -= arr[ind]
#     r= printKSubsequence(ind+1, arr, k, s)

#     return l+r


# # Function call
# arr = [1, 2, 1]
# print(printKSubsequence(0, arr, 2, 0))


# Combination Sum @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# https://leetcode.com/problems/combination-sum/

# so as this problem contains the structure of array of digits leading to target sum
# so similar to subsequnce problems we can use recursion by increasing index
# and adding a number calculating with recursion if its included in any subsequence
# then removing the same number and calculating recursion for matching subsequences
# without that number both conditions with increasing index untill lenght of original array

# now for this problem we are allowed to use same number unlimited times
# so we have to remember that we have to include same number in recursion
# by keeping the same index
# but to avoid the infinite loop, we have to reduce the target with that number
# and also check if that number is still less than target
# cz if target become less than current number, it will become negative

# now we have tried adding the same number few times now
# if the target value is equal to zero, we will add the temp arr ie subsequence
# to the resultant array which will give output

# but if the target becomes less than current value,
# we will avoid further recursion with that number and increase index
# but before that remember to remove the element after previous recursion ended

# so recursion will flow like this
# first declare global result array
# call the function with temp= empty array and ind=0 along with arr and target

# if the base condition ie ind is equal to len(arr)
# and target becomes zero (as we are reducing target in recursion)
# copy of temp will be stored in result array

# the value at index if less than target will be added to temp
# and use recursion with target - that value and keep index same
# now after all those inside recursions when the recursion ends
# remove the last added value
# and use recursion for next index

# at the end we will get result array


# def Combination_sum(ind, arr, target, temp):

#     # base condition
#     if ind == len(arr):
#         if target == 0:
#             # print("inserted",temp)
#             final.append(temp[:])
#         return

#     if arr[ind] <= target:
#         temp.append(arr[ind])
#         # print(temp)
#         Combination_sum(ind, arr, target-arr[ind], temp)
#         temp.pop()
#         # print("popped",temp)
#     Combination_sum(ind+1, arr, target, temp)


# candidates = [2, 3, 6, 7]
# target = 7
# final = []
# Combination_sum(0, candidates, target, [])
# print(final)


# # Combination Sum 2 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# # problem link: https://leetcode.com/problems/combination-sum-ii/

# def combinationSum2(candidates, target):
#     def helper(ind, tempArr, target, res):

#         if target == 0:
#             res.append(list(tempArr))
#             return

#         for i in range(ind, len(candidates)):

#             # imp condition to avoid duplicates as for same numbers
#             # like 1 1 1 2 2, for recursion tree first 1 will start
#             # when it moves it doesnot matter if its first one or second one
#             # so only initial one is enough so it checks
#             # if i>ind ie its not first one and is same as previous one then skip it
#             if (i > ind and candidates[i] == candidates[i-1]):
#                 continue

#             if candidates[i] > target:
#                 break

#             tempArr.append(candidates[i])
#             helper(i+1, tempArr, target-candidates[i], res)
#             tempArr.pop()

#     candidates.sort()
#     res = []
#     helper(0, [], target, res)
#     return res


# candidates = [10, 1, 2, 7, 6, 1, 5]
# target = 8
# print(combinationSum2(candidates, target))


# # Subset Sum 1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# # problem link: https://practice.geeksforgeeks.org/problems/subset-sums2234/1

# # a subset is subsequnce plus empty set


# # TC: O(2^n*n) SC: O(n) extra n in tc due to 'sum'
# def helper(ind, arr, res, temp):

#     if ind >= len(arr):
#         res.append(sum(temp))
#         return

#     temp.append(arr[ind])
#     helper(ind+1, arr, res, temp)

#     temp.pop()
#     helper(ind+1, arr, res, temp)


# arr = [3, 2, 1]
# ind, temp, res = 0, [], []
# helper(ind, arr, res, temp)
# print(sorted(res))


# # TC: O(2^n) SC: O(n) #instead of keeping array we just need sum value
# def helper(ind, arr, res, temp):

#     if ind >= len(arr):
#         res.append(temp)
#         return

#     # pick the element
#     # temp += arr[ind]
#     # helper(ind+1, arr, res, temp)

#     # not pick the element
#     # temp -= arr[ind]
#     # helper(ind+1, arr, res, temp)

#     # or this can be shortened by directly adding for that specific recursive call
#     # for next call, not add it ie not pick it

#     helper(ind+1, arr, res, temp+arr[ind])

#     helper(ind+1, arr, res, temp)


# arr = [3, 2, 1]
# ind, temp, res = 0, 0, []
# helper(ind, arr, res, temp)
# print(sorted(res))


# # Sub Sets 2 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# # problem link:https://leetcode.com/problems/subsets-ii/

# # # TC: O(n*2^n) SC: O(n) #extra time for conversion to tuple
# def helper(ind, arr, res, temp):
#     if ind >= len(arr):
#         res.add(tuple(temp[:]))
#         return
#     temp.append(arr[ind])
#     helper(ind+1, arr, res, temp)
#     temp.pop()
#     helper(ind+1, arr, res, temp)

# ind, res, temp = 0, set(), []
# nums.sort()
# helper(ind, nums, res, temp)
# return res


# # Without Using set ie without extra N

# def helper(ind, temp):
#     # when recursion is called temp is added to resultant array
#     res.append(temp.copy())

#     for i in range(ind, len(nums)):
#         if i != ind and nums[i] == nums[i-1]:
#             continue

#         temp.append(nums[i])
#         helper(i+1, temp)
#         temp.pop()


# nums = [1, 2, 2]
# nums.sort()
# ind, res, temp = 0, [], []
# helper(ind, temp)
# print(res)


# # Permutations @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# # Problem link: https://leetcode.com/problems/permutations/


# #         first of all we need a temp arr to store each permutation
# #         and we will also need a way to keep track of which number is already in temp
# #         so we will use map to check if its in temp arr or not

# #         so when we add a number in temp we will set its map value to 1
# #         and after recursions we will reduce it to 0 when we pop from temp

# #         so flow will be as follows
# #         before that define base case which will be
# #         if the len of temp is equal to input arr, its a permutation
# #         now we will loop through each number to check if its in temp arr using mapp
# #         if its not there append it to temp, and set its value in map as 1
# #         then to append the next set of digits call recursion with updated temp and mapp
# #         when all numbers are added base condition will be satisfied
# #         store that permutation and return to exit that recursion call
# #         for next permutation we will need to rearrange the digits
# #         so pop the recent digit and set its value as 0 in mapp

# #         now this loop will continue and recursion will move
# #         and we will get all permutations

# # TC: O(n!*n) permutations and loop
# # SC: O(n) to store the temp arr + depth of recursion tree

# def permute(nums):

#         def helper(temp,mapp):
#             if len(temp)==len(nums):
#                 return res.append(temp[:])

#             for i in nums:
#                 if not mapp[i]:
#                     temp.append(i)
#                     mapp[i]=1
#                     helper(temp,mapp)
#                     x=temp.pop()
#                     mapp[x]-=1


#         temp,mapp=[],{i:0 for i in nums}
#         res=[]
#         helper(temp,mapp)
#         return res

# nums=[1,2,3]
# print(permute(nums))
# # OP: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


#         now we can also solve this question without using extra map
#         instead we can just swap the digits in nums arr
#         for each level we will asign an index with which other digits will be swapped
#         and to swap all these index with specified index
#         we will loop from that index to len of nums
#         and after each swap call recursively for next level of index

#         now when these index will cross the len of nums we will store that permutation

#         and imp that we also have to reswap after each recursion
#         like we used to do pop from the temp arr after recursion

# TC: O(n!*n) permutations and loop
# SC: O(n)+O(n) addition to res arr + recursion tree

# def permute(nums):
#     def helper(ind,nums):
#         if ind>=len(nums):
#             # print(nums)
#             res.append(nums.copy())
#             return
#         for i in range(ind,len(nums)):
#             nums[ind],nums[i]=nums[i],nums[ind]
#             helper(ind+1,nums)
#             nums[ind],nums[i]=nums[i],nums[ind]

#     res=[]
#     helper(0,nums)
#     return res


# nums=[1,2,3]
# print(permute(nums))
# # OP: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


# N - QUEENS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# # Problem-link
# # ans link by striver: https://takeuforward.org/data-structure/n-queen-problem-return-all-distinct-solutions-to-the-n-queens-puzzle/


# def solveNQueens(n):

#     def checker(row, col, board, n):

#         r,c=row,col

#         # check left side
#         while (c>=0):
#             if board[r][c]=="Q":
#                 return False
#             c-=1

#         # check left upward side
#         r,c=row,col

#         while (r>=0 and c>=0):
#             if board[r][c]=="Q":
#                 return False
#             c-=1
#             r-=1

#         # check left downward side
#         r,c=row,col
#         while (r<n and c>=0):
#             if board[r][c]=="Q":
#                 return False
#             c-=1
#             r+=1
#         return True

#     def queens(col,board,n):

#         if col==n:
#             # print(board)
#             ans.append(["".join(i) for i in board])
#             return

#         for row in range(n):
#             if checker(row,col,board,n):
#                 board[row][col]="Q"
#                 queens(col+1,board,n)
#                 board[row][col]="."

#     board=[["." for i in range(n)] for j in range(n)]
#     # print(board)
#     ans=[]
#     queens(0,board,n)
#     return ans

# n=4
# print(solveNQueens(n))


# # Optimized version where we can store the left_side, left_downwards, and left_upwards in array

# def solveNQueens(n):

#     def queens(col,board,n):

#         if col==n:
#             # print(board)
#             ans.append(["".join(i) for i in board])
#             return

#         for row in range(n):
#             if not left_side[row] and\
#             not left_downwards[row+col] and\
#             not left_upwards[(col-row)]:

#                 board[row][col]="Q"

#                 left_side[row]=1
#                 left_downwards[row+col]=1
#                 left_upwards[(col-row)]=1

#                 queens(col+1,board,n)
#                 board[row][col]="."

#                 left_side[row]=0
#                 left_downwards[row+col]=0
#                 left_upwards[(col-row)]=0

#     board=[["." for i in range(n)] for j in range(n)]
#     left_side=[0 for i in range(n)]
#     left_downwards=[0 for i in range(2*n-1)]
#     left_upwards=[0 for i in range(2*n-1)]
#     # print(board)
#     ans=[]
#     queens(0,board,n)
#     return ans

# n=4
# print(solveNQueens(n))
