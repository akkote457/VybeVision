# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 15:14:03 2026

@author: Anoop Kote
"""

"""
color_histogram_batch.py
------------------------
Gets the color breakdown of every image in a folder.
Saves results to a CSV file.

Usage:
    python color_histogram_batch.py
"""

import cv2
import os
import csv

folder = input("Paste your image folder path: ").strip().strip('"')

if not os.path.exists(folder):
    print("Can't find that folder.")
    input("Press Enter to close.")
    exit()

extensions = (".jpg", ".jpeg", ".png", ".bmp", ".webp")
images = [f for f in os.listdir(folder) if f.lower().endswith(extensions)]

if not images:
    print("No images found.")
    input("Press Enter to close.")
    exit()

csv_path = os.path.join(folder, "color_data.csv")

print(f"\nFound {len(images)} images. Processing...\n")

with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow([
        "filename",
        "red_avg", "red_min", "red_max",
        "green_avg", "green_min", "green_max",
        "blue_avg", "blue_min", "blue_max",
        "dominant_color",
    ])

    for filename in images:
        path = os.path.join(folder, filename)
        img  = cv2.imread(path)

        if img is None:
            print(f"  SKIP  {filename}")
            continue

        b, g, r = cv2.split(img)

        avgs = {"Red": r.mean(), "Green": g.mean(), "Blue": b.mean()}
        dominant = max(avgs, key=avgs.get)

        writer.writerow([
            filename,
            round(float(r.mean()), 2), int(r.min()), int(r.max()),
            round(float(g.mean()), 2), int(g.min()), int(g.max()),
            round(float(b.mean()), 2), int(b.min()), int(b.max()),
            dominant,
        ])

        print(f"  OK    {filename}  →  dominant: {dominant}")

print(f"\nDone. Saved to: {csv_path}")
input("\nPress Enter to close.")