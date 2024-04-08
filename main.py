import os
import shutil

def create_subfolder_if_needed(folder_path, subfolder_name):
    subfolder_path = os.path.join(folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    return subfolder_path
def clean_folder(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = filename.split('.')[-1].lower()
            if file_extension:
                subfolder_name = f"{file_extension.upper()} Files" 
                subfolder_path = create_subfolder_if_needed(folder_path, subfolder_name)
                file_path = os.path.join(folder_path, filename)
                new_location = os.path.join(subfolder_path,filename)
                if not os.path.exists(new_location):
                    shutil.move(file_path, subfolder_path)
                    print(f"Moved: {filename} -> {subfolder_name}/")
                else:
                    print(f"Skipped: {filename}already exists in {subfolder_name}/")
                

if __name__ == "__main__":
    # print("Desktop Cleaner")
    folder_path = os.path.join(os.path.expanduser("~"), "Downloads")

    # folder_path = "C:\Users\dough\Downloads"
    if os.path.isdir(folder_path):
        clean_folder(folder_path)
        print("Cleaning Complete")
    else:
        print("Invalid folder in path")
    
    
    
## check if code looks good pls