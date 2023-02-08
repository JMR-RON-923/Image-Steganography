from LSBSteg import*

#encoding
steg = LSBSteg(cv2.imread("new_image.png"))
new_im = steg.encode_image(cv2.imread("Image.png"))
cv2.imwrite("Secrete_image.png", new_im)