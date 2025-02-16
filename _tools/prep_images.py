import os
import sys
from pathlib import Path
from PIL import Image

# Default settings
MAX_WIDTH = 1200
WEBP_QUALITY = 85  # Adjust for balance between quality and size

def process_image(input_path, output_path):
    """Resizes, strips metadata, compresses, and converts an image to WebP."""
    try:
        with Image.open(input_path) as img:
            # Convert to RGB (fixes PNGs with transparency)
            if img.mode in ("P", "RGBA"):
                img = img.convert("RGB")
            
            # Resize while keeping aspect ratio
            width_percent = MAX_WIDTH / float(img.width)
            new_height = int(float(img.height) * width_percent)
            img = img.resize((MAX_WIDTH, new_height), Image.LANCZOS)
            
            # Save as WebP (no metadata)
            img.save(output_path, "WEBP", quality=WEBP_QUALITY, optimize=True)
            print(f"✅ Processed: {input_path} → {output_path}")

    except Exception as e:
        print(f"❌ Error processing {input_path}: {e}")

def process_directory(raw_dir, output_dir):
    """Recursively process images and maintain directory structure."""
    raw_dir = Path(raw_dir)
    output_dir = Path(output_dir)

    for root, _, files in os.walk(raw_dir):
        relative_path = Path(root).relative_to(raw_dir)
        output_subdir = output_dir / relative_path
        output_subdir.mkdir(parents=True, exist_ok=True)

        for file in files:
            if not file.lower().endswith(("jpg", "jpeg", "png", "bmp", "tiff")):
                continue
            
            input_path = Path(root) / file
            output_path = output_subdir / f"{Path(file).stem}.webp"
            process_image(input_path, output_path)

if __name__ == "__main__":
    # Get command-line arguments
    if len(sys.argv) < 2:
        print("❌ Usage: python process_images.py <input_folder> [output_folder]")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2] if len(sys.argv) > 2 else "output_images"

    process_directory(input_folder, output_folder)
    print("\n✅ Image processing complete!")

