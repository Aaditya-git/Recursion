from collections import defaultdict
def hasDuplicate(nums,k) -> bool:

    result = []
    fre = defaultdict(list)
    for item in nums:
        fre[item] = fre.get(item,0) + 1

    
    for num, count in fre.items():
            # fre.items() gives (key, value) pairs
        if count >= k:               # check if frequency is at least k
            result.append(num)       # add that number to result
    print(result)
if __name__ == "__main__":
    k  = 2
    nums=[1,2,1,2,1,2,3,1,3,2]
    hasDuplicate(nums,k)