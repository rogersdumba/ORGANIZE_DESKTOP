import streamlit as st
import os
import shutil

def organize_desktop(desktop_path):
    script_folder = os.path.dirname(os.path.realpath(__file__))
    
    files_folder = os.path.join(desktop_path, 'Files')
    folders_folder = os.path.join(desktop_path, 'Folders')

    if not os.path.exists(files_folder):
        os.makedirs(files_folder)
    if not os.path.exists(folders_folder):
        os.makedirs(folders_folder)

    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)

        # Skip the organizing folders and the script's own directory
        if item in ['Files', 'Folders'] or item_path == script_folder:
            continue

        try:
            if os.path.isfile(item_path):
                shutil.move(item_path, files_folder)
            elif os.path.isdir(item_path):
                shutil.move(item_path, folders_folder)
        except Exception as e:
            raise Exception(f"Could not move {item_path}: {e}")

# Streamlit UI
st.title("Desktop Organizer")

desktop_path = st.text_input("Enter your desktop path:", placeholder=r'Enter Your Desktop Path Here!')

if st.button("Organize Desktop"):
    if desktop_path:
        if os.path.exists(desktop_path) and os.path.isdir(desktop_path):
            try:
                organize_desktop(desktop_path)
                st.success("Desktop organized successfully!")
            except Exception as e:
                st.error(f"Failed to organize desktop: {e}")
        else:
            st.error("Please enter a valid desktop path.")
    else:
        st.error("Please enter a valid desktop path.")
