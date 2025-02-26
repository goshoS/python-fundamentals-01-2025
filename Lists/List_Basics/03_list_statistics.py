n = int(input())

positive_nums = []
negative_nums = []


for _ in range(n):
    nums = int(input())
    if nums >= 0:
        positive_nums.append(nums)

    elif nums < 0:
        negative_nums.append(nums)


print(positive_nums)
print(negative_nums)
print(f"Count of positives: {len(positive_nums)}")
print(f"Sum of negatives: {sum(negative_nums)}")