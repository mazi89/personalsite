from django.shortcuts import render

def display_html(request):
        return render(request, 'loan_calc/base.html')