money_as_string = input().split(", ")
beggar_count = int(input())
money_as_int = []

for money in money_as_string:
    money_as_int.append(int(money))

beggar_profit = []
starting_index = 0

for current_beggar in range(beggar_count):
    current_beggar_sum = 0
    for current_index_of_money in range(starting_index, len(money_as_int), beggar_count):
        current_beggar_sum += money_as_int[current_index_of_money]
    beggar_profit.append(current_beggar_sum)
    starting_index += 1

print(beggar_profit)

