'''
两数之和
'''
import random
from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        obj = {}
        for idx, element in enumerate(nums):
            another = target - element
            if another in obj:
                return [obj[another], idx]
            obj[element] = idx

def main():
    '''
    # case test
    >>> s = Solution()
    >>> s.two_sum([2, 7, 11, 15], 9)
    [0, 1]
    '''

if __name__ == "__main__":
    random.seed(1234) # for deterministic doctest output
    import doctest

    doctest.testmod()
