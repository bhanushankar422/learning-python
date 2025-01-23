# load inputs from console and print them

# Read input from a file
with open('input.txt', 'r') as file:
    input1 = file.readline().strip()
    input2 = int(file.readline().strip())

# Print the inputs
print("First input:", input1)
print("Second input:", input2)
