from django.urls import path
from pages.views import Home,Contact,About, team
urlpatterns = [
    path('', Home),
    #path('category/<int:cat_id>/member/<int:mem_id>',Members, name="member"),
    path('members/',team, name="team"),
    path('contact/', Contact),
    path('about/',About)
]