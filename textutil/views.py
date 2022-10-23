# I have created this file
from django.shortcuts import render


def index(request):
    params = {'name': "Vedant", "place": "Mars"}
    return render(request, 'index.html', params)


def analyze(request):
    # Get the text
    query = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        # remove punctuations
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in query:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':"Remove Punctuations", 'analyzed_text':analyzed}
        # analyse the text
        # return render(request, "analyze.html",params)
        query = analyzed

    if fullcaps == "on":
        # convert into uppercase
        analyzed = ""
        for char in query:
            analyzed += char.upper()
        params = {'purpose': "Changed to upper", 'analyzed_text': analyzed}
        # return render(request,"analyze.html", params)
        query= analyzed

    if newlineremover =="on" :
        # remover newlines
        analyzed = ""
        for char in query:
            if char != "\n" and char != "\r":
                analyzed += char

        params = {'purpose': "extra space removed", 'analyzed_text': analyzed}
        # return render(request, "analyze.html",params)
        query = analyzed

    if extraspaceremover == 'on':
        # remove extra white spaces
        analyzed = ""
        for index, char in enumerate(query):
            if not (query[index] == " " and query[index + 1] == " "):
                analyzed += char
        params = {'purpose': "extra space removed", 'analyzed_text': analyzed}
        # return render(request, "analyze.html", params)
        query = analyzed

    if charcount =="on":
        # count the number of characters in query
        analyzed = f"the number of characters are: {len(query)}"

        params = {'purpse': "character count is", 'analyzed_text':query + "\n" + analyzed}

    if removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on" and charcount != "on":
        return render(request, "displayerror.html")

    return render(request, "analyze.html", params)


def contact(request):

    return render(request,"contact.html")


def about(request):

    return render(request,"about.html")

