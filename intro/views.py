from django.shortcuts import render

# Create your views here.
def Latte_intro(request):
	return render(request, 'intro/Latte_intro.html')

def Raon_intro(request):
	return render(request, 'intro/Raon_intro.html')

def Tag_intro(request):
	return render(request, 'intro/Tag_intro.html')

def Core_intro(request):
	return render(request, 'intro/Core_intro.html')

def club_intro(request):
	return render(request, 'intro/club_intro.html')