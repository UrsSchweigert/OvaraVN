import sys
from PIL import Image
src,dst=sys.argv[1:3]
Image.open(src).convert("RGB").resize((1920,1088),Image.LANCZOS).save(dst)
