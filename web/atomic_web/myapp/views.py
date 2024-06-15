from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def starting_screen(request):

    data = [
        {
        "class": 0,
        "x": 0.255956,
        "y": 0.065217,
        "width": 0.032987,
        "height": 0.041128
    },
    {
        "class": 0,
        "x": 0.282529,
        "y": 0.112221,
        "width": 0.032376,
        "height": 0.045828
    },
    {
        "class": 0,
        "x": 0.386683,
        "y": 0.149236,
        "width": 0.035431,
        "height": 0.077556
    },
    {
        "class": 0,
        "x": 0.385461,
        "y": 0.476498,
        "width": 0.017104,
        "height": 0.041128
    },
    {
        "class": 0,
        "x": 0.603238,
        "y": 0.556404,
        "width": 0.021381,
        "height": 0.048179
    },
    {
        "class": 0,
        "x": 0.35675,
        "y": 0.053467,
        "width": 0.013439,
        "height": 0.029377
    },
    {
        "class": 0,
        "x": 0.384239,
        "y": 0.057579,
        "width": 0.018326,
        "height": 0.028202
    },
    {
        "class": 0,
        "x": 0.222358,
        "y": 0.013514,
        "width": 0.018326,
        "height": 0.024677
    },
    {
        "class": 0,
        "x": 0.41631,
        "y": 0.819624,
        "width": 0.018937,
        "height": 0.043478
    },
    {
        "class": 0,
        "x": 0.410812,
        "y": 0.972385,
        "width": 0.01405,
        "height": 0.031727
    },
    {
        "class": 0,
        "x": 0.799633,
        "y": 0.323149,
        "width": 0.02077,
        "height": 0.103408
    }
    ]

    if request.method == 'POST' and request.FILES.get('photo'):
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        uploaded_file_url = fs.url(filename)
        
        #тут сделаем обработку


        context = {
            'uploaded_file_url': uploaded_file_url,
            'data': data,
        }
        return render(request, 'starting_screen.html', context)
    
    context = {
        'uploaded_file_url': '',
        'data': data,
    }

    return render(request, 'starting_screen.html', context)# Create your views here.
