#   meetings/views.py
#   Patrick W. Montgomery
#   created: 9/19/2016

#   import statements
from django.shortcuts import render
from django.utils import timezone
from .models import Minutes

#   function for returning the rendered view of the meetings index page
def meetings_index(request):
    meeting_minutes = Minutes.objects.all().order_by('meeting_date')
    return render(request, 'meetings/meetings_index.html', {'meeting_minutes': meeting_minutes})