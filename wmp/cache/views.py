from django.shortcuts import render
from django.conf import settings

# Create your views here.
def getcache(request,key=''):
	# query = SerialNumber.objects.filter(current_operation__slug = slug)
	# print (query)
	query = request.GET.get('q')
	data = get_cache(query)
	
	return render(request, 'cache/cache.html', {'key':query,'value':data})


def get_cache(key):
	import urllib3
	http = urllib3.PoolManager()
	url = '%s/%s' % (settings.CACHE_URL,key)
	print (url)
	r = http.request('GET',url )
	if r.status == 200:
		return r.data.decode("utf-8")
	else:
		return ''