from django.urls import path, include

from employees import views

app_name = 'employee'

urlpatterns = [
    path('accounts/login/', views.EmplLoginView.as_view(), name='login'),
    path('accounts/logout/', views.EmplLogoutView.as_view(), name='logout'),
    path('positions/delete/<int:pk>', views.PositionDelete.as_view(), name='positions_delete'),
    path('positions/update/<int:pk>', views.PositionUpdate.as_view(), name='positions_update'),
    path('positions/create/', views.PositionCreate.as_view(), name='positions_create'),
    path('positions/', views.PositionList.as_view(), name='positions'),
    path('subdivisions/delete/<int:pk>', views.SubdivisionDelete.as_view(), name='subdivisions_delete'),
    path('subdivisions/update/<int:pk>', views.SubdivisionUpdate.as_view(), name='subdivisions_update'),
    path('subdivisions/create/', views.SubdivisionCreate.as_view(), name='subdivisions_create'),
    path('subdivisions/', views.SubdivisionList.as_view(), name='subdivisions'),
    path('users/create/', views.UserCreate.as_view(), name='user_create'),
    path('users/', views.UsersList.as_view(), name='users'),
    path('emplooyees/delete/<int:pk>', views.EmployeeDelete.as_view(), name='employee_delete'),
    path('emplooyees/update/<int:pk>', views.EmployeeUpdate.as_view(), name='employee_update'),
    path('emplooyees/detail/<int:pk>', views.EmployeeDetail.as_view(), name='employee_detail'),
    path('emplooyees/create/', views.EmployeeCreate.as_view(), name='employee_create'),
    path('employees/', views.EmployeeList.as_view(), name='employees'),
    path('', views.main_page, name='main'),
]
