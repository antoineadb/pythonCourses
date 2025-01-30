
def decorator(func):
    def wrapper():
        print("Avant")
        func()
        print("Après")
    return wrapper

@decorator
def say_hello():
    print("Bonjour !")


say_hello()
