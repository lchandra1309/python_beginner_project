from tkinter import *
from pytube import YouTube
from tkinter import filedialog as fd
from tkinter import messagebox

import os

root=Tk()
root.title='Youtube Downloader'

root.iconbitmap(r'youtube_samples\youtube.ico')

#  functions for the button

def downloadfile():
    global urllink
    pathfinder=str(downloadpath.get())

    urllink=str(urlentry.get())
    youtube=YouTube(urllink)
    data=youtube.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first()
    # data=youtube.streams.get_by_itag(243)
    data.download(pathfinder)


def fileview():
    global pathfile
    global urlentry

    pathfile=fd.askdirectory()
    downloadpath.insert(0,str(pathfile))
    button.destroy()
    button1=Button(label2,text='change path',padx=25,pady=10,command=fileview)
    button1.grid(row=1,column=0)

    label3=LabelFrame(root,padx=10,pady=10)
    label3.pack()
    headlabel=Label(label3,text='paste the youtube link to download')
    headlabel.pack()
    urlentry=Entry(label3,width=50,borderwidth=10)
    urlentry.pack()
    if len(str(downloadpath.get())) !=0:
        button2=Button(label3,text='Download',command=downloadfile)
        button2.pack()
    else:
        button2=Button(label3,text='Download',command=downloadfile,state=DISABLED)
        button2.pack()


# basic buttons and labels

label=Label(root,text='Enter the Link below to Download youtube videos..')
label.pack()

label2=LabelFrame(root,padx=10,pady=10)
label2.pack()

global downloadpath

downloadpath=Entry(label2,width=50,borderwidth=5)
downloadpath.grid(row=0,column=0)

button=Button(label2,text='Choose Folder to Save Downloaded videos',command=fileview)
button.grid(row=1,column=0)
root.mainloop()