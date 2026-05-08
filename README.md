# 🗂️ FileOrganizer

> Drop it in any folder. Run it once. Watch the chaos become order — with duplicate detection built in.

![Python](https://img.shields.io/badge/Python-3.6+-3776AB?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-brightgreen?style=flat)

---

## ✨ What it does

FileOrganizer is a single Python script that **automatically sorts any messy folder** into clean subfolders by file type — and silently kills duplicates along the way.

No config. No install. Just run it.

---

## ⚡ Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/you/file-organizer.git

# 2. Drop organize.py into any messy folder

# 3. Run it
python organize.py
```

---

## 🖥️ Live Output

```
Moved: resume.pdf        → Documents/
Moved: vacation.jpg      → Images/
Duplicate deleted: vacation_copy.jpg
Moved: app.py            → Code/
Moved: setup.exe         → Programs/
Moved: beats.mp3         → Music/

Done organizing.
```

---

## 📁 Categories

| Folder | Extensions |
|--------|------------|
| 🖼️ Images | `.jpg` `.jpeg` `.png` `.gif` `.webp` |
| 🎬 Videos | `.mp4` `.mkv` `.avi` |
| 🎵 Music | `.mp3` `.wav` |
| 📄 Documents | `.pdf` `.docx` `.txt` `.pptx` `.xlsx` |
| 🗜️ Archives | `.zip` `.rar` `.7z` |
| ⚙️ Programs | `.exe` `.msi` |
| 💻 Code | `.py` `.js` `.html` `.css` |
| 📦 Others | Everything else |

---

## 🔥 Features

- ✅ **MD5 duplicate detection** — hashes every file; identical files are deleted, not just renamed
- ✅ **Safe conflict resolution** — if a filename already exists, appends `_1`, `_2`… instead of overwriting
- ✅ **Zero dependencies** — pure Python standard library, no `pip install` needed
- ✅ **Self-aware** — skips its own script file so it never moves itself

---

## 🚀 How It Works

```
📁 Scan folder → 🔍 MD5 duplicate check → 🏷️ Match extension → ✅ Move to category folder
```

1. Walks the target folder (top-level only)
2. Hashes each file with MD5 — deletes exact duplicates immediately
3. Matches the file extension to a category
4. Creates the category subfolder if it doesn't exist
5. Moves the file — safely renames if a conflict exists

---

## 🤝 Contributing

Contributions are what make open source great. Here's how you can help:

| Type | How |
|------|-----|
| ➕ Add file types | Edit `FILE_CATEGORIES` in the script and open a PR |
| 🐛 Report a bug | Open a GitHub Issue with your OS + the file that caused it |
| 💡 Feature ideas | Suggest dry-run mode, config files, logging in Discussions |
| ⭐ Star the repo | Helps others find the project |

```bash
# Fork → Clone → Edit → PR
git checkout -b feature/my-improvement
git commit -m "feat: add dry-run mode"
git push origin feature/my-improvement
```

---

## 📄 License

MIT — free to use, modify, and distribute.

---

<p align="center">Made with Python · Drop it in, run it, done.</p>
