from django.urls import path

from .views import view_sensor

urlpatterns = {

    path('sensors/', view_sensor),
    # TODO: зарегистрируйте необходимые маршруты
}
