import cv2


def digitalNegative(img):
    L = img.max()
    img2 = L - img
    return img2


def rotateimagebyClockwise(img):
    rotatedimg = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    return rotatedimg


filterMap = {
    "digitalNegative": digitalNegative,
    "rotateimagebyClockwise": rotateimagebyClockwise
}
