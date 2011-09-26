# KaeruFTPLoad
Quick FTP uploader with python and pygtk.
I made this originally for myself since I wanted to be able to
upload files directly from my computer to my FTP server without
having to open up an FTP client.

If you use a desktop environment such as XFCE, you can even set the program as one
of the options in the context menu and upload an array of files in just one click!

If you run it from the command line without specifing with files you want to upload,
it will show a GTK file chooser.

## Dependencies
* Python 2
* PyGTK
* pynotify

## How to run
`python ftpupload.py file1 file2 file3`
`./ftpupload.py file1 file2 file3` works too

## Configuration
In the file `kaeruftpload.conf` you can set your FTP details.

* host: your FTP server's hostname
* user: your FTP user
* password: your FTP user's password
* directory: the directory in which you want to upload the files
* url: the url that you would use to access your file (you can leave it 
empty)

I added the url parameter because I like to copy the links to the files I
have just uploaded and paste them on IRC or something.

The configuration file has an example setup, just in case the explanation above was
not enough.

## Notes
I made this for my own use, so the code might not be the best, I focused
in making it work. I might optimize it and make it nicer over time if I feel like it.
