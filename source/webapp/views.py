from django.shortcuts import render


# Create your views here.

def math(request):
    if request.method == 'GET':
        return render(request, 'math.html')
    else:
        x = int(request.POST.get('x'))
        y = int(request.POST.get('y'))
        value = request.POST.get('name')

        if value == 'Add':
            result = x + y
        elif value == 'Subtract':
            result = x - y
        elif value == 'Multiply':
            result = x * y
        elif value == 'Divide':
            if y == 0:
                result = 'ZeroDivisionError'
            else:
                result = x / y

        context = {
            'x': x,
            'y': y,
            'value': value,
            'result': result,
        }
        return render(request, 'math.html', context)
