from django.shortcuts import render, redirect
from .models import Let
from .forms import LetForm
# Create your views here.

def flights(request):
    if request.method == 'POST':
        form = LetForm(request.POST, request.FILES)
        if form.is_valid():
            let = form.save(commit=False)
            let.kreator = request.user
            fotografija = form.cleaned_data['fotografija']
            let.save()
            return redirect("flights")
    queryset = Let.objects.filter(kreator=request.user, aerodromPoletuva='Skopje').all()
    context = {'flights': queryset, 'form': LetForm}
    return render(request,"flights.html", context=context)

def index(request):
    return render(request, "index.html")