# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 17:46:40 2017

@author: Dion
"""

import mne
from  tkinter import *
from tkinter.filedialog import askopenfilename

root = Tk()
filename =  askopenfilename(title = "choose your file",filetypes = (("set files","*.set"),("all files","*.*")))
print (filename)
root.withdraw()


DionData = mne.io.read_raw_eeglab(filename, montage=None, eog=(), event_id=None, event_id_func='strip_to_integer', preload=False, verbose=None, uint16_codec=None)

DionData.load_data()

DionData.plot(block=True)

DionData.filter(1, 30)

DionData.plot(block=True)

DionData.save('C:\\Users\\Dion\\Desktop\\EEGDataThing.raw.fif', overwrite=True) 