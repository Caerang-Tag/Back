from django.shortcuts import render

# Create your views here.
def main(request):
	return render(request, 'main/main.html') #templates/main/main.html을 리턴해서 화면에 출력
