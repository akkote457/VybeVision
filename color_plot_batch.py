# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 15:17:01 2026

@author: Anoop Kote
"""

"""
color_plot_batch.py
-------------------
Saves a color histogram plot for every image in a folder.
Plots go into a "plots" subfolder.

Install first:
    pip install matplotlib

Usage:
    python color_plot_batch.py
"""

import cv2
import matplotlib.pyplot as plt
import os

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

output_folder = os.path.join(folder, "plots")
os.makedirs(output_folder, exist_ok=True)

print(f"\nFound {len(images)} images. Processing...\n")

for filename in images:
    path = os.path.join(folder, filename)
    img  = cv2.imread(path)

    if img is None:
        print(f"  SKIP  {filename}")
        continue

    b, g, r = cv2.split(img)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle(filename, fontsize=12)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    axes[0].imshow(img_rgb)
    axes[0].set_title("Original")
    axes[0].axis("off")

    axes[1].set_title("Color Histogram")
    axes[1].set_xlabel("Pixel Value (0=dark, 255=bright)")
    axes[1].set_ylabel("Number of Pixels")

    for channel, color, label in [(r,"red","Red"),(g,"green","Green"),(b,"blue","Blue")]:
        hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
        axes[1].plot(hist, color=color, label=label, linewidth=1.5)

    axes[1].legend()
    axes[1].set_xlim([0, 256])

    plt.tight_layout()

    out_name = os.path.splitext(filename)[0] + "_plot.png"
    out_path = os.path.join(output_folder, out_name)
    plt.savefig(out_path)
    plt.close()

    print(f"  OK    {filename}")

print(f"\nDone. Saved to: {output_folder}")
input("\nPress Enter to close.")