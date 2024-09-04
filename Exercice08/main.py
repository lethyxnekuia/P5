def log_decorator(func):
    def wrapper():
        print("Exécution de la fonction...")
        func()
        print("Fonction exécutée avec succès.")
    return wrapper


@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")


function_test()
