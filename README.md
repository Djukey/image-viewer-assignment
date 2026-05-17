# image-viewer-assignment
Alightweight Python tool that loads an image, applies basic transformations, and converts it between different color spaces. 
**What it does**

# TRANSFORMATION
The tool loads our choosen image (Donald Trump face) and will display a series of processed versions, one after another:

- Original Image (RGB)
- Resized: scaled to a new pixel size using **cv2.resize()** which will rebuilds the image at a new pixel grid.
- Rotated: Relocates pixels 90 degrees clockwise using **cv2.rotate()** which swaps width amnd heights with no detail lost
- Flipped: mirrored horizontally using **cv2.flip ()** which mirroa the image. Horizontal code 1, vertical code 0 and code -1 is both.

# COLOR SPACES
- RGB : using **cv2.COLOR_BGR2RGB** it's essential because OpenCV loads images as BGR; this converts to RGB for correct display. 
- Grayscale: converted to a single brightness channel. Now, using **cv2.COLOR_BGR2GRAY** reduces 3 channels to 1 which is about 1/3 the data so it processes faster.
- HSV: Convert to Hue, Saturation, Value color space using **cv2.COLOR_BGR2HSV** which separates color(hue) from brightness(value), that is more robust to lighting changes.

# REQUIREMENTS

Python 3.13+

OpenCV (opencv-python)

Matplotlib 


# Installation
This project was developed using an Anaconda environment, run from the Windows Command Prompt. Personally, I think that OpenCV installed more reliably this way on Windows than with pip.
Open command Prompt and run :

**conda create -n cv-week1 python=3.10**

**conda activate cv-week1**

**conda install -c conda-forge opencv matplotlib**

If there is an error, place the image named photo.jpg.jpg in the same folder as image._viewer.py
In command prompt, activate the environment and run the script : 

**conda activate cv-week1**

**python image_viewer.py**

A window opens and displays the original image inn RGB. Each time an  image appears, close it to see the next one. 


# How to run
Place our image named photo.jpg.jpg in the same folder as image_viewver.py or you can elect to do rename otherwise
Run: python **image_viewer.py**
A window opens and displays the original image in RGB. Now, each time an image appears close it to see the next one and repeat it continuously. 

# References 
- Bradski, G. (2000). The OpenCV library. Dr. Dobb's Journal of Software Tools, 25(11), 120–125.
- Mulla, R. (2022, March 20). Image processing with OpenCV and Python [Video]. YouTube. https://www.youtube.com/watch?v=kSqxn6zGE0c
- Hummingbird. (2021, June 2). Color spaces in computer vision - RGB, HSV and LAB (theory + code) [Video]. YouTube. https://www.youtube.com/watch?v=MmBBVTniWFg

IMAGE SOURCE : https://bookstore.gpo.gov/products/official-presidential-portrait-donald-trump-8x10-2017-2021 Official Presidential Portrait of Donald Trump (8x10) 2017-2021

