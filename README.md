# 🎥 HOLO2NET  Hologram Video Converter 

Holo2net is a command-line script that permits to change a video to a pyramid hologram with Artificial Intelligence, by separating the foreground and removing the background without any parallaxes. It's a powerful tool for creating holographic visual content for educational or creative projects.

## ⚙️ Requirements 

Holo2net is working on Linux with Python 3.6. It requires the following libraries and tools to function correctly:
* **u2net library**: A deep learning model for semantic segmentation.
* **backgroundremover**: A Python tool for background removal.
* **ffmpeg**: A complete, cross-platform solution to record, convert, and stream audio and video.

This script needs a CPU and a graphic card to work at its best capacity.

## 💻 Script Descriptions 

### **HOLO2NET.sh**

This is the main bash script that automates the entire process. It takes a video file as input, uses `backgroundremover` to isolate the foreground object, and then uses a complex `ffmpeg` filter to rotate and arrange the four quadrants of the video to create the final holographic pyramid effect.

### **explanations.py**

This Python script generates a visual schema of the geometric transformations applied by the main script. It uses the `Pillow` library to create a PNG image (`hologram_schema.png`) that visually explains how the video is rotated and flipped to form the four faces of the hologram.

### **transformations_geometriques.pdf**

This PDF document provides a detailed, academic explanation of the mathematical principles behind the holographic effect. It uses LaTeX to present the geometric transformations (rotations, horizontal and vertical flips) and their corresponding matrix formulas. The document is for those who wish to understand the theoretical foundation of the script's visual effects.

## 🚀 Usage 

To run the script, simply execute it from your terminal with your video file as an argument:
```sh
./HOLO2NET.sh your_video_file.mp4
```

## ⚖️ Credits & License 

**License:** 

![Logo de la licence CC BY-NC-ND](CC_BY-NC-ND.png)

**Author:** Thibaut LOMBARD

**GitHub:** [https://github.com/Lombard-Web-Services/HOLO2NET](https://github.com/Lombard-Web-Services/HOLO2NET)

### 📜 Credits 
* **Backgroundremover**: A Python tool for background removal.
* **FFmpeg**: A complete, cross-platform solution for audio and video.
* **NVIDIA**: For GPU support.
* **SquirLMixes**: For the test videos used in the project.

### 📖 License Details

This work is licensed under the **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License**. To view a copy of this license, visit [http://creativecommons.org/licenses/by-nc-nd/4.0/](http://creativecommons.org/licenses/by-nc-nd/4.0/) or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

The main conditions of this license are:
* **Attribution (BY):** You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
* **NonCommercial (NC):** You may not use the material for commercial purposes.
* **NoDerivatives (ND):** If you remix, transform, or build upon the material, you may not distribute the modified material.
