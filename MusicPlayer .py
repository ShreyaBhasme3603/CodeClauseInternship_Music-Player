import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x200")

        self.folder_path = ""

        self.create_widgets()

        pygame.init()

    def create_widgets(self):
        self.folder_label = tk.Label(self.root, text="Select a folder:")
        self.folder_label.pack()

        self.folder_entry = tk.Entry(self.root, width=30)
        self.folder_entry.pack()

        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_folder)
        self.browse_button.pack()

        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack()

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        self.pause_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack()

    def browse_folder(self):
        self.folder_path = filedialog.askdirectory()
        self.folder_entry.delete(0, tk.END)
        self.folder_entry.insert(0, self.folder_path)

    def play_music(self):
        if self.folder_path:
            music_files = [os.path.join(self.folder_path, file) for file in os.listdir(self.folder_path) if file.endswith(".mp3")]
            for file in music_files:
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()
                # while pygame.mixer.music.get_busy():   # uncomment you want to not available other option when playing song
                #     continue

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
