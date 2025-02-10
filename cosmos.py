import requests
import json

#TASK #1
# Write a Python script that makes a GET request to a space API (e.g., The Solar System OpenData) to fetch data about planets.
# Parse the JSON response and extract information about each planet, such as its name, mass, and orbit period.
def fetch_planet_data():
    try:
        url = "https://api.le-systeme-solaire.net/rest/bodies/"
        response = requests.get(url)
        planets = response.json()["bodies"]
        
        for planet in planets: 
            if planet["isPlanet"]:
                name = planet["englishName"]
                mass = planet["mass"]["massValue"]
                orbit_days = planet["sideralOrbit"]
                print(f"Planet: {name}, Mass: {mass}, Orbit : {orbit_days} days")
        
        return planets

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# TASK #2
# Perform a simple analysis, such as finding the planet with the longest orbit period or the heaviest planet.
print("=" * 50)

def fetch_heaviest_planet():
    planets = fetch_planet_data()
    planet_mass = []

    for planet in planets:
        if planet["isPlanet"]: 
            mass = planet["mass"]["massValue"]
            planet_mass.append(mass)
            mass = max(planet_mass) 
            if planet["mass"]["massValue"] == mass :
                name = planet["name"]
                return name , mass

   
name, mass = fetch_heaviest_planet()
print(f"\nThe heaviest planet is {name}, with a mass of {mass} kg.")
