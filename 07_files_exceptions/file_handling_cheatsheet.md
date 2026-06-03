# File Handling Cheatsheet

## File Modes

r  -> Read file  
w  -> Write file (overwrites old content)  
a  -> Append data at end of file  
x  -> Create new file  

---

## Reading Methods

read()       -> Reads complete file  
readline()   -> Reads one line  
readlines()  -> Reads all lines as list  

---

## Important Functions

strip()      -> Removes spaces and \n  
close()      -> Closes the file  
open()       -> Opens a file  

---

## Best Practice

with open()  -> Automatically closes file  

---

## OS Module

os.getcwd()       -> Current working directory  
os.path.exists()  -> Checks file/folder exists  
os.mkdir()        -> Creates folder  

---

## pathlib

Path()         -> Creates path object  
exists()       -> Checks file exists  
read_text()    -> Reads file content  
write_text()   -> Writes file content  

---

## JSON Functions

json.dump()  -> Writes JSON into file  
json.load()  -> Reads JSON from file  

---

## Important Notes

'w' mode deletes old content  
'a' mode keeps old content  

Use 'w' carefully  

Always close files properly