# Backtracking
import random

# Initialize list of numbers and results
nums = [1, 2, 3]
results = []

print("Start: ")
print(f"Nums: {nums}");
print(f"Results: {results}");
print("");

# Backtracking algorithm to randomly select numbers from nums and add to results
print("Organizing numbers...");
while nums != []:
   ran = (random.choice(nums));
   results.append(ran);
   for item in results:
      if item in nums:
        del nums[nums.index(item)];
        print(f"Nums: {nums}");
        print(f"Results: {results}");
        break;
print("Numbers organized!");
print("");
print("Finish: ")
print(f"Nums left: {nums}");
print(f"Results: {results}");