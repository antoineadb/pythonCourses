
def command_handler(func):
    if not hasattr(command_handler, 'commands'):
        command_handler.commands = []
    def wrapper():
        command_handler.commands.append(func)
    return wrapper

@command_handler
def start():
    print("Démarrage de l'application")

@command_handler
def stop():
    print("Arrêt de l'application")

@command_handler
def restart():
    print("Redémarrage de l'application")

start()
stop()
restart()

for cmd in command_handler.commands:
    print(cmd.__name__)