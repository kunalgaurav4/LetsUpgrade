cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
else:
    print(car.title())


# checking for Inequality

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# if Statements

age = 19
if age >= 18:
    print("You are old enough to vote!")


# if-else Statements
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# range
for i in range(3):
    print(i)

for i in range(3, 100, 25):
    print(i)


for i in range(11):              
    for j in range(i):            
        print('*', end='')        
    print('')    