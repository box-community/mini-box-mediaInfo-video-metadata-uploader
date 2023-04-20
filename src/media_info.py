from pymediainfo import MediaInfo


def get_media_info_by_url(download_url: str) -> dict:
    """get the file by id"""

    media_info_raw = MediaInfo.parse(download_url)
    track_general = media_info_raw.general_tracks[0]
    media_info = track_general.to_data()
    return media_info


def get_media_info_by_file_path(file_path: str) -> dict:
    """get the file by path"""

    media_info_raw = MediaInfo.parse(file_path)
    track_general = media_info_raw.general_tracks[0]
    media_info = track_general.to_data()
    return media_info