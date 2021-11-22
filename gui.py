from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk


def execute():
	global dockercompose_name
	x=dockercompose_nameobj.get()
	dockercompose_name = x
	global application_name
	y=application_nameobj.get()
	application_name = y
	global app_id
	j=app_idobj.get()
	app_id = j
	
	root.destroy()   
    
	
def select_path():
	global destination_path
	path= filedialog.askdirectory(title="Select a Path")
	Label(root, text=path, font=3).grid(row=9,column=0)
	destination_path = path


root=tk.Tk()
root.title("Generation MACM from docker compose - Author: Luca Di Girolamo")
root.geometry("600x400")


dockercompose_nameobj=tk.StringVar()
destination_pathobj=tk.StringVar()
application_nameobj=tk.StringVar()
app_idobj=tk.StringVar()



button= tk.Button(root, text="Seleziona directory", command= select_path)

# creating a label

#description
description = tk.Label(root, text = '1-Inserire nome del file docker-compose (senza estensione) \nInserire Application Name\nInserire App Id \n2-Selezionare il path in cui salvare il MACM in output cliccando su "Seleziona directory" \n3-Esegui \nNB. Il file docker-compose dovrà trovarsi nella stessa directory in cui è eseguito il generator_cypher', font=('calibre',8, 'bold'))

name_label = tk.Label(root, text = 'Docker Compose file:', font=('calibre',10, 'bold'))
name_label2 = tk.Label(root, text = 'Application Name:', font=('calibre',10, 'bold'))
name_label3 = tk.Label(root, text = 'App Id:', font=('calibre',10, 'bold'))

name_entry = tk.Entry(root,textvariable = dockercompose_nameobj, font=('calibre',10,'normal'))
name_entry2 = tk.Entry(root,textvariable = application_nameobj, font=('calibre',10,'normal'))
name_entry3 = tk.Entry(root,textvariable = app_idobj, font=('calibre',10,'normal'))

pathprint = tk.Label(root, text = destination_pathobj, font=('calibre',10, 'bold'))

space = tk.Label(root, text= "\n")

exe = tk.Button(root,text = 'Esegui generator cypher', command = execute)


description.grid(row=0,column=0)
space.grid(row=1,column=0)
name_label.grid(row=2,column=0)
name_entry.grid(row=3,column=0)
name_label2.grid(row=4,column=0)
name_entry2.grid(row=5,column=0)
name_label3.grid(row=6,column=0)
name_entry3.grid(row=7,column=0)
button.grid(row=8,column=0)
exe.grid(row=10,column=0)

dockercompose_name=str(dockercompose_nameobj)
application_name=str(application_nameobj)
app_id=str(app_idobj)
destination_path=str(destination_pathobj)



root.mainloop()

