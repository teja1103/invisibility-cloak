# Invisibility Cloak 🎭

A real-time computer vision project that creates an "invisibility cloak" effect using your webcam and OpenCV. This project demonstrates color-based object detection and background replacement techniques to create the illusion of invisibility.

## 🎯 What It Does

The invisibility cloak effect works by:
1. Capturing a reference background image without you in it
2. Detecting a specific colored cloth/cloak (red by default) in the live video stream
3. Replacing the detected cloth area with the previously captured background
4. Creating the illusion that you're invisible wherever the cloth covers you

## 🚀 Features

- **Real-time invisibility effect** using your webcam
- **Two modes of operation:**
  - `main.py`: Uses captured background for invisibility effect
  - `image.py`: Uses a custom replacement image instead of background
- **Advanced image processing** with noise reduction and edge smoothing
- **Automatic color detection** for red-colored cloaks
- **Horizontal flipping** for mirror-like experience

## 🛠️ Requirements

### Dependencies
- Python 3.x
- OpenCV (`cv2`)
- NumPy

### Hardware
- Webcam/camera connected to your computer
- A red-colored cloth, towel, or any red object to act as the "cloak"

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd invisibilty-cloak
   ```

2. **Install required packages:**
   ```bash
   pip install opencv-python numpy
   ```

## 🎮 Usage

### Basic Invisibility Cloak (main.py)

```bash
python main.py
```

**Steps:**
1. Run the script and **step away from camera** when prompted
2. Wait for background capture (about 2 seconds)
3. Put on your red cloth/cloak
4. Watch yourself become invisible!
5. Press 'q' to quit

### Custom Image Replacement (image.py)

```bash
python image.py
```

**Additional Requirements:**
- Place a `replacement.jpg` image in the project directory
- This image will appear wherever the red cloak is detected

**Steps:**
1. Add your `replacement.jpg` file to the project folder
2. Run the script and step away for background capture
3. Use your red cloak to reveal the replacement image
4. Press 'q' to quit

## 🎨 How It Works

### Technical Overview

1. **Background Capture**: 
   - Captures 100 frames and uses median filtering to create a clean background reference
   - Reduces noise and handles minor camera movements

2. **Color Detection**:
   - Converts frames to HSV color space for better color detection
   - Uses two HSV ranges to detect red colors effectively:
     - Range 1: `[0, 120, 70]` to `[10, 255, 255]`
     - Range 2: `[170, 120, 70]` to `[180, 255, 255]`

3. **Image Processing**:
   - **Morphological operations** to reduce noise
   - **Gaussian blur** for smooth edges
   - **Dilation** to fill gaps in detection

4. **Background Replacement**:
   - Uses bitwise operations to combine background and foreground
   - Seamlessly blends the replacement with the live video

### Key Computer Vision Techniques

- **HSV Color Space**: More robust for color-based detection
- **Morphological Operations**: Noise reduction and shape refinement
- **Gaussian Blur**: Edge smoothing for natural appearance
- **Bitwise Operations**: Efficient image masking and combination

## 🎯 Customization

### Changing the Cloak Color

Edit the HSV ranges in either `main.py` or `image.py`:

```python
# For different colors, adjust these values
lower_red1 = np.array([0, 120, 70])      # Lower bound 1
upper_red1 = np.array([10, 255, 255])    # Upper bound 1
lower_red2 = np.array([170, 120, 70])    # Lower bound 2  
upper_red2 = np.array([180, 255, 255])   # Upper bound 2
```

**Common HSV ranges:**
- **Blue**: `[100, 150, 0]` to `[140, 255, 255]`
- **Green**: `[40, 150, 0]` to `[80, 255, 255]`
- **Yellow**: `[20, 150, 0]` to `[30, 255, 255]`

### Adjusting Detection Sensitivity

Modify these parameters for better detection:

```python
# Morphological operation kernel sizes
cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((7, 7), np.uint8))

# Gaussian blur intensity
cv2.GaussianBlur(mask, (21, 21), 0)
```

## 📁 Project Structure

```
invisibilty-cloak/
├── main.py          # Main invisibility cloak script
├── image.py         # Custom image replacement version
├── git.sh           # Git helper script
├── README.md        # This file
└── replacement.jpg  # (Required for image.py) Custom replacement image
```

## 🚨 Troubleshooting

### Common Issues

1. **Camera not detected**: Ensure your webcam is connected and not being used by other applications

2. **Poor color detection**: 
   - Ensure good lighting conditions
   - Use a solid colored cloth without patterns
   - Adjust HSV ranges for your specific cloth color

3. **Replacement image not found** (image.py):
   - Make sure `replacement.jpg` exists in the project directory
   - Ensure the image file is not corrupted

4. **Laggy performance**:
   - Close other applications using the camera
   - Reduce the number of background frames captured (line 14 in main.py)

### Performance Tips

- Use solid colored backgrounds for better results
- Ensure good, even lighting
- Keep the cloak material smooth and wrinkle-free
- Stand at an appropriate distance from the camera

## 🎥 Demo

1. Position yourself in front of your camera
2. Run the script and step away during background capture
3. Hold up your red cloth and watch the magic happen!
4. Move the cloth around to see different parts of yourself "disappear"

## 🤝 Contributing

Feel free to fork this project and submit pull requests for:
- Additional color detection ranges
- Performance improvements
- New visual effects
- Better error handling
- UI improvements

## 📚 Learning Resources

This project demonstrates several important computer vision concepts:
- Color space conversions (BGR to HSV)
- Image masking and bitwise operations
- Morphological image processing
- Real-time video processing
- Background subtraction techniques

## 📄 License

This project is open source. Feel free to use, modify, and distribute as needed.

---

**Enjoy your magical invisibility cloak! 🪄✨**
