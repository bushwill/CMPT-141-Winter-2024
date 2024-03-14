# Will Bushell, abc123, 12345678, Jeffrey Long
# this is designed to help with question 1 of A5
squared_list = [x**2 for x in range(1,6)]

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruit_lengths = [len(fruit) for fruit in fruits]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]

print('Squared numbers:', squared_list)
print('Fruit lengths:', fruit_lengths)
print('Even numbers:', even_numbers)
