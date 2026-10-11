import cv2
    # IDENTIFYING IMAGE TYPE
image = cv2.imread("rabbit.jpg") #(reads the image)
print(type(image))# (prints the image type)
print(image.shape)# (prints the image shape)