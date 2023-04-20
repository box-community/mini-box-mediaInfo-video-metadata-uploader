"""Handles box file api"""

import os

from boxsdk import Client
from boxsdk.object.file import File


def get_file_by_id(client: Client, file_id: str) -> File:
    """Returns the box file by id"""

    file = client.file(file_id=file_id).get()
    return file


def download_file_to_path(
    file: File, path: str, file_name: str | None = None, autocreate_path: bool = False
) -> None:
    """Downloads the file to the given path"""

    # check if path exists
    if not os.path.exists(path):
        if autocreate_path:
            os.makedirs(path)
        else:
            raise Exception("Path does not exist")

    # handle file_name
    if file_name is None:
        file_path = os.path.join(path, file.name)
    else:
        file_path = os.path.join(path, file_name)

    with open(file_path, "wb") as file_object:
        file.download_to(file_object)


def get_files_by_folder_id(client: Client, folder_id: str) -> list[File]:
    """Returns the box files in a folder"""

    folder = client.folder(folder_id=folder_id).get()
    items = folder.get_items()
    files = []
    for item in items:
        if item.type == "file":
            files.append(item.get())

    return files
