# 🗂️ File Organizer (Python + Tkinter)

An enhanced **Python desktop application** that organizes files in a selected folder into categorized subfolders (Images, Documents, Videos, Music, Archives, etc.) based on file extensions.  
Built with a clean GUI using **Tkinter**, this "Pro" version includes **progress tracking**, **move/copy options**, and a **cancel button** for better control.

---

## 🚀 Features

- ✅ Automatically organizes files into folders by category  
- ⚙️ Choose between **Move** or **Copy** mode  
- 📊 Real-time progress bar with remaining file count  
- ❌ Cancel operation anytime  
- 🖥️ Modern Tkinter interface (non-resizable)  
- 💡 Easy customization of folder categories and extensions  

---

## 🧠 How It Works

1. Launch the program  
2. Browse and select the source folder  
3. Choose whether to *Move* or *Copy* files  
4. Click **Organize Files**  
5. Watch the progress bar as files are organized into folders  

If you cancel midway, the program stops immediately and shows how many files were processed.

---

## 📂 Folder Categories

| Category   | File Extensions |
|-------------|----------------|
| Images      | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp` |
| Documents   | `.pdf`, `.doc`, `.docx`, `.txt`, `.xls`, `.xlsx`, `.ppt`, `.pptx` |
| Videos      | `.mp4`, `.mkv`, `.mov`, `.avi` |
| Music       | `.mp3`, `.wav`, `.aac` |
| Archives    | `.zip`, `.rar`, `.7z` |
| Programs    | `.exe`, `.msi` |
| Others      | Unrecognized file types |

---

## 🧰 Requirements

- **Python 3.8+**
- Tkinter (included with Python on Windows)
- Optional: PyInstaller (for .exe build)

Install Tkinter manually if missing:
```bash
pip install tk
```

---

## 🖱️ How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/Gero41is/FileOrganizer.git
   ```
2. Navigate to the folder:
   ```bash
   cd FileOrganizer
   ```
3. Run the program:
   ```bash
   python main.py
   ```

---

## ⚙️ Build Executable (.exe)

Create a standalone Windows executable:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

The output `.exe` will be located in the `dist` folder.

---

## 🧑‍💻 Author

**Gerges Isaac (Gero41is)**  
📍 Egypt  
💬 Student in Information Systems  
🔗 [GitHub Profile](https://github.com/Gero41is)

---

## 📜 License

Licensed under the **MIT License** — you’re free to modify and distribute for personal or educational use.

---

**Made with ❤️ using Python and Tkinter**
