# Pokedex
abbasbdhabdhsabdhasdbj

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
Running the **pokedex_view** which is a GUI application that uses data extracted with a use of **html_handler**:
```
py -m pokedex_view.py
```
