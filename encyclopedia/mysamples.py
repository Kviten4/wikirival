"""
def search(request):   
    query = request.POST.get("q")
    query_list = [query.strip(), query.capitalize().strip() , query.upper().strip()]
    list_articles = util.list_entries()
    results = []
    for query_item in query_list:       
        if query_item in list_articles:
            name = reverse("encyclopedia:article", args=[query])
            return HttpResponseRedirect(name)
        else:
            for article in list_articles:
                if article.find(query_item) != -1:
                    results.append(article)
    results = list(set(results))
    return render(request, "encyclopedia/search.html", {
        "results": results
    })
"""
"""
def search(request):   
    query = request.GET.get("q")
    query_list = [query.strip(), query.capitalize().strip() , query.upper().strip()]
    list_articles = util.list_entries()
    results = []
    for query_item in query_list:       
        if query_item in list_articles:
            name = reverse("encyclopedia:article", args=[query])
            return HttpResponseRedirect(name)
        else:
            for article in list_articles:
                if article.find(query_item) != -1:
                    results.append(article)
    results = list(set(results))
    return render(request, "encyclopedia/search.html", {
        "results": results
    })
"""
"""
def search(request):   
    q = request.POST.get("q")
    query = q.upper().strip()
    list_articles = util.list_entries()
    try:
        for item in list_articles:   
            if query == item.upper():
                return HttpResponseRedirect(reverse("encyclopedia:article", args=[query]))
    except:
        results = []
        for item in list_articles:
            itemlower = item.upper()
            if itemlower.find(query) != -1:
                results.append(item)
        results = list(set(results))
        return render(request, "encyclopedia/search.html", {
            "results": results
        })
"""

def search(request):   
    query = request.POST.get("q")
    list_articles = util.list_entries()
    results = []
    for art_item in list_articles:   
        if query.lower() in art_item.lower():
            return HttpResponseRedirect(reverse("encyclopedia:article", args=[query]))
        else:
            for art_item in list_articles:
                low = art_item.lower()
                if low.find(query.lower()) != -1:
                    results.append(art_item)
            results = list(set(results))
            return render(request, "encyclopedia/search.html", {
                "results": results
            })

def search(request):   
    query = request.POST.get("q")
    list_articles = util.list_entries()
    results = []
    for art_item in list_articles:   
        if query.lower() == art_item.lower():
            return HttpResponseRedirect(reverse("encyclopedia:article", args=[query]))

    for art_item in list_articles:
        low = art_item.lower()
        if low.find(query.lower()) != -1:
            results.append(art_item)
    results = list(set(results))
    return render(request, "encyclopedia/search.html", {
    "results": results
    })


def search(request):   
    q = request.GET.get("q")
    query = q.upper().strip()
    list_articles = util.list_entries()
    results = []
    for item in list_articles:       
        if query == item.upper():
            return HttpResponseRedirect(reverse("encyclopedia:article", args=[query]))
        else:
            for item in list_articles:
                if item.upper().find(query) != -1:
                    results.append(item)
    results = list(set(results))
    return render(request, "encyclopedia/search.html", {
        "results": results
    })

def search(request):   
    q = request.GET.get("q")
    query = q.upper().strip()
    list_articles = util.list_entries()    
    for item in list_articles:       
        if query == item.upper():
            return HttpResponseRedirect(reverse("encyclopedia:article", args=[query]))
    results = []
    for item in list_articles:
        if item.upper().find(query) != -1:
            results.append(item)
    results = list(set(results))
    return render(request, "encyclopedia/search.html", {
        "results": results
    })

