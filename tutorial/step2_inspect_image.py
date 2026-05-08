"""
Step 2 — Visually verify pixel crop coordinates.

Uses inspect_image() to display the cropped region on key pages before
running the full extraction.  Confirm that each crop looks correct, then
proceed to step3_extract_image.py.

Run for the first page, a representative middle page, and the last page.

Close each window after inspecting the crop.
"""

from image_extractor import inspect_image

# ---------------------------------------------------------------------------
# PDF path
# ---------------------------------------------------------------------------

PDF_PATH = r"C:\PATH\TO\University_Utah_FORGE_78B-32_FMI_Interpretation_20.pdf"  # <-- EDIT THIS

# ---------------------------------------------------------------------------
# Pixel coordinates (from step1_find_pixel_range.py)
# ---------------------------------------------------------------------------

# First included page (index 0): log starts part-way down
PIXEL_COORDS_FIRST = {
    "x_start": 768.0,
    "x_end":   987.0,
    "y_start": 1199.5,
    "y_end":   1223.5,
    "zoom":    2.0,
}

# Middle pages: full-height strips
PIXEL_COORDS_DEFAULT = {
    "x_start": 768.5,
    "x_end":   987.0,
    "y_start":   0.0,
    "y_end":  1223.5,
    "zoom":    2.0,
}

# Last included page (index 194): log ends before the bottom of the page
PIXEL_COORDS_LAST = {
    "x_start": 768.0,
    "x_end":   987.5,
    "y_start":   0.0,
    "y_end":   855.0,
    "zoom":    2.0,
}

# ---------------------------------------------------------------------------
# Pages to verify
#   Adjust page indices here if you want to check additional pages.
# ---------------------------------------------------------------------------

PAGES_TO_CHECK = [
    (0,   PIXEL_COORDS_FIRST,   "first page"),
    (97,  PIXEL_COORDS_DEFAULT, "middle page"),
    (194, PIXEL_COORDS_LAST,    "last page"),
]

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    for page_num, coords, label in PAGES_TO_CHECK:
        print(f"\n--- inspect_image: {label} (page index {page_num}) ---")
        inspect_image(PDF_PATH, page_num=page_num, pixel_coords=coords)
