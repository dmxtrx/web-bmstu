from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def student(request):
    data = {
        "fio": "Romanov Dmitrii Olegovich",
        "group": "IU6-64B"
    }
    return JsonResponse(data)

@csrf_exempt
def check(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            if body.get("laba") == "delay labu":
                return JsonResponse({}, status=200)
            else:
                return JsonResponse({"error": "Invalid data"}, status=400)
        except:
            return JsonResponse({"error": "Bad request"}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)