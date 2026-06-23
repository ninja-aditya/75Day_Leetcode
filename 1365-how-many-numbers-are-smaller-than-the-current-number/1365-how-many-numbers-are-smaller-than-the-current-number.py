class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer = []
        for i in nums:
            c = 0 
            for j in nums:
                if j<i:
                    c+=1
            answer.append(c)
        return answer