# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(n):
    return n % 2 == 0


print(is_even(2))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
# eo = is_even(num)
# YOUR CODE HERE
# if eo == True:
#     print("Even!")
# else:
#     print("Odd")

# print("Even!") if eo == True else print("Odd")

eo = num % 2 == 0 and "Even!" or "Odd"
print(eo)
