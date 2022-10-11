import os
import re
import shutil

# Input the destination
destination = '/Users/dhairyaostwal/Downloads/' # Here you can change the Destination of the VTOP Download Folder


directoryList = os.chdir(destination)
print(os.getcwd())

files = os.listdir()
pattern = re.compile(r"\d\d-\d\d-20\d\d_(.+)$")

for f in [file for file in files if os.path.isfile(file)]:
	x=pattern.search(f)
	name=f
	if x:
		name=x.group(0)
		name=re.sub(r"_"," ",name)
		name=re.sub(r"  +"," ",name)
		shutil.move(os.path.join(os.getcwd(),f),os.path.join(os.getcwd(),name))
		
print("Success :)")
