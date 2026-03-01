#!/usr/bin/env python3
"""
Generate an SVG image from bitmap_64x24.BITMAP
Usage: python bitmap_to_svg.py
Outputs: images/intro_bitmap.svg
"""
import os
from bitmap_64x24 import BITMAP

OUT_DIR = "images"
OUT_FILE = os.path.join(OUT_DIR, "intro_bitmap.svg")
SCALE = 8  # pixels per bitmap cell
W = len(BITMAP[0])
H = len(BITMAP)

def make_svg(bitmap, scale=SCALE, out_path=OUT_FILE):
    width = W * scale
    height = H * scale
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f'<?xml version="1.0" encoding="utf-8"?>\n')
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">\n')
        # background (black)
        f.write(f'  <rect width="100%" height="100%" fill="#000"/>\n')
        # draw white pixels
        f.write('  <g fill="#fff">\n')
        for y, row in enumerate(bitmap):
            for x, ch in enumerate(row):
                if ch == "1":
                    rx = x * scale
                    ry = y * scale
                    f.write(f'    <rect x="{rx}" y="{ry}" width="{scale}" height="{scale}" />\n')
        f.write('  </g>\n')
        f.write('</svg>\n')
    print(f"Saved {out_path} ({width}x{height})")

if __name__ == "__main__":
    make_svg(BITMAP)
