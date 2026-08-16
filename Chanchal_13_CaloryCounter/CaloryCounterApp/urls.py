from django.urls import path
from CaloryCounterApp.views import *
from CaloryCounterApp.calorie_views import *

urlpatterns = [
    path('', home_view, name='home_view'),
    path('register/', register_view, name='register_view'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),

    path('profile/', profile_view, name='profile_view'),
    path('update_profile/', update_profile, name='update_profile'),


    path('calorie_list/', calorie_list, name='calorie_list'),
    path('add_calorie/', add_calorie, name='add_calorie'),
    path('edit_calorie/<int:c_id>/', edit_calorie, name='edit_calorie'),
    path('delete_calorie/<int:c_id>/', delete_calorie, name='delete_calorie'),

    path('dashboard_view>/', dashboard_view, name='dashboard_view'),
]