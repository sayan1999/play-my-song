from utils import loaddata
from gui import window1
from os import system as sysrun

sysrun('rhythmbox-client --clear-queue &')
sysrun('rhythmbox-client --stop')

data=loaddata('./objects/df.obj')
songlist=data['song'].tolist()

window1(data, songlist)