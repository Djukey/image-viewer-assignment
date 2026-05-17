import cv2
import matplotlib.pyplot as plt
image = cv2.imread("photo.jpg.jpg")
if image is None:
    print("FAILED to load. Files Python sees here:")
    import os
    print(os.listdir())

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")
plt.show()

resized_image = cv2.resize(image_rgb, (300, 200))

plt.imshow(resized_image)
plt.title("Resized Image")
plt.axis("off")
plt.show()

rotated_image = cv2.rotate(image_rgb, cv2.ROTATE_90_CLOCKWISE)

plt.imshow(rotated_image)
plt.title("rotated Image")
plt.axis ("off")
plt.show()

flipped_image = cv2.flip(image_rgb, 1)

plt.imshow(flipped_image)
plt.title("Flipped Image")
plt.axis("off")
plt.show()

grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(grayscale_image, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")
plt.show()

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

plt.imshow(hsv_image)
plt.title("HSV Image")
plt.axis("off")
plt.show()