from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def exercise(request):

    e = { '子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥' }
    f = []
    f.append('りんご')
    f.append('みかん')
    f.append('バナナ')

    return render(request, 'exercise.html', { 'eto':e, 'fruits':f } )
