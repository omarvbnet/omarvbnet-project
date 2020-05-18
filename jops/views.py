from django.shortcuts import render, get_object_or_404
from .models import Job

def home(req):
   
	return render(req, 'jobs/home.html', {'jobs':Job.objects})
def jobdetail(req, job_id):

	detailjob1 = get_object_or_404(Job, pk=job_id)
	return render(req, 'jobs/detail.html', {'job':detailjob1})		