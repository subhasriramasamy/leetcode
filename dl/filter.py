import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("a.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sobel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]])
sobel_y = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]])
edge_x = cv2.filter2D(gray, -1, sobel_x)
edge_y = cv2.filter2D(gray, -1, sobel_y)
edges = cv2.magnitude(
    edge_x.astype(np.float32),
    edge_y.astype(np.float32))
edges = np.uint8(np.clip(edges, 0, 255))
_, edges = cv2.threshold(edges, 80, 255, cv2.THRESH_BINARY)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Input - vase")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(edges, cmap="gray")
plt.title("Edges Alone")
plt.axis("off")
plt.show()
        