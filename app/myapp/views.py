from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

def index(req):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Our service is very quick'
    feature1.is_true = True

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.details = 'Our service is very reliable'
    feature2.is_true = True

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Easy to use'
    feature3.details = 'Our service is easy to use'
    feature3.is_true = True

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'False'
    feature4.details = 'Our service is very False'
    feature4.is_true = False

    feature5 = Feature()
    feature5.id = 4
    feature5.name = 'True'
    feature5.details = 'Our service is very true'
    feature5.is_true = True

    features = [feature1, feature2, feature3, feature4, feature5]

    return render(req, 'index.html', {
        'features': features
    })

def counter(req):
    text = req.POST['text']
    amount_words = len(text.split(' '))
    return render(req, 'counter.html', {'text': text, 'amount': amount_words})
