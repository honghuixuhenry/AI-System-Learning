def partition(nums, left, right):
    pivot = nums[right]
    i = left - 1
    for j in range(left, right):
        if nums[j] < pivot:
            i +=1 
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[right] = nums[right], nums[i+1]
    return i+1 

def quick_sort(nums, left, right):
    if left < right:
        pivot = partition(nums, left, right)
        quick_sort(nums, left, pivot-1)
        quick_sort(nums, pivot+1, right)

nums = [7,4,9,2,5]
quick_sort(nums, 0, 4)
print(nums)