from django.urls import path
from .views import AlbumList, AlbumDetail,AlbumDestroy
from .views import ArtistList, ArtistDetail,ArtistDestroy
urlpatterns = [
    path('artists/', ArtistList.as_view()),
    path('artists/<int:pk>/', ArtistDetail.as_view()),
    path('artists/create/', ArtistList.as_view()),
    path('artists/<int:pk>/update/', ArtistDetail.as_view()),
    path('artists/<int:pk>/delete/', ArtistDestroy.as_view()),

    path('albums/', AlbumList.as_view()),
    path('albums/<int:pk>/', AlbumDetail.as_view()),
    path('albums/create/', AlbumList.as_view()),
    path('albums/<int:pk>/update/', AlbumDetail.as_view()),
    path('albums/<int:pk>/delete/', AlbumDestroy.as_view()),
    path('albums/<int:artist_id>/artist', AlbumList.as_view()),

]
