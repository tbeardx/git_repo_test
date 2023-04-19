import sys
import re
from zipfile import ZipFile

# Create a ZipFile Object and load sample.zip in it
with ZipFile(sys.argv[1], 'r') as zipObj:
   # Get list of files names in zip
   listOfiles = zipObj.namelist()
   # Iterate over the list of file names in given list & print them
   for elem in listOfiles:
   	if re.search(sys.argv[2], elem, re.IGNORECASE):
   		print(elem)

# if __name__ == '__main__':
#     # Change this to the directory you want to search for zip files in
#     # path = "C:/Users/MyUser/Documents"
#    #  path = "C:\ITE_IVV"
#    path = "C:\Users\will.elliott\OneDrive - PeopleTec, Inc\ITE IV&V\Software\Scripts\T901 Draft Drawings 2020-03-09.zip"

#     # Find all zip files in the directory and subdirectories
#    zip_paths = find_zips(path)

    # Process each zip file by extracting its contents to a new folder
    # for zip_path in zip_paths:
    #     process_zip(zip_path)