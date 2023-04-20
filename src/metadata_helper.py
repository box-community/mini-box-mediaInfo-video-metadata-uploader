""" Handle metadata fecthing and processing for box files"""
import os

from boxsdk.object.file import File
from boxsdk.object.metadata import Metadata
from boxsdk.object.metadata_template import MetadataTemplate


def file_metadata_set(
    file: File,
    template: MetadataTemplate,
    media_info: dict,
) -> Metadata:
    """update the file metadata"""

    template_fields = template["fields"]

    metadata_mapped = {}
    for field in template_fields:
        metadata_mapped[field["key"]] = media_info.get(field["displayName"])

    # convert values from list to strings
    for key, value in metadata_mapped.items():
        if isinstance(value, list):
            metadata_mapped[key] = ", ".join(value)

    # remove none values
    metadata_mapped = {k: v for k, v in metadata_mapped.items() if v is not None}

    # # convert integers to strings
    # for key, value in metadata_mapped.items():
    #     if isinstance(value, int):
    #         metadata_mapped[key] = str(value)

    # adjust some values directly from file
    metadata_mapped["fileName"] = file.name
    metadata_mapped["otherFileName"] = file.name
    metadata_mapped["fileExtension"] = os.path.splitext(file.name)[1]

    # convert dict values into string
    metadata_mapped["folderName"] = ""
    for folder in file.path_collection["entries"]:
        metadata_mapped["folderName"] = (
            metadata_mapped.get("folderName", "") + "/" + folder["name"]
        )

    metadata_mapped["completeName"] = metadata_mapped["folderName"] + "/" + file.name

    applied_metadata = file.metadata(
        scope="enterprise", template=template.template_key
    ).set(metadata_mapped)

    return applied_metadata
