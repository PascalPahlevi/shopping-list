from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Muhamad Pascal Alfin Pahlevi',
        'class': 'PBP Kelas International'
    }

    return render(request, 'main.html', context)