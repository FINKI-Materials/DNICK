from django.shortcuts import render, redirect
from .models import Event, Band, BandEvent
from .forms import EventForm
# Create your views here.

def index(request):
    queryset = Event.objects.filter(kreator=request.user)
    context = {'events' : queryset}
    return render(request,"index.html", context=context)

def addEvent(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            field1 = form.cleaned_data['field1']
            field2 = form.cleaned_data['field2']
            field3 = form.cleaned_data['field3']
            field4 = form.cleaned_data['field4']
            bandsNames = field2.split(',')
            event = Event()
            event.kreator = request.user
            event.ime = field1
            event_name = 'Example Event'  # Replace with actual event name
            event_date = '2023-06-01'  # Replace with actual event date
            event_poster = None  # Replace with actual event poster
            event_creator = request.user  # Assuming the logged-in user is the creator
            event_is_outdoor = False  # Replace with actual value
            event, created = Event.objects.get_or_create(
                ime=event.ime,
                defaults={
                    'vremeOdrzuvanje': event_date,
                    'poster': event_poster,
                    'kreator': event_creator,
                    'daliENaOtvoreno': event_is_outdoor,
                }
            )
            bands = []
            for name in bandsNames:
                band, created = Band.objects.get_or_create(ime=name)
                bandEvent = BandEvent.objects.get_or_create(event=event, band=band)
                bands.append(band)

            return redirect("index")
    form = EventForm()
    context = {'form': form}
    return render(request, "masterAdd.html", context=context)