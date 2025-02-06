from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Greeting
from django.core import serializers

# Create your views here.

html_response = '''
<html>
    <body>
        <h1>Hello Monday Morning  :( !</h1>
    </body>
</html>
'''

bye_response = '''
<html>
    <body>
        <h1>Bye Monday Morning  :( !</h1>
    </body>
</html>
'''

data = [
    {
        'name': 'Ash',
        'greeting': 'Huh?!'
    },
    {
        'name': 'Bash',
        'greeting': 'Beatup!'
    },
    {
        'name': 'Cash',
        'greeting': 'Money!'
    },
]

def myview(request):
    print('------', request.method)
    if request.method == 'GET':
        rdata = request.GET
        name = rdata.get('name')
        # return HttpResponse(html_response)
        
        # return render(
        #     request, 
        #     'hello.html', 
        #     {'data': Greeting.objects.filter(name=name)})

        # return JsonResponse(list(Greeting.objects.all().values()), safe=False)

        return HttpResponse(serializers.serialize('json', Greeting.objects.all()), content_type='application/json')

    elif request.method == 'POST':
        # return HttpResponse('Posted!')
        print(request.POST)
        pdata = request.POST
        g = Greeting(name=pdata.get('name'), greeting=pdata.get('greeting'))
        Greeting.save(g)
        return render(
            request, 
            'hellopost.html', 
            {'name': pdata.get('name'), 'greeting': pdata.get('greeting')}
        )

def byeview(request):
    return HttpResponse(bye_response)
