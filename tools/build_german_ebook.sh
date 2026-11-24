#!/bin/bash
# Build the German ebook: full book, 2-chapter sample, cover, upload folder, checks.
# The author name is read from the English epub's metadata at run time; it is never
# printed or stored in this file. Run from the repository root:
#   tools/build_german_ebook.sh [--allow-missing]
set -e
cd "$(dirname "$0")/.."
EN=publish/books/the-man-the-tide-brought-in.epub
[ -f "$EN" ] || { echo "Missing $EN (build the English epub first)"; exit 1; }
ALLOW=""; [ "$1" = "--allow-missing" ] && ALLOW="--allow-missing"

python3 tools/assemble_german.py $ALLOW

AUTHOR="$(unzip -p "$EN" OEBPS/content.opf | python3 -c 'import sys,re; m=re.search(r"<dc:creator[^>]*>(.*?)</dc:creator>", sys.stdin.read(), re.S); print(m.group(1) if m else "")')"
[ -n "$AUTHOR" ] || { echo "Could not read the author from the English epub"; exit 1; }
# the name is XML-escaped in the metadata; make_epub escapes it again, so undo that once
AUTHOR="$(printf '%s' "$AUTHOR" | python3 -c 'import sys,html; print(html.unescape(sys.stdin.read()), end="")')"

python3 tools/make_cover.py --art art/store/cover/cover_c.png --author "$AUTHOR" \
  --title-lines "Der Mann, den" "die Flut brachte" --out publish/books/cover_de.jpg
python3 tools/make_epub.py --lang de --author "$AUTHOR" --cover publish/books/cover_de.jpg \
  --out publish/books/der-mann-den-die-flut-brachte.epub
python3 tools/make_epub.py --lang de --author "$AUTHOR" --cover publish/books/cover_de.jpg --sample 2 \
  --out publish/books/der-mann-den-die-flut-brachte-leseprobe.epub

mkdir -p publish/apple-books-upload
cp publish/books/der-mann-den-die-flut-brachte.epub publish/apple-books-upload/book_de.epub
cp publish/books/der-mann-den-die-flut-brachte-leseprobe.epub publish/apple-books-upload/sample_de.epub
cp publish/books/cover_de.jpg publish/apple-books-upload/cover_de.jpg

GAPS=""; [ -n "$ALLOW" ] && GAPS="--allow-gaps"
python3 tools/check_epub.py publish/apple-books-upload/book_de.epub $GAPS
python3 tools/check_epub.py publish/apple-books-upload/sample_de.epub
