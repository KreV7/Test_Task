from django.urls import path, include

from employees import views

app_name = 'employee'

urlpatterns = [
    path('accounts/login/', views.EmplLoginView.as_view(), name='login'),
    path('positions/delete/<int:pk>', views.PositionDelete.as_view(), name='positions_delete'),
    path('positions/update/<int:pk>', views.PositionUpdate.as_view(), name='positions_update'),
    path('positions/create/', views.PositionCreate.as_view(), name='positions_create'),
    path('positions/', views.PositionList.as_view(), name='positions'),
    path('subdivisions/delete/<int:pk>', views.SubdivisionDelete.as_view(), name='subdivisions_delete'),
    path('subdivisions/update/<int:pk>', views.SubdivisionUpdate.as_view(), name='subdivisions_update'),
    path('subdivisions/create/', views.SubdivisionCreate.as_view(), name='subdivisions_create'),
    path('subdivisions/', views.SubdivisionList.as_view(), name='subdivisions'),
    path('', views.main_page, name='main'),
]
