from django.urls import path
from first_app.views import home, store_task
urlpatterns = [
    path('', home),
    path('store_new_task/', store_task, name='storetask'),
]
