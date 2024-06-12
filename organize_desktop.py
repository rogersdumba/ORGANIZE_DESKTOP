import os
import shutil

def organize_desktop():
    # Correct desktop path for Windows using raw string literal
    desktop = r'C:\Users\roger\OneDrive\Desktop'
    script_folder = os.path.dirname(os.path.realpath(__file__))
    print(f"Desktop path: {desktop}")
    print(f"Script folder path: {script_folder}")
    
    files_folder = os.path.join(desktop, 'Files')
    folders_folder = os.path.join(desktop, 'Folders')

    if not os.path.exists(files_folder):
        os.makedirs(files_folder)
    if not os.path.exists(folders_folder):
        os.makedirs(folders_folder)

    for item in os.listdir(desktop):
        item_path = os.path.join(desktop, item)

        # Skip the organizing folders and the script's own directory
        if item in ['Files', 'Folders'] or item_path == script_folder:
            continue

        try:
            if os.path.isfile(item_path):
                shutil.move(item_path, files_folder)
            elif os.path.isdir(item_path):
                shutil.move(item_path, folders_folder)
        except Exception as e:
            print(f"Could not move {item_path}: {e}")

if __name__ == "__main__":
    organize_desktop()
    print("Desktop organized successfully!")
