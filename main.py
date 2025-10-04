#a = 5
#b = 10

#rectangle_area = a * b
#print("Area of rectangle = ", rectangle_area)

s = input("Enter snake_case text:")
capital_camel_case = s.replace('_', " ").title().replace(' ', '')
print("Capital camel case: ", capital_camel_case)
print("lower camel case: ", capital_camel_case[0].lower() + capital_camel_case[1:])