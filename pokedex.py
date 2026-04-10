import locale
import platform
import pandas as pd

from pokemondraw import bulbasaur, dragonite, charizard, __pokemon_draw, charmeleon
from pathlib import Path

if platform.system() == "Windows":
    locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil')
else:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

version = "0.1v"

ash = """
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠟⠛⠛⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⡿⠛⢉⣠⣤⣶⣶⣶⣶⣶⣦⣄⠈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⠏⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡏⠀⣿⣿⣿⣿⠟⠋⡉⠙⣿⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⠀⣿⣿⡿⠃⠠⠾⠿⠿⠿⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⠀⣿⣿⣦⣤⣤⣤⣤⣤⣴⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⠇⠀⠉⠉⠁⠀⠀⠀⠀⠉⠉⠛⠛⠿⠿⠇⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿
    ⣿⠏⠁⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⢈⣹⣿⣿⣿⣿
    ⣿⣷⣶⠖⠀⠀⢻⣿⣿⣿⡇⢀⣠⣴⣶⣶⣶⣿⣿⡇⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿
    ⣿⣿⣧⠀⠀⠀⢸⠁⣠⠈⢻⣿⣿⣿⠁⣤⠈⢿⣿⣤⣴⠀⠀⠀⠀⠀⠙⢿⣿⣿
    ⣿⡿⠋⠀⠀⠀⢸⠀⠙⠀⢸⣿⣿⣿⠀⠹⠀⢸⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⣨⣿
    ⣿⣦⣄⡀⠀⠀⣾⣤⣤⣤⣾⣿⣿⣿⣤⣤⣤⣿⣿⠛⠁⠀⠀⠀⠐⣶⣿⣿⣿⣿
    ⣿⣿⣿⣿⣷⠀⢿⣿⣿⡁⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⠀⣀⣀⣤⣼⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣦⡈⠙⠻⢷⣤⣀⣀⣠⡾⠿⠛⠋⢉⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⡈⠉⠉⣁⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    """



# Seek Pokemon csv file and load to a Pandas dataframe
def seek_pokemon_file():

    while True:
        try:

            archive = Path(f"pokemon.csv")

            # Verify if the file exists in the current directory
            if not Path(archive).is_file():
                print(f"File '{archive}' not found. Please try again.")

                input("Check file and press enter to continue")
                continue

            # Read the spreadsheet using Pandas
            df_base = pd.read_csv(archive, encoding = "UTF-8", sep = "," )
            print(f"File {archive} loaded successfully!")

            df_base["number"] = range(1, len(df_base) + 1)

            return df_base
        
        # Return error message if the file cannot be read
        except Exception as e:
            print(f"An error occurred while trying to read the file: {e}. Please try again.")

# Program boot message
def __initialyze():
    print(f"""--------------- Pokemon Data Analysis ------------------

        Analysis of data from the Pokemon universe (Gen I to VII)
        Author - Paulo Izidoro
        Data -  {pd.Timestamp.now()}\n\n""")
    
pokedex = seek_pokemon_file()
__initialyze()


#print(pokedex["japanese_name"].tail(15))

#print(pokedex["type1"].unique().tolist())
#print(pokedex["type2"].dropna().unique().tolist())

# Return a list of dictionaries with the unique pokemon types and their respective index in a array
def __type_list(pokedex):
    
    # Create a list with all unique pokemon types
    list = pokedex["type1"].sort_values().unique().tolist()

    ind = 0 
    type_list = []

    while ind < len(list):
        type_list.append({"number" : ind,
                          "type" : list[ind]})
        ind += 1

    for i in type_list:
        print(f"{i['number']} - {i['type']}")

    pass

def __search_pokemon_by_type (pokedex, pokemon_type):
    return pokedex[(pokedex["type1"] == pokemon_type.lower()) | (pokedex["type2"] == pokemon_type.lower())][["pokedex_number", "name", "type1", "type2"]].reset_index(drop=True)   

    pass

def __list_of_games():

    games = ["Red, Blue, Green & Yellow ", 
                     "Gold, Silver & Crystal", 
                     "Ruby, Sapphire & Emerald", 
                     "Diamond, Pearl & Platinum", 
                     "Black & White", 
                     "X & Y", 
                     "Sun & Moon"]
    
    for i in games:
        print(i)

def __list_of_generations(pokedex):

    generation = []
    i = 0
    while i < len(pokedex["generation"].unique()):

        games = ["Red, Blue, Green & Yellow ", 
                     "Gold, Silver & Crystal", 
                     "Ruby, Sapphire & Emerald", 
                     "Diamond, Pearl & Platinum", 
                     "Black & White", 
                     "X & Y", 
                     "Sun & Moon"]
        
        generation.append({
                        "Generation" : i + 1,
                        "Games" : games[i],
                        "count" : pokedex[pokedex["generation"] == i + 1]["pokedex_number"].count()
                      })
        
        i += 1

    for ill in generation:
        print(f"Generation " + str(ill['Generation']) + "\n" +
                "Games: " + ill['Games'] + "\n" +
                "Number of Pokemon: " + str(ill['count'])+ "\n")

    print("Total number of Pokemon: " + str(pokedex["pokedex_number"].count())) 

    pass

def __pokemon_list(pokedex):

    charmeleon()

    pokemon_list = pokedex[[
                            "pokedex_number", 
                            "name",
                            "japanese_name",
                            "classfication",
                            "type1", 
                            "type2",
                            "generation",
                            "height_m",
                            "weight_kg",
                            "attack",
                            "defense",
                            "speed",
                            "hp",
                            "sp_attack",
                            "sp_defense"
                            ]].reset_index(drop = True)

    return pokemon_list


def __search_pokemon_by_generation(pokedex):
    def search(generation):

        pokemon_list =  pokedex[pokedex["generation"] == generation][[
            "pokedex_number", 
            "name",
            "japanese_name",
            "classfication",
            "type1", 
            "type2",
            "generation",
            "height_m",
            "weight_kg",
            "attack",
            "defense",
            "speed",
            "hp",
            "sp_attack",
            "sp_defense"

            ]].reset_index(drop=True)   
        
        print(pokemon_list)

        print(f"Total number of Pokemon in Generation {generation}: " + str(pokemon_list["pokedex_number"].count()))

        pass

    while True:
        try:
            generation_input = int(input(f"Enter the generation number (1 to {pokedex['generation'].max()}): "))
            
            if generation_input < 1 or generation_input > pokedex["generation"].max():
                print(f"Invalid input. Please enter a number between 1 and {pokedex['generation'].max()}.")
                continue
            else:
                search(generation_input)
                break

        except ValueError:
            print(f"Invalid input. Please enter a number between 1 and {pokedex['generation'].max()}.")
            continue

    pass


# Create a menu with system options
def __menu():

    option = -1

    print(__pokemondraw())

    menu = f"""POKEDEX --- Version {version}

    1 - List all pokemon throughout all generations
    2 - List all generations main games
    3 - Search all pokemon of a specific type
    4 - Search all pokemon from a specific generation
    5 - List all pokemon types
    0 - Exit

    """

    while option != 0:        

        try:

            print(menu)

            option = int(input(f"Choose option number: "))
            
            options = [1,2,3,4,5,6,0]

            if option not in options:
                continue

            match option:

                # 1 - List all pokemon throughout all generations
                case 1: 
                    print(__pokemon_list(pokedex))
                
                # 2 - List all generations main games
                case 2: 
                    __list_of_generations(pokedex)
                
                # 3 - Search all pokemon of a specific type
                case 3: 

                    while True:
                        try:

                            # List all types of pokemon
                            __type_list(pokedex)

                            pokemon_type = input(f"Digit the pokemon type: ")
                            
                            print(__search_pokemon_by_type(pokedex, pokemon_type.lower()))

                            break
                        
                        except ValueError:

                            print("Invalid Option.")


                
                #4 - Search all pokemon from a specific generation
                case 4: 
                    continue
                
                # 5 - List all pokemon types
                case 5: 
                    continue
                
                # 0 - Exit
                case 0: 
                    break
            

        except ValueError:
            print(f"Invalid option!")

            continue





### Sessão de testes
 

#__menu()


# List all pokemons
print("Cheguei")
__pokemon_draw()
print(__pokemon_list(pokedex))
print("Terminei")

#bulbasaur()
#dragonite()
#charizard()

#__list_of_games()


# List all types of pokemon
#__type_list(pokedex)

# Resume of each generation
#__list_of_generations(pokedex)

# Search for all pokemon of a specific type, in this case, "fire"
#print(__search_pokemon_by_type(pokedex, "fire"))

# Search for all pokemon of a specific generation, in this case, "Generation 1"
#__search_pokemon_by_generation(pokedex)



### Fim da sessão de testes