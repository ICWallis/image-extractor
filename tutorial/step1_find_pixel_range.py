"""
Step 1 — Interactively define pixel crop coordinates.

Use pxl_range() to click two corners on a rendered PDF page and record the
resulting coordinate dict.  Run this step once per unique page layout
(typically: first page, a representative middle page, and the last page).

The coordinates produced here are used in step2_inspect_image.py and
step3_extract_image.py.

BEFORE RUNNING
--------------
Edit the PDF_PATH variable below to point to where
University_Utah_FORGE_78B-32_FMI_Interpretation_20.pdf is stored on your computer.

USAGE
-----
1. Edit PDF_PATH, then run this file.
2. A matplotlib window opens showing the rendered page. Use the built-in 
   zoom/pan tools to navigate to the top-left corner of the log strip you 
   want to crop.
3. Click "Selection Mode" to enable clicking, then click the top-left corner
   of the log strip you want to crop. 
4. Once you are happy with your selection, press "Accept Point" to lock it in.
5. Toggle selection mode again, then navigate to the bottom-right corner of 
   the log strip.
6. Once you are happy with your selection in the bottom-right corner, press 
   "Accept Point" again.
7. Close the window — the coordinate dict is printed to the terminal.
8. Update the hard-coded coordinates in step2 and step3 as needed.
"""

from logprint_extractor import pxl_range

# ---------------------------------------------------------------------------
# PDF path
# ---------------------------------------------------------------------------

PDF_PATH = r"C:\PATH\TO\University_Utah_FORGE_78B-32_FMI_Interpretation_20.pdf"  # <-- EDIT THIS

# ---------------------------------------------------------------------------
# Pages to inspect
#   0-indexed.  The PDF has 196 pages (indices 0–195).
#   Page 195 is a cover/summary page and is excluded from the log.
#   Typical pages to define coordinates for:
#     - 0   : first included page (log may start part-way down)
#     - 97  : a representative middle page (full-height strip)
#     - 194 : last included page (log may end before the bottom)
# ---------------------------------------------------------------------------

PAGES_TO_DEFINE = {
    "first":  0,    # log starts part-way down this page
    "middle": 97,   # full-height representative page
    "last":   194,  # last included page before the excluded cover page
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    results = {}

    for label, page_num in PAGES_TO_DEFINE.items():
        print(f"\n{'='*60}")
        print(f"  Defining coordinates for: {label} page  (index {page_num})")
        print(f"{'='*60}")

        coords = pxl_range(PDF_PATH, page_num=page_num)

        if coords is not None:
            results[label] = coords
            print(f"\nCoordinates for '{label}' page (copy into step2/step3):")
            print(f"  {coords}")
        else:
            print(f"  No coordinates captured for '{label}' page (window closed early).")

    print("\n\n--- Summary of all captured coordinates ---")
    for label, coords in results.items():
        print(f"  {label:8s}: {coords}")
