import json
from django.http import HttpResponse


def cross_origin(func):
    def cross_origin_decorator(request):
        response = func(request)
        if isinstance(response, HttpResponse):
            response['Access-Control-Allow-Origin'] = '*'
            if request.method == 'OPTIONS':
                response['Access-Control-Allow-Headers'] = 'x-session-user'
                response['Access-Control-Allow-Methods'] = 'GET, POST, DELETE'
        return response

    return cross_origin_decorator


def returns_http_query(func):
    def returns_json_decorator(request):
        response = func(request)
        if isinstance(response, HttpResponse):
            response['Content-Type'] = 'application/json; charset=utf-8'
        else:
            response = HttpResponse(response)
            response['Content-Type'] = 'application/json; charset=utf-8'
        return response

    return returns_json_decorator
