# Pokedex
A Web Scraping and GUI applictaions which extract information about all the known Pokemon and later uses that information to present a comprehensive and interactive encyclopedia for any interested person who wants to learn more about those magical creatures.<br />
(More in the "[Key features](#Key-features)" section)

## Dependencies
Install needed libraries and modules:
```
py -m pip install requests
py -m pip install beautifulsoup4
py -m pip install Pillow
```
**requests** module used for requesting the url and fetching response, **beautifulsoup4** used for parsing/extracting information from HTML documents and **Pillow** adds image processing capabilities to Python interpreter.

## How to run
Running the **html_handler.py** used for extracting needed information from https://pokemondb.net/pokedex/national website (not needed if data already extracted):
```
py -m html_handler.py
```
(May take a couple of minutes for the program to finish)
<br /><br />
Running the **pokedex_view.py** which is a GUI application that uses data extracted with a use of **html_handler.py**:
```
py -m pokedex_view.py
```
## Example of use

## Key features
**html_handler.py** allows us getting information on all 1010 Pokemon. It scrapes the https://pokemondb.net/pokedex/national website and saves the images and text files containing information about Pokemon's type, species, height, weight, evolution line and their brief description.<br /><br />
**pokedex_view.py** is the main page of the Pokedex.It shows full list of all the Pokemon, allows sorting the list by name or number (both descending and ascending). It provides ability to filter the list by part or full name or number and showing only Pokemons with numbers from and to inputted ones. Moreover be double clicking on the lists element we are taken to this Pokemon's page.<br /><br />
**pokemon_page.py** is the chosen Pokemon's page. We can view it's full description, obtained thanks to html_handler.py and from this page go to the different Pokemon's page, which is either before or after it in the Pokedex or is in this Pokemon's evolutionary line. Other than that we are able to go back to the main page of the Pokedex.


