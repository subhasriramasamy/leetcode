class Solution:
    def twoSum(numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        left =0
        right = n-1
        while left < right:
            
            if numbers[left]+ numbers[right]==target:
                return [left+1,right+1]
            elif numbers[left]+ numbers[right] > target:
                right = right - 1
            elif numbers[left]+ numbers[right] < target:
                left = left + 1
            else:
                return -1

    numbers = [2,3,4,5]
    target = 6
    print(twoSum(numbers, target))
    
#learned at 16/11/26
#o(n) time complexity due to the while loop and o(1) space complexity since we are not using any extra space
#hash method is used in the 2sum problem but here we are using the two pointer method since the array is pre-sorted


'''
ReCap

class Solution:
    def twoSum(numbers: list[int], target: int) -> list[int]:
        
        n = len(numbers)
        left = 0
        right = n-1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1,right+1]
            elif numbers[left] + numbers[right] < target:
                left = left + 1
            elif numbers[left] +numbers[right] > target:
                right = right - 1
                return -1

    numbers = [1,2,3,6]
    target = 5
    print(twoSum(numbers, target))
    

        
   '''             