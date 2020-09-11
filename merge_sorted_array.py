'''
1 = [1,4,6]
2 = [2]
1 = [1,2,4,6]
'''
nums1 = [8,4,6,1]
nums2 = [10,12,2]
position_saved = 0
# sorting the array
nums1.sort()
# nums2.sort()
print(nums2)
for j in range(len(nums2)):
    # compare it with nums 2 element
    for i in range(len(nums1)):
        
        if nums2[j]>=nums1[i]:
            position_saved = i
    nums1.insert(position_saved+1,nums2[j])

print(nums1)

