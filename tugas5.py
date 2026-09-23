# Get the value of n from the user
n = int(input("Enter n value: "))

# Loop through each row from 1 to n
for i in range(1, n + 1):
    # Print the current number 'i', repeated 'i' times with a space in between
    for j in range(i):
        print(i, end=" ")
    # Move to the next line after printing each row
    print()