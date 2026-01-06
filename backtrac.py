# Backtracking approach to shuffle numbers until they are in the order [3, 2, 1]

def shuffle_backtracking(nums, results):
    # Base case: all numbers used
    if not nums:
        print(f"Checking: {results}")
        return results == [3, 2, 1]

    # Try each possible choice
    for i in range(len(nums)):
        choice = nums[i]

        # Choose
        results.append(choice)

        # Explore
        if shuffle_backtracking(nums[:i] + nums[i+1:], results):
            return True  # stop when solution is found

        # Un-choose (BACKTRACK)
        results.pop()

    return False

def shuffle():
    nums = [1, 2, 3]
    results = []

    print("Start:")
    shuffle_backtracking(nums, results)

    print("\nFinish:")
    print(f"Results: {results}")
    
shuffle()
