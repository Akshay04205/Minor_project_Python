def add(*numbers):
    total = numbers[0]
    for num in numbers[1:]:
        total += num
    return total

def sub(*numbers):
    total = numbers[0]
    for num in numbers[1:]:
        total -= num
    return total

def mul(*numbers):
    total = numbers[0]
    for num in numbers[1:]:
        total *= num
    return total

def div(*numbers):
    total = numbers[0]
    for num in numbers[1:]:
        total /= num
    return total


print("WELCOME TO CALCULATOR")
print("For addition (+) use 'add'")
print("For subtraction (-) use 'sub'")
print("For multiplication (*) use 'mul'")
print("For division (/) use 'div'")

operation = input("enter operation: ").lower()
numbers = list(map(float,input("Enter numbers seprated by space: ").split()))

if operation == "add":
    result = add(*numbers)
elif operation == "sub":
    result = sub(*numbers)
elif operation == "mul":
    result = mul(*numbers)
elif operation == "div":
    result = div(*numbers)
else:
    print("Invalid Input")
    exit()

print("Result: ",result)