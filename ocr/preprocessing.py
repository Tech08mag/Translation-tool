from helper.json_actions import read_json


import cv2
import numpy as np

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

def binarize(cv2_im, threshold=127):
    """Returns an OpenCV image of cv2_im as a black and white bitmap."""
    cv2_im = grayscale(cv2_im)
    return cv2.threshold(cv2_im, threshold, 255, cv2.THRESH_BINARY)[1]

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

def thin_lines(cv2_im):
    """Returns an OpenCV image of cv2_im with black lines thinned."""
    kernel = np.ones((2, 2), np.uint8)
    return cv2.dilate(cv2_im, kernel)

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

def crop(cv2_im, crop_size=10):
    """Returns an OpenCV image of cv2_im with cropped edges."""
    height, width = cv2_im.shape[:2]
    new_height = height - crop_size
    new_width = width - crop_size
    return cv2_im[crop_size:new_height, crop_size:new_width]

def add_border(cv2_im, border_size=None, border_color=(255, 255, 255), top=10, bottom=10, left=10, right=10):
    """Returns an OpenCV image of cv2_im with an added white border."""
    if border_size is not None:
        top = border_size
        bottom = border_size
        left = border_size
        right = border_size

    return cv2.copyMakeBorder(cv2_im,
        top=top, bottom=bottom,
        left=left, right=right,
        borderType=cv2.BORDER_CONSTANT,
        value=border_color)

# Additional functions for deskewing images
def getSkewAngle(cvImage) -> float:
    gray = cv2.cvtColor(cvImage, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
    dilate = cv2.dilate(thresh, kernel, iterations=2)
    contours, _ = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    largestContour = contours[0]
    minAreaRect = cv2.minAreaRect(largestContour)
    angle = minAreaRect[-1]
    if angle < -45:
        angle = 90 + angle
    return -1.0 * angle

def rotateImage(cvImage, angle: float):
    (h, w) = cvImage.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(cvImage, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

def deskew(cvImage):
    angle = getSkewAngle(cvImage)
    return rotateImage(cvImage, -1.0 * angle)


def preprocessing_handler(img: str):
    preprocesses: list = []
    preprocesses.append(read_json("settings.json", "grayscale"))
    preprocesses.append(read_json("settings.json", "binarize"))
    preprocesses.append(read_json("settings.json", "brightness"))
    preprocesses.append(read_json("settings.json", "contrast"))
    preprocesses.append(read_json("settings.json", "invert"))
    preprocesses.append(read_json("settings.json", "thin_lines"))
    preprocesses.append(read_json("settings.json", "thicken_lines"))
    preprocesses.append(read_json("settings.json", "denoise"))
    preprocesses.append(read_json("settings.json", "crop"))
    preprocesses.append(read_json("settings.json", "border"))

    print(preprocesses)

    preprocession: str = read_json("settings.json", "preprocession")
    if preprocession != "":
        for r in preprocesses:
            imgCV = open(img)
            match r:
                case "grayscale":
                    imgCV = grayscale(imgCV)
                    save(imgCV, "screenshot.png")
                case "brightness":
                    brightness_value = float(read_json("settings.json", "brightness_value"))
                    imgCV = brightness(imgCV, brightness_value)
                    save(imgCV, "screenshot.png")
                case "binarize":
                    imgCV = binarize(imgCV)
                    save(imgCV, "screenshot.png")
                case "contrast":
                    contrast_value = float(read_json("settings.json", "contrast_value"))
                    imgCV = contrast(imgCV, contrast_value)
                    save(imgCV, "screenshot.png")
                case "invert":
                    imgCV = invert(imgCV)
                    save(imgCV, "screenshot.png")
                case "thin_lines":
                    imgCV = thin_lines(imgCV)
                    save(imgCV, "screenshot.png")
                case "thicken_lines":
                    imgCV = thicken_lines(imgCV)
                    save(imgCV, "screenshot.png")
                case "denoise":
                    imgCV = denoise(imgCV)
                    save(imgCV, "screenshot.png")
                case "crop":
                    crop_value = read_json("settings.json", "crop_value")
                    imgCV = crop(imgCV, crop_value)
                    save(imgCV, "screenshot.png")
                case "border":
                    border_size = read_json("settings.json", "border_size")
                    imgCV = add_border(imgCV, border_size)
                    imgCV = open(img)