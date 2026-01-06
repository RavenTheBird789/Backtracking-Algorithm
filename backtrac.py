# Shuffling Permutation For Recursive Shuffle (Backtracking)
import random
import time

def shuffle():
   # Initialize list of numbers and results
   nums = [1, 2, 3]
   results = []

   print("Start: ")
   print(f"Nums: {nums}");
   print(f"Results: {results}");
   print("");

   # Shuffling Permutation algorithm to randomly select numbers from nums and add to results
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

   if results != [3, 2, 1]:
       print("Solution Is Not Reversed, Reshuffling...");
       time.sleep(2);
       shuffle();
   else:
      print("Successfully Shuffled In Reversed!");
shuffle();
