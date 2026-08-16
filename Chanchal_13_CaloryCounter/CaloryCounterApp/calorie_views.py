from datetime import date
from django.db.models.aggregates import Sum
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from CaloryCounterApp.forms import *

# Create your views here.


@login_required
def calorie_list(request):

    data = consumedColorieModel.objects.filter(user=request.user).order_by('-created_at')

    context = {
        'data' : data,
    }

    return render(request, 'calorie_list.html', context)


@login_required
def add_calorie(request):

    form_data = calorieConsumedForm()

    if request.method == 'POST':
        form_data = calorieConsumedForm(request.POST)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('calorie_list')

    context = {
        'form': form_data,
        'title': 'Add Consumed Calorie',
        'btn': 'Add Calorie'
    }

    return render(request, 'base_form.html', context)


@login_required
def edit_calorie(request, c_id):

    data = consumedColorieModel.objects.get(id=c_id)

    form_data = calorieConsumedForm(instance=data)

    if request.method == 'POST':
        form_data = calorieConsumedForm(request.POST, instance=data)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('calorie_list')

    context = {
        'form': form_data,
        'title': 'Edit Consumed Calorie',
        'btn': 'Update Calorie'
    }

    return render(request, 'base_form.html', context)


@login_required
def delete_calorie(request, c_id):

    consumedColorieModel.objects.get(id=c_id).delete()

    return redirect('calorie_list')


@login_required
def dashboard_view(request):

    try:
        required_calorie = profileModel.objects.get(user=request.user).bmr
    except profileModel.DoesNotExist:
        return redirect('profile_update')

    today_consumed = consumedColorieModel.objects.filter(
        user=request.user,
        created_at=date.today()
    )

    total_consumed = today_consumed.aggregate(total=Sum('calorie'))

    total_calory = round(total_consumed['total'] or 0.00, 2)

    if total_calory < required_calorie:
        suggestion = 'You consumed less calorie today, eat more!'
    else:
        suggestion = 'You consumed more calorie today, eat less!'

    context = {
        'required_calorie' : required_calorie,
        'total_consumed' : total_calory,
        'less_more' : round(total_calory - required_calorie, 2),
        'today_consumed' : today_consumed,
        'suggestion' : suggestion,
    }

    return render(request, 'dashboard.html', context)