from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Emp
from django.core import serializers

import logging

logger = logging.getLogger(__name__)

response = '''
<html>
<body>
<h1>Hello World!</h1>
</body>
</html>
'''

emp_data = [
    {
        'name': 'Ramesh',
        'empid': 1
    },
    {
        'name': 'Suresh',
        'empid': 2
    },

]

# Create your views here.
def test(request):
    # return HttpResponse(response)
    # return render(request, 'test1.html')
    return JsonResponse({'hello': 'world'})

def emp_search(request):
    print("--",request.method,"--")
    if request.method == 'GET':
        params = request.GET
        name = params.get('name')
        # data = [*Emp.objects.filter(name__icontains=name).values()]
        # data = Emp.objects.filter(name__icontains=name)
        # return render(request, 'empresult.html', {'data': data})

        # format = 'json'
        format = params.get('format', 'json')
        data = serializers.serialize(format, Emp.objects.all())

        # return JsonResponse(data, safe=False)
        return HttpResponse(data, content_type=f'application/{format}')

        # return render(
        #     request,
        #     'empresult.html', 
        #     {'data': [e for e in Emp.objects.all().values()]})

        # return JsonResponse([*Emp.objects.all()], safe=False)
        # return render(request, 'empform.html')
    elif request.method == 'POST':
        data = request.POST 
        print(data)
        if 'name' in data and 'id' in data:
            name = data.get('name')
            id = int(data.get('id'))
            print(name, id)
            emp = Emp(id=id, name=name)
            Emp.save(emp)
            return JsonResponse([e for e in Emp.objects.all().values()], safe=False)
            # return JsonResponse([*Emp.objects.all().values()], safe=False)

            # return JsonResponse([*Emp.objects.all()], safe=False)
            # return render(request, 'postsuccess.html',
            #             {'name': name, 'id': id}
            # )
        else:
            return render(request, 'postfailure.html')


def myview(request):
    if request.method == 'GET':
        return myview_get(request)
    elif request.method == 'POST':
        ...
    elif request.method == 'PUT':
        ...
    elif request.method == 'DELETE':
        ...

def myview_get(request):
    ...


def table(request):
    return render(request, 'table.html')