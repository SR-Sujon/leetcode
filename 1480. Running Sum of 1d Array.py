class solutions:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            if((i+1) == len(nums)):
                break
            else:
                nums[i+1] = nums[i]+nums[i+1]
        return nums

# Taking-Inputs
lst = []
# number of elements as input
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
    element = int(input())
    lst.append(element) # adding the element

# Showing-Output
output = []
soln = solutions() #object creation
output = soln.runningSum(lst)
print(output)