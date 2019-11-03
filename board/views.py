from django.shortcuts import render

def board(request):
    return render(request, 'board.html')

def write(request):
    return render(request, 'write.html')
