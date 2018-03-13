import heapq

def kthLargestElement(nums, k):
    h = nums[:k]
    heapq.heapify(h)
    for x in nums[k:]:
        heapq.heappushpop(h, x)
    return h

