import sys
import os.path
import urllib
from ftplib import FTP
from time import time
from zlib import crc32

class ftp_uploader:
    def __init__(self, host, user, password, directory, url):
        self.host = host
        self.user = user
        self.password = password
        self.directory = directory
        self.url = url

    def upload_files(self, file_names):
        log = []

        try:
            ftp = FTP(self.host, self.user, self.password)
            ftp.cwd(self.directory)
        except:
            ftp.quit()
            return 0

        try:
            for x in file_names:
                full_name = os.path.abspath(x)
                file = open(full_name, "rb")

                file_hash = str(crc32(file.read(1048576))) # Read in 1MB
                file.seek(0)

                file_name = "{0}-{1}".format(file_hash[:3], os.path.basename(full_name))

                result = self.url + urllib.quote(file_name) + "\n";
                result += ftp.storbinary("STOR " + file_name, file)
                log.append(result)
        except:
            ftp.quit()
            return 1

        ftp.quit()

        return "\n".join(log)
