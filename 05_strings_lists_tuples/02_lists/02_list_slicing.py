fruits = ["Apple", "Banana", "Mango"]

fruits[0:2] = ["Melon", "Kiwi"]
print(fruits)


# sliding window technique
nums = [1, 2, 3, 4, 5, 6]

window_size = 3

for i in range(len(nums) - window_size + 1):
    window = nums[i:i+window_size]
    print(window)

