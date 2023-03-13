# importing libraries
from pygame import mixer
from tkinter import *
import tkinter.font as font
import tkinter
from tkinter import filedialog
from tinytag import TinyTag


# add many songs to the playlist
def addsongs():
    # a list of songs is returned
    temp_song = filedialog.askopenfilenames(initialdir="music-library/", title="Choose a song", filetypes=(("wav Files", "*.wav"),))
    # loop through everyitem in the list
    for s in temp_song:
        songs_list.insert(END, s)
        tag = TinyTag.get(s)
        pathlist.append(s)
        namelist.append(tag.title)
        timelist.append(tag.duration)
        artistlist.append(tag.artist)
        albumlist.append(tag.album)
        #print(tag.title)


def deletesong():
    curr_song = songs_list.curselection()
    songs_list.delete(curr_song[0])
    pathlist.pop(curr_song[0])
    namelist.pop(curr_song[0])
    timelist.pop(curr_song[0])
    artistlist.pop(curr_song[0])
    albumlist.pop(curr_song[0])


def Play():
    song = songs_list.get(ACTIVE)
    song = f'{song}'
    mixer.music.load(song)
    mixer.music.play()
    # update the label
    this_one = songs_list.curselection()
    this_one = this_one[0]
    text1.set(str(namelist[this_one]))
    text2.set(str(timelist[this_one])) 
    text3.set(str(artistlist[this_one]))
    text4.set(str(albumlist[this_one]))

# to pause the song
def Pause():
    mixer.music.pause()


# to stop the  song
def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)


# to resume the song

def Resume():
    mixer.music.unpause()


# Function to navigate from the current song
def Previous():
    # to get the selected song index
    previous_one = songs_list.curselection()
    # to get the previous song index
    previous_one = previous_one[0] - 1
    if (previous_one < 0): previous_one = songs_list.size() - 1
    # to get the previous song
    temp2 = songs_list.get(previous_one)
    temp2 = f'{temp2}' # need boundary judgment
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0, END)
    # activate new song
    songs_list.activate(previous_one)
    # set the next song
    songs_list.selection_set(previous_one)
    # update the label
    this_one = songs_list.curselection()
    this_one = this_one[0]
    text1.set(str(namelist[this_one]))
    text2.set(str(timelist[this_one])) 
    text3.set(str(artistlist[this_one]))
    text4.set(str(albumlist[this_one]))


def Next():
    # to get the selected song index
    next_one = songs_list.curselection()
    # to get the next song index
    next_one = next_one[0] + 1
    if (next_one >= songs_list.size()): next_one = 0
    # to get the next song
    temp = songs_list.get(next_one)
    temp = f'{temp}' # need boundary judgment
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_clear(0, END)
    # activate newsong
    songs_list.activate(next_one)
    # set the next song
    songs_list.selection_set(next_one)
    # update the label
    this_one = songs_list.curselection()
    this_one = this_one[0]
    text1.set(str(namelist[this_one]))
    text2.set(str(timelist[this_one])) 
    text3.set(str(artistlist[this_one]))
    text4.set(str(albumlist[this_one]))

pathlist = []
namelist = []
timelist = []
artistlist = []
albumlist = []

# creating the root window
root = Tk()
root.title('DataFlair Music player App ')
# initialize mixer
mixer.init()
#
#headIMG = tkinter.PhotoImage(file=r"starsky2.png")
#label_img = tkinter.Label(root, image = headIMG, height=12, width=94)
#label_img.grid(columnspan=9)

# create the listbox to contain songs
songs_list = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=('arial', 15), height=24, width=94,
                     selectbackground="gray", selectforeground="black")
songs_list.grid(columnspan=9,row = 0)

# font is defined which is to be used for the button font
defined_font = font.Font(family='microsoft yahei')

# play button
playBTN = tkinter.PhotoImage(file=r"play button2.png")
play_button = Button(root, text="Play", width=160, height = 160, image=playBTN,command=Play)
play_button['font'] = defined_font
play_button.grid(row=1, column=0)

# pause button
pauseBTN = tkinter.PhotoImage(file=r"pause button2.png")
pause_button = Button(root, text="Pause", width=160, height = 160, image=pauseBTN,command=Pause)
pause_button['font'] = defined_font
pause_button.grid(row=1, column=1)

# stop button
stopBTN = tkinter.PhotoImage(file=r"stop button2.png")
stop_button = Button(root, text="Stop", width=160, height = 160, image=stopBTN,command=Stop)
stop_button['font'] = defined_font
stop_button.grid(row=1, column=2)

# resume button
resumeBTN = tkinter.PhotoImage(file=r"resume button2.png")
Resume_button = Button(root, text="Resume", width=160, height = 160, image=resumeBTN,command=Resume)
Resume_button['font'] = defined_font
Resume_button.grid(row=1, column=3)

# previous button
previousBTN = tkinter.PhotoImage(file=r"sea you next3.png")
previous_button = Button(root, text="Prev", width=160, height = 160, image=previousBTN,command=Previous)
previous_button['font'] = defined_font
previous_button.grid(row=1, column=4)

# nextbutton
nextBTN = tkinter.PhotoImage(file=r"sea you next2.png")
next_button = Button(root, text="Next", width=160, height = 160, image=nextBTN,command=Next)
next_button['font'] = defined_font
next_button.grid(row=1, column=5)

# label
text1 = StringVar()
text2 = StringVar()
text3 = StringVar()
text4 = StringVar()
lb1 = tkinter.Label(root, textvariable=text1)
lb1.grid(row=2, column=0)
lb2 = tkinter.Label(root, textvariable=text2)
lb2.grid(row=2, column=1)
lb3 = tkinter.Label(root, textvariable=text3)
lb3.grid(row=2, column=2)
lb4 = tkinter.Label(root, textvariable=text4)
lb4.grid(row=2, column=3)
# menu
my_menu = Menu(root)
root.config(menu=my_menu)
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=add_song_menu)
add_song_menu.add_command(label="Add songs", command=addsongs)
add_song_menu.add_command(label="Delete song", command=deletesong)

mainloop()
