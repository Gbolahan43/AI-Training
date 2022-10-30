a = int(input("Enter a 0-9:"))
b = int(input("Enter b 0-9:"))
c = int(input("Enter c 0-9:"))
print("a is: " + str(a))
print("a is: " + str(b))
print("a is: " + str(c))

sol1 = (-b-((b**2)-(4*a*c)))/(2*a)
sol2 = (-b+((b**2)-(4*a*c)))/(2*a)
# sol1 = float(abs(sol1))
# sol2 = float(abs(sol2))
print
print('The solution are {0:.2f} and {1:.2f}'.format(sol1,sol2))