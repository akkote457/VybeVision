# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 14:27:54 2026

@author: Anoop Kote
"""

"""
edges.py
--------
Takes an image and finds all the edges in it.
This is how a vision system starts to see shapes.

Usage:
    python edges.py
"""

import cv2

path = input("Drop your image here: ").strip().strip('"')

img   = cv2.imread(path)
gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)

cv2.imshow("Original", gray)
cv2.imshow("Edges", edges)

print("\nShowing original and edges side by side.")
print("Press Q to close.")

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()