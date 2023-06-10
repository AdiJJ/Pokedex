# Pokedex
A Web Scraping and GUI applictaions which extract information about all the known Pokemon and later uses that information to present a comprehensive and interactive encyclopedia for any interested person who wants to learn more about those mysthical creatures.<br />
(More in the "Key features" section)

## Dependencies
Install needed libraries and modules:
```
py -m pip install requests
py -m pip install beautifulsoup4
py -m pip install Pillow
```
**requests** module used for requesting the url and fetching response, **beautifulsoup4** used for parsing/extracting information from HTML documents and **Pillow** adds image processing capabilities to Python interpreter.

## How to run
Running the **html_handler** used for extracting information from the website (not needed if data already extracted):
```
py -m html_handler.py
```
(May take a couple of minutes for the program to finish)
<br /><br />
Running the **pokedex_view** which is a GUI application that uses data extracted with a use of **html_handler**:
```
py -m pokedex_view.py
```
