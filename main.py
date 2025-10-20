import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

cancel_operation = False  # Global flag to stop the process

def organize_files():
    global cancel_operation
    cancel_operation = False  # Reset cancel flag

    source_folder = folder_path.get()
    if not source_folder:
        messagebox.showwarning("Warning", "Please select a folder first.")
        return

    folders = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Videos": [".mp4", ".mkv", ".mov", ".avi"],
        "Music": [".mp3", ".wav", ".aac"],
        "Archives": [".zip", ".rar", ".7z"],
        "Programs": [".exe", ".msi"],
        "Others": []
    }

    # Create folders if they don’t exist
    for folder in folders:
        folder_dir = os.path.join(source_folder, folder)
        if not os.path.exists(folder_dir):
            os.makedirs(folder_dir)

    all_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
    total_files = len(all_files)

    if total_files == 0:
        messagebox.showinfo("Info", "No files found in the selected folder.")
        return

    progress_bar["maximum"] = total_files
    moved_count = 0
    action = action_var.get()  # "move" or "copy"

    for index, filename in enumerate(all_files, start=1):
        if cancel_operation:
            progress_label.config(text="❌ Operation cancelled.")
            messagebox.showinfo("Cancelled", f"Operation cancelled.\nFiles processed: {moved_count}/{total_files}")
            return

        file_path = os.path.join(source_folder, filename)
        moved = False

        for folder, extensions in folders.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                dest = os.path.join(source_folder, folder, filename)
                if action == "move":
                    shutil.move(file_path, dest)
                else:
                    shutil.copy2(file_path, dest)
                moved = True
                break

        if not moved:
            dest = os.path.join(source_folder, "Others", filename)
            if action == "move":
                shutil.move(file_path, dest)
            else:
                shutil.copy2(file_path, dest)

        moved_count += 1
        remaining = total_files - moved_count
        progress_bar["value"] = index
        progress_label.config(text=f"Processing {index}/{total_files} | Remaining: {remaining}")
        root.update_idletasks()

    messagebox.showinfo("Success", f"✅ Files organized successfully!\nTotal files processed: {moved_count}")
    progress_label.config(text="Done ✅")
    progress_bar["value"] = 0


def cancel():
    global cancel_operation
    cancel_operation = True


def browse_folder():
    selected_folder = filedialog.askdirectory()
    folder_path.set(selected_folder)


# GUI setup
root = tk.Tk()
root.title("File Organizer Pro")
root.geometry("500x360")
root.resizable(False, False)

folder_path = tk.StringVar()
action_var = tk.StringVar(value="move")  # default option

# Folder input section
tk.Label(root, text="Select a folder to organize:", font=("Arial", 12)).pack(pady=10)
tk.Entry(root, textvariable=folder_path, width=50).pack(pady=5)
tk.Button(root, text="Browse", command=browse_folder, width=10).pack(pady=5)

# Choose action (Move or Copy)
tk.Label(root, text="Choose action:", font=("Arial", 11)).pack(pady=10)
frame_action = tk.Frame(root)
frame_action.pack()
tk.Radiobutton(frame_action, text="Move files", variable=action_var, value="move").pack(side="left", padx=10)
tk.Radiobutton(frame_action, text="Copy files", variable=action_var, value="copy").pack(side="left", padx=10)

# Buttons for actions
frame_btns = tk.Frame(root)
frame_btns.pack(pady=15)
tk.Button(frame_btns, text="Organize Files", command=organize_files, width=18, bg="#4CAF50", fg="white").pack(side="left", padx=10)
tk.Button(frame_btns, text="Cancel", command=cancel, width=10, bg="#E53935", fg="white").pack(side="left")

# Progress bar and label
progress_bar = ttk.Progressbar(root, length=420, mode='determinate')
progress_bar.pack(pady=10)
progress_label = tk.Label(root, text="", font=("Arial", 10))
progress_label.pack()

root.mainloop()