from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def starting_screen(request):

    data = [
        {
            "class": 0,
            "x": 0.422419,
            "y": 0.311986,
            "width": 0.022602,
            "height": 0.052879
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
