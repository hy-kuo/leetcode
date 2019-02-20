class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        l1 = len(nums1)
        l2 = len(nums2)
        if (l1 + l2)%2==0:
            p = [int((l1+l2)/2)-1, int((l1+l2)/2)] 
        else:
            p = [int((l1+l2+1)/2 - 1)]
            
        i = 0
        j = 0
        m = []
        while i+j < (l1+l2+1)/2:
            if i < l1 and j < l2:
                if nums1[i] <= nums2[j]:
                    m.append(nums1[i])
                    i+=1
                else:
                    m.append(nums2[j])
                    j+=1
            elif i >= l1:
                m.append(nums2[j])
                j += 1
            elif j >= l2:
                m.append(nums1[i])
                i += 1
        if len(p) < 2:
            median = m[p[0]]
        else:
            median = (m[p[0]] + m[p[1]]) / 2
        return median