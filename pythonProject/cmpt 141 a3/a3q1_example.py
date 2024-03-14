# Will Bushell, abc123, 12345678, Jeffrey Long
# this is designed to help with question 1 of A3
email = "willy.bobilly@wahoo.com.ca"    # This email has:   1. one or more characters before the @
string_split1 = email.split("@")                         # 2. exactly one @ character
print("String_split1:", string_split1)                   # 3. at least one period after the @
username = string_split1[0]                              # 4. characters between the @ and .
domain_and_extension = string_split1[1]
print("Username:", username)
print("Domain_and_extension:", domain_and_extension)
string_split2 = domain_and_extension.split(".")
print("string_split2:", string_split2)
domain = string_split2[0]               # if the entered email has more than one . character,
extension = string_split2[1:]           # the domain variable will only take what is before the
print("Username:", username)            # FIRST . symbol after the @
print("Domain:", domain)
print("Extension:", extension)          # this does not need to be printed in the assignment
