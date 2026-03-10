# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

 

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order
# -----------------------------------------번역

# 정수가 들어있는 배열 nums가 비내림차순(non-decreasing order) 으로 정렬되어 있다.

# 배열에서 중복된 값을 제자리(in-place)에서 제거하여 각 고유한 값이 한 번만 나타나도록 만들어라.

# 또한 원소들의 상대적인 순서는 유지되어야 한다.

# 배열 nums에서 고유한 원소의 개수를 k라고 할 때,
# 중복을 제거한 뒤 고유한 원소의 개수 k를 반환하라.

# 중복 제거 후:

# 배열 nums의 앞쪽 k개의 원소에는
# 정렬된 상태의 고유한 값들이 들어 있어야 한다.

# k - 1 이후의 인덱스에 있는 값들은 무엇이 들어 있어도 상관없다.

# 채점 방식 (Custom Judge)

# 채점기는 다음과 같은 코드로 여러분의 함수를 테스트한다.

# int[] nums = [...]; // 입력 배열
# int[] expectedNums = [...]; // 정답 배열

# int k = removeDuplicates(nums); // 여러분의 함수 호출

# assert k == expectedNums.length;

# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }

# 모든 조건을 통과하면 정답으로 인정된다.

# 예제 1

# 입력

# nums = [1,1,2]

# 출력

# 2, nums = [1,2,_]



# 예제 2

# 입력

# nums = [0,0,1,1,1,2,2,3,3,4]

# 출력

# 5, nums = [0,1,2,3,4,_,_,_,_,_]


# nums = [0,0,1,1,1,2,2,3,3,4]

# class Solution(object):
#     def removeDuplicates(self, nums):
#        memory = 0
#        for i in range(len(nums)):
#            if i == 0:
#                memory = nums[i]
#            elif memory == nums[i]:
#                nums[i] = '_'
#            else:
#                memory = nums[i]
               
       
       
#        new_idx = 0
#        for i in range(len(nums)):
#            if nums[i] != '_':
#                nums[new_idx],nums[i] = nums[i],nums[new_idx]
#                new_idx +=1
#        return new_idx
nums = [0,0,1,1,1,2,2,3,3,4]

class Solution(object):
    def removeDuplicates(self, nums):
        memory = 0
        for i in range(len(nums)):
            if i == 0:
                memory = nums[i]
            elif memory == nums[i]:
                nums[i] = '_'
            else:
                memory = nums[i]

        new_idx = 0
        for i in range(len(nums)):
            if nums[i] != '_':
                nums[new_idx], nums[i] = nums[i], nums[new_idx]
                new_idx += 1
        return new_idx


solution = Solution()
k = solution.removeDuplicates(nums)

print("정답:", k)
print("배열:", nums)
#  def removeDuplicates(nums):
#     if not nums:
#         return 0

#     slow = 0

#     for fast in range(1, len(nums)):
#         if nums[fast] != nums[slow]:
#             slow += 1
#             nums[slow] = nums[fast]

#     return slow + 1      ai