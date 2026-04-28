"""
Extract a chapter from the source PDF using Marker.
Produces clean markdown with images in extracted/<chapter-tag>/.

Usage:
    uv run --with "marker-pdf[full]" --with "pymupdf" python scripts/extract_chapter.py \
        --start-page 33 --end-page 53 \
        --chapter-tag ch01-introducing-kubernetes
"""

import argparse
import subprocess
import sys
from pathlib import Path

import fitz


def build_chapter_pdf(src_pdf: Path, start: int, end: int, tmp_pdf: Path) -> int:
    """Extract pages [start, end] (1-indexed, inclusive) into a temp PDF."""
    tmp_pdf.parent.mkdir(parents=True, exist_ok=True)
    src = fitz.open(src_pdf)
    dst = fitz.open()
    for p in range(start - 1, end):
        dst.insert_pdf(src, from_page=p, to_page=p)
    count = dst.page_count
    dst.save(tmp_pdf)
    src.close()
    dst.close()
    return count


def main():
    parser = argparse.ArgumentParser(description="Extract a chapter PDF with Marker")
    parser.add_argument("--pdf", type=Path, default=Path("source/k8s-in-action-2e.pdf"))
    parser.add_argument("--start-page", type=int, required=True,
                        help="Chapter start page (1-indexed, inclusive)")
    parser.add_argument("--end-page", type=int, required=True,
                        help="Chapter end page (1-indexed, inclusive)")
    parser.add_argument("--chapter-tag", type=str, required=True,
                        help="Output subdirectory name, e.g. ch01-introducing-kubernetes")
    args = parser.parse_args()

    if not args.pdf.exists():
        print(f"PDF not found: {args.pdf}")
        sys.exit(1)

    out_dir = Path("extracted") / args.chapter_tag
    tmp_pdf = Path(".tmp") / f"{args.chapter_tag}.pdf"

    print(f"Source: {args.pdf}")
    print(f"Pages:  {args.start_page}–{args.end_page}")
    print(f"Output: {out_dir}/")

    # Step 1: Build temp chapter PDF
    page_count = build_chapter_pdf(args.pdf, args.start_page, args.end_page, tmp_pdf)
    print(f"Temp PDF: {page_count} pages → {tmp_pdf}")

    # Step 2: Run Marker
    print("Running Marker (this may take a few minutes)...")
    result = subprocess.run([
        "marker_single", str(tmp_pdf),
        "--output_dir", str(out_dir),
        "--output_format", "markdown",
    ], capture_output=False)

    if result.returncode != 0:
        print(f"Marker failed with exit code {result.returncode}")
        sys.exit(result.returncode)

    # Cleanup temp PDF
    if tmp_pdf.exists():
        tmp_pdf.unlink()

    # Stats
    md_files = sorted(out_dir.rglob("*.md"))
    img_files = sorted(out_dir.rglob("*.jpeg")) + sorted(out_dir.rglob("*.jpg")) + sorted(out_dir.rglob("*.png"))
    print(f"\nDone. Output in {out_dir}/")
    print(f"  Markdown: {len(md_files)}")
    print(f"  Images:   {len(img_files)}")
    if md_files:
        lines = md_files[0].read_text().count("\n")
        print(f"  Lines:    ~{lines}")


if __name__ == "__main__":
    main()
