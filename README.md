# image_converter
resize image, edit photo, resize to upload image in web.
Pillow, the Python Imaging Library (PIL) fork, provides a wide range of tools for image manipulation. Below is an overview of the major tools and functions you can use from Pillow:

### 1. **Opening and Saving Images:**

- **Opening an image:**
  ```python
  from PIL import Image
  im = Image.open('image.jpg')
  ```

- **Saving an image:**
  ```python
  im.save('output.jpg')
  ```

- **Saving an image in a different format:**
  ```python
  im.save('output.png', 'PNG')
  ```

### 2. **Image Information:**

- **Get image size (width, height):**
  ```python
  width, height = im.size
  ```

- **Get image format (e.g., JPEG, PNG):**
  ```python
  format = im.format
  ```

- **Get image mode (e.g., RGB, L):**
  ```python
  mode = im.mode
  ```

### 3. **Resizing and Cropping:**

- **Resizing an image:**
  ```python
  im_resized = im.resize((new_width, new_height), Image.Resampling.LANCZOS)
  ```

- **Cropping an image:**
  ```python
  left, top, right, bottom = 100, 100, 400, 400
  im_cropped = im.crop((left, top, right, bottom))
  ```

- **Thumbnail (resize while preserving aspect ratio):**
  ```python
  im.thumbnail((width, height))
  ```

### 4. **Rotating and Flipping:**

- **Rotating an image:**
  ```python
  im_rotated = im.rotate(90)  # Rotate 90 degrees
  ```

- **Flipping an image horizontally:**
  ```python
  im_flipped = im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
  ```

- **Flipping an image vertically:**
  ```python
  im_flipped = im.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
  ```

### 5. **Transformations:**

- **Affine transformation (e.g., skewing, rotating with a custom matrix):**
  ```python
  from PIL import Image
  matrix = [1, 0, 0, 0, 1, 0]  # Example matrix for affine transformation
  im_transformed = im.transform(im.size, Image.AFFINE, matrix)
  ```

### 6. **Filtering:**

Pillow provides several built-in filters to apply to an image.

- **Apply a blur filter:**
  ```python
  from PIL import ImageFilter
  im_blurred = im.filter(ImageFilter.BLUR)
  ```

- **Apply a sharpen filter:**
  ```python
  im_sharpened = im.filter(ImageFilter.SHARPEN)
  ```

- **Gaussian Blur:**
  ```python
  im_gaussian_blurred = im.filter(ImageFilter.GaussianBlur(radius=2))
  ```

### 7. **Image Enhancements:**

- **Enhance the brightness of an image:**
  ```python
  from PIL import ImageEnhance
  enhancer = ImageEnhance.Brightness(im)
  im_brightened = enhancer.enhance(1.5)  # 1.0 means no change
  ```

- **Enhance the contrast of an image:**
  ```python
  enhancer = ImageEnhance.Contrast(im)
  im_contrasted = enhancer.enhance(2.0)  # 1.0 means no change
  ```

- **Enhance the sharpness of an image:**
  ```python
  enhancer = ImageEnhance.Sharpness(im)
  im_sharpened = enhancer.enhance(2.0)  # 1.0 means no change
  ```

- **Enhance color:**
  ```python
  enhancer = ImageEnhance.Color(im)
  im_colored = enhancer.enhance(1.5)  # 1.0 means no change
  ```

### 8. **Working with Transparency and Alpha Channel:**

- **Adding transparency (alpha channel):**
  ```python
  im_with_alpha = im.convert("RGBA")  # Convert image to RGBA (with alpha channel)
  ```

- **Set transparency:**
  ```python
  im_with_alpha.putalpha(128)  # Set alpha (transparency) to 128
  ```

### 9. **Drawing on Images:**

- **Create a drawing context:**
  ```python
  from PIL import ImageDraw
  draw = ImageDraw.Draw(im)
  ```

- **Draw text:**
  ```python
  from PIL import ImageFont
  font = ImageFont.truetype("arial.ttf", 30)  # Choose font and size
  draw.text((x, y), "Hello, World!", font=font, fill="black")
  ```

- **Draw shapes (e.g., rectangles, ellipses):**
  ```python
  draw.rectangle([x1, y1, x2, y2], outline="black", width=3)
  draw.ellipse([x1, y1, x2, y2], outline="red", width=3)
  ```

### 10. **Working with Image Formats:**

- **Convert between different formats:**
  ```python
  im_png = im.convert('PNG')  # Convert to PNG format
  ```

- **Get EXIF data from images (for metadata like orientation):**
  ```python
  exif_data = im._getexif()
  ```

### 11. **Merging and Combining Images:**

- **Paste one image onto another:**
  ```python
  im.paste(im2, (x, y))  # Paste im2 onto im at coordinates (x, y)
  ```

- **Composite images (blending images together):**
  ```python
  from PIL import ImageChops
  im_composite = ImageChops.multiply(im, im2)  # Blend images
  ```

### 12. **Color Manipulation:**

- **Convert image to grayscale:**
  ```python
  im_gray = im.convert('L')  # Convert to grayscale
  ```

- **Convert image to RGB:**
  ```python
  im_rgb = im.convert('RGB')  # Convert to RGB
  ```

- **Get histogram of an image:**
  ```python
  histogram = im.histogram()
  ```

### 13. **Image Compression and Quality Control:**

- **Adjust quality during saving (JPEG, PNG):**
  ```python
  im.save('compressed.jpg', quality=80)  # JPEG with lower quality
  ```

- **Save PNG with compression level:**
  ```python
  im.save('compressed.png', compress_level=9)  # Compress PNG with max compression
  ```

### 14. **Advanced Image Manipulation:**

- **Image Masking:**
  ```python
  mask = Image.new('L', (width, height), 0)
  im_masked = Image.composite(im, im2, mask)
  ```

- **Apply a convolution filter:**
  ```python
  kernel = [
      [-1, -1, -1],
      [-1,  8, -1],
      [-1, -1, -1]
  ]
  im_filtered = im.filter(ImageFilter.Kernel((3, 3), kernel))
  ```

---

These are just some of the tools available in Pillow to manipulate and process images. Pillow offers powerful functionality for handling image operations in Python, whether you are resizing, cropping, drawing, or working with transparency.

Let me know if you need help with specific functions or how to implement any of these features!
