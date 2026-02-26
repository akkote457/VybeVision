# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 13:54:43 2026

@author: Anoop Kote
"""

import cv2

path = input("Drop your image here: ").strip().strip('"')

img  = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()