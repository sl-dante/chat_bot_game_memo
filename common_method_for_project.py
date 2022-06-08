import urllib
from pathlib import Path


def load_photo(photo_path, upload):
    absolute_path = Path(__file__).resolve().parents[0]
    path = f"{absolute_path}\\assets\\img_for_project\\china_chess\\{photo_path}"
    photo = upload.photo_messages(path)
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'

    return attachment
