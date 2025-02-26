repetitions = int(input())
lst_numbers = []

for _ in range(repetitions):
    current_number = int(input())
    lst_numbers.append(current_number)

command = input()

filtered_lst = []

if command == "even":
    for element in lst_numbers:
        if element % 2 == 0:
            filtered_lst.append(element)

elif command == "odd":
    for element in lst_numbers:
        if element % 2 != 0:
            filtered_lst.append(element)

elif command == "negative":
    for element in lst_numbers:
        if element < 0:
            filtered_lst.append(element)

elif command == "positive":
    for element in lst_numbers:
        if element >= 0:
            filtered_lst.append(element)

print(filtered_lst)