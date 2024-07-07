from django.shortcuts import render
from .forms import TextForm
from .utils import classify_text
from .models import Transaction

def classify_text_view(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            prediction = classify_text(text)
            # Save to the database
            Transaction.objects.create(text=text, prediction=prediction)
            return render(request, 'classifier/result.html', {'text': text, 'prediction': prediction})
    else:
        form = TextForm()
    
    return render(request, 'classifier/classify.html', {'form': form})
