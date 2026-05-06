import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .utils import encode_image, decode_image
from django.conf import settings

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y

def index(request):
    context = {'active_tab': request.POST.get('tab', 'steganography')}
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        # Steganography Logic
        if action == 'encode':
            image = request.FILES.get('image')
            message = request.POST.get('message')
            if image and message:
                fs = FileSystemStorage()
                filename = fs.save(image.name, image)
                input_path = fs.path(filename)
                output_filename = 'encoded_' + filename
                output_path = os.path.join(settings.MEDIA_ROOT, output_filename)
                try:
                    actual_output_path = encode_image(input_path, message, output_path)
                    output_filename = os.path.basename(actual_output_path)
                    context['encoded_image_url'] = fs.url(output_filename)
                    context['success'] = "Message encoded successfully!"
                except Exception as e:
                    context['error'] = str(e)
                
        elif action == 'decode':
            image = request.FILES.get('image')
            if image:
                fs = FileSystemStorage()
                filename = fs.save(image.name, image)
                image_path = fs.path(filename)
                try:
                    decoded_message = decode_image(image_path)
                    context['decoded_message'] = decoded_message
                except Exception as e:
                    context['error'] = str(e)

        # Euclidean Logic
        elif action == 'calculate_gcd':
            try:
                a = int(request.POST.get('a'))
                b = int(request.POST.get('b'))
                context['gcd_result'] = gcd(a, b)
                context['input_a'] = a
                context['input_b'] = b
            except ValueError:
                context['error'] = "Please enter valid integers."

        elif action == 'calculate_egcd':
            try:
                a = int(request.POST.get('a'))
                b = int(request.POST.get('b'))
                g, x, y = extended_gcd(a, b)
                context['egcd_result'] = {
                    'gcd': g,
                    'x': x,
                    'y': y,
                    'equation': f"{g} = ({a} * {x}) + ({b} * {y})"
                }
                context['input_a'] = a
                context['input_b'] = b
            except ValueError:
                context['error'] = "Please enter valid integers."
                    
    return render(request, 'steganography/index.html', context)
