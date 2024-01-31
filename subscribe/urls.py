from django.urls import include, path
from subscribe.views import subscribe, thank_you

urlpatterns = [
    path('subscribe/', subscribe, name="subscribe" ),
    path('thank_you', thank_you, name="thank_you")

]