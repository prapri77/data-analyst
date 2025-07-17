"""
file_object = open("filename.txt", "mode")
File Modes:

"r": Read mode (default). Opens for reading.
"w": Write mode. Opens for writing, creating a new file or overwriting an existing one.
"a": Append mode. Opens for writing, adding new content to the end of an existing file.
"x": Exclusive creation mode. Creates a new file and opens it for writing; raises an error if the file already exists.
"b": Binary mode. Used with other modes (e.g., "rb", "wb") for handling binary data (images, executables).
"+": Update mode. Used with other modes (e.g., "r+", "w+") for both reading and writing.
"t" - Text - Default value. Text mode

reading
read(): Reads the entire content of the file.
readline(): Reads a single line from the file.
readlines(): Reads all lines into a list.

write(string): Writes a string to the file.
writelines(list_of_strings): Writes a list of strings to the file.

Closing Files:
It is crucial to close files after operations to release system resources and ensure data integrity.
file_object.close()
"""
with open("textfile\\demofile.txt" , "r") as r:
    #print(r.read()) #read entire line
    #print(r.read(5)) retrun hello from file
    print(r.readline()) #line by line
    print(r.readline())

with open("textfile\\demofile.txt") as f:
  for x in f:
    print(x)

with open("textfile\\demofile.txt", "a") as f: #append
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("textfile\\demofile.txt") as f:
  print(f.read()) #read after append
  #print(f.readlines())

# with open("demofile.txt", "w") as f:
#   f.write("Woops! I have deleted the content!") writing

# #open and read the file after the overwriting:
# with open("demofile.txt") as f:
#   print(f.read())

#f = open("myfile.txt", "x") support only new files

import os 

if os.path.exists("textfile\\demofile.txt"):
  print("file exists")
  file_data = open("textfile\\demofile.txt", 'r')
  content = file_data.read()

  with open("textfile\\demo_file.txt", 'w') as new_file: # here writing older file to new file
    new_file.write(content)
    
else:
  print("file doesnt exist")

c_d = os.getcwd()
print(f"current directory:",c_d) 

contents = os.listdir('.')  # Lists contents of the current directory
print(f"Directory contents: {contents}")

# new_directory = "my_new_folder"
# os.mkdir(new_directory)  # Creates a new directory
# print(f"Directory '{new_directory}' created.")

"""
import os 
def current_path(): 
    print("Current working directory before") 
    print(os.getcwd()) 
    print() 
current_path() 
os.chdir('../') 
current_path() 

import os
directory = "prasanth"
parent_dir = "D:/Pycharm projects/GeeksForGeeks/Authors"
path = os.path.join(parent_dir, directory)
os.makedirs(path)
print("Directory '% s' created" % directory)

import os #importing os module
size = os.path.getsize("filename")
print("Size of the file is", size," bytes.")

os.mkdir()
os.makedirs()
os.listdir()
os.remove()
os.rmdir()
os.name
os.close()
os.rename()
os.path.getsize()
os.path.exists() 
"""