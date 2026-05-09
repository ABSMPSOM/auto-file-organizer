
from asyncio import log
import os
import shutil
import hashlib
from pathlib import Path
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext

# ===== CURRENT SCRIPT DIRECTORY =====

TARGET_FOLDER = os.path.dirname(os.path.abspath(__file__))

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
    "Shortcut": [".lnk", ".url", ".desktop",".lnk"],
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

def organize_files(folder, log):
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
            log(f"Moved: {file} -> {category}")
            print(f"Moved: {file} -> {category}")
        except Exception as e:
            log(f"Error moving {file}: {e}")
            print(e)

# ===== UI =====
def main():
    # ===== BROWSE FUNCTION =====
    def browse_folder():
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            path_var.set(folder_selected)
            folder_label.config(
                text=f"📂 Target Folder:\n{folder_selected}"
            )
    def log(msg):

        log_box.config(state='normal')

        log_box.insert(tk.END, msg + "\n")

        log_box.see(tk.END)

        log_box.config(state='disabled')
    # ===== MAIN WINDOW =====
    root = tk.Tk()
    root.title("File Organizer")
    root.geometry("1000x450")
    
    # ===== TITLE =====
    title = tk.Label(
        root,
        text="📁 Auto File Organizer",
        font=("Arial", 18, "bold")
    )
    title.pack(pady=15)
    # ===== PATH VARIABLE =====
    path_var = tk.StringVar()
    # ===== BROWSE BUTTON =====
    browse_btn = tk.Button(
        root,
        text="Browse Folder",
        font=("Arial", 11),
        width=18,
        height=2,
        command=browse_folder
    )
    start_btn = tk.Button(
        root,
        text="Start Organizing",
        font=("Arial", 11),
        width=18,
        height=2,
        command=lambda: [organize_files(path_var.get(), log), messagebox.showinfo("Done", "Files have been organized!")],

    )
    browse_btn.pack(pady=10)
    start_btn.pack(pady=10)
    # ===== FOLDER LABEL =====
    folder_label = tk.Label(
        root,
        text="No folder selected",
        wraplength=450,
        justify="center",
        font=("Arial", 10)
    )
    folder_label.pack(pady=10)

    # ===== LOG SHOW =====
    log_box = scrolledtext.ScrolledText(
        root,
        font=("Consolas", 10),
        width=80,
        height=10,
        bg="#1e1e1e",
        fg="white",
        insertbackground="white"
        )
    log_box.pack(
        padx=50, 
        pady=50,
        fill="both", 
        expand=True
        )

    # ===== START =====
    root.mainloop()


# ===== START =====

if __name__ == "__main__":
    main()
    organize_files(TARGET_FOLDER, log)
    print("\nDone organizing.")