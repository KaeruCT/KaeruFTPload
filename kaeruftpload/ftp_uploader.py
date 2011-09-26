import sys
import os.path
from ftplib import FTP
from time import time

class ftp_uploader:
	def __init__(self, host, user, password, directory, url):
		self.host = host
		self.user = user
		self.password = password
		self.directory = directory
		self.url = url
	
	def upload_files(self, file_names):
		log = []
		ftp = FTP(self.host, self.user, self.password)

		ftp.cwd(self.directory)

		for x in file_names:
			full_name = os.path.abspath(x)
			file = open(full_name, "rb")
			
			file_name = str(time())+x.split("/").pop();
			
			result = self.url+file_name + "\n";
			result += ftp.storbinary("STOR " + file_name, file)
			log.append(result)

		ftp.quit()
		
		return "\n".join(log)