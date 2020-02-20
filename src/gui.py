from os import system as sysrun, _exit as stop
from difflib import get_close_matches
import tkinter as tk
from functools import partial 

def stopApp(root):
	
	sysrun('killall rhythmbox')
	root.destroy()
	stop(0)


def makechoice(matches, index):	
	
	choice=matches[index]
	return choice


def window1(data, songlist):
	
	root = tk.Tk()  
	root.geometry('400x200+100+200') 
	root.title('Match My Song')

	titlevar = tk.StringVar()  
	label = tk.Label(root, text="Enter song name: ").grid(row=1, column=0) 
	entry = tk.Entry(root, textvariable=titlevar)
	entry.grid(row=1, column=2)  

	call_result = partial(matchsong, data, songlist, titlevar, root)

	buttonCal = tk.Button(root, text="Stop", command=partial(stopApp, root)).grid(row=3, column=0)
	entry.bind('<Return>', call_result)
	entry.focus_set()
	root.mainloop()


def reselect(root, data, songlist):
	
	root.destroy()
	window1(data, songlist)


def matchsong(data, songlist, titlevar, root, _):
	
	title=titlevar.get()	
	matches=get_close_matches(title, songlist)
	root.destroy()
	window2(data, songlist, matches)	
	

def window2(data, songlist, matches):

    # create window
    root = tk.Tk()        
    root.geometry("600x600+100+200")  	      
    root.title("Play My Song :)")
    

    # listbox construction
    listbox = tk.Listbox(root)	    
    call_result=partial(playsong, root, data, songlist, listbox, matches)

    i=1
    for match in matches:
    	listbox.insert(i,match)
    	i=i+1    

    listbox.focus_set()
    listbox.select_set(0)
    listbox.bind('<Return>', call_result)
    listbox.pack()  


    caller_to_reselect=partial(reselect, root, data, songlist)        
    reselectbtn = tk.Button(root, text = "reselect", command=caller_to_reselect)
    reselectbtn.pack()

    caller_to_addToQ = partial(add_to_queue, data, matches, listbox)
    addToQ = tk.Button(root, text = "Add to Queue", command=caller_to_addToQ)
    addToQ.pack(side=tk.RIGHT)
          
    root.mainloop()


def add_to_queue(data, matches, listbox):

	index=listbox.curselection()[0]
	choice=makechoice(matches, index)

	songlocation = data[data["song"]==choice]['location'].iat[0]

	print("Playing ", choice, "at ", songlocation)
	sysrun('rhythmbox-client --enqueue \"'+songlocation+"\" &")	


def playsong(root, data, songlist, listbox, matches, _):
	
	index=listbox.curselection()[0]
	choice=makechoice(matches, index)

	songlocation = data[data["song"]==choice]['location'].iat[0]

	print("Playing ", choice, "at ", songlocation)
	sysrun('rhythmbox-client --play-uri=\"'+songlocation+"\" &")
	root.destroy()
	window1(data, songlist)