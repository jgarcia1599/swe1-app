from django.http import HttpResponse

def index(request):
    return HttpResponse("""
        <h1>Welcome to My Django App</h1>
        <ul>
            <li><a href="/admin/">Admin Interface</a></li>
            <li><a href="/polls/">Polls Application</a></li>
        </ul>
    """) 