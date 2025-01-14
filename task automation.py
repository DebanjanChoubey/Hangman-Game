import os
import shutil

# Mapping of file extensions to folder names
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java", ".cs", ".ts"],
    "Others": []  # Files with unknown extensions
}

def organize_files(directory):
    """
    Organizes files in the given directory into subfolders based on file types.

    Args:
        directory (str): Path to the directory to organize.
    """
    # Ensure the provided directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    # Iterate through files in the directory
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(file)

        # Find the folder for the file
        folder_name = "Others"
        for category, extensions in FILE_CATEGORIES.items():
            if ext.lower() in extensions:
                folder_name = category
                break

        # Create the folder if it doesn't exist
        folder_path = os.path.join(directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # Move the file to the folder
        shutil.move(file_path, os.path.join(folder_path, file))
        print(f"Moved: {file} -> {folder_name}")

if __name__ == "__main__":
    # Prompt the user for the directory path
    target_directory = input("Enter the directory path to organize: ").strip()
    organize_files(target_directory)
