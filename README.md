# Pokedex
A Web Scraping program which extracts information about all the known Pokemon and GUI applictaion which uses the scraped information to present a comprehensive and interactive Pokemon encyclopedia for any interested person who wants to learn more about those magical creatures.<br />
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
## Key features
**html_handler.py** allows us getting information on all 1010 Pokemon. It scrapes the https://pokemondb.net/pokedex/national website and saves the images and text files containing information about Pokemon's type, species, height, weight, evolution line and their brief description.<br /><br />
**pokedex_view.py** is the main page of the Pokedex.It shows full list of all the Pokemon, allows sorting the list by name or number (both descending and ascending). It provides ability to filter the list by part or full name or number and showing only Pokemons with numbers from and to inputted ones. Moreover be double clicking on the lists element we are taken to this Pokemon's page.<br /><br />
**pokemon_page.py** is the chosen Pokemon's page. We can view it's full description, obtained thanks to html_handler.py and from this page go to the different Pokemon's page, which is either before or after it in the Pokedex or is in this Pokemon's evolutionary line. Other than that we are able to go back to the main page of the Pokedex.

## Examples of use
* **Sorting by number:**<br />
![sorting_by_number1](https://github.com/AdiJJ/Pokedex/assets/129506645/e920b763-0fe1-4bde-8df2-53f2f40d38e9)
* **Sorting by name:**<br />
![sorting_by_name](https://github.com/AdiJJ/Pokedex/assets/129506645/afbee12a-514d-4e4e-93b0-0597c4ba4d2d)
* **Search by name:**<br />
![search_by_name](https://github.com/AdiJJ/Pokedex/assets/129506645/8db26e11-6d0c-40b3-b911-3e4a77d4e32b)
* **Search by number:**<br />
![search_by_number](https://github.com/AdiJJ/Pokedex/assets/129506645/9cda0b31-cd53-4823-9df7-fab37ddc95a8)
* **Search between two numbers:**<br />
![search_between_numbers](https://github.com/AdiJJ/Pokedex/assets/129506645/6b1a4d85-56c1-4746-a03c-af1904f13c45)
* **Remove filters and applied sorting:**<br />
![remove_filters](https://github.com/AdiJJ/Pokedex/assets/129506645/6ec7160e-c4bd-4093-8508-fb6887a86fe6)
* **Navigating through Pokemon's page:**<br />
![pokemon_page](https://github.com/AdiJJ/Pokedex/assets/129506645/0a319173-6ac2-4059-b89e-a530a5e22b00)

## Challanges faced
* Actually receiving what I want from the website, that is better understanding html structure and methods to scrape it properly.
* Learning about new before unknown tkinter widgets and their functionality (for example: how to insert data into Listbox and how to call method after clicking on its element).
* Changing between two pages.
* Managing displaying correct information for proper Pokemon.
* Displaying the image properly.
* Arranging all the widget in a pleasing way.

## Lessons Learned
Now I am better acquainted with beautifulsoup4 and tkinter libraries and what they have to offer, as well I am now more familiar with object-oriented programming using PYTHON language. Of course points presented in "[Challanges faced](#Challanges-faced)" section aren't as challanging as they were at the beggining of this project. 



