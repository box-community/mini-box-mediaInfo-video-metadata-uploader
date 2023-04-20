from media_info import get_media_info_by_url
from file_helper import get_files_by_folder_id
from metadata_helper import file_metadata_set
from metadata_template_create import get_metadata_template_by_name
from boxsdk import BoxAPIException, Client
import config

def attachMetdata(client: Client, parent_folder_id: str):
    """Process media file and fill in the metadata info using 'as-user'
    security context"""

    template = get_metadata_template_by_name(
        client, config.metadata_template_name
    )
    files = get_files_by_folder_id(client, parent_folder_id)
    files_metadata = []

    for file in files:
        print('Processing file: ' + str(file.id))
        # get media info
        media_info = get_media_info_by_url(file.get_download_url())

        # set the metadata
        try:
            metadata = file_metadata_set(file, template, media_info)
            files_metadata.append(metadata)
        except BoxAPIException as error:
            raise ValueError(f"Error: {error}")

    print(len(files_metadata))
