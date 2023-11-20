from django.http.response import HttpResponse
from django.shortcuts import render
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    inputus = request.POST.get('q')
    if inputus in util.list_entries():
        return render(request, "encyclopedia/entry.html",{
            "TITLE":inputus,
            "ENTRYPAGE":markdown2.markdown(util.get_entry(inputus)),
        })
    else: 
        
        return render(request,"encyclopedia/searchresult.html")


def titentry(request, TITLE):
    if (util.get_entry(TITLE)== None):
        return render(request, "encyclopedia/error.html")
    else:
        return render(request, "encyclopedia/entry.html",{
            "TITLE":TITLE,
            "ENTRYPAGE":markdown2.markdown(util.get_entry(TITLE)),
        })
