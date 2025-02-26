factor = int(input())
count = int(input())

lst = []

for number in range(1, count + 1):
    number *= factor
    lst.append(number)

print(lst)