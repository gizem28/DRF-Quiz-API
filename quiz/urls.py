from django.urls import path
from rest_framework import routers
from .views import CategoryView, QuizListView

# router= routers.DefaultRouter()
# router.register('' , QuizView)
# router.register('category' , CategoryView)
# # router.register('category/title', QuizView)
urlpatterns = [
    path("", QuizListView.as_view(), name='quiz')
]

# urlpatterns += router.urls