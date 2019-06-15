# Create your tests here.
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from musics.models import Music

class MusicViewTestCase(APITestCase):
    url_detail_route = '/api/musics/{}/detail/'
    url_list_route = '/api/musics/all_singer/'

    def setUp(self):
        print('setUp')
        self.client = APIClient()
        self.request_data = {
            'song': 'song_test',
            'singer': 'singer_test'
        }

        self.music = Music.objects.create(song='song_test', singer='singer_test')

    def test_api_music_detail_route(self):
        print('test_api_music_detail_route')
        music = Music.objects.get(pk=self.music.id)
        response = self.client.get(self.url_detail_route.format(self.music.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('song', None), music.song)
        self.assertEqual(response.data.get('singer', None), music.singer)

    def test_api_music_list_route(self):
        print('test_api_music_list_route')
        music = Music.objects.values_list('singer', flat=True).distinct()
        response = self.client.get(self.url_list_route)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(next(iter(response.data)), next(iter(music)))