from django.shortcuts import render

# @csrf_exempt
# Create your views here.
def todolist(request):
    if request.method == 'GET':
        todolists = Todolist.objects.all()
        serializer = TodolistSerializer(todolist)
        return JsonResponse(serializer.data, safe=False)
