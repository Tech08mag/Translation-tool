import cv2
import numpy as np
import pytesseract as tess
from PIL import Image


def getTextfromImage(image, sourcelang: str):
    img = Image.open(image)
    text = tess.image_to_string(img, lang=sourcelang)
    return text

def open(filename):
    """Returns an OpenCV image of an image file."""
    cv2_im = cv2.imread(filename)
    if cv2_im is None:
        raise FileNotFoundError('No image file named ' + filename)
    return cv2_im

def save(cv2_im, filename='image.png'):
    """Saves the OpenCV image in cv2_im as an image file."""
    cv2.imwrite(filename, cv2_im)

def grayscale(cv2_im):
    """Returns an OpenCV image of cv2_im as a grayscale image."""
    return cv2.cvtColor(cv2_im, cv2.COLOR_BGR2GRAY)

def brightness(cv2_im, setting):
    """Returns an OpenCV image of cv2_im with changed brightness."""
    setting = min(max(setting, -1.0), 1.0)
    cv2_im = cv2_im.astype(np.float32) / 255.0
    cv2_im = cv2_im + setting
    cv2_im = np.clip(cv2_im, 0, 1)
    return (cv2_im * 255).astype(np.uint8)

def contrast(cv2_im, setting):
    """Returns an OpenCV image of cv2_im with changed contrast."""
    setting = max(setting, 0)
    cv2_im = cv2_im.astype(np.float32) / 255.0
    mean = np.mean(cv2_im)
    cv2_im = (cv2_im - mean) * setting + mean
    cv2_im = np.clip(cv2_im, 0, 1)
    return (cv2_im * 255).astype(np.uint8)

def invert(cv2_im):
    """Returns an OpenCV image of cv2_im with the colors inverted."""
    return cv2.bitwise_not(cv2_im)

def thicken_lines(cv2_im):
    """Returns an OpenCV image of cv2_im with black lines thickened."""
    kernel = np.ones((2, 2), np.uint8)
    return cv2.erode(cv2_im, kernel)

def denoise(cv2_im):
    """Returns an OpenCV image of cv2_im denoised."""
    kernel = np.ones((1, 1), np.uint8)
    cv2_im = cv2.morphologyEx(cv2_im, cv2.MORPH_OPEN, kernel)
    cv2_im = cv2.morphologyEx(cv2_im, cv2.MORPH_CLOSE, kernel)
    cv2_im = cv2.medianBlur(cv2_im, 3)
    return cv2_im

def preproccessImage(filename):
    img = open(filename)
    img = grayscale(img)
    img = invert(img)
    img = thicken_lines(img)
    img = denoise(img)
    save(img)