import os
import shutil

folder_path=input("Enter the path of the folder you want to organize: ").strip()
if not os.path.exists(folder_path):
    print("The specified folder does not exist. Please check the path and try again.")
    exit()
if not os.path.isdir(folder_path):
    print("The specified path is not a folder. Please provide a valid folder path.")

files=os.listdir(folder_path)
file_groups={}

for file in files:
    if os.path.isfile(os.path.join(folder_path,file)):
        fileName,ext=os.path.splitext(file)
        ext=ext.lower()
        if ext=="":
            ext="no_extension"
        if ext in file_groups:
            file_groups[ext].append(file)
        else:
            file_groups[ext]=[file]

for ext,files in file_groups.items():
    print("\n")
    print(f"{ext} Files:")
    folder_for_ext=os.path.join(folder_path,ext.lstrip('.'))
    os.makedirs(folder_for_ext,exist_ok=True)
    files.sort()
    for file in files:
        print(f"-{file}")
        source=os.path.join(folder_path,file)
        destination=os.path.join(folder_for_ext,file)
        if os.path.exists(destination):
            fileName,ext=os.path.splitext(file)
            destination=os.path.join(folder_for_ext,f"{fileName}_copy{ext}")
        try:
            shutil.move(source,destination)
        except Exception as e:
            print(f"Error moving {file}:{e}")


