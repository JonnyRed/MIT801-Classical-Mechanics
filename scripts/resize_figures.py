from pathlib import Path
import sys, subprocess, shutil

# Ensure Pillow is installed
try:
    from PIL import Image
except Exception:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"]) 
    from PIL import Image

FIG_DIR = Path(__file__).resolve().parent.parent / 'figures'
BACKUP_DIR = FIG_DIR / 'backup-originals'
BACKUP_DIR.mkdir(exist_ok=True)

exts = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}
files = [p for p in FIG_DIR.iterdir() if p.is_file() and p.suffix.lower() in exts]
if not files:
    print('No image files found in', FIG_DIR)
    sys.exit(0)

for f in files:
    # skip the backup folder itself
    if f.parent == BACKUP_DIR:
        continue
    # backup original if not already backed up
    backup_path = BACKUP_DIR / f.name
    if not backup_path.exists():
        shutil.copy2(f, backup_path)
        print(f'Backed up {f.name} -> {backup_path}')
    try:
        im = Image.open(f)
        w, h = im.size
        new_size = (max(1, int(w * 0.75)), max(1, int(h * 0.75)))
        im2 = im.resize(new_size, Image.LANCZOS)
        # overwrite original
        im2.save(f, optimize=True, quality=90)
        print(f'Resized {f.name}: {w}x{h} -> {new_size[0]}x{new_size[1]}')
    except Exception as e:
        print('Failed to process', f, e)

print('Done')
