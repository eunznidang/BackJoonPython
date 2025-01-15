def solution(nums):
    answer = 0
    
    nums2=len(nums)/2
    nums=list(set(nums))
    if nums2>len(nums):
        answer=len(nums)
    else:
        answer=nums2
        
    return answer