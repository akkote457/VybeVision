# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 14:23:04 2026

@author: Anoop Kote
"""

"""
pixel_values.py
---------------
Shows you what an image looks like as raw numbers.
This is what every vision system actually sees.

Usage:
    python pixel_values.py
"""

import cv2
import numpy as np

path = input("Drop your image here: ").strip().strip('"')

img  = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h, w = gray.shape

print(f"\n  Image size: {w} x {h} pixels")
print(f"  Total pixels: {w * h:,}")
print(f"\n  Each pixel is a number from 0 (black) to 255 (white)")
print(f"\n  Top-left 10x10 corner as numbers:")
print(f"  {'-'*60}")

# Print a 10x10 sample of pixel values from top left
sample = gray[:10, :10]
for row in sample:
    print("  " + "  ".join(f"{val:3}" for val in row))

print(f"\n  Stats across the whole image:")
print(f"  Darkest pixel:  {gray.min()}")
print(f"  Brightest pixel:{gray.max()}")
print(f"  Average:        {gray.mean():.1f}")

input("\nPress Enter to close.")