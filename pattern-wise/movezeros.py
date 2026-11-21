nums = [0,1,0,3,12]

n = len(nums)
l = 0

for r in range(n):
    if nums[r] != 0:
        nums[l],nums[r]=nums[r],nums[l]
        l+=1

print(nums)
