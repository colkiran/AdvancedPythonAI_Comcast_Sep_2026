
from django.views import View
from django.http import JsonResponse

class JsonResponseMixin:

    def render_to_json(self, data):
        return JsonResponse(data)


class Myview(JsonResponseMixin, View):

    def get(self, request):
        data = {"message": "hello world"}
        return self.render_to_json(data)
