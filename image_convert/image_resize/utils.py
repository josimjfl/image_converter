from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

def crop_and_compress_image(image, target_size_kb=500, target_width=500, target_height=500):
    im = Image.open(image)
    im = im.convert('RGB')  # Convert to RGB if it's not
    
    # Get the current dimensions of the image
    width, height = im.size
    
    # Determine the crop box based on the width and height comparison
    if width > height:
        # If width is larger, keep the full height and crop the excess width
        left = (width - height) // 2
        top = 0
        right = left + height
        bottom = height
    else:
        # If height is larger, keep the full width and crop the excess height
        top = (height - width) // 2
        left = 0
        right = width
        bottom = top + width
    
    # Crop the image to the center based on the width/height comparison
    im = im.crop((left, top, right, bottom))
    
    # Resize the image to 500x500 while keeping the aspect ratio
    im = im.resize((target_width, target_height), Image.Resampling.LANCZOS)
    
    # Compress the image to reduce its file size
    quality = 90
    output = BytesIO()
    
    # Keep reducing quality until the image size is below the target size
    while True:
        output.seek(0)
        im.save(output, format='JPEG', quality=quality)
        
        # Check the size of the image (in bytes)
        image_size_kb = len(output.getvalue()) / 1024  # Convert bytes to KB
        
        # If the image size is less than or equal to the target size, break the loop
        if image_size_kb <= target_size_kb:
            break
        
        # Reduce quality for the next iteration
        quality -= 5
        if quality < 10:  # Set a lower limit for quality
            break
    
    output.seek(0)
    
    # Return the compressed image as InMemoryUploadedFile
    return InMemoryUploadedFile(
        output, 'ImageField', image.name, 'image/jpeg', len(output.getvalue()), None
    )
