import cv2
import shutil
img = cv2.imread("text.jpg")
original = "text.txt"
for i in range(10000):
    cv2.imwrite(f"train/images/text{i}.jpg", img)
    shutil.copyfile(original, f"train/labels/text{i}.txt")
