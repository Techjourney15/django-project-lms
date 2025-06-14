from django.shortcuts import render

# Create your views here.
def home (request):
    """
    Render the home page of the LMS application.
    
    Args:
        request: The HTTP request object.
        
    Returns:
        HttpResponse: Rendered home page template.
    """
    return render(request, 'home.html') 