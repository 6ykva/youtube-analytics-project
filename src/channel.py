import os
import json

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id

        self.channel = self.get_channel_info()

        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/channel/' + self.channel_id
        self.subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """
        Загружаем сервис по API
        """
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def get_channel_info(self):
        """
        Загружаем информацию о сервисе
        """
        channel = self.get_service().channels().list(id=self.__channel_id,
                                                     part='snippet,statistics').execute()
        return channel

    @property
    def channel_id(self):
        """
        __channel_id сделали private
        """
        return self.__channel_id

    def to_json(self, file_name):
        """
        Наполняем данными о сервисе и формируем файл
        """
        data = {'id канала: ': self.channel_id,
                'Название канала: ': self.title,
                'Описание канала': self.description,
                'Ссылка на канал': self.url,
                'Количество подписчиков': self.subscriber_count,
                'Количество видео': self.video_count,
                'Общее количество просмотров': self.view_count
                }
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
