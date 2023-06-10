# Author: Adrian Janus s24768
"""
This module provides the functionality needed for getting and saving needed information on
all the known Pokemon

Libraries/Modules:
    requests -- Allows getting the html contents from web page to later get needed information from it
    BeautifulSoup -- Allows extracting information from the html document
    os -- Provides a way to interact with operating system. Used for saving the images
          and creation of text files filled with data received from web page parsing
          as well creation of needed directories in which those files will be stored in

Classes:
    PokemonInfo -- A class containing all the methods needed for realization of this modules functionality

Functions/Methods:
    getHtmlContent -- Makes a request to a web page and gets its html content in text form
    createPokemon -- Extracts needed information from specific Pokemon page and saves it in correct folders
    createAllPokemon -- Creates folders to keep Pokemon information in, gets all individual Pokemon pages
                        and calls createPokemon method on all of them
"""

import requests
from bs4 import BeautifulSoup
import os


class PokemonInfo():
    """
    A class containing functions for getting and manipulating https://pokemondb.net/pokedex/national page information

    Functions/Methods:
        getHtmlContent -- Makes a request to a web page and gets its html content in text form
        createPokemon -- Extracts needed information from specific Pokemon page and saves it in correct folders
        createAllPokemon -- Creates folders to keep Pokemon information in, gets all individual Pokemon pages
                            and calls createPokemon method on all of them
    """

    def getHtmlContent(self, s):
        """
        Makes a request to a web page and gets its html content in text form

        Args:
            s: The input web page url

        Returns:
             The html contents in text form
        """
        response = requests.get(s)
        html_content = response.text
        return html_content

    def createPokemon(self, pokemon):
        """
        Extracts needed information from specific Pokemon page and saves it in correct folders.
        Finds information on Pokemons name, its number in pokedex, its species, height, weight, type,
        its brief description, its evolution line and between which two other Pokemon it is placed in the Pokedex.
        It saves this data in proper .txt file in directory Pokemon_Info.
        Moreover it saves the image representing this Pokemon, found on its page, in directory Pokemon_Images.

        Args:
             pokemon: The input web page url
        """
        soup = BeautifulSoup(self.getHtmlContent(pokemon), "html.parser")
        name = soup.find('h1').text
        if "(male)" in name:
            name=name.replace(" (male)","")
        if "(female)" in name:
            name=name.replace(" (female)","")
        number, species, height, weight, type = "", "", "", "", ""
        i, j, ni, si, wi, hi, ti = 0, 0, 0, 0, 0, 0, 0
        for child in soup.find('table').find_all('tr'):
            for header in child.find_all('th'):
                if header.text == "National №":
                    ni = i
                if header.text == "Type":
                    ti = i
                if header.text == "Species":
                    si = i
                if header.text == "Height":
                    hi = i
                if header.text == "Weight":
                    wi = i
                i = i + 1
            for data in child.find_all('td'):
                if j == ni:
                    number = data.text.strip()
                if j == ti:
                    type = data.text.strip()
                if j == si:
                    species = data.text.strip()
                if j == hi:
                    height = data.text.strip()
                if j == wi:
                    weight = data.text.strip()
                j = j + 1
        # If no cell-med-text class then there is no information on this Pokemon provided
        try:
            pokemon_entry = soup.find('td', class_="cell-med-text").text
        except:
            pokemon_entry = "No Pokemon info provided"
            pass
        # If no infocard-list-evo class then there is no information on this Pokemons evolution provided
        try:
            pokemon_evo = '->'.join(
                [p.text for p in soup.find('div', class_="infocard-list-evo").find_all('a', class_="ent-name")[:3]])
        except:
            pokemon_evo = name + " does not evolve"
            pass
        # If no entity-nav-prev class this is the first Pokemon in the list
        try:
            prev_pokemon = soup.find('a', class_="entity-nav-prev").text
        except:
            prev_pokemon = "no prev"
            pass
        # If no entity-nav-next class this is the last Pokemon in the list
        try:
            next_pokemon = soup.find('a', class_="entity-nav-next").text
        except:
            next_pokemon = "no next"
            pass
        img = soup.find('meta', property="og:image").get('content')
        image_response = requests.get(img)
        image_name = "./Pokemon_Images/" + number + "_" + name + ".gif"
        if not os.path.exists(image_name):
            with open(image_name, "wb") as f:
                f.write(image_response.content)
                f.close()
        info_path = "./Pokemon_Info/" + number + "_" + name + ".txt"
        if not os.path.exists(info_path):
            with open(info_path, "w", encoding="utf-8") as f:
                f.write(type + "\n")
                f.write(species + "\n")
                f.write(height + "\n")
                f.write(weight + "\n")
                f.write(pokemon_evo + "\n")
                f.write(pokemon_entry + "\n")
                f.write(prev_pokemon + "\n")
                f.write(next_pokemon + "\n")
                f.close()

    def createAllPokemon(self):
        """
        Creates folders to keep Pokemon information in, gets all individual Pokemon web pages urls
        and calls createPokemon method on all of them
        """
        soup = BeautifulSoup(self.getHtmlContent("https://pokemondb.net/pokedex/national"), "html.parser")
        link = "https://pokemondb.net"
        # If the directory already exists it won't be created again
        try:
            os.mkdir("Pokemon_Images")
        except:
            pass
        try:
            os.mkdir("Pokemon_Info")
        except:
            pass
        for a in soup.find_all('a', class_="ent-name"):
            if "pokedex" in a.get('href'):
                self.createPokemon(link + a.get('href'))


pokemon_initiator = PokemonInfo()
pokemon_initiator.createAllPokemon()
