
def backtrack(nums, path, used, results):
    if len(path) == len(nums):
        results.append(path[:])
        return
    for num in nums:
        if num in used:
            continue
        path.append(num)
        used.add(num)
        backtrack(nums, path, used, results)
        path.pop()
        used.remove(num)

def permute(nums):
    path = []
    results = []
    used = set()
    backtrack(nums, path, used, results)
    return results

print(permute([1,2,3]))

print(permute([1,2,3,4]))
