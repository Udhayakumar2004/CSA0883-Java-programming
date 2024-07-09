def find_duplicate(nums):
    # Phase 1: Finding the intersection point of the two runners.
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    # Phase 2: Finding the entrance to the cycle.
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare

# Example usage
nums = [1, 3, 4, 2, 2]
result = find_duplicate(nums)
print("Output:", result)  # Output: 2
