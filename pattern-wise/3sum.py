nums = [-1,0,1,2,-1,-4]

nums.sort()
res = []
n = len(nums)

for i in range(0, n-2):
    if i> 0 and nums[i]== nums[i-1]:
        continue
    
    l = i+1
    r = n-1
    while l<r:
        summ = nums[i]+nums[l] + nums [r]
        if summ == 0:
            res.append([nums[i],nums[l],nums[r]])
            while l<r and nums[l]==nums[l+1]:
                l=l+1
            while l<r and nums[r]==nums[r-1]:
                r=r-1
            l = l+1
            r = r - 1

        elif summ< 0:
            l = l+1

        else:
            r = r-1

print(res)
# time complexity is O(n^2) since we are using two loops and space complexity is O(1) since we are not using any extra space



'''
BRUTE FORCE METHOD :
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        l=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if nums[i]+nums[j]+nums[k]==0 and i!=j and j!=k and i!=k:
                        l.append([nums[i],nums[j],nums[k]])

        r=[]
        for i in l:
            r.append(sorted(i))

        print(r)
        ans=[]
        for i in r:
            if i not in ans:
                ans.append(i)

        return ans
        

        
        '''           


        
                