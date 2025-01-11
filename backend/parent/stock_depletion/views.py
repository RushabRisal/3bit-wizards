from django.shortcuts import render # type: ignore
from joblib import load # type: ignore
model=load('../ML/savedModels/regression.joblib')
# Create your views here.
def predictor(request):
    return render(request,'index.html')

def formInfo(request):
    first=int(request.GET.get('first'))
    # second=int(request.GET.get('second'))
    y_pred=model.predict([[first]])
    print(y_pred)
    return render(request,'result.html')