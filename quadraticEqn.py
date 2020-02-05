import cmath

a = int(input('Enter First Number'))
b = int(input('Enter Second Number'))
c = int(input('Enter Third Number'))

d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The Solution are {0} and {1}'.format(sol1,sol2))

