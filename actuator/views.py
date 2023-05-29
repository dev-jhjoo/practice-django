from django.http import JsonResponse, HttpResponse


# Create your views here.
def healthcheck(request, status='200'):
    if int(status) == 200:
        return JsonResponse({'result_code': 0, 'result_message': 'ok'}, status=int(status))
    else:
        return JsonResponse({'result_code': 9999, 'result_message': 'error'}, status=int(status))
