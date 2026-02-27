# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 15:13:29 2026

@author: Anoop Kote
"""

"""
color_histogram.py
------------------
Shows the color breakdown of an image.
How much red, green, and blue is in it.
That's the color spectrum.

Usage:
    python color_histogram.py
"""

import cv2
import numpy as np

path = input("Drop your image here: ").strip().strip('"')

img = cv2.imread(path)
if img is None:
    print("Can't read that image.")
    input("Press Enter to close.")
    exit()

# Split into blue, green, red channels
b, g, r = cv2.split(img)

print(f"\n  Color breakdown:")
print(f"  {'─'*35}")
print(f"  Red   avg: {r.mean():.1f}  min: {r.min()}  max: {r.max()}")
print(f"  Green avg: {g.mean():.1f}  min: {g.min()}  max: {g.max()}")
print(f"  Blue  avg: {b.mean():.1f}  min: {b.min()}  max: {b.max()}")

# Dominant color
avgs = {"Red": r.mean(), "Green": g.mean(), "Blue": b.mean()}
dominant = max(avgs, key=avgs.get)
print(f"\n  Dominant color: {dominant}")

# Show original
cv2.imshow("Original", img)
cv2.imshow("Red Channel",   r)
cv2.imshow("Green Channel", g)
cv2.imshow("Blue Channel",  b)

print("\n  Showing all 4 windows. Press Q to close.")

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()