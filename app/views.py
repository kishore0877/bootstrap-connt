from django.shortcuts import render
def bootstrap_cdn(request):
    return render(request,'bootstrap_cdn.html')
def conn(request):
    return render(request,'conn.html')