# Virtual Controlled Mouse  

**Overview**  
The **Virtual Controlled Mouse** is an innovative project leveraging **image processing** to enable hands-free mouse control using simple colored markers. This project demonstrates how computer vision can be combined with Python libraries to create an intuitive virtual interface.  

---

## **Features**  

- **Hands-Free Mouse Control**:  
  Move your hand to control the mouse pointer seamlessly.  

- **Click Interaction**:  
  Perform mouse clicks by bringing the two colored markers closer together.  

- **Real-Time Image Processing**:  
  Uses color segmentation to track markers and determine pointer position dynamically.  

---

## **Technical Details**  

### **Implementation**  

1. **Color Segmentation**:  
   Two green-colored papers fixed to fingers are detected using image processing techniques.  
   - The system identifies markers based on their distinct color.  
   - A line is formed between the two markers, and its midpoint is used to control the mouse pointer.  

2. **Mouse Control**:  
   - The **pynput** library is used to control mouse actions programmatically.  
   - The mouse pointer moves based on the midpoint of the detected markers.  
   - A click is triggered when the two markers come close to each other.  

3. **GUI**:  
   - The **wxPython** library is used for any graphical interface or interaction if required.  

---

## **Requirements**  

### **Hardware**  
- A webcam or camera-enabled device to capture hand movements.  

### **Software**  
- Python 3.x  
- Required libraries:  
  - `pynput`  
  - `wxPython`  
  - `OpenCV` (for image processing and color segmentation)  

### **Installation**  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-repo-name/Virtual-Controlled-Mouse.git  
   cd Virtual-Controlled-Mouse  
   ```  

2. Install dependencies:  
   ```bash  
   pip install pynput wxPython opencv-python  
   ```  

3. Run the script:  
   ```bash  
   python virtual_mouse.py  
   ```  

---

## **How It Works**  

1. **Setup**:  
   - Attach green-colored papers to two fingers.  
   - Ensure proper lighting for accurate color detection.  

2. **Mouse Movement**:  
   - Move your hand while keeping the markers visible to the webcam.  
   - The pointer follows the midpoint of the line connecting the two markers.  

3. **Mouse Click**:  
   - Bring the two markers close together to simulate a mouse click.  

---

## **Future Enhancements**  

- Add support for gestures to simulate additional mouse functionalities (e.g., right-click, scroll).  
- Enhance color detection for varying lighting conditions.  
- Implement multi-color segmentation for more complex controls.  
- Integrate with AR/VR platforms for immersive experiences.  

---

## **Contributions**  

Contributions and suggestions are welcome! Feel free to fork the repository and create a pull request.
