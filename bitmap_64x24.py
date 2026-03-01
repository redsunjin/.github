# Bitmap 64x24

"""
This script generates a 64x24 bitmap.
"""

def generate_bitmap():
    bitmap = [[0 for _ in range(64)] for _ in range(24)]
    # Example: Setting some pixels
    bitmap[0][0] = 1
    bitmap[1][1] = 1
    return bitmap

if __name__ == '__main__':
    bmp = generate_bitmap()
    print(bmp)