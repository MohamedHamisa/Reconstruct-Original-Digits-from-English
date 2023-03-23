class Solution:
    def originalDigits(self, s):
        from collections import Counter
        c = Counter(s)
        nums = [0] * 10
        nums[0] = c['z']
        nums[2] = c['w']
        nums[4] = c['u']
        nums[6] = c['x']
        nums[8] = c['g']
        nums[1] = c['o'] - nums[0] - nums[2] - nums[4]
        nums[3] = c['h'] - nums[8]
        nums[5] = c['f'] - nums[4]
        nums[7] = c['s'] - nums[6]
        nums[9] = c['i'] - nums[5] - nums[6] - nums[8]
        return ''.join(str(i) * n for i, n in enumerate(nums))
