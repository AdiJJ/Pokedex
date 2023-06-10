# Author: Adrian Janus s24768
"""
This module provides functionality needed to visualize the main page of the Pokedex and providing the user
with the possibility of sorting, filtering through the list of all the Pokemon, as well entering the separate
Pokemon page of the Pokemon chosen from the list.

Libraries/Modules:
    pokemon_page -- Module used for creating a page/frame for a specific Pokemon
    re -- Provides support for regular expressions. Allows better filtering and sorting of the Pokemon list
    tkinter -- Allows creation of graphical user interface. Thanks to it the Pokedex can be properly displayed
    os -- Provides a way to interact with operating system. Thanks to is we can get a list of all Pokemon saved in a Pokemon_Info directory

Classes:
    App -- A class representing the main page of the Pokedex. It contains all the modules' methods.

Functions/Methods:
    __init__ -- Initializes the main window of the application
    insertPokemonList -- Inserts all the pokemon from the list to Pokemon ListBox
    removeFilters -- Removes all the filters and sorting performed on the pokemon list and calls insertPokemon list method
    orderingCondition -- Returns only the name of the Pokemon from the list (without its number), which is needed for sorting by name
    orderPokemonList -- Sorts the Pokemon list based on the option chosen from the "Order Menu" and calls the method insertPokemonList
    filterName -- Filters the Pokemon list based on the name inputted and calls the method insertPokemonList
    searchName -- Gets the input from the Name Entry field and calls filterName method
    filterNumber -- Filters the Pokemon list based on the number inputted and calls the method insertPokemonList
    searchNumber -- Gets the input from the Number Entry field and calls filterNumber method
    filterBetweenNumbers -- Filters the Pokemon list between two numbers inputted and calls the method insertPokemonList
    searchBetweenNumbers -- Gets the input from the From Number Entry and To Number Entry fields and calls filterBetweenNumbers method
    goToPokemonPage -- Hides the main page and opens the page of the specific Pokemon that has been chosen
    mainloop -- Starts the application and executes what we wish to execute in an application
"""
import pokemon_page
import re
import tkinter as tk
import os

class App:
    """
        A class representing the main page of the Pokedex. It contains all the modules' methods.

        Functions/Methods:
            __init__ -- Initializes the main window of the application
            insertPokemonList -- Inserts all the pokemon from the list to Pokemon ListBox
            removeFilters -- Removes all the filters and sorting performed on the pokemon list and calls insertPokemon list method
            orderingCondition -- Returns only the name of the Pokemon from the list (without its number), which is needed for sorting by name
            orderPokemonList -- Sorts the Pokemon list based on the option chosen from the "Order Menu" and calls the method insertPokemonList
            filterName -- Filters the Pokemon list based on the name inputted and calls the method insertPokemonList
            searchName -- Gets the input from the Name Entry field and calls filterName method
            filterNumber -- Filters the Pokemon list based on the number inputted and calls the method insertPokemonList
            searchNumber -- Gets the input from the Number Entry field and calls filterNumber method
            filterBetweenNumbers -- Filters the Pokemon list between two numbers inputted and calls the method insertPokemonList
            searchBetweenNumbers -- Gets the input from the From Number Entry and To Number Entry fields and calls filterBetweenNumbers method
            goToPokemonPage -- Hides the main page and opens the page of the specific Pokemon that has been chosen
            mainloop -- Starts the application and executes what we wish to execute in an application
    """
    def __init__(self):
        """
        Initiates the main page of the Application and the Application itself.
        Provides all the working widgets of the application, like:
        pokemon_listbox Listbox from which we can select a Pokemon and move to its page,
        remove_filters is a Button which removes all the filters and sorting from the Pokemon list,
        sorting_menu is an OptionMenu which allows sorting of the list on option selection,
        name_search_bar which allows filtering based on entered name
        number_search_bar which allows filtering based on entered number
        number_search_ToFrom is a Button which allows filtering between two numbers entered

        Returns:
            None
        """
        self.window = tk.Tk()
        self.window.title("Pokedex")
        self.window.geometry("680x800")
        self.window.resizable(False, False)

        self.main_frame = tk.Frame(self.window)
        self.main_frame.grid(row=0, column=0)

        self.frame_left = tk.Frame(self.main_frame)
        self.frame_right = tk.Frame(self.main_frame)
        self.frame_left.pack(side="left", padx=20)
        self.frame_right.pack(side="right", padx=20)

        self.pokemon_list_label = tk.Label(self.frame_left, text="Pokemon list:", font=('Courier New', 12))
        self.pokemon_list_label.grid(row=0, column=0)
        self.pokemon_listbox = tk.Listbox(self.frame_left, height=40, width=25, font=('Courier New', 12))
        self.pokemon_listbox.grid(row=1, column=0)
        self.pokemon_listbox.bind('<Double-1>', self.goToPokemonPage)

        #If there is no Pokemon_Info directory the Pokemon list will be empty
        try:
            self.pokemon_list = os.listdir("./Pokemon_Info")
        except:
            self.pokemon_list =[]
        self.pokemon_list_copy = self.pokemon_list.copy()

        self.insertPokemonList()

        self.remove_filters = tk.Button(self.frame_right, text="Remove Filters", command=self.removeFilters,
                                        font=('Courier New', 12))
        self.remove_filters.grid(row=0, column=0)

        self.sorting_menu_options = ["by number asc↑", "by number desc↓", "by name asc↑", "by name desc↓"]
        self.sorting_menu_label = tk.Label(self.frame_right, text="Order", font=('Courier New', 12))
        self.sorting_menu_label.grid(row=1, column=0)
        # clicked -- currently selected option of the menu
        self.clicked = tk.StringVar(self.frame_right)
        self.clicked.set(self.sorting_menu_options[0])
        self.sorting_menu = tk.OptionMenu(self.frame_right, self.clicked, *self.sorting_menu_options)
        self.sorting_menu.config(font=('Courier New', 12))
        self.sorting_menu.grid(row=1, column=1)
        # when an option is selected from the menu the orderPokemonList is triggered
        self.clicked.trace('w', self.orderPokemonList)

        self.name_search_bar = tk.Entry(self.frame_right)
        self.name_search_bar.grid(row=2, column=1)
        self.name_search_button = tk.Button(self.frame_right, text="Search Name", command=self.searchName,
                                            font=('Courier New', 12))
        self.name_search_button.grid(row=2, column=0)

        self.number_search_bar = tk.Entry(self.frame_right)
        self.number_search_bar.grid(row=3, column=1)
        self.number_search_button = tk.Button(self.frame_right, text="Search Number", command=self.searchNumber,
                                              font=('Courier New', 12))
        self.number_search_button.grid(row=3, column=0)

        self.toFromFrame = tk.Frame(self.frame_right)
        self.toFromFrame.grid(row=4, column=0, columnspan=5)
        self.from_label = tk.Label(self.toFromFrame, text="From:", font=('Courier New', 12))
        self.from_label.grid(row=0, column=1)
        self.number_search_from = tk.Entry(self.toFromFrame, width=10)
        self.number_search_from.grid(row=0, column=2)
        self.to_label = tk.Label(self.toFromFrame, text="To:", font=('Courier New', 12))
        self.to_label.grid(row=0, column=3)
        self.number_search_to = tk.Entry(self.toFromFrame, width=10)
        self.number_search_to.grid(row=0, column=4)
        self.number_search_ToFrom = tk.Button(self.toFromFrame, text="Search", command=self.searchBetweenNumbers,
                                              font=('Courier New', 12))
        self.number_search_ToFrom.grid(row=0, column=0)

    def insertPokemonList(self):
        """
        Inserts all the pokemon from the list to Pokemon ListBox

        Returns:
            None
        """
        self.pokemon_listbox.delete(0, tk.END)
        for pk in self.pokemon_list:
            pk = "#" + " ".join(pk.split("_")).replace(".txt", "")
            self.pokemon_listbox.insert(tk.END, pk)

    def removeFilters(self):
        """
        Removes all the filters and sorting performed on the pokemon list and calls insertPokemon list method

        Returns:
            None
        """
        self.pokemon_list = self.pokemon_list_copy.copy()
        self.insertPokemonList()

    def orderingCondition(self, element):
        """
        Removes the number from the pokemon name in the list, which is needed for sorting by name

        Args:
            element: An element of the Pokemon list (name of a pokemon with its number

        Returns:
            A part of the element without the pokemons number
        """
        return element[5:]

    def orderPokemonList(self, *args):
        """
        Sorts the Pokemon list based on element selected from the Order Menu

        Args:
            args: The elements of the Order Menu

        Returns:
            None
        """
        if self.clicked.get() == "by number desc↓":
            self.pokemon_list.sort(reverse=True)
        if self.clicked.get() == "by number asc↑":
            self.pokemon_list.sort()
        if self.clicked.get() == "by name asc↑":
            self.pokemon_list.sort(key=self.orderingCondition)
        if self.clicked.get() == "by name desc↓":
            self.pokemon_list.sort(reverse=True, key=self.orderingCondition)
        self.insertPokemonList()

    def filterName(self, condition):
        """
        Filters the Pokemon list based on the name inputted and calls the method insertPokemonList

        Args:
            condition: a name or part of it needed to be found in the list

        Returns:
            None
        """
        self.pokemon_listbox.delete(0, tk.END)
        new_pokemon_list = []
        for pokemon in self.pokemon_list:
            if re.compile(condition, flags=re.IGNORECASE).search(pokemon[5:-4]):
                new_pokemon_list.append(pokemon)
        self.pokemon_list = new_pokemon_list.copy()
        self.insertPokemonList()

    def searchName(self):
        """
        Gets the input from the Name Entry field and calls filterName method

        Returns:
            None
        """
        entry = self.name_search_bar.get()
        self.name_search_bar.delete(0, tk.END)
        self.filterName(entry)

    def filterNumber(self, condition):
        """
        Filters the Pokemon list based on the number inputted and calls the method insertPokemonList

        Args:
            condition: a number or part of it needed to be found in the list

        Returns:
            None
        """
        self.pokemon_listbox.delete(0, tk.END)
        new_pokemon_list = []
        for pokemon in self.pokemon_list:
            if re.compile(condition, flags=re.IGNORECASE).search(pokemon[0:4]):
                new_pokemon_list.append(pokemon)
        self.pokemon_list = new_pokemon_list.copy()
        self.insertPokemonList()

    def searchNumber(self):
        """
        Gets the input from the Number Entry field and calls filterNumber method

        Returns:
            None
        """
        entry = self.number_search_bar.get()
        self.number_search_bar.delete(0, tk.END)
        self.filterNumber(entry)

    def filterBetweenNumbers(self, from_, to_):
        """
        Filters the Pokemon list between two numbers inputted and calls the method insertPokemonList

        Args:
            from_: a number from which the list should include the elements of the Pokemon list
            to_: a number to which the list should include the elements of the Pokemon list

        Returns:
            None
        """
        self.pokemon_listbox.delete(0, tk.END)
        self.pokemon_list.sort()
        if re.findall(r'^$', from_):
            from_ = self.pokemon_list[0][:4]
        if re.findall(r'^$', to_):
            to_ = self.pokemon_list[-1][:4]
        new_pokemon_list = []
        for pokemon in self.pokemon_list:
            # prevents an error that would have been raised if user inputed something that is not a number
            try:
                if int(from_) <= int(pokemon[0:4].lstrip("0")) and int(to_) >= int(pokemon[0:4].lstrip("0")):
                    new_pokemon_list.append(pokemon)
            except:
                pass
        self.pokemon_list = new_pokemon_list.copy()
        self.insertPokemonList()

    def searchBetweenNumbers(self):
        """
        Gets the input from the From Number Entry and To Number Entry fields and calls filterBetweenNumbers method

        Returns:
            None
        """
        from_ = self.number_search_from.get()
        to_ = self.number_search_to.get()
        self.number_search_to.delete(0, tk.END)
        self.number_search_from.delete(0, tk.END)
        self.filterBetweenNumbers(from_, to_)

    def goToPokemonPage(self, event):
        """
        Hides the main page and opens the page of the specific Pokemon that has been chosen from Pokemon ListBox

        Args:
            event: Event signifying the double click on an element of the ListBox

        Returns:
            None
        """
        pokemonName = " ".join(self.pokemon_listbox.get(self.pokemon_listbox.curselection()).strip().split(" ")[1:])
        pokemonClass = pokemon_page.Pokemon(self.window, self.main_frame, pokemonName)
        pokemonClass.grid(row=0, column=0)
        self.main_frame.grid_forget()

    def mainloop(self):
        """
        Starts the application and executes what we wish to execute in an application

        Returns:
            None
        """
        self.window.mainloop()

if __name__=="__main__":
    game_instance = App()
    game_instance.mainloop()
