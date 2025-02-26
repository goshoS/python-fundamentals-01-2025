n = int(input())
word = input()
lst_of_strings = []
filtered_lst = []


for _ in range(n):
    strings = input()
    lst_of_strings.append(strings)

    if word in strings:
        filtered_lst.append(strings)

print(lst_of_strings)
print(filtered_lst)