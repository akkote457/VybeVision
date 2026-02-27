# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 19:33:59 2026

@author: Anoop Kote
"""

"""
face_count_batch.py
-------------------
Counts how many faces are in each image in a folder.
Saves results to a CSV.

Usage:
    python face_count_batch.py
"""

import cv2
import os
import csv

# Built in face detector - no API needed
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

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

csv_path = os.path.join(folder, "face_counts.csv")
output_folder = os.path.join(folder, "faces_detected")
os.makedirs(output_folder, exist_ok=True)

print(f"\nFound {len(images)} images. Processing...\n")

total_faces = 0

with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["filename", "face_count"])

    for filename in images:
        path = os.path.join(folder, filename)
        img  = cv2.imread(path)

        if img is None:
            print(f"  SKIP  {filename}")
            continue

        gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))
        count = len(faces)
        total_faces += count

        # Draw boxes around faces and save
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,180), 2)

        out_path = os.path.join(output_folder, filename)
        cv2.imwrite(out_path, img)

        writer.writerow([filename, count])
        print(f"  {count} face(s)   {filename}")

print(f"\nTotal faces found: {total_faces}")
print(f"CSV saved to:      {csv_path}")
print(f"Images saved to:   {output_folder}")
input("\nPress Enter to close.")