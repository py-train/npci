from django.shortcuts import render
from django.http import HttpResponse

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


def myview(request):
    # return HttpResponse(html_response)
    return render(request, 'hello.html')

def byeview(request):
    return HttpResponse(bye_response)
