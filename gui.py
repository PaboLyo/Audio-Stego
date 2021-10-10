import tkinter as tk
import tkinter.font as tkFont
import sys
import os

from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from AudioStegnographyAlgo.LSBAudioStego import LSBAudioStego
from PIL import Image
from moviepy.editor import *

class App:
    def __init__(self, root):
        #setting title
        root.title("Audio Stegano")
        #setting window size
        width=900
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        lblAudioExtractor=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        lblAudioExtractor["font"] = ft
        lblAudioExtractor["fg"] = "#333333"
        lblAudioExtractor["justify"] = "center"
        lblAudioExtractor["text"] = "Audio Extractor"
        lblAudioExtractor.place(x=0,y=10,width=148,height=30)

        lblFileInput=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lblFileInput["font"] = ft
        lblFileInput["fg"] = "#333333"
        lblFileInput["justify"] = "center"
        lblFileInput["text"] = "Input:"
        lblFileInput.place(x=0,y=40,width=59,height=30)

        lblFileOutput=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lblFileOutput["font"] = ft
        lblFileOutput["fg"] = "#333333"
        lblFileOutput["justify"] = "center"
        lblFileOutput["text"] = "Output:"
        lblFileOutput.place(x=0,y=70,width=51,height=30)

        lblFileInputDirectory=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lblFileInputDirectory["font"] = ft
        lblFileInputDirectory["fg"] = "#333333"
        lblFileInputDirectory["justify"] = "left"
        lblFileInputDirectory["text"] = "label"
        self.vidFileVar = StringVar()
        lblFileInputDirectory["textvariable"]=self.vidFileVar
        lblFileInputDirectory.place(x=60,y=40,width=300,height=30)

        lblFileOutputDirectory=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lblFileOutputDirectory["font"] = ft
        lblFileOutputDirectory["fg"] = "#333333"
        lblFileOutputDirectory["justify"] = "left"
        lblFileOutputDirectory["text"] = "label"
        lblFileOutputDirectory.place(x=60,y=70,width=208,height=30)

        btnAudioConverter=tk.Button(root)
        btnAudioConverter["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        btnAudioConverter["font"] = ft
        btnAudioConverter["fg"] = "#000000"
        btnAudioConverter["justify"] = "center"
        btnAudioConverter["text"] = "Extract Audio to wav"
        btnAudioConverter.place(x=160,y=110,width=129,height=30)
        btnAudioConverter["command"] = self.btnAudioConverter_command

        btnAudioSelector = tk.Button(root)
        btnAudioSelector["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        btnAudioSelector["font"] = ft
        btnAudioSelector["fg"] = "#000000"
        btnAudioSelector["justify"] = "center"
        btnAudioSelector["text"] = "Select File"
        btnAudioSelector.place(x=20, y=110, width=129, height=30)
        btnAudioSelector["command"] = self.btnAudioSelector_command

        lblAudioEncDec=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        lblAudioEncDec["font"] = ft
        lblAudioEncDec["fg"] = "#333333"
        lblAudioEncDec["justify"] = "center"
        lblAudioEncDec["text"] = "Audio Encoder / Decoder"
        lblAudioEncDec.place(x=10,y=150,width=186,height=30)

        lblAudioEnc=tk.Label(root)
        ft = tkFont.Font(family='Times',size=11)
        lblAudioEnc["font"] = ft
        lblAudioEnc["fg"] = "#333333"
        lblAudioEnc["justify"] = "center"
        lblAudioEnc["text"] = "Encoding"
        lblAudioEnc.place(x=0,y=190,width=70,height=25)

        lblAudioInput=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lblAudioInput["font"] = ft
        lblAudioInput["fg"] = "#333333"
        lblAudioInput["justify"] = "center"
        lblAudioInput["text"] = "Audio Input:"
        lblAudioInput.place(x=0,y=220,width=83,height=30)

        lblText=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lblText["font"] = ft
        lblText["fg"] = "#333333"
        lblText["justify"] = "center"
        lblText["text"] = "Text Input:"
        lblText.place(x=0,y=250,width=72,height=30)

        lblAudioInputDirectory=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lblAudioInputDirectory["font"] = ft
        lblAudioInputDirectory["fg"] = "#333333"
        lblAudioInputDirectory["justify"] = "left"
        lblAudioInputDirectory["text"] = ""
        self.fileVar = StringVar()
        lblAudioInputDirectory["textvariable"] = self.fileVar
        lblAudioInputDirectory.place(x=80,y=220,width=220,height=30)

        self.entryText = tk.Entry(root)
        self.entryText.place(x=80, y=250)
        self.entryText.insert(0, "Enter String to encode ")

        btnFileLocation=tk.Button(root)
        btnFileLocation["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        btnFileLocation["font"] = ft
        btnFileLocation["fg"] = "#000000"
        btnFileLocation["justify"] = "center"
        btnFileLocation["text"] = "Select File to Encode"
        btnFileLocation.place(x=10,y=290,width=128,height=30)
        btnFileLocation["command"] = self.btnFileLocation_command

        btnAudioEncode=tk.Button(root)
        btnAudioEncode["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        btnAudioEncode["font"] = ft
        btnAudioEncode["fg"] = "#000000"
        btnAudioEncode["justify"] = "center"
        btnAudioEncode["text"] = "Encode"
        btnAudioEncode.place(x=150,y=290,width=70,height=30)
        btnAudioEncode["command"] = self.btnAudioEncode_command

        lblAudioDec=tk.Label(root)
        ft = tkFont.Font(family='Times',size=11)
        lblAudioDec["font"] = ft
        lblAudioDec["fg"] = "#333333"
        lblAudioDec["justify"] = "center"
        lblAudioDec["text"] = "Decoding"
        lblAudioDec.place(x=350,y=190,width=70,height=25)

        lblAudioEncInput=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lblAudioEncInput["font"] = ft
        lblAudioEncInput["fg"] = "#333333"
        lblAudioEncInput["justify"] = "center"
        lblAudioEncInput["text"] = "Encoded Input Location:"
        lblAudioEncInput.place(x=320,y=220,width=200,height=49)

        lblAudioEncInputDirectory=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lblAudioEncInputDirectory["font"] = ft
        lblAudioEncInputDirectory["fg"] = "#333333"
        lblAudioEncInputDirectory["justify"] = "center"
        lblAudioEncInputDirectory["text"] = "test"
        self.decodeFileVar = StringVar()
        lblAudioEncInputDirectory["textvariable"] = self.decodeFileVar
        lblAudioEncInputDirectory.place(x=530,y=220,width=241,height=44)

        btnFileDecLocation = tk.Button(root)
        btnFileDecLocation["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        btnFileDecLocation["font"] = ft
        btnFileDecLocation["fg"] = "#000000"
        btnFileDecLocation["justify"] = "center"
        btnFileDecLocation["text"] = "Select Audio File to Decode"
        btnFileDecLocation.place(x=330,y=290,width=240,height=30)
        btnFileDecLocation["command"] = self.btnFileDecLocation_command

        btnAudioDecode=tk.Button(root)
        btnAudioDecode["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        btnAudioDecode["font"] = ft
        btnAudioDecode["fg"] = "#000000"
        btnAudioDecode["justify"] = "center"
        btnAudioDecode["text"] = "Decode"
        btnAudioDecode.place(x=580,y=290,width=77,height=30)
        btnAudioDecode["command"] = self.btnAudioDecode_command

        lblAudioOutput=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lblAudioOutput["font"] = ft
        lblAudioOutput["fg"] = "#333333"
        lblAudioOutput["justify"] = "center"
        lblAudioOutput["text"] = "Output:"
        lblAudioOutput.place(x=330,y=340,width=77,height=30)

        lblAudioOutputText=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lblAudioOutputText["font"] = ft
        lblAudioOutputText["fg"] = "#333333"
        lblAudioOutputText["justify"] = "center"
        lblAudioOutputText["text"] = "label"
        self.decodedString = StringVar()
        lblAudioOutputText["textvariable"]=self.decodedString
        lblAudioOutputText.place(x=330,y=370,width=344,height=103)

        self.enocdedLocation = StringVar()
        self.locationOfEncodeFile = Label(root, textvariable=self.enocdedLocation)
        self.locationOfEncodeFile.place(x=10, y=280)

    def btnAudioSelector_command(self):
        print("Selecting File!")
        self.selectVidFile()

    def btnAudioConverter_command(self):
        print("Converting audio file to wav & mp3")
        self.extractmp3wav()


    def btnFileLocation_command(self):
        print("Selecting an Audio File for encoding Now")
        self.selectFile()

    def btnFileDecLocation_command(self):
        print("Selecting an Audio File Now")
        self.selectFileDecode()

    def btnAudioEncode_command(self):
        print("Encoding Audio Now")
        self.encode()

    def btnAudioDecode_command(self):
        print("Decoding Audio Now")
        self.decode()

    def selectFile(self):
        # file selection
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("Wav files", "*.wav"), ("all files", "*.*")))
        self.fileSelected = root.filename
        self.fileVar.set(root.filename)

    def selectFileDecode(self):
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("Wav files", "*.wav"), ("all files", "*.*")))
        self.fileSelcetedForDecode = root.filename
        self.decodeFileVar.set(root.filename)
        print("1: " +self.fileSelcetedForDecode)

    def selectVidFile(self):
        # file selection
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("Mp4 files", "*.mp4"), ("all files", "*.*")))
        self.vidFile = root.filename
        self.baseFileName = root.filename
        self.vidFileVar.set(root.filename)

    def extractmp3wav(self):
        #
        video_object = VideoFileClip(self.vidFile)
        self.get_audio(self.baseFileName, video_object)

    def get_audio(self,base_filename, video_object):
        """Returns the audio track only of a video clip"""
        #video_object.audio.write_audiofile(filename=f'output\\{base_filename}_audio.wav')
        #video_object.audio.write_audiofile(filename=f'output\\{base_filename}_audio.mp3')
        video_object.audio.write_audiofile(base_filename + "_audio.wav")


    def encode(self):
        """Select LSB Algo to encode"""
        print("Start Of Encode Algo")
        algo = LSBAudioStego()
        result = algo.encodeAudio(self.fileSelected, self.entryText.get())
        self.enocdedLocation.set(result)
        print("End Of Encode Algo")
        print("Encoded Location:" + result)

    def decode(self):
        """"Select LSB Algo to decode"""
        print("Start Of Decode Algo")
        algo = LSBAudioStego()
        result = algo.decodeAudio(self.fileSelcetedForDecode)
        self.decodedString.set(result)
        print("End Of Decode Algo")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
