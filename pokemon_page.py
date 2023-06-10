# Author: Adrian Janus s24768
"""
This module provides functionality needed to visualize the Pokemon page of the Pokedex and providing the user
with the possibility of going between different Pokemon pages and going back to the main page

Libraries/Modules:
    tkinter -- Allows creation of graphical user interface. Thanks to it the Pokedex can be properly displayed
    from PIL:
        Image -- Allows loading images files from files
        ImageTk -- Contains support to create and modify Tkinter BitmapImage and PhotoImage objects from PIL images
        (Thanks to those two modules the images are displayed properly)
    os -- Provides a way to interact with operating system. Thanks to it we can read data from Pokemon text files and get a list of Pokemons text files and images

Classes:
    Pokemon -- A class representing a Frame of the Pokemon page and contains all the modules' methods

Functions/Methods:
    __init__ -- Initializes the pokemon page
    initiate -- Provides all the application widgets needed for visualization and user interaction
    goToPokemonPage -- Shows a different Pokemon page and hides the current one
    getInformation -- Extracts data from the current Pokemons text file
    getPhoto -- Gets a proper image of the current Pokemon to be later displayed on the page
    goBack -- Goes back to the main page and hides the current Pokemon page
"""

import tkinter as tk
from PIL import Image,ImageTk
import os
class Pokemon(tk.Frame):
    """
        A class representing a Pokemon Frame and containing methods that allow it to have some functionality

        Functions/Methods:
            __init__ -- Initializes the pokemon page
            initiate -- Provides all the application widgets needed for visualization and user interaction
            goToPokemonPage -- Shows a different Pokemon page and hides the current one
            getInformation -- Extracts data from the current Pokemons text file
            getPhoto -- Gets a proper image of the current Pokemon to be later displayed on the page
            goBack -- Goes back to the main page and hides the current Pokemon page
    """
    def __init__(self,window,mainframe,name):
        """
        Initializes the pokemon class with its parameters and initializes the Pokemon page itself (displays it)
        with a use of initiate method.

        Args:
            window: The Window of the current running application
            mainframe: The Frame of the Main Page
            name: Name of the Pokemon
        """
        self.window=window
        self.name=name
        self.main_frame=mainframe
        tk.Frame.__init__(self,self.window)
        self.initiate()
    def initiate(self):
        """
        Provides all the application widgets needed for visualization and user interaction, like:
        go_back_button, which allows user to go back to the main page,
        evo_labels that allow to jump to this Pokemons evolution or pre-evolution
        prev_Pokemon_label that allows to go to the Pokemons page that is before it in the Pokedex
        next_Pokemon_label that allows to go to the Pokemons page that is after it in the Pokedex
        """
        pokemonName = self.name
        informationList=self.getInformation(pokemonName)
        number=informationList[0]
        type = informationList[1]
        species=informationList[2]
        height = informationList[3]
        weight = informationList[4]
        evolution=informationList[5]
        entry=informationList[6]
        prev_pok=informationList[7]
        next_pok=informationList[8]

        upper_frame=tk.Frame(self)
        upper_frame.pack(side="top",fill=tk.X,expand=True)
        center_frame = tk.Frame(self)
        center_frame.pack(expand=True,fill=tk.X)
        center_left_frame=tk.Frame(center_frame)
        center_left_frame.pack(side=tk.LEFT,expand=True, fill=tk.X)
        center_right_frame = tk.Frame(center_frame)
        center_right_frame.pack(side=tk.RIGHT, expand=True, fill=tk.X,padx=(20,0))
        bottom_frame = tk.Frame(self)
        bottom_frame.pack(side="bottom",fill=tk.X,expand=True)

        go_back_button = tk.Button(upper_frame, text="Go Back", command=self.goBack,width=10)
        go_back_button.pack(fill=tk.BOTH,side=tk.LEFT)

        title_label = tk.Label(upper_frame, text=number+" "+pokemonName,font=('Courier New bold', 24))
        title_label.pack(fill=tk.BOTH, expand=True)

        image = self.getPhoto(pokemonName,center_left_frame)
        image.pack(ipady=100)

        type_title=tk.Label(center_right_frame, text="Type:", font=('Courier New bold', 12), justify="left")
        type_title.pack(expand=True, anchor=tk.W)
        type_label = tk.Label(center_right_frame, text=type, font=('Courier New ', 12), justify="left")
        type_label.pack(expand=True, anchor=tk.W,pady=(0,5))

        species_title = tk.Label(center_right_frame, text="Species:", font=('Courier New bold', 12), justify="left")
        species_title.pack( expand=True, anchor=tk.W)
        species_label = tk.Label(center_right_frame, text=species, font=('Courier New', 12), justify="left")
        species_label.pack(expand=True, anchor=tk.W, pady=(0, 5))

        height_title = tk.Label(center_right_frame, text="Height:", font=('Courier New bold', 12), justify="left")
        height_title.pack(expand=True, anchor=tk.W)
        height_label = tk.Label(center_right_frame, text=height, font=('Courier New', 12), justify="left")
        height_label.pack(expand=True, anchor=tk.W, pady=(0, 5))

        weight_title = tk.Label(center_right_frame, text="Weight:", font=('Courier New bold', 12), justify="left")
        weight_title.pack(expand=True, anchor=tk.W)
        weight_label = tk.Label(center_right_frame, text=weight, font=('Courier New', 12), justify="left")
        weight_label.pack(expand=True, anchor=tk.W, pady=(0, 5))

        evo_title = tk.Label(center_right_frame, text="Evolution:", font=('Courier New bold', 12), justify="left")
        evo_title.pack(expand=True, anchor=tk.W)
        evo_frame=tk.Frame(center_right_frame)
        evo_frame.pack(expand=True, anchor=tk.W, pady=(0, 5))
        evolution_list=evolution.split("->")
        for i in range(len(evolution_list)):
            evo_label = tk.Label(evo_frame, text=evolution_list[i], font=('Courier New', 12), justify="left")
            evo_label.pack(expand=True, side=tk.LEFT)
            if pokemonName != evolution_list[i] and "does not evolve" not in evolution_list[i]:
                evo_label.config(fg="blue")
                evo_label.bind("<Button-1>", self.goToPokemonPage)
            if(i<len(evolution_list)-1):
                evo_label = tk.Label(evo_frame, text="→", font=('Courier New', 12), justify="left")
                evo_label.pack(expand=True, side=tk.LEFT)

        entry_title = tk.Label(center_right_frame, text="Entry:", font=('Courier New bold', 12), justify="left")
        entry_title.pack(expand=True,anchor=tk.W)
        entry_label = tk.Label(center_right_frame, text=entry, font=('Courier New', 12), wraplength=340, justify="left")
        entry_label.pack(expand=True,anchor=tk.W)

        if prev_pok!="no prev":
            prev_Pokemon_label=tk.Label(bottom_frame, text=prev_pok, font=('Courier New', 12),fg="blue")
            prev_Pokemon_label.pack(side=tk.LEFT)
            prev_Pokemon_label.bind("<Button-1>", self.goToPokemonPage)

        if next_pok != "no next":
            next_Pokemon_label = tk.Label(bottom_frame, text=next_pok, font=('Courier New', 12), fg="blue")
            next_Pokemon_label.pack(side=tk.RIGHT)
            next_Pokemon_label.bind("<Button-1>", self.goToPokemonPage)

    def goToPokemonPage(self,event):
        """
        Shows a different Pokemon page and hides the current one

        Args:
            event:  Event signifying the clicking on a Label
        """
        pokemonName=event.widget.cget("text")
        if "#" in pokemonName:
            pokemonName=" ".join(pokemonName.split(" ")[1:])
        pokemonClass=Pokemon(self.window,self.main_frame,pokemonName)
        pokemonClass.grid(row=0,column=0)
        self.destroy()

    def getInformation(self,pokemonName):
        """
        Extracts data from the current Pokemons text file

        Args:
            pokemonName: The name of the Pokemon we want to get information on

        Returns: list of all the information of this Pokemon or a string "No information available" if there is no
        information provided
        """
        txtPath=""
        #If there is no file corresponding to the Pokemon we will want the method to return adequate message instead of a list
        try:
            contents=os.listdir("./Pokemon_Info")
            for p in contents:
                if pokemonName == p.split("_")[1].replace(".txt",""):
                    txtPath=p
                    break

            f=open("./Pokemon_Info/"+txtPath,"r",encoding="utf-8")
            contents=f.read().strip()
            f.close()
            list=contents.split("\n")
            list.insert(0,txtPath.split("_")[0])
            return list
        except:
            return "No information available"

    def getPhoto(self,pokemonName,container):
        """
        Gets a proper image of the current Pokemon to be later displayed on the page

        Args:
            pokemonName: The name of the Pokemon we want to get image of
            container: The container in which the image should be displayed in

        Returns:
            A Label, which is an image of the current Pokemon or a Label saying "No Photo Available"
        """
        txtPath = ""
        #If there is no image of this Pokemon aveliable method returns a Label saying "No Photo Aveliable" instead of an image
        try:
            contents = os.listdir("./Pokemon_Images")
            for p in contents:
                if pokemonName == p.split("_")[1].replace(".gif",""):
                    txtPath = p
                    break
            self.image = Image.open("./Pokemon_Images/"+txtPath)
            self.image = self.image.resize((290, int(290/self.image.width*self.image.height)))
            self.image = ImageTk.PhotoImage(self.image)
            label_image = tk.Label(container, image=self.image)
            return label_image
        except:
            return tk.Label(self,text="No Photo Available")
            pass

    def goBack(self):
        """
        Goes back to the main page and hides the current Pokemon page
        """
        self.main_frame.grid(row=0, column=0)
        self.destroy()