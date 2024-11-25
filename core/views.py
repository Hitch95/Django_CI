from django.http import HttpResponse

# Create your views here.
def hello_world(request):
    html = f'''
    <html>
        <body>
            <h1>Hello World!</h1>
        </body>
    </html>
    '''
    return HttpResponse(html)