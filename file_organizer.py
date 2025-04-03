# file_organizer.py

import os
import shutil

# Dictionary to map file extensions to folder names
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Others": []
}

# Organize files into folders based on their extensions
def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return
    
    # Iterate through files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Skip if it is a directory
        if os.path.isdir(file_path):
            continue
        
        # Get file extension
        _, ext = os.path.splitext(filename)
        
        # Determine folder based on file extension
        folder_name = "Others"
        for key, extensions in file_types.items():
            if ext.lower() in extensions:
                folder_name = key
                break
        
        # Create target folder if not exists
        target_folder = os.path.join(folder_path, folder_name)
        os.makedirs(target_folder, exist_ok=True)
        
        # Move the file
        try:
            shutil.move(file_path, os.path.join(target_folder, filename))
            print(f"Moved: {filename} -> {folder_name}")
        except Exception as e:
            print(f"Error moving file '{filename}': {e}")

# Main function to start the file organizer
def main():
    print("Welcome to the File Organizer!")
    folder_path = input("Enter the path of the folder to organize: ")
    organize_files(folder_path)
    print("File organization complete!")

# Start the script
if __name__ == "__main__":
    main()
