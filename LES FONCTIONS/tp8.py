def mystere(a, b):
    a = a * 2
    b.append(4)
    print("Dans la fonction:", a, b)

x = 5
y = [1, 2, 3]
mystere(x, y)
print("Après appel:", x, y)
# Output:
# Dans la fonction: 10 [1, 2, 3, 4]
# Après appel: 5 [1, 2, 3, 4]

# 2. Function to exchange values of two variables
def echanger(a, b):
    a, b = b, a
    return a, b

x, y = 5, 10
x, y = echanger(x, y)
print(x, y)  # Output: 10 5

# 3. Function to add element to a list without modifying the original list
def ajouter_element(lst, elem):
    new_list = lst.copy()  # Create a copy of the original list
    new_list.append(elem)
    return new_list

# Test
original_list = [1, 2, 3]
result_list = ajouter_element(original_list, 4)
print("Original List:", original_list)  # Output: Original List: [1, 2, 3]
print("New List:", result_list)         # Output: New List: [1, 2, 3, 4]

