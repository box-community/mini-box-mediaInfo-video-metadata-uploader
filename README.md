<img src="images/box-dev-logo-clip.png" 
alt= “box-dev-logo” 
style="margin-left:-10px;"
width=40%;>
# Mini Box MediaInfo Video Metadata Uploader
This script is based off a [larger project](https://github.com/box-community/box-metadata-media) created by [barduinor](https://github.com/barduinor). Instead of using Docker or FastAPI, it lets you locally apply video metadata (duration, frame rate, etc) to all files in a specified folder. It uses the [MediaInfo](https://mediaarea.net/en/MediaInfo) python library to grab the video metadata based on a download URL taken from the Box API.

You will need to have [python](https://www.python.org/downloads/) installed on your machine. 

## Tutorial authentication
This tutorial shows using client credentials authentication. You are not restricted to using this authentication type, but there is not code for using the other types in this repository. Find out about other kinds in the [developer documentation](https://developer.box.com/guides/authentication/)

## Box setup steps
INSERT MORE HERE

## Script configuration
Clone the github repo and open it in a code editor - like [vscode](https://code.visualstudio.com/).
```
git clone INSERT LINK
code .
``` 

In `src/config.py` add in your client id, client secret, enterprise id, and the name you wish to call the metadata template.

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Create a metadata template
If you have never ran the script before, or wish to create/use a new metadata template, run the following command with the `-c` argument. It will overwrite an existing metadata template. It uses the JSON template from /sample_template to automatically create the correct template and fields. 
```
python3 src/main.py -c
```

## Create a metadata template
To apply data to all files in a folder, run the following command with the `-m PARENT_FOLDER_ID` argument. The service account created after the Box administrator authorized the application will need to be collaborated into the parent folder. It is not recommended to run this for folder id `0`, because there is not a lot of error handling built in. 
```
python3 src/main.py -m PARENT_FOLDER_ID
```

### Questions
If you get stuck or have questions, make sure to ask on our [Box Developer Forum](https://support.box.com/hc/en-us/community/topics/360001932973-Platform-and-Developer-Forum)