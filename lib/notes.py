# Decorator adds functionality to functions while avoiding redundancy.
# You can add to an object without modifying it structure.
# Another way to write DRY code. 

def decorator(func):
    def wrapper():
        print("I am the output that lets you know the function is about to be called.")
        func()
        print("I am the output that lets you know the function has been called.")
    return wrapper

@decorator
def get_called():
    print("I am the function and I am being called.")

get_called()
# I am the output that lets you know the function is about to be called.
# I am the function and I am being called.
# I am the output that lets you know the function has been called.

# Let's look at an example of when we would want to use decorators.

def sweep_floors(time):
    if 1100 < time < 2100:
        print("Sweeping the floors...")
    else:
        print("I'm off duty!")

def wash_dishes(time):
    if 1100 < time < 2100:
        print("Washing the dishes...")
    else:
        print("I'm off duty!")

def chop_vegetables(time):
    if 1100 < time < 2100:
        print("Chopping the vegetables...")
    else:
        print("I'm off duty!")

# There's a pretty clear pattern here: our employees only work from 11 to 9! Including code in every single function to check if anyone's working is not ideal. Let's refactor this with a decorator:

def check_working_hours(func):
    def wrapper(time):
        if 1100 < time < 2100:
            func(time)
        else:
            print("I'm off duty!")
    return wrapper

@check_working_hours
def sweep_floors(time):
    print("Sweeping the floors...")

@check_working_hours
def wash_dishes(time):
    print("Washing the dishes...")

@check_working_hours
def chop_vegetables(time):
    print("Chopping the vegetables...")

sweep_floors(800)
# I'm off duty!
wash_dishes(1000)
# I'm off duty!
chop_vegetables(1200)
# Chopping the vegetables...


#What are the two options for invoking a decorator?
#A function_call() or @pie_syntax.


