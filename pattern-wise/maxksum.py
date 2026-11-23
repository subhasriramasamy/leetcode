nums = [1,5,4,2,9,9,9] 
k = 3 
n = len(nums)
i = 0
maxadd = 0
while i<n-k+1:
    if  nums[i] != nums[i+1] and nums[i+2] != nums[i] and nums[i+1] != nums[i+2]:
        add = nums[i] + nums[i+1] + nums[i+2]
        maxadd=max(maxadd,add)
        i+=1
    else:
        i+=1

print(maxadd)
            