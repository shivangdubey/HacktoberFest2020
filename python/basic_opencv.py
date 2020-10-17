#This is a simple menu driven program to enable basic operations 
# on an image using the OpenCV library and python
import cv2


# Read and print the image


def print_image():

    cv2.imshow('Image', image)
    cv2.waitKey(0)


# Convert to Grayscale


def grayscale_image():
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale Image', grayscale_image)
    cv2.waitKey(0)

# Rotate the image


def rotate(angle):
    (h, w, d) = image.shape
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, int(angle), 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    cv2.imshow("Rotated Image", rotated)
    cv2.waitKey(0)


# Resize the image preserving the aspect ratio

def resize(new_height):
    (h, w, d) = image.shape
    ratio = float(new_height) / w
    dim = (int(new_height), int(h * ratio))
    resized = cv2.resize(image, dim)
    cv2.imshow("Resized Image", resized)
    cv2.waitKey(0)


print("Enter or paste the path to the image below:\n")
path = input()
image = cv2.imread(path)

print("What would you like to do?\n1. Rotate\n2. Convert to grayscale\n3. Resize\n4. Print\n")
ch = int(input())
if ch == 1:
    print("Enter the angle by which the image should be rotated (-ve value if clockwise):\n")
    angles = input()
    rotate(angles)
elif ch == 2:
    grayscale_image()
elif ch == 3:
    print("Enter the height required(image will be in the same aspect ratio as before):\n")
    height = input()
    resize(height)
elif ch == 4:
    print_image()
else:
    print("Invalid Option!")
