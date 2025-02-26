numbers = list(map(int, input().split()))
remove_count = int(input())  

for _ in range(remove_count):  
    numbers.remove(min(numbers))

print(", ".join(map(str, numbers)))
