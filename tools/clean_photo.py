import sys
import cv2
import numpy as np
from PIL import Image
from rembg import remove

def clean_image(input_path, output_path="assets/photo-ready.png"):
    # 1. Background Removal
    with open(input_path, 'rb') as f:
        input_bytes = f.read()
    subject_bytes = remove(input_bytes)
    
    # Convert bytes to OpenCV image format
    nparr = np.frombuffer(subject_bytes, np.uint8)
    img_rgba = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)
    
    # Extract alpha channel mask
    b, g, r, alpha = cv2.split(img_rgba)
    gray = cv2.cvtColor(cv2.merge([b, g, r]), cv2.COLOR_BGR2GRAY)
    
    # 2. CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)
    
    # 3. Composite onto white background
    white_bg = np.ones_like(gray, dtype=np.uint8) * 255
    alpha_factor = alpha.astype(float) / 255.0
    final_img = (enhanced * alpha_factor + white_bg * (1.0 - alpha_factor)).astype(np.uint8)
    
    cv2.imwrite(output_path, final_img)
    print(f"✅ Prepared image saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python clean_photo.py <path-to-photo>")
        sys.exit(1)
    clean_image(sys.argv[1])
