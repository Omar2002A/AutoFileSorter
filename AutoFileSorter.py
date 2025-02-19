import os
import shutil

downloadPath = r"C:\Users\LENOVO\Downloads"

fileTypes = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".xlsx", ".pptx", ".txt"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "APP": [".exe"],
    "Scripts": [".py"],
    "Miscellaneous": [".obj", ".tar", ".asm", ".ms14"] 
}


for folder in fileTypes.keys():
    folder_path = os.path.join(downloadPath, folder)
    os.makedirs(folder_path, exist_ok=True)  


for file in os.listdir(downloadPath):
    file_path = os.path.join(downloadPath, file)
    
    if os.path.isfile(file_path): 
        for folder, extensions in fileTypes.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(downloadPath, folder, file))
                break

print("✔️ All files have been sorted successfully! ✅")
