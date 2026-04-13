def two_sum(num, target):
    seen = {}
    for idx in range(len(num)):
        diff = target - num[idx]
        if diff in seen:
            return (seen[diff], idx)
        seen[num[idx]] = idx

print(two_sum([1,2,3,4,5], 6))