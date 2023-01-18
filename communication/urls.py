from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("room/<int:pk>", views.room_detail, name="room"),
    path("create-room", views.CreateRoomView.as_view(), name="create_room"),
    path("update-room/<int:pk>", views.UpdateRoomView.as_view(), name="update_room"),
    path("delete-room/<int:pk>", views.DeleteRoomView.as_view(), name="delete_room"),
    path("delete-message/<int:pk>", views.DeleteMessageView.as_view(), name="delete_message"),
]
