# Will Bushell, abc123, 12345678, Jeffrey Long
# this is designed to help with question 3 of A5

testlist = []
wblist = []

f = open("wbnumbers.txt", "r")
for i in f:
  testlist.append(i)
  i = i.strip()
  wblist.append(i)

print("Test List (Before Stripping):")
print(testlist)
print("WB List (After Stripping):")
print(wblist)
print("The \n character adds a new line, like pressing the enter key")

