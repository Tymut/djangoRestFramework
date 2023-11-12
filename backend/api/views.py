from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    print(request.GET)
    body = request.body
    data = {}
    try:
       data = json.loads(body)
    except:
        pass
    print(data.keys())
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
