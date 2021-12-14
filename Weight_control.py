# Weight_control app
print("enter your sex: male or female")
sex=input()
print("enter your weight in kg")
x=weight=int(input ())
print("enter your height in cm")
y=height=float(input())
print("enter your age")
z=age=int(input())

# bmr:basal metabolic rate
if sex == "male":
    bmr=((10*x)+(6.25*y)-(5*z)+5)
    print("your required Calories income to keep your weight without changing is",bmr)
else:
    bmr=((10*x)+(6.25*y)-(5*z)-161)
    print("your required Calories income to keep your weight without changing is",bmr)

# from health app
print("enter your income calories until now")
ic=income_calories=int(input())
print("enter what is your aim dude: loss, gain or keep")
i=input()
if i=="loss":
    if bmr<=ic:
        print("move your fat ass or shut your mouth for tomorrow breakfast")
    else: 
        print("good job dude")
if i=="gain": 
    if bmr<ic:
        print("good job")
    else: 
        print("you need to eat more idiot, do you want me to suggest something to eat?")
if i=="keep":
    if ic==bmr:
        print("that is soo good, do not eat and go to sleep right now")
    elif bmr>ic: 
        print("careful! you are gonna loose weight from now on")
    else:
        print("careful! you are gonna gain weight from now on")