#Single Type Pokemon Calculator
#Will calculate what to use when faced against a person of said type


weakness = {
    "fire" : ["ground", "water", "rock"],
    "water" : ["electric", "grass"],
    "grass" : ["bug", "fire", "flying", "ice", "poison"],
    "ice" : ["fight", "fire", "rock", "steel"],
    "bug" : ["fire", "flying", "rock"],
    "ghost" : ["dark", "ghost"],
    "dark" : ["bug", "fairy", "fighting"],
    "psychic" : ["dark", "ghost", "bug"],
    "fighting" : ["flying", "fairy", "psychic"],
    "steel" : ["fight", "fire", "ground"],
    "fairy" : ["poison", "steel"],
    "dragon" : ["ice", "dragon", "fairy"],
    "poison" : ["psychic", "ground"],
    "ground" : ["water", "grass", "ice"],
    "rock" : ["fighting", "grass", "ground", "steel", "water"],
    }

def sWeakness(type_a):
    if type_a in weakness:
        print(weakness[type_a])
    else:
        print("Sorry, " + type_a + " is unrecognized.")
