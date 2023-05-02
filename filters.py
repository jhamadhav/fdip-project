import cv2


def digitalNegative(img):
    L = img.max()
    img2 = L - img
    return img2


filterMap = {
    "digitalNegative": digitalNegative
}
