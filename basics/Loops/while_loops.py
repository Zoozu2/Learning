age = 24
num = 0
count = 0


while num < age:       
# we used while loop to check if num is less than age
    if num == 2:
        num+=1
        continue
    if num % 2 == 0:
        print(num)
        count += 1
    if num>10:
        break
    
    num += 1

print(f'Final number: {num}')
print(f'Final count: {count}')

# Explaination of the above code:
# We have a variable called age which is 24
# We have a variable called num which is 0
# We have a variable called count which is 0
#
# While num is less than age, do the following:
# If num is equal to 2, then add 1 to num and continue
# If num is divisible by 2, then print num and add 1 to count
# If num is greater than 10, then break
# Add 1 to num
#
# Print the final number 
# Print the final count