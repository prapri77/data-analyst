my_list = [10, 20, 30, 40, 50]

for i, current_value in enumerate(my_list):
    # Print the current value
    print(f"Current Value: {current_value}")

    # Check if there's a previous value
    if i > 0:
        previous_value = my_list[i - 1]
        print(f"Previous Value: {previous_value}")

    # Check if there's a next value
    if i < len(my_list) - 1:
        next_value = my_list[i + 1]
        print(f"Next Value: {next_value}")

    print("-" * 20) # Separator for clarity

#Python's next() function returns the next item of an iterator.
#Syntax : next(iter, stopdef)
l = [1, 2, 3]
l_iter = iter(l)  
print(next(l_iter))
print(next(l_iter))

# define a list
l = [1, 2, 3]  
# create list_iterator
l_iter = iter(l)  

while True:
    # item will be "end" if iteration is complete
    item = next(l_iter, "end") #here end is default value after finishing iterator to avoid error
    if item == "end":
        break
    print(item)

list1 = [1]

# converting list to iterator
list_iter = iter(list1)

print(next(list_iter))
print(next(list_iter, "No more element"))
