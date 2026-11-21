from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("S.png").convert("L")

img = img.resize((6, 6))

matrice = np.array(img)

print(matrice)

binary_matrice = matrice < 128

binary_matrice = binary_matrice.astype(int)

print(binary_matrice)

output = Image.fromarray((binary_matrice * 255).astype("uint8"))

output = output.resize((300, 300))

output.show()

plt.imshow(binary_matrice, cmap="gray", interpolation="nearest")

plt.xticks(range(6))
plt.yticks(range(6))
plt.grid(True)

plt.show()