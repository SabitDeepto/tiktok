from django.urls import path

from Merchant_Management import views

urlpatterns = [
    path('create', views.create_merchant, name='create_merchant'),
    path('list', views.merchant_list, name='merchant_list'),
    # path('list', views.ambassador_list, name='ambassador_list'),
    # path('delete_ambassador', views.delete_ambassador, name='delete_ambassador'),
    # path('update/<int:id>/', views.update, name='update'),
    # path('delete/<int:id>/', views.delete, name='delete'),



]