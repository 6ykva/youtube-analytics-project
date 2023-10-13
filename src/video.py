from googleapiclient.discovery import build


class Video:
    """
    Создаем класс Video
    """
    def __init__(self, video_id: str) -> None:
        self.video_id = video_id
        info = self.get_info()
        self.title = info['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/' + self.video_id
        self.view_count = int(info['items'][0]['statistics']['viewCount'])
        self.like_count = int(info['items'][0]['statistics']['likeCount'])

    def __str__(self):
        return self.title

    def get_info(self):
        info = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                id=self.video_id
                                                ).execute()
        return info

    @classmethod
    def get_service(cls):
        """
        Загружаем сервис по API
        """
        api_key = 'AIzaSyBCgL6CnIFgroMqCKtQBoj5puwTWwSFaSs'
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube


class PLVideo(Video):
    """
    Создаем класс PLVideo и наследуем от класса Video
    """
    def __init__(self, video_id, playlist_id) -> None:
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        return self.title
