import time

def add_time(delay=1):
    def decorator(func):
        def wrapper():
            time.sleep(delay)
            func()
        return wrapper
    return decorator


@add_time(delay=1)
def a_command():
    print("Bonjour")

@add_time(delay=2)
def other_command():
    print("Comment ça va ?")

@add_time(delay=3)
def another_command():
    print("Super !")

a_command()
other_command()
another_command()
