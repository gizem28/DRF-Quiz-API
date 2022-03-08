from django.urls import path
from rest_framework import routers
from .views import CategoryView, QuizView

router= routers.DefaultRouter()
router.register('' , QuizView)
router.register('category' , CategoryView)
# router.register('category/title', QuizView)
urlpatterns = [

]

urlpatterns += router.urls