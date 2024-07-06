# connectors.py
import requests

class ContactServiceConnector:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def send_ping(self, endpoint: str):
        response = requests.get(url=endpoint)
        return response.status_code == 200

    def send_request(self, method: str, path: str, data=None, params=None):
        url = f"{self.endpoint}/{path.lstrip('/')}"
        response = requests.request(method=method, url=url, data=data, params=params)
        return response

    def getAllBlogs(self):
        return self.send_request('get', '/')

    def create_blog(self, data: dict):
        return self.send_request('post', '/', data=data)

    def get_blog_by_id(self, blog_id: str):
        return self.send_request('get', f'/{blog_id}')

    def update_blog(self, blog_id: str, data: dict):
        return self.send_request('put', f'/{blog_id}', data=data)

    def delete_blog(self, blog_id: str):
        return self.send_request('delete', f'/{blog_id}')

    def get_authorization_url(self):
        return self.send_request('get', '/api/blogs')
