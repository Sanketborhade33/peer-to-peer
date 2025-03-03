# from django.urls import path
# from .views import home, user_login  # Use the renamed function

# urlpatterns = [
#     path("", home, name="home"),
#     path("login/", user_login, name="login"),
   
# ]





from django.urls import path
from .views import home, user_login, lender_list, borrower_list  # Use the renamed function
from .views import lender_registration

from .views import borrower_registration


from .views import chat_room #for chat
from .views import borrower_list, chat_room


urlpatterns = [
    path("", home, name="home"),
    path("login/", user_login, name="login"),
    path('register/', lender_registration, name='lender_registration'),
    path('lenders/', lender_list, name='lender_list'),

     path('borrower/register/', borrower_registration, name='borrower_registration'),


     path('borrowers/', borrower_list, name='borrower_list'),


    #  for chat

  


path('borrowers/', borrower_list, name='borrower_list'),
path('chat/<int:receiver_id>/', chat_room, name='chat_room'),


   
   
]
