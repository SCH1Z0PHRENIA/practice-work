n = len(nums)

for i in range(n):
    for j in range(0, n - i - 1):          
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

  return nums[]

unsorted_list = [87, 34, 566, 12, 900, 45, 862, 345]
sorted_list = bubble_sort(unsorted_list)
print("Sorted array:", sorted_list)