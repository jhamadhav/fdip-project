import cv2
import numpy as np
import matplotlib.pyplot as plt


def digitalNegative(img):
    L = img.max()
    img2 = L - img
    return img2


def rotateimagebyClockwise(img):
    rotatedimg = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    return rotatedimg


def rotateimagebyAnticlockwise(img):
    rotatedimg = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    return rotatedimg


def imageflip(img, direction=1):
    direction = direction
    # direction: 'H' -> Horizontal , 'V' -> vertical , else-> diagonal
    if 'H' == 1:
        img_v = cv2.flip(img, 1)
    elif 'V' == 0:
        img_v = cv2.flip(img, 0)
    else:
        img_v = cv2.flip(img, -1)
    return img_v


def contrastStretching(img):
    # Create zeros array to store the stretched image
    minmax_img = np.zeros((img.shape[0], img.shape[1]), dtype='uint8')
    # Loop over the image and apply Min-Max formulae
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            minmax_img[i, j] = 255*(img[i, j]-np.min(img)) / \
                (np.max(img)-np.min(img))
    return minmax_img


def gammaTransformation(img, gamma_val=2.2):
    # Apply Gamma=2.2 on the normalised image and then multiply by scaling constant (For 8 bit, c=255)
    gamma_two_point_two = np.array(255*(img/255)**gamma_val, dtype='uint8')
    return gamma_two_point_two


def logTransformation(img):
    # Apply log transform.
    c = 255/(np.log(1 + np.max(img)))
    log_transformed = c * np.log(1 + img)
    # Specify the data type.
    log_transformed = np.array(log_transformed, dtype=np.uint8)
    return log_transformed


def graySlicing(img):
    #  gray level slicing
    m, n = img.shape
    for i in range(m):
        for j in range(n):
            if img[i][j] > 100 and img[i][j] < 200:
                img[i][j] = 210
    return img


def BitplaneSlicing(img):
    lst = []
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # width = no. of bits
            lst.append(np.binary_repr(img[i][j], width=8))

            # We have a list of strings where each string represents binary pixel value. To extract bit planes we need to iterate over the strings and store the characters corresponding to bit planes into lists.
            # Multiply with 2^(n-1) and reshape to reconstruct the bit image.
    eight_bit_img = (np.array(
        [int(i[0]) for i in lst], dtype=np.uint8) * 128).reshape(img.shape[0], img.shape[1])
    seven_bit_img = (np.array(
        [int(i[1]) for i in lst], dtype=np.uint8) * 64).reshape(img.shape[0], img.shape[1])
    six_bit_img = (np.array([int(i[2]) for i in lst], dtype=np.uint8)
                   * 32).reshape(img.shape[0], img.shape[1])
    five_bit_img = (np.array([int(i[3]) for i in lst],
                             dtype=np.uint8) * 16).reshape(img.shape[0], img.shape[1])
    four_bit_img = (np.array([int(i[4]) for i in lst],
                             dtype=np.uint8) * 8).reshape(img.shape[0], img.shape[1])
    three_bit_img = (np.array(
        [int(i[5]) for i in lst], dtype=np.uint8) * 4).reshape(img.shape[0], img.shape[1])
    two_bit_img = (np.array([int(i[6]) for i in lst],
                            dtype=np.uint8) * 2).reshape(img.shape[0], img.shape[1])
    one_bit_img = (np.array([int(i[7]) for i in lst],
                            dtype=np.uint8) * 1).reshape(img.shape[0], img.shape[1])

    # Concatenate these images for ease of display using cv2.hconcat()
    finalr = cv2.hconcat(
        [eight_bit_img, seven_bit_img, six_bit_img, five_bit_img])
    finalv = cv2.hconcat(
        [four_bit_img, three_bit_img, two_bit_img, one_bit_img])

    # Vertically concatenate
    final = cv2.hconcat([finalr, finalv])
    return final


def histogramegen(img):
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    fig = plt.gcf()
    fig.canvas.draw()
    # Now we can save it to a numpy array.
    data = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    return data


def contrastcontrol(img, contrast=18):
    # define the alpha and beta
    alpha = contrast  # Contrast control (0,127)
    beta = 5  # Brightness control (0,100)

    # call convertScaleAbs function
    adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return adjusted


filterMap = {
    "digitalNegative": digitalNegative,
    "rotateimagebyClockwise": rotateimagebyClockwise,
    "rotateimagebyAnticlockwise": rotateimagebyAnticlockwise,
    "imageflip": imageflip,
    "contrastStretching": contrastStretching,
    "gammaTransformation": gammaTransformation,
    "logTransformation": logTransformation,
    "grayLevelSlicing": graySlicing,
    "bitPlaneSlicing": BitplaneSlicing,
    "histoGramGenration": histogramegen,
    "contrastControl": contrastcontrol
}
