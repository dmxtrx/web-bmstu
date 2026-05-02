from django.shortcuts import render, redirect

def index(request):
    context = {'full_name': 'Барсиков Окак Котович', 'group': 'АК2-61'}
    return render(request, 'schedule/index.html', context)

def update_schedule(request):
    if request.method == 'POST':
        day = request.POST.get('day')
        paras = request.POST.getlist('para')
        subject = request.POST.get('subject')
        lesson_type = request.POST.get('lesson_type')

        print(f'day {day}')
        print(f'paras {paras}')
        print(f'subject {subject}')
        print(f'lesson_type {lesson_type}')
        return redirect('schedule')
    return redirect('schedule')

def home(request):
    context = {'full_name': 'Барсиков Окак Котович','group': 'АК2-61'}
    return render(request, 'schedule/fio.html', context)
