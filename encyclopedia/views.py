from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse, HttpResponseBadRequest
from django.urls import reverse
from . import util
import markdown
import random
from django import forms


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def article(request, title):
    content = util.get_entry(title)
    if content == None:
        return HttpResponseNotFound()
    else:
        return render(request, "encyclopedia/article.html", {
            "title": title,
            "articleContent": markdown.markdown(content)
        })

def randompage(request):
    title = random.choice(util.list_entries())
    name = reverse("encyclopedia:article", args=[title])
    return HttpResponseRedirect(name)

def search(request):   
    q = request.GET.get("q")
    if len(q) == 0 or q.isspace() == True:
        return HttpResponseRedirect(reverse("encyclopedia:index"))
    query = q.strip().upper()
    list_articles = util.list_entries()    
    for item in list_articles:       
        if query == item.upper():
            return HttpResponseRedirect(reverse("encyclopedia:article", args=[query]))
    results = []
    for item in list_articles:
        if item.upper().find(query) != -1:
            results.append(item)
    return render(request, "encyclopedia/search.html", {
        "results": results
    })

class NewArticleForm(forms.Form):
    NewArticleTitle = forms.CharField(label = "Title", widget = forms.TextInput(attrs={'class': 'titleart', 'name':'title'}))
    NewArticleContent = forms.CharField(label = "Content", widget = forms.Textarea(attrs={'name':'content'}))

def crnewpage(request):
    if request.method == "POST":
        form = NewArticleForm(request.POST)
        if form.is_valid():
            NewArticleTitle = form.cleaned_data["NewArticleTitle"]
            NewArticleContent = '#'+ NewArticleTitle + '\n' + form.cleaned_data["NewArticleContent"]            
            q = request.POST.get("exist") 
            list_entries = util.list_entries()
            for entry in list_entries:
                if NewArticleTitle.upper() == entry.upper() and q == "forbid":
                    return render(request, "encyclopedia/crnewpage.html", {
                        "exist": True
                        })
            oldtitle = request.POST.get("oldtitle")
            if oldtitle and NewArticleTitle.upper() != oldtitle.upper():
                for entry in list_entries:
                    if NewArticleTitle.upper() == entry.upper():
                        return render(request, "encyclopedia/crnewpage.html", {
                            "exist": True
                            })
                util.delete(oldtitle)
            util.save_entry(NewArticleTitle, NewArticleContent)
            return HttpResponseRedirect(reverse("encyclopedia:article", args=[NewArticleTitle]))
        else:
            return render(request, "encyclopedia/crnewpage.html", {
        "form": form
        })

    return render(request, "encyclopedia/crnewpage.html", {
        "form": NewArticleForm()
        })

def editarticle(request):
    if request.method == "POST":
        form = NewArticleForm()
        title = request.POST.get("title")
        form['NewArticleTitle'].initial = title
        text = util.get_entry(title)
        Split = text.split("\n", 1)
        NewArticleContent = Split[1]
        form['NewArticleContent'].initial = NewArticleContent
        return render(request, "encyclopedia/edit.html", {
                "form": form,
                "title": title
            })
