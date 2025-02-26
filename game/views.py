from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import random

def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
    return render(request, 'game.html')

def guess(request):
    guess = int(request.GET.get('guess', 0))
    number = request.session['number']
    if guess < number:
        return JsonResponse({'message': 'Too low! Try again.'})
    elif guess > number:
        return JsonResponse({'message': 'Too high! Try again.'})
    else:
        request.session['number'] = random.randint(1, 100)
        return JsonResponse({'message': 'Congratulations! You guessed it! New number generated.'})

