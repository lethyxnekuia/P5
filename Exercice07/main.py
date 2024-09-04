## Écrivez votre code ici !

def square(number):
    try:
        if isinstance(number, (int, float)):
            return number ** 2
        else:
            raise ValueError
    except ValueError:
        print("Le paramètre doit être un nombre !")
        return None


print(square(2))
print(square("p"))
