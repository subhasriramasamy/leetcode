nums = [2,0,2,1,1,0]

n = len(nums)

low = 0
mid = 0
high = n-1

while mid <=high:
    if nums[mid] == 0:
        nums[mid] = nums[low]
        nums[low] = 0
        mid += 1
        low+=1
    elif nums[mid] == 1:
        mid = mid +1

    else:
        nums[mid] = nums[high]
        nums[high] = 2
        high = high - 1

print(nums)