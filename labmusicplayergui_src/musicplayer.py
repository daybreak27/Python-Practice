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

        # StringVar objects to store track and status
        self.track = StringVar()
        self.status = StringVar()
        self.inputVar = StringVar()

        # Creating trackframe for songtrack label & trackstatus label
        trackframe = LabelFrame(self.root, text="Song Track", relief=GROOVE)
        trackframe.place(x=0, y=0, width=600, height=100)

        # Associating StringVar objects with labels
        songtrack = Label(trackframe, textvariable=self.track, width=25).grid(
            row=0, column=0, padx=10, pady=5)
        trackstatus = Label(trackframe, textvariable=self.status, width=15).grid(
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
        search_input = Entry(searchframe, width=30, textvariable=self.inputVar)
        search_input.grid(row=1, column=1, padx=1, pady=1)
        Button(searchframe, text="Search",
               command=self.search).grid(row=1, column=2, padx=1, pady=1)
        
        #Binding enter key to search
        search_input.bind('<Return>', lambda event: self.search())

        # Changing directory for fetching songs
        os.chdir("./music")
        # Inserting songs into playlist
        self.refresh()

    def search(self):
        """
        An algorithm is a step-by-step procedure to solve a problem or perform a task.
        This search algorithm filters the playlist based on the input provided
        in the search_input Entry widget.
        """
        try:
            query = self.inputVar.get().lower()
            all_songs = os.listdir()
            self.playlist.delete(0, END)
            for song in all_songs:
                if query in song.lower() and song.lower().endswith(('.mp3', '.ogg', '.wav')):
                    self.playlist.insert(END, song)
        except Exception as e:
            self.status.set(f"Error: {e}")

    def playsong(self):
        """
        Displays selected song and its playing status and plays the song.
        """
        try:
            song = self.playlist.get(ACTIVE)
            self.track.set(song)
            self.status.set("Playing")
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
        except Exception as e:
            self.status.set(f"Error: {e}")

    def stopsong(self):
        """Displays stopped status and stops the song."""
        try:
            self.status.set("Stopped")
            pygame.mixer.music.stop()
        except Exception as e:
            self.status.set(f"Error: {e}")

    def pausesong(self):
        """Displays the paused status and pauses the song."""
        try:
            self.status.set("Paused")
            pygame.mixer.music.pause()
        except Exception as e:
            self.status.set(f"Error: {e}")

    def unpausesong(self):
        """Displays the playing status and unpauses the song."""
        try:
            self.status.set("Playing")
            pygame.mixer.music.unpause()
        except Exception as e:
            self.status.set(f"Error: {e}")

    def refresh(self):
        """
        Clears the current playlist and fills it with all valid sound files
        from the music folder. All exception messages are appended to the
        status in their default string form.
        """
        try:
            self.inputVar.set("")  # Clear the search input
            self.playlist.delete(0, END)
            for file in os.listdir():
                if not file.startswith('.') and file.lower().endswith(('.mp3', '.ogg', '.wav')):
                    self.playlist.insert(END, file)
        except Exception as e:
            self.status.set(f"Error: {e}")


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
