import requests
import os
from dotenv import load_dotenv
from datetime import datetime


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.url = "https://cloud-api.yandex.net:443/v1/disk/resources/"

    def get_headers(self) -> dict:
        """Метод устанавливает заголовки, которые используются в каждом запросе"""
        return {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {self.token}",
        }

    def check_exist_folder(self, folder: str) -> bool:
        url = self.url
        headers = self.get_headers()
        params = {"path": folder}
        resp = requests.get(url=url, headers=headers, params=params)
        return resp.status_code == 200

    def create_folder(self, folder: str) -> int:
        url = self.url
        headers = self.get_headers()
        params = {"path": folder}
        resp = requests.put(url=url, headers=headers, params=params)
        return resp.status_code


def get_token():
    dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    return os.environ.get("YA_DISK_TOKEN")


def create_yadisk_folder(folder):
    ya_disk = YaUploader(get_token())
    folder_name = folder
    resp_code = ya_disk.create_folder(folder_name)

    return resp_code


def main():
    folder_name = f'test_{datetime.now().strftime("%Y%m%d-%H%M%S")}'
    print(f"Creating folder: {folder_name}")
    resp = create_yadisk_folder(folder_name)
    print(f"Response code: {resp}")


if __name__ == "__main__":
    main()
