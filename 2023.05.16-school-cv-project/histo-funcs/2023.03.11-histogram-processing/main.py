# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# # Load the image
# img = cv2.imread('image.jpg', 0)

# # Create a histogram using OpenCV's built-in function
# hist = cv2.calcHist([img],[0],None,[256],[0,256])

# # Plot the histogram using Matplotlib
# plt.hist(img.ravel(),256,[0,256])
# plt.show()

# import cv2
# import numpy as np

# # Load the image
# img = cv2.imread('image.jpg', 0)

# # Apply histogram equalization 
# equ = cv2.equalizeHist(img)

# # Display the original and equalized images
# cv2.imshow('Original image', img)
# cv2.imshow('Equalized image', equ)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# from PIL import Image
# import numpy as np

# # Load the image
# img = Image.open('image.jpg').convert('L')

# # Convert the image to a numpy array
# img_arr = np.array(img)

# # Compute the histogram
# hist, bins = np.histogram(img_arr.flatten(), 256, [0, 256])

# # Compute the cumulative distribution function (CDF)
# cdf = hist.cumsum()

# # Normalize the CDF
# cdf_normalized = cdf * 255 / cdf[-1]

# # Map the intensity values using the normalized CDF
# equalized_img_arr = np.interp(img_arr.flatten(), bins[:-1], cdf_normalized)

# # Reshape the equalized image to its original shape
# equalized_img_arr = np.reshape(equalized_img_arr, img_arr.shape)

# # Convert the image array back to an image object
# equalized_img = Image.fromarray(np.uint8(equalized_img_arr))

# # Display the original and equalized images
# # img.show()
# equalized_img.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
img = cv2.imread('img2.jpeg', cv2.IMREAD_GRAYSCALE)

# Create an empty numpy array to store the histogram
hist = np.zeros((256), dtype=int)

# Iterate over each pixel in the image
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        # Increment the histogram bin corresponding to the pixel value
        hist[img[i,j]] += 1

# Plot the histogram
plt.bar(range(256), hist)
plt.show()

# Equalize the image histogram
cdf = np.cumsum(hist) 
cdf_min = cdf[img.min()]
img_eq = ((cdf[img] - cdf_min) * 255 / (img.size - cdf_min)).astype(np.uint8)
img_eq_2 = ((cdf[img]) * 255 / (img.size)).astype(np.uint8)


# Display the original and equalized images
cv2.imshow('Original Image', img)
cv2.imshow('Equalized Image', img_eq)
cv2.imshow('Equalized Image _Baho', img_eq_2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# In this code, we first load an image in grayscale using the cv2.imread function. Then, we create an empty numpy array to store the histogram and iterate over each pixel in the image to increment the corresponding histogram bin. We use the plt.bar function from the Matplotlib library to plot the histogram.

# Next, we perform histogram equalization on the image using the cumulative distribution function (CDF) of the histogram. We first compute the CDF using the np.cumsum function and then use it to calculate the equalized pixel values. Finally, we display the original and equalized images using the cv2.imshow function.
