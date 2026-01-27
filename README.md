# 📺 Ad-free YouTube Player

> **A Voice-Controlled Desktop YouTube Player**

This desktop application allows you to search, watch, and control YouTube videos without ads using a clean Python interface. It features **Voice Control** and **Mouse Control** modes, letting you operate the player with simple voice commands or standard clicks.

---

## 🛠 Tech Stack

| Category | Technologies |
| :--- | :--- |
| **GUI** | ![PySimpleGUI](https://img.shields.io/badge/PySimpleGUI-GUI-blue?style=flat&logo=python&logoColor=white) |
| **Media Engine** | ![VLC](https://img.shields.io/badge/VLC-LibVLC-orange?style=flat&logo=vlc&logoColor=white) |
| **Voice & Audio** | ![SpeechRecognition](https://img.shields.io/badge/SpeechRecognition-API-green?style=flat) ![gTTS](https://img.shields.io/badge/gTTS-Google_TTS-yellow?style=flat&logo=google&logoColor=white) |
| **YouTube Tools** | ![Pytube](https://img.shields.io/badge/Pytube-Downloader-red?style=flat&logo=youtube&logoColor=white) |

---

## 🚀 Key Features

-   **🚫 Ad-Free Experience**: Streams videos directly without interrupting ads.
-   **🗣️ Voice Control Mode**:
    -   Search videos by voice: *"Search funny cats"*
    -   Playback controls: *"Play"*, *"Pause"*, *"Stop"*
    -   Volume controls: *"Mute"*, *"Unmute"*
    -   Window controls: *"Full screen"*, *"Minimize"*
-   **🖱️ Mouse Control Mode**: Standard graphical interface for typing searches and clicking buttons.
-   **📥 Video Downloader**: Download your favorite videos directly to your machine.
-   **📝 Subtitles**: Fetch and display English subtitles automatically.

---

## 🎥 Demo Video

> **[Watch the Demo Video](https://drive.google.com/file/d/1Bwd2yTlz0-6Vkh3Kjr6Ms-jOeDwnHOfL/view?usp=sharing)**

---

## 📦 Installation & Setup

### Prerequisites
1.  **Python 3.x**
2.  **VLC Media Player**: Must be installed on your system (bits should match your Python version, e.g., 64-bit Python -> 64-bit VLC).

### Steps

1.  **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/Ad-free-Youtube-Player.git
    cd Ad-free-Youtube-Player
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application**
    ```bash
    python Youtube.py
    ```

---

## 🗣️ Voice Commands Guide

| Command | Action |
| :--- | :--- |
| **"Search [query]"** | Searches YouTube and plays the first result. |
| **"Play" / "Pause"** | Resumes or pauses the video. |
| **"Download"** | Downloads the current video as MP4. |
| **"Subtitle"** | Enabling subtitles (if available). |
| **"Full Screen"** | Maximizes the player window. |
| **"Exit"** | Closes the application. |

---

*Experience YouTube your way—hands-free and ad-free.*
