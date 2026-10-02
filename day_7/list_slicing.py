nums = [10, 2, 3, 5]
letters = ["A", "V", "C", "D", "E", "F", "G"]
nums_2 = nums[:] #

word = "Hello world"

word_sliced = word[1:3]

print(word_sliced)

nums_3 = nums[0:2] #[start:end] array slicing

letters_sliced = letters[1:5:2] #[start:end:step]

letters_reversed = letters[::-1] #Reversing an array

print("Reversed array - ", letters_reversed)

print(letters_sliced)

print(nums_3)

nums.append(200)

print(nums_2)