"""
Step 3 — Batch extract depth-labelled PNG strips.

Uses extract_image() to process all included pages of the PDF and save each
cropped strip as a PNG file named with its depth range, e.g.:
    FORGE_78B-32 224.70 - 228.65.png

Output files are saved to the OUTPUT_DIR folder defined below.
"""

from image_extractor import extract_image
import os

# ---------------------------------------------------------------------------
# PDF path & output directory
# ---------------------------------------------------------------------------

PDF_PATH = (
    r"C:\Users\irene\Dropbox (Personal)\Cubic-Earth\Marketing\ALT_colab"
    r"\DigitisingLogPrints\ExampleData"
    r"\University_Utah_FORGE_78B-32_FMI_Interpretation_20.pdf"
)

OUTPUT_DIR = os.path.join(
    r"C:\Users\irene\Dropbox (Personal)\Cubic-Earth\Marketing\ALT_colab"
    r"\DigitisingLogPrints\ExampleData",
    "extracted_FORGE_78B32",
)

# ---------------------------------------------------------------------------
# Well metadata
# ---------------------------------------------------------------------------

WELL_NAME  = "FORGE_78B-32"
TOP_DEPTH  = 224.7   # metres — depth at the top of the log (first included page)
BASE_DEPTH = 999.4   # metres — depth at the base of the log (last included page)

# ---------------------------------------------------------------------------
# Pages to exclude
#   Page 196 (0-indexed) has no log data.
# ---------------------------------------------------------------------------

EXCLUDE_PAGES = [196]

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
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    saved = extract_image(
        pdf_path=PDF_PATH,
        output_dir=OUTPUT_DIR,
        wellname=WELL_NAME,
        top_depth=TOP_DEPTH,
        base_depth=BASE_DEPTH,
        pixel_coords_first=PIXEL_COORDS_FIRST,
        pixel_coords_default=PIXEL_COORDS_DEFAULT,
        pixel_coords_last=PIXEL_COORDS_LAST,
        exclude_pages=EXCLUDE_PAGES,
    )

    print(f"\nExtracted {len(saved)} PNG files.")
    print(f"First : {saved[0]}")
    print(f"Last  : {saved[-1]}")
