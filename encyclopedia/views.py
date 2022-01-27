from django.http.response import HttpResponse
from django.shortcuts import render
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def titentry(request, TITLE):
    entrypage = util.get_entry(TITLE)
    newentrypage = markdown2.markdown(entrypage)
    return render(request, "encyclopedia/entry.html",{
        "TITLE":TITLE,
        "ENTRYPAGE":newentrypage
    })