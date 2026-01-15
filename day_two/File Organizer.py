import os
import shutil


path = r"\Users\zahoraty\Downloads" 


file_mapping = {
    "Images": [".jpg", ".jpeg", ".png", ".gif",".jfif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Zipped": [".zip", ".rar"],
    "music" : [".mp3"]
}

files = os.listdir(path)

for file in files:
    
    _, extension = os.path.splitext(file)
    extension = extension.lower()

    for folder_name, extensions in file_mapping.items():
        if extension in extensions:
            folder_path = os.path.join(path, folder_name)
            
          
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
          
            original_path = os.path.join(path, file)
            new_path = os.path.join(folder_path, file)
            shutil.move(original_path, new_path)

print("done")