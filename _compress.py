import os, sys
from PIL import Image

src = r"D:\Desktop\funhistory\assets"
bak = r"D:\Desktop\funhistory\_backup\assets_orig"
os.makedirs(bak, exist_ok=True)

for f in sorted(os.listdir(src)):
    if not f.lower().endswith(('.jpg','.jpeg','.png')): continue
    p = os.path.join(src, f)
    bp = os.path.join(bak, f)
    if not os.path.exists(bp):
        import shutil; shutil.copy2(p, bp)
    im = Image.open(bp).convert('RGB')
    w,h = im.size
    maxw = 1200
    if w > maxw:
        im = im.resize((maxw, int(h*maxw/w)), Image.LANCZOS)
    im.save(p, 'JPEG', quality=78, optimize=True, progressive=True)
    print(f, round(os.path.getsize(p)/1024), 'KB')
