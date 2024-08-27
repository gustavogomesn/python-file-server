# File Server # 

A file explorer that works over local area network (Wi-Fi/Ethernet) using Python/Flask server. You can define a directory to upload and download any folder or file. Moreover, it also lets you stream videos or audio files if your browser supports it.

**Description**
-
Server works on,
- Linux (Tested on Ubuntu 22)

**Frameworks**
-
- Flask (Server)
- Some Bootstrap 5 

Double click to open folder or execute supported files, hover or select rows to able download and delete buttons

**How to Run**
-
Clone this repository by using,
    
    git clone https://github.com/gustavogomesn/python-file-server.git

Make sure you have requirements installed. You can use the following command to install,

    pip install -r requirements.txt
    
Now, open terminal/command prompt in the file-server directory and run the main.py file by using the following command,

    python3 setup.py

You will have to configure the [config.json](config.json) file with your paths,

Example for Linux,

    "UPLOAD_FOLDER": "/home/user/Desktop/SERVER",
    "LOG_FOLDER": "/var/log",


This should start the Flask Server in your terminal window. By default, it is run on port 8000. You can access it by going to,
- **(IP Address of your Server)** (from any other browser on the same network)

## Next Features ##

- [ ] Handle exceptions
- [ ] Activity log
- [ ] Window compatibily
- [ ] Hide complete path in server address
- [ ] Delete zip files in temp directory after download a folder
- [ ] Add breadcrumbs	

