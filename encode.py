from LSBSteg import *

#encoding
steg = LSBSteg(cv2.imread("Image.png"))
img_encoded = steg.encode_text("This is a Secrete Message.")
cv2.imwrite("new_image.png", img_encoded)