import streamlit as st
import os
import shutil

def organize_desktop(desktop):
    script_folder = os.path.dirname(os.path.realpath(__file__))
    st.write(f"Desktop path: {desktop}")
    st.write(f"Script folder path: {script_folder}")
    
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
            st.write(f"Could not move {item_path}: {e}")

# Streamlit app
st.title("Desktop Organizer")

# Input text field for desktop path
desktop_path = st.text_input("Enter the path to your desktop:", placeholder="C:\\Users\\roger\\OneDrive\\Desktop")

# Button to start the organization process
if st.button("Organize"):
    if desktop_path:
        organize_desktop(desktop_path)
        st.write("Desktop organized successfully!")
    else:
        st.write("Please enter a valid desktop path.")
