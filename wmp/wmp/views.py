from django.shortcuts import render

from operation.models import Operation

def home(request):
	return render(request, 'home.html', {})

# def wip(request):
# 	query = Operation.objects.filter(status='A')
# 	return render(request, 'reports/wip.html', {'object_list':query})


