<img src="images/box-dev-logo-clip.png" 
alt= “box-dev-logo” 
style="margin-left:-10px;"
width=40%;>
# Mini Box MediaInfo Video Metadata Uploader
This script is based off a [larger project](https://github.com/box-community/box-metadata-media) created by [barduinor](https://github.com/barduinor). Instead of using Docker or FastAPI, it lets you locally apply video metadata (duration, frame rate, etc) to all files in a specified folder. It uses the [MediaInfo](https://mediaarea.net/en/MediaInfo) python library to grab the video metadata based on a download URL taken from the Box API.

You will need to have [python](https://www.python.org/downloads/) installed on your machine. 
You will need to have [MediaInfo](https://mediaarea.net/en/MediaInfo) library installed in your system.

## Tutorial authentication
This tutorial shows using client credentials authentication. You are not restricted to using this authentication type, but there is not code for using the other types in this repository. Find out about other kinds in the [developer documentation](https://developer.box.com/guides/authentication/).

## Box setup steps
Since this script creates a metadata template for you, you will not need to make one in Box; however, you will need to create a folder and upload a few mp4 files to process. It is recommended that you set this tutorial up in a Sandbox environment, as you will need admin privileges. Find more about sandboxes [here](https://support.box.com/hc/en-us/articles/360043697274-Managing-developer-sandboxes-for-Box-admins).

1. Create a Box folder and make note of its folder id for a later step.
2. Upload some .mp4 video files to process. If you don't have any, find some [here](https://www.pexels.com/search/videos/demo/).
3. Create a new application in the [Box Developer Console](https://app.box.com/developers/console). Click Create new app > Custom App > Server Authentication(Client Credentials Grant) > Type in a name > Click Create App.
4. Under the configuration tab, select App + Enterprise, followed by checking the boxes for Read/Write all files. Then, click Save Changes in the top right.
5. Copy the client id of the application. Back in the Box Admin Console, follow the steps to [approve a custom application](https://developer.box.com/guides/authorization/custom-app-approval/).
6. Back on the General Settings tab of the application you created in the Box Developer Console, you should now see an email that starts like AutomationUser_... in the Service Account Info section. Copy that email. Back in the main Box Web App, collaborate the service account into the folder you created in step 1. 

## Script configuration
Clone the github repo and open it in a code editor - like [vscode](https://code.visualstudio.com/).
```
git clone git@github.com:Smartoneinok/mini-box-mediaInfo-video-metadata-uploader.git
code .
``` 

Create a `src/config.py` file based on the example. Add in your client id, client secret, enterprise id, and the name you wish to call the metadata template.

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