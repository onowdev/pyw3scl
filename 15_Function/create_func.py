from xxlimited import foo


def myFunction():
    print("Hello this My Function")

myFunction()

print("Function With Argument")

# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

def function1(presiden):
    print(presiden + "Kepala Nagara Indonesia")

function1("Ir. Soekarno")
function1("HM. Soeharto")
function1("Bj. Habibie")
function1("H. Abdurahman Wachid")
function1("Ibu. Megawati soekarno Putri")
function1("DR. Susilo Bambang Yudhoyono")
function1("Ir. Joko Widodo")

print("Number of Arguments")

def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Agus", "Sugiono")

print("Arbitrary Arguments, *args")

# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:

def myFunction2(*kids):
    print("The Youngest child is" + kids[2])

myFunction2("Emil","tobhias","Linus")

print("Keyword Arguments")
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.

def myfunction3(child1, child2, child3):
    print("The Youngest Child is" + child3)

myfunction3(child1="Emil", child2="Thobias", child3="Linus")

print("==============")
print("Arbitrary Keyword Arguments, **kwargs")

def myfunction4(**kid):
    print("His last name is" +  kid["lname"])

myfunction4(fname = "Toni", lname = "Blair")

print("=============")
print("Default Parameter Value")

# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:

def my_function2(country = "Norway"):
    print("I am from" + country)

my_function2("Sweden")
my_function2("India")
my_function2()
my_function2("Brazil")

print("=============================")
print("Passing a list as an Argument")

def myFunction5(food):
    for x in food:
        print(x)

fruits = ["apple","banana","cherry"]

myFunction5(fruits)

print("============")
print("Return Value")

def myfunc1(x):
    return 5 * x

print(myfunc1(4))
print(myfunc1(7))
print(myfunc1(9))