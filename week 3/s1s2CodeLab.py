# if s1 and s2 are equal length
s1 = "hi"
s2 = "sammy"
s3 = ""

for index in range(0, max(len(s1), len(s2))):
    if index < len(s1):
        s3 = s3 + s1[index]
    if index < len(s2):
        s3 = s3 + s2[index]

print(s3)
