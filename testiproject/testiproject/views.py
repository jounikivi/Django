from django.http import HttpResponse
import random

def home(request):
    name ='jouni' # HARD CODE
    number = random.randint(1, 99999) # RANDOM


    #DATABASE

    
    H1_STRING = f"""
    <h1>hello {name} - {number}</h1>
    """

    P_STRING = f"""
    <p>hello {name} - {number}</p>
    """
    HTML_STRING = H1_STRING + P_STRING
    return HttpResponse(HTML_STRING)