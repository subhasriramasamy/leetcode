height = [0,1,0,2,1,0,1,3,2,1,2,1]

n = len(height)
left = 0
right = n-1
maxleft = height[left]
maxright = height[right]
water = 0

while left < right:
    if maxleft<maxright:
        left +=1
        maxleft = max(maxleft, height[left])
        water+= maxleft - height[left]

    else:
        right -=1
        maxright = max(maxright, height[right])
        water += maxright - height[right]

print(water)




'''BRUTE FORCE APPROACH
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

n = len(height)
water = 0

for i in range(0,n):
    leftm =0
    rightm = 0

    for j in range(0,i+1):
        leftm = max(leftm, height[j])


    for j in range(i,n):
        rightm = max(rightm, height[j])

    water += min(leftm,rightm)- height[i]


print(water)
O(n^2) time complexity and O(1) space complexity DUE TO THE USE OF TWO LOOPS 
BUT THE PROBLEM STATES THAT THE TIME COMPLEXITY SHOULD BE O(n) AND SPACE COMPLEXITY SHOULD BE O(1)
THEREFORE THE TWO POINTER METHOD IS USED ABOVE THIS CODE
'''
        
