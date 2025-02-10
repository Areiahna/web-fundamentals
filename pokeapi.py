import requests
import json


#TASK 2

# Write a Python script to make a GET request to the Pokémon API (https://pokeapi.co/api/v2/pokemon/pikachu).
# Extract and print the name and abilities of the Pokémon.
# Expected Outcome:
# The script should output the name of the Pokémon (Pikachu) and a list of its abilities.

try:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/pikachu")
    poke_data = response.json()

    if isinstance(poke_data,dict):

        ability_count = len(poke_data["abilities"]) 
        index = 0

        poke_dict = {
            "name": poke_data["name"],
            "abilities" : []
        } 

        while index < ability_count :
            poke_dict["abilities"].append(poke_data["abilities"][index]["ability"]["name"])
            index += 1 
        
        print(poke_dict)

except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

print(f"\n")


# TASK 3: Analyzing and Displaying Data

    # Modify the script to fetch data for three different Pokémon.

    # Create a function to calculate and return the average weight of these Pokémon.

    # Print the names, abilities, and average weight of the three Pokémon.

pokemon_names = ["snorlax", "bulbasaur", "charmander"]

def fetch_pokemon_data(pokemon_list):

    try:
        for pokemon in pokemon_list:
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

            # Atempting to GET data from api for {pokemon}
            response = requests.get(url)
            poke_data = response.json()

            if isinstance(poke_data, dict): 
                
                name = pokemon
                ability_count = len(poke_data["abilities"])
                weight = poke_data["weight"]
                # Extracting abilities
                abilities = []
                for ability in poke_data["abilities"]:
                    abilities.append(ability["ability"]["name"])
                

                print(f"Pokemon: {name}\nWeight: {weight}\nAbilities({ability_count}): {abilities}\n")
            
            else:
                status = poke_data.get("status")
                reason = poke_data.get("reason","Unkown error")
                print(f"Error {status}: {reason}")    

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
                   

fetch_pokemon_data(pokemon_names)




def calculate_average_weight(pokemon_list):
    poke_weight = []
    try:
        for pokemon in pokemon_list:
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

            response = requests.get(url)
            poke_data = response.json()

            if isinstance(poke_data, dict):
                poke_weight.append(poke_data["weight"])

        average_weight = sum(poke_weight)/len(pokemon_list)
        print(f"The average weight of all 3 pokemons is {round(average_weight,2)}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

calculate_average_weight(pokemon_names)



        

