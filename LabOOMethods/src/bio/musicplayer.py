# Importing Required Modules & libraries
from tkinter import *
from tkinter.ttk import *
import pygame
import os

DEBUG = True


class MusicPlayer:
    """One object of this class represents a tkinter GUI application that plays
    audio files."""

    def __init__(self, root):
        """Creates a tkinter GUI application that plays audio files."""
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("1000x200+200+200")
        pygame.init()
        pygame.mixer.init()
        # TODO: Make the self.track and self.status StringVar objects

        # Creating trackframe for songtrack label & trackstatus label
        trackframe = LabelFrame(self.root, text="Song Track", relief=GROOVE)
        trackframe.place(x=0, y=0, width=600, height=100)
        # TODO Below make the self.track the textvariable for songtrack and
        # the self.status the textvariable for trackstatus
        songtrack = Label(trackframe).grid(
            row=0, column=0, padx=10, pady=5)
        trackstatus = Label(trackframe).grid(
            row=0, column=1, padx=10, pady=5)

        # Creating buttonframe
        buttonframe = LabelFrame(
            self.root, text="Control Panel", relief=GROOVE)
        # Inserting song control Buttons
        buttonframe.place(x=0, y=100, width=600, height=100)
        Button(buttonframe, text="Play", command=self.playsong).grid(
            row=0, column=0, padx=10, pady=5)
        Button(buttonframe, text="Pause", command=self.pausesong
               ).grid(row=0, column=1, padx=10, pady=5)
        Button(buttonframe, text="Unpause", command=self.unpausesong
               ).grid(row=0, column=2, padx=10, pady=5)
        Button(buttonframe, text="Stop", command=self.stopsong).grid(
            row=0, column=3, padx=10, pady=5)
        Button(buttonframe, text="Refresh From Folder",
               command=self.refresh).grid(row=1, column=3, padx=10, pady=5)

        # Creating songsframe
        songsframe = LabelFrame(self.root, text="Song Playlist", relief=GROOVE)
        songsframe.place(x=600, y=0, width=400, height=150)
        scrol_y = Scrollbar(songsframe, orient=VERTICAL)
        self.playlist = Listbox(songsframe, yscrollcommand=scrol_y.set,
                                selectbackground="gold",
                                selectmode=SINGLE, relief=GROOVE)
        # Applying Scrollbar to playlist Listbox
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)

        # Adding playlist search controls
        searchframe = LabelFrame(self.root, relief=GROOVE)
        searchframe.place(x=600, y=145, width=400, height=50)
        search_input = Entry(searchframe, width=30)
        # TODO: Make the self.inputVar StringVar object
        # TODO Below make the self.inputVar the textvariable for search_input
        search_input.grid(row=1, column=1, padx=1, pady=1)
        Button(searchframe, text="Search",
               command=self.search).grid(row=1, column=2, padx=1, pady=1)

        # Changing directory for fetching songs
        os.chdir("./music")
        # Inserting songs into playlist
        self.refresh()

    def search(self):
        """
        TODO: Explain below in this docstring what an algorithm is.
        Then explain how your search algorithm is implemented in this method.
        Use a least two full sentences of U.S. English.
        TODO: Remove from the self.playlist ListBox any filename that does not
        partially match the characters from the self.inputVar of the
        search_input Entry widget. Catch any possible exceptions.
        """

    def playsong(self):
        """
        TODO:
        Displays selected song and its playing status and plays the song.
        """

    def stopsong(self):
        """TODO: Displays stopped status and stops the song."""

    def pausesong(self):
        """TODO: Displays the paused status and pauses the song."""

    def unpausesong(self):
        """TODO: Displays the playing status and unpauses the song."""

    def refresh(self):
        """
        TODO:
        Clears the current playlist and fills it with all valid sound files
        from the music folder. All exception messages are appended to the
        status in their default string form.
        See the .pdf reference files for how to insert items into a tkinter
        Listbox.
        """

        # TODO: First clear the search_input Entry widget via self.inputVar

        # TODO: Ignore files whose names that start with "."
        # and those that are not .mp3, .ogg, or .wav files


def main():
    """Create main window and start a MusicPlayer application on it."""
    # Creating TK root window
    root = Tk()
    # Passing root to the MusicPlayer constructor
    app = MusicPlayer(root)
    # Start the main GUI loop
    root.mainloop()


if __name__ == "__main__":
    main()
