# i have created this
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext =(request.POST.get('text', 'default'))
    removepunc = request.POST.get("removepunc", 'off')
    fullcaps = request.POST.get("fullcaps", 'off')
    newlineremover = request.POST.get("newlineremover", 'off')
    extraspaceremover = request.POST.get("extraspaceremover", 'off')



    if removepunc == "on":
        punctuations = '''!()-{}[];:"'/<+>\,.?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'analyzed_text': analyzed, 'purpose': 'remove punctuation'}
        djtext = analyzed

    if fullcaps == "on":
        analyzed=""
        for char in djtext:
            analyzed += char.upper()
        params = {'analyzed_text': analyzed, 'purpose': 'UPPERCASE'}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ''
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            else:
                analyzed += ' '
        params = {'analyzed_text': analyzed, 'purpose': 'Removed new lines'}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for i in range(len(djtext)):
            if not(djtext[i] == ' ' and djtext[i+1] == ' '):
                analyzed += djtext[i]
        params = {'analyzed_text': analyzed, 'purpose': 'extra space remover'}
        djtext = analyzed
    if(removepunc != "on" and extraspaceremover != "on" and newlineremover != "on" and fullcaps != "on"):
        params = {'analyzed_text': djtext, 'purpose': 'charcount'}

    return render(request, 'analyze.html', params)




