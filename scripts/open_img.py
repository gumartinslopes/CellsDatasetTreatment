from PIL import Image
import matplotlib.pyplot as plt
i = 5
selected_image = Image.open(f'../CellsDataset/inverted_segmentation/{i}.png')
plt.imshow(selected_image)
plt.title(f'Image {i}')
plt.show()