#Image Conversion form JFL IT Lab
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageUploadForm
from .utils import crop_and_compress_image
from .models import ConvertedImage

def image_convert_view(request):
    if request.method == 'POST' and 'image' in request.FILES:
        image = request.FILES['image']
        
        # Compress and crop the uploaded image
        converted_image = crop_and_compress_image(image, target_size_kb=500)
        
        # Save only the converted image to the database (not the original)
        converted_image_instance = ConvertedImage.objects.create(
            converted_image=converted_image
        )
        
        # Provide feedback to the user and allow them to view/download the converted image
        return render(request, 'image_resize/upload.html', {
            'message': 'Converted image successfully saved!',
            'converted_image_url': converted_image_instance.converted_image.url
        })
    
    return render(request, 'image_resize/upload.html')


