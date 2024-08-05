import os
import shutil

path = r"C:/Users/Phage/Desktop/C0D3/File SOrter/final bin" #configure path OF BIN here, type in between the ""
path += "/"
print(path)

items_moved = 0 #GLOBAL VARIABLE 

def add_file_type(file_type): #adds file type to FOLDER list and file_type identifiers
    if file_type == '':
        pass
    elif file_type != '': 
        folder_names.append(file_type)
        file_types["." + file_type] = file_type
    return   

# OBJECTIVES ----------------------------
# check if there is a folder for each file format if not then create one
# organize each file based on file format and then move them to their respective directories

file_names = os.listdir(path) #Lists all files found in directory
#print(file_names)

folder_names = [] #LIST OF FOLDERS ----------- add here extra folder (DEPENDING ON TYPES)
file_types = {} #DICT OF filetype:folder ------------ FILE TYPE IDENTIFIERS HERE

for file_name in file_names:
    if '.' not in file_name:
        #print('passed')
        pass
    else:
        splitter = file_name.rsplit('.', 1)
        #print(f"file type is {splitter[1]}")
        add_file_type(splitter[1])

print(f"Types of documents found in {path}: {file_types.keys()}") # LOG - DISPLAYS TYPES OF DOCUMENTS FOUND


# FOLDER CREATOR
for folders in range(0, len(folder_names)):
    if not os.path.exists(path + folder_names[folders]):
        print(f"Created path {path + folder_names[folders]}")
        os.makedirs(path + folder_names[folders])



# FILE MOVER - iterates through each FILE and each known FILE TYPE, then moves it to its corresponding folder according to its identifier
for file in file_names: 
    for file_type in file_types:
        try:
            if file_type in file and not os.path.exists(path + file_types[file_type] + '/' + file): #multi - format
                shutil.move(path + file, path + file_types[file_type] + '/' + file)
                print(f"moved {file} to {path + file_types[file_type] + '/'}")
                items_moved += 1
        except:
            print("ERROR: Some files could not be moved")


print(f"{items_moved} total items moved.")
        
