SENTINEL = -99  

print("Enter numbers to sum, or enter", SENTINEL, "to quit.")

total_sum = 0
while True:
    try:
        user_input = int(input("Enter a number: "))
        if user_input == SENTINEL:
            break  
        total_sum += user_input
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("The sum of the entered numbers is:", total_sum)


input("\nNext program")

sum = 0
data = int(input("How long? (enter 0 to end) "))
while data != 0:
    sum = sum + data
    data = int(input("How long? (enter 0 to end) "))
print("Sum:",sum)


for i in range(10):
	print(i)

# Example: Python Nested For Loop
for i in range(3):  # Outer loop
	for j in range(2):  # Inner loop
		print(f"Outer: {i}, Inner: {j}")

x = input("\nNext program")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
	for y in fruits:
		print(x, y)


x = input("\nNext program")

outer_counter = 0
while outer_counter < 3:
	print(f"Outer loop iteration: {outer_counter}")
	inner_counter = 0  
	while inner_counter < 2:
		print(f"  Inner loop iteration: {inner_counter}")
		inner_counter += 1
        
	outer_counter += 1

x = input("\nNext program")

for multiplicant in range(1, 11):
	for multiplier in range(1, 4):
		expression = f"{multiplicant:>2d} × {multiplier}"
		product = multiplicant * multiplier
		print(f"{expression} = {product:>2d}", end="\t")
	print()
