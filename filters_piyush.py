import cv2
import numpy as np

def summer_filter(image):
  def gamma_function(channel, gamma):
      invGamma = 1/gamma
      table = np.array([((i / 255.0) ** invGamma) * 255
                        for i in np.arange(0, 256)]).astype("uint8") #creating lookup table
      channel = cv2.LUT(channel, table)
      return channel

  image[:, :, 0] = gamma_function(image[:, :, 0], 0.75) # down scaling blue channel
  image[:, :, 2] = gamma_function(image[:, :, 2], 1.25) # up scaling red channel
  hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
  hsv[:, :, 1] = gamma_function(hsv[:, :, 1], 1.2) # up scaling saturation channel
  image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
  return image

def winter_filter(image):
  def gamma_function(channel, gamma):
    invGamma = 1/gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")
    channel = cv2.LUT(channel, table)
    return channel

  image[:, :, 0] = gamma_function(image[:, :, 0], 1.25) # down scaling blue channel
  image[:, :, 2] = gamma_function(image[:, :, 2], 0.75) # up scaling red channel
  hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
  hsv[:, :, 1] = gamma_function(hsv[:, :, 1], 0.8) # up scaling saturation channel
  image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
  return image

def old_tv_filter(image):
  height, width = image.shape[:2]
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  thresh = 0.8 # creating threshold. This means noise will be added to 80% pixels
  for i in range(height):
      for j in range(width):
          if np.random.rand() <= thresh:
              if np.random.randint(2) == 0:
                  # adding random value between 0 to 64. Anything above 255 is set to 255.
                  gray[i, j] = min(gray[i, j] + np.random.randint(0, 64), 255) 
              else:
                  # subtracting random values between 0 to 64. Anything below 0 is set to 0.
                  gray[i, j] = max(gray[i, j] - np.random.randint(0, 64), 0) 
  return gray

def addition(image1,image2):
  gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
  gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
  added = cv2.add(gray1,gray2)
  return added

def subtraction(image1,image2):
  gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
  gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
  subtracted = cv2.subtract(gray1,gray2)
  return subtracted

def AND_op(image1,image2):
  gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
  gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
  ANDed = cv2.bitwise_and(gray1,gray2,mask = None)
  return ANDed

def OR_op(image1,image2):
  gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
  gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
  ORed = cv2.bitwise_or(gray1,gray2,mask = None)
  return ORed

def XOR_op(image1,image2):
  gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
  gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
  XORed = cv2.bitwise_xor(gray1,gray2,mask = None)
  return XORed

def Horizontal_stack(image1,image2):
  stacked_H = np.concatenate((image1,image2), axis = 1)
  return stacked_H

def Vertical_stack(image1,image2):
  stacked_V = np.concatenate((image1,image2), axis = 0)
  return stacked_V
