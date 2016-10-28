# This needs to accept an image and an form format code
# The form format code is going to be on the paper, and will specify what types of questions there are
# The form format code is a nth character long string that tells the type of question and order
# Basically, load an image, get the bubbled answers, and then create a report sheet
#
# Author: Thomas Hayden
# Date created: 10/13/2016
# Date revised: 10/13/2016


from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2

class Loader():

    def __init__(self):
        self.minimumPixels = 400
        self.bubblesPerQuestion = 5
        self.filledInBubbles = {}

    def load(self, imagePath):
        # Used to be used when this was a stand alone thing. Now its useless, but I'm afraid to get rid of it
        # Argue with the arguments
        #ap = argparse.ArgumentParser()
        #ap.add_argument("-i", "--image", required=True, help="path to the input image")
        #args = vars(ap.parse_args())

        # Load the image, convert it to grayscale, blur it just a bit, then find edges
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(blurred, 75, 200)

        # Find contours in the edge map, then initialize the contour that corresponds to the document
        cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        docCnt = None

        # Ensure that at least one contour was found
        if len(cnts) > 0:
            # Sort the contours according to their size in
            # descending order
            cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

            # Loop over the sorted contours
            for c in cnts:
                # Approximate the contour
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.02 * peri, True)

                # If the approximated contour has four points,
                # then we can assume we have found the paper
                if len(approx) == 4:
                    docCnt = approx
                    break

        # Apply a four point perspective transform to both the original image and grayscale image to obtain a top-down view of the paper
        paper = four_point_transform(image, docCnt.reshape(4, 2))
        warped = four_point_transform(gray, docCnt.reshape(4, 2))

        # Apply thresholding to binarize the warped piece of paper
        thresh = cv2.threshold(warped, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

        # Find contours in the thresholded image, then initialize the list of contours that correspond to questions
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        questionCnts = []

        # Loop over the contours
        for c in cnts:
            # Compute the bounding box of the contour, then use the bounding box to derive the aspect ratio
            (x, y, w, h) = cv2.boundingRect(c)
            ar = w / float(h)

            # In order to label the contour as a question, region should be sufficiently wide, sufficiently tall, and have an aspect ratio approximately equal to 1
            if w >= 20 and h >= 20 and ar >= 0.9 and ar <= 1.1:
                questionCnts.append(c)

        # Sort the question contours top-to-bottom
        # We now have a list of contors from left to right, top to bottom
        questionCnts = contours.sort_contours(questionCnts,method="top-to-bottom")[0]

        # Each question has 5 possible answers, to loop over the question in batches of 5
        for (q, i) in enumerate(np.arange(0, len(questionCnts), self.bubblesPerQuestion)):
            # Sort the contours for the current question from
            # left to right, then initialize the index of the
            # bubbled answer
            cnts = contours.sort_contours(questionCnts[i:i + self.bubblesPerQuestion])[0]
            notBubbled = [None] * self.bubblesPerQuestion
            bubbled = [None] * self.bubblesPerQuestion

            count = 0
            # Loop over the sorted contours
            for (j, c) in enumerate(cnts):
                # Construct a mask that reveals only the current
                # "bubble" for the question
                mask = np.zeros(thresh.shape, dtype="uint8")
                cv2.drawContours(mask, [c], -1, 255, -1)
                cv2.drawContours(paper, [c], 0, 255, 0)

                # Apply the mask to the thresholded image, then
                # count the number of non-zero pixels in the
                # bubble area
                mask = cv2.bitwise_and(thresh, thresh, mask=mask)
                total = cv2.countNonZero(mask)

                # If the current total has a larger number of total
                # non-zero pixels, then we are examining the currently
                # bubbled-in answer
                if bubbled[j*(count+1)] is None and total > self.minimumPixels:
                    print total
                    bubbled[j*(count+1)] = (total, j)
                else:
                    bubbled[j*(count+1)] = None
                    notBubbled[j*(count+1)] = (total, j)
            count = count + 1

            # Initialize the contour color and the index of the
            # filled in bubble
            color = (0, 255, 0)

            for (i, bubble) in enumerate(bubbled):
                if bubbled[i] is not None:
                    # Add this bubble to the dictionary of filled in bubbles
                    self.filledInBubbles.update({q:bubbled[i][1]})

                    # Draw the outline of bubbles which appear to be filled in
                    cv2.drawContours(paper, [cnts[bubbled[i][1]]], -1, color, 3)

        # Display the sheet with all detected bubbles. Ones which are filled
        # in are green, where as blank ones are blue
        cv2.imshow("Result", paper)
        cv2.waitKey(0)

        # Print out the values of the questions and the answers
        for i in self.filledInBubbles:
            print(i, self.filledInBubbles[i])
