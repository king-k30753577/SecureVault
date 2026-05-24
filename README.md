# SecueVault

# 🔐 SecureVault

SecureVault is a local encrypted file vault built using:

- Python
- Flask
- HTML
- CSS
- JavaScript
- SQLite
- FFmpeg

The project is specially designed for mobile usage with Termux and supports:

✅ Secure file storage  
✅ AES encryption  
✅ Video streaming using HLS  
✅ Modern mobile UI  
✅ Delete system  
✅ Localhost hosting  
✅ Multi-file upload  
✅ Timestamp-hash storage system  

---

# 📌 Features

## 🔒 Secure File Storage

Files are encrypted before storage.

Normal users cannot directly access the actual content from file manager because encrypted binary data is stored instead of raw files.

---

## 🎥 HLS Video Streaming

Large videos are automatically converted into:

playlist.m3u8
segment0.ts
segment1.ts
segment2.ts

### This allows:
•smooth streaming
•lower RAM usage
•faster loading
•partial loading instead of full 1GB decryption.

---
## 📱 Mobile Optimized UI

•Glassmorphism design
•Animated cards
•Responsive layout
•Popup delete confirmation
•Cyber-style interface
### Optimized for:
•Android browsers
•Termux localhost server

---
## ⚙️ Technologies Used

Technology	Purpose

Flask	Backend server
HTML/CSS/JS	Frontend
SQLite	Metadata database
FFmpeg	Video segmentation
Cryptography	AES encryption
HLS.js	Video streaming

---

## 📂 Project Structure
```
securevault/
│
├── app.py
├── vault.db
│
├── templates/
│   ├── index.html
│   └── video.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
├── data/
│   ├── files/
│   ├── streams/
│   └── temp/
│
└── keys/
    └── secret.key
```
---
📥 Installation (Termux)

1. Update Packages
```sh 
pkg update && pkg upgrade -y
```

---

2. Install Python & FFmpeg
```sh
pkg install python ffmpeg git -y
```

---

3. Install Required Python Libraries
```sh
pip install flask cryptography waitress aiofiles flask-cors python-magic
```

---

## 🚀 Running The Project:
### Setup Instructions
 1. **Navigate to the project directory:**


3. **Start the development server:**
   ```sh
   python app.py
   ```
**Access the application:**
   Open your web browser and navigate to:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)



---

## 📤 Uploading Files
1. Open localhost webpage

2. Click file picker

3. Select one or multiple files

4. Click on secure and then you delete or see your files whenever you come to localhost.


---

## 🎬 Video Streaming System

When a large video is uploaded:

movie.mp4

It gets converted into:
```text
playlist.m3u8
segment0.ts
segment1.ts
segment2.ts
```
This method is called:
**HLS (HTTP Live Streaming)**

Advantages:
No full 1GB loading
Faster playback
Streaming like YouTube
Better mobile performance

---
## 🗑 Delete System &#128465

Each file card contains:
Open button
Dustbin icon 🗑️
When dustbin icon is clicked:

popup appears
asks confirmation

delete option shown in red
Deleting removes:

✅ encrypted files
✅ video segments
✅ database records


---

## 🔐 Encryption System

Current encryption:
AES Encryption using cryptography library
Each file gets:
timestamp hash
randomized secure filename
encrypted binary storage



---

## 🧠 Database System

SQLite database stores:
original file name
secure hash name
upload date
upload time
file type
stream folder location
Database file:
vault.db


---

+ ⚠️ Important Notes
  
Large Video Processing

1GB videos may take time on mobile because FFmpeg has to:
split video
create segments
generate playlists


- Do not close Termux during processing.

---

**Secret Key**
**Encryption key:**
**keys/secret.key**
- Do NOT delete this file.

If deleted: all encrypted files become unreadable.

---

## 🛠 Future Improvements

**Planned features:**
+ Login authentication
+ Password protection
+ Folder system
+ Search bar
+ Thumbnail previews
+ Upload progress bar
+ Background processing
+ Auto cleanup system
+ Full encrypted HLS streaming
+ APK conversion



---

## 📜 License

This project is for educational and personal usage.


---

## 👨‍💻 Developer

~~~Created using:
Python
Flask
HTML
CSS
JavaScript
FFmpeg
Termux

