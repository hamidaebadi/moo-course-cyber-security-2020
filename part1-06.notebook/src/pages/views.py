from django.shortcuts import render

# Create your views here.

def addPageView(request):
    items = request.session.get('items', [])
    #handling post request
    if request.method == 'POST':
        item = request.POST.get('content', '').strip()
        items.append(item)
        request.session['items'] = items

    if len(items) > 10:
        lst_indx = len(items)-1
        recent_items = []
        for i in range(10):
            recent_items.append(items[lst_indx])
            lst_indx -=1
        items = recent_items
    return render(request, 'pages/index.html', {'items' : items})


def erasePageView(request):
    request.session['items'] = []
    items = []
    return render(request, 'pages/index.html', {'items' : items})


def homePageView(request):
	# use sessions (the data is stored in a database db.sqlite that is then accessed using a cookie)
    items = request.session.get('items', [])
    if len(items) > 10:
        lst_indx = len(items)-1
        recent_items = []
        for i in range(10):
            recent_items.append(items[lst_indx])
            lst_indx -=1
        items = recent_items
	# shorter way of writing instead of loader
    return render(request, 'pages/index.html', {'items' : items})
