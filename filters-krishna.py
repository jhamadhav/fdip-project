import cv2


def not_filter(image):
    return cv2.bitwise_not(image)

def noise_removal(image):
    return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

def cartoonify(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(image, 9, 300, 300)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

def histogram_equalization(image):
    return cv2.equalizeHist(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))



def brightness_control(image, alpha=1.0, beta=0):
    """
    Adjusts the brightness of an image using the alpha and beta values.
    
    Args:
        image: Numpy array representing the input image.
        alpha: Scaling factor for the pixel values (default=1.0).
        beta: Value added to each pixel after scaling (default=0).
        
    Returns:
        Numpy array representing the output image with adjusted brightness.
    """
    bright_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return bright_image

def multiplication(image, factor=1.0):
    """
    Multiplies each pixel of an image by a factor.
    
    Args:
        image: Numpy array representing the input image.
        factor: Multiplication factor for the pixel values (default=1.0).
        
    Returns:
        Numpy array representing the output image with multiplied pixel values.
    """
    mult_image = cv2.convertScaleAbs(image, alpha=factor)
    return mult_image


def division(image, divisor=1.0):
    """
    Divides each pixel of an image by a divisor.
    
    Args:
        image: Numpy array representing the input image.
        divisor: Value to divide each pixel by (default=1.0).
        
    Returns:
        Numpy array representing the output image with divided pixel values.
    """
    div_image = cv2.convertScaleAbs(image, alpha=1.0/divisor)
    return div_image

def canny_edge_detection(image, threshold1=100, threshold2=200):
    """
    Applies Canny edge detection on an image.
    
    Args:
        image: Numpy array representing the input image.
        threshold1: Lower threshold value (default=100).
        threshold2: Upper threshold value (default=200).
        
    Returns:
        Numpy array representing the output image with detected edges.
    """
    edges = cv2.Canny(image, threshold1=threshold1, threshold2=threshold2)
    return edges


def smoothing(image, kernel_size=5):
    """
    Applies Gaussian blurring on an image to smooth it.
    
    Args:
        image: Numpy array representing the input image.
        kernel_size: Size of the Gaussian kernel (default=5).
        
    Returns:
        Numpy array representing the output image with smoothed pixels.
    """
    smoothed_image = cv2.GaussianBlur(image, ksize=(kernel_size, kernel_size), sigmaX=0, sigmaY=0)
    return smoothed_image


def sharpening(image, kernel_size=3, strength=1):
    """
    Applies unsharp masking on an image to sharpen it.
    
    Args:
        image: Numpy array representing the input image.
        kernel_size: Size of the Gaussian kernel (default=3).
        strength: Strength of the sharpening effect (default=1).
        
    Returns:
        Numpy array representing the output image with sharpened pixels.
    """
    blurred = cv2.GaussianBlur(image, ksize=(kernel_size, kernel_size), sigmaX=0, sigmaY=0)
    sharpened = cv2.addWeighted(image, 1+(strength/10), blurred, -(strength/10), 0)
    return sharpened


filterMap = {
    "noiseRemoval": noise_removal,
    "NotFilter":not_filter,
    "Cartoonify": cartoonify,
    "Hist_Equali": histogram_equalization,
    "brightness_control":brightness_control,
    "multiplication":multiplication,
    "division":division,
    "canny_edge_detection":canny_edge_detection,
    "smoothing":smoothing,
    "sharpening":sharpening
}