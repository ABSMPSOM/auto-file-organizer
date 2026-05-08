# Auto File Organizer

Smart Python file organizer that automatically sorts files into category folders, removes duplicate files using MD5 hash comparison, and keeps directories clean with zero manual work.

---

## Features

* Automatic file categorization
* Duplicate file detection and removal
* Auto folder creation
* Smart file renaming if same filename exists
* Supports multiple file types
* Organizes files inside current script directory
* Lightweight and fast
* Recursive-safe organization logic

---

## Supported Categories

### Media

* Images
* Videos
* Music

### Documents & Data

* Documents
* Presentations
* Spreadsheets

### Compressed & Executable

* Archives
* Programs

### Development & Design

* Code files
* Design & 3D assets
* Fonts

### System

* Shortcuts

Unknown file types are automatically moved into:

```text
Others/
```

---

## Supported File Extensions

### Images

```text
.jpg .jpeg .png .gif .webp .bmp .tiff .svg .ico .heic .raw
```

### Videos

```text
.mp4 .mkv .avi .mov .wmv .flv .webm .m4v
```

### Music

```text
.mp3 .wav .aac .flac .ogg .m4a .wma .midi
```

### Documents

```text
.pdf .docx .doc .txt .rtf .odt .md
```

### Presentations

```text
.pptx .ppt .key .odp
```

### Spreadsheets

```text
.xlsx .xls .csv .ods
```

### Archives

```text
.zip .rar .7z .tar .gz .bz2 .iso .tgz
```

### Programs

```text
.exe .msi .apk .bat .cmd .sh .dmg .pkg .app
```

### Code

```text
.py .js .html .css .java .cpp .c .cs .json .xml .php .rb .sql .yaml
```

### Design & 3D

```text
.psd .ai .xd .fig .blend .obj .stl .step
```

### Fonts

```text
.ttf .otf .woff .woff2
```

### Shortcuts

```text
.lnk .url .desktop
```

---

## How It Works

The script:

1. Detects the current script directory
2. Scans all files inside the folder
3. Identifies file type by extension
4. Creates category folders automatically
5. Moves files into matching folders
6. Detects duplicate files using MD5 hashing
7. Deletes duplicates automatically
8. Renames files if same filename already exists

---

## Example

Before:

```text
Folder/
 ├── movie.mp4
 ├── image.png
 ├── notes.pdf
 ├── script.py
 ├── song.mp3
```

After:

```text
Folder/
 ├── Videos/
 ├── Images/
 ├── Documents/
 ├── Code/
 ├── Music/
```

---

## Installation

Install Python:

https://www.python.org/downloads/

Clone repository:

```bash
git clone https://github.com/ABSMPSOM/auto-file-organizer.git
```

Go to project folder:

```bash
cd auto-file-organizer
```

---

## Usage

Run:

```bash
python organizer.py
```

The script will automatically organize the folder where it exists.

---

## Future Improvements

* GUI version
* Drag and drop support
* Auto monitoring mode
* Recycle bin recovery
* AI-based file recognition
* Scheduled automatic organization

---

## License

MIT License

---

## Author

Soumen Sadhukhan

Built with Python because manually organizing files is a task humanity should have automated years ago.
