# USAGE
# With default parameters
#     python3 02_encode.py
# OR specifying the dataset, encodings and detection method
#     python3 02_encode.py -i dataset -e encodings.pickle -d hog

## Acknowledgement
## This code is adapted from:
## https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/

# import the necessary packages
from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os

path = os.path.abspath(os.path.dirname(__file__))
os.chdir(path) 

class EncodeCam():
    def __init__(self):
        # construct the argument parser and parse the arguments
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--dataset", default = "dataset",
            help="path to input directory of faces + images")
        ap.add_argument("-e", "--encodings", default = "encodings.pickle",
            help="path to serialized db of facial encodings")
        ap.add_argument("-d", "--detection-method", type = str, default = "hog",
            help="face detection model to use: either `hog` or `cnn`")
        args = vars(ap.parse_args())

        # grab the paths to the input images in our dataset
        print("[INFO] quantifying faces...")
        imagePaths = list(paths.list_images(args["dataset"]))

        # initialize the list of known encodings and known names
        knownEncodings = []
        knownNames = []

        # loop over the image paths
        for (i, imagePath) in enumerate(imagePaths):
            # extract the person name from the image path
            print("[INFO] processing image {}/{}".format(i + 1, len(imagePaths)))
            name = imagePath.split(os.path.sep)[-2]

            # load the input image and convert it from RGB (OpenCV ordering)
            # to dlib ordering (RGB)
            image = cv2.imread(imagePath)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # detect the (x, y)-coordinates of the bounding boxes
            # corresponding to each face in the input image
            boxes = face_recognition.face_locations(rgb, model = args["detection_method"])

            # compute the facial embedding for the face
            encodings = face_recognition.face_encodings(rgb, boxes)
            
            # loop over the encodings
            for encoding in encodings:
                # add each encoding + name to our set of known names and encodings
                knownEncodings.append(encoding)
                knownNames.append(name)

        # dump the facial encodings + names to disk
        print("[INFO] serializing encodings...")
        data = { "encodings": knownEncodings, "names": knownNames }

        with open(args["encodings"], "wb") as f:
            f.write(pickle.dumps(data))
