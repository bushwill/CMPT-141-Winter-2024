# Will Bushell, abc123, 12345678, Jeffrey Long
# this is designed to help with question 2 of A5

wblist = [
    ['James', 8, 4],
    ['Timmy', 9, 2],
    ['Sammy', 1, 2],
    ['Rango', 10000, 1],
    ['Luke "Hates Five" Wilson', 6, 5]
]

sum = 0
count = 0
for guy in wblist:
    print(guy[0], "loves the number", guy[1], "and hates", guy[2])
    sum += guy[2]
    count += 1

print("The sum of all hated numbers is:", sum/count)
