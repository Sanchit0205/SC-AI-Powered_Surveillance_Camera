
# 🚀 AI-Powered Surveillance Camera  
### 🔍 Real-time face detection and recognition with alerts using MobileNet and Flask.  

---

### 💡 **Overview**
This project uses **OpenCV**, **Face Recognition**, and **Flask** for real-time surveillance. It detects and identifies known faces while triggering voice alerts for unknown individuals. You can also access the **live camera feed remotely** via a web interface.

---

### ⚙️ **Features**
- 🟢 **Real-time face recognition** using OpenCV and Face Recognition.  
- 🌐 **Web interface** to view the live camera feed remotely.  
- 🔊 **Voice alerts** for unknown individuals.  
- 🎯 **MobileNet model** for fast and accurate face detection.  
- ✅ **Multi-threaded alerts** for smoother TTS performance.  

---

### 🛠️ **Installation and Setup**

#### ✅ **1. Clone the repository:**
```bash
git clone https://github.com/<your-username>/AI-Powered_Surveillance_Camera.git
cd AI-Powered_Surveillance_Camera
```

#### ✅ **2. Create a virtual environment:**
```bash
python -m venv .venv          # Create virtual environment
.venv\Scripts\activate         # Activate it (Windows)
source .venv/bin/activate      # For Linux/Mac
```

#### ✅ **3. Install dependencies:**
```bash
pip install -r requirements.txt
```

---

### 🚀 **Usage**

#### ✅ **1. Start the server:**
```bash
python server.py
```

#### ✅ **2. Access the web interface:**
- Open your browser and go to:  
```
http://127.0.0.1:5000
```

---

### 📁 **Folder Structure**
```
📁 AI-Powered_Surveillance_Camera  
 ┣ 📁 images                      # Known face images  
 ┣ 📁 models                      # Pre-trained MobileNet model  
 ┣ 📁 templates                   # HTML templates for the web interface  
 │   ┗ 📄 index.html              # Live feed web page  
 ┣ 📄 server.py                   # Flask server with face detection & alerts  
 ┣ 📄 requirements.txt            # Dependencies  
 ┣ 📄 README.md                   # Project documentation  
 ┣ 📄 .gitignore                  # Ignoring  
```

---

### 🔥 **Technologies Used**
- 🛠️ **Python** (Face recognition, Flask, OpenCV)  
- 🌐 **Flask** (Web interface)  
- 🎯 **OpenCV** (Face detection and video processing)  
- 🔥 **Face Recognition** (Encoding and matching faces)  
- 📢 **Pyttsx3** (Text-to-speech voice alerts)  

---

### ✅ **Dependencies**
The project uses the following Python libraries:
```plaintext
Flask
opencv-python
face-recognition
pyttsx3
numpy
```

---

### 🔥 **Future Enhancements**
- 📧 **Email or SMS notifications** on unknown detection.  
- 🔥 **Store logs** of detected individuals with timestamps.  
- 📊 **Admin dashboard** for better monitoring and logs management.  
- 🎯 **Face mask detection** integration.  


### 🚀 **🔥 You're All Set!**
