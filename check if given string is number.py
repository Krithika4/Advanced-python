#check if given string is number
number = lambda s : s.replace('.','',1).isdigit() if s else False
print(number("123"))
print(number("abc"))
print(number("12.34"))