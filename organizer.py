import os
import shutil
import hashlib
from pathlib import Path

# ===== CURRENT SCRIPT DIRECTORY =====

TARGET_FOLDER = os.path.dirname(os.path.abspath(__file__))

    # ===== FILE TYPES =====

# ===== EXPANDED FILE TYPES =====

FILE_CATEGORIES = {
    # Media
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tiff", ".svg", ".ico", ".heic", ".raw"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".m4v"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".wma", ".midi"],
    
    # Documents & Data
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".rtf", ".odt", ".md"],
    "Presentations": [".pptx", ".ppt", ".key", ".odp"],
    "Spreadsheets": [".xlsx", ".xls", ".csv", ".ods"],
    
    # Compressed & Executable
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".iso", ".tgz"],
    "Programs": [".exe", ".msi", ".apk", ".bat", ".cmd", ".sh", ".dmg", ".pkg", ".app"],
    
    # Dev & Design
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".cs", ".json", ".xml", ".php", ".rb", ".sql", ".yaml"],
    "Design_and_3D": [".psd", ".ai", ".xd", ".fig", ".blend", ".obj", ".stl", ".step"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
    
    # System
    "Shortcuts": [".lnk", ".url", ".desktop"]
}

    # ===== HASH FUNCTION =====

def get_file_hash(file_path):
    hash_md5 = hashlib.md5()

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)

    return hash_md5.hexdigest()

# ===== CATEGORY DETECTOR =====

def get_category(extension):

    extension = extension.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    return "Others"

# ===== ORGANIZER =====

def organize_files(folder):
    seen_hashes = {}
    # ✅ Use os.listdir instead of os.walk to avoid re-scanning created subfolders
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        # Skip directories and this script
        if os.path.isdir(file_path):
            continue
        if file == os.path.basename(__file__):
            continue
        extension = Path(file).suffix
        category = get_category(extension)
        category_folder = os.path.join(folder, category)
        os.makedirs(category_folder, exist_ok=True)
        try:
            file_hash = get_file_hash(file_path)
            if file_hash in seen_hashes:
                print(f"Duplicate deleted: {file}")
                os.remove(file_path)
                continue
            seen_hashes[file_hash] = file_path
        except:
            continue
        destination = os.path.join(category_folder, file)
        if os.path.abspath(file_path) == os.path.abspath(destination):
            continue
        counter = 1
        new_destination = destination
        while os.path.exists(new_destination):
            name = Path(file).stem
            suffix = Path(file).suffix
            new_destination = os.path.join(category_folder, f"{name}_{counter}{suffix}")
            counter += 1
        try:
            shutil.move(file_path, new_destination)
            print(f"Moved: {file} -> {category}")
        except Exception as e:
            print(e)

    # ===== START =====

if __name__ == "__main__":
    organize_files(TARGET_FOLDER)
    print("\nDone organizing.")