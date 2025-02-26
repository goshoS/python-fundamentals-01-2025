string_of_nums = input().split()
inverted_list = []

for nums in string_of_nums:
    inverted_num = -int(nums)
    inverted_list.append(inverted_num)

print(inverted_list)