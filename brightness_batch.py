"""
brightness_batch.py
-------------------
Shows each image side by side with its brightness histogram.
Saves plots to a "brightness_plots" subfolder.

Install first:
    pip install matplotlib

Usage:
    python brightness_batch.py
"""

import cv2
import matplotlib.pyplot as plt
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

output_folder = os.path.join(folder, "brightness_plots")
os.makedirs(output_folder, exist_ok=True)
csv_path = os.path.join(folder, "brightness.csv")

print(f"\nFound {len(images)} images. Processing...\n")

with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["filename", "avg_brightness", "assessment"])

    for filename in images:
        path = os.path.join(folder, filename)
        img  = cv2.imread(path)

        if img is None:
            print(f"  SKIP  {filename}")
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        avg  = gray.mean()

        if avg < 60:
            assessment = "DARK"
        elif avg < 130:
            assessment = "DIM"
        elif avg < 200:
            assessment = "BRIGHT"
        else:
            assessment = "VERY BRIGHT"

        writer.writerow([filename, round(avg, 1), assessment])

        # Plot
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        fig.suptitle(f"{filename}  —  {assessment}  (avg: {round(avg,1)})", fontsize=12)

        # Left — original image
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        axes[0].imshow(img_rgb)
        axes[0].set_title("Original")
        axes[0].axis("off")

        # Right — brightness histogram
        hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
        axes[1].plot(hist, color="white", linewidth=1.5)
        axes[1].fill_between(range(256), hist.flatten(), alpha=0.4, color="white")
        axes[1].set_facecolor("#111111")
        axes[1].set_title("Brightness Distribution")
        axes[1].set_xlabel("Pixel Value (0=black, 255=white)")
        axes[1].set_ylabel("Number of Pixels")
        axes[1].axvline(x=avg, color="yellow", linestyle="--", label=f"avg: {round(avg,1)}")
        axes[1].legend()
        axes[1].set_xlim([0, 256])

        plt.tight_layout()

        out_name = os.path.splitext(filename)[0] + "_brightness.png"
        out_path = os.path.join(output_folder, out_name)
        plt.savefig(out_path, facecolor="#222222")
        plt.close()

        print(f"  {assessment:<12} {round(avg,1):>6}   {filename}")

print(f"\nDone. Plots saved to: {output_folder}")
print(f"CSV saved to:         {csv_path}")
input("\nPress Enter to close.")