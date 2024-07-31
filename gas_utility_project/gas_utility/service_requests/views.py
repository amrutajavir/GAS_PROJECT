from django.shortcuts import render, redirect
from .forms import ServiceRequestForm

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Ensure there's an 'index' view defined
        else:
            return render(request, 'service_requests/submit_request.html', {'form': form})
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/submit_request.html', {'form': form})

def index(request):
    
    return render(request, 'service_requests/index.html')
