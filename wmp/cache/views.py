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
	if key == None :
		return ''
	import redis
	db = redis.StrictRedis('wmp-redis', 6379, charset="utf-8", decode_responses=True)
	if not db.exists(key): #does the hash exist?
		return ''
	data = db.get(key)
	return data
	# # import urllib3
	# # import os
	# # http = urllib3.PoolManager()
	# # return os.getenv('CACHE_SERVER_URL', 'test')
	# # import os
	# # # retun case_url
	# cacheurl = os.getenv('CACHE_SERVER_URL', 'test')
	# url = '%s/%s' % (cacheurl,key)
	# # return url
	# # # url = '%s/%s' % ('http://127.0.0.1:8001',key)
	# # # 'CACHE_SERVER_URL'
	# # # print (url)
	# r = http.request('GET',url )
	# if r.status == 200:
	# 	return r.data.decode("utf-8")
	# else:
	# 	return ''