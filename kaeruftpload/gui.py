import pygtk
pygtk.require('2.0')
import gtk
import file_chooser
import ftp_uploader
import pynotify

class gui:
	def __init__(self):
		
		self.title = "KaeruFTPLoad"
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title(self.title)
		self.window.connect("destroy", self.destroy)
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_size_request(300, 100)
		
		self.mainbox = gtk.VBox(False, 0)
		self.mainbox.show()
		self.window.add(self.mainbox)
		
		self.scrolled_window = gtk.ScrolledWindow()
		self.scrolled_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
		self.mainbox.add(self.scrolled_window)
		self.scrolled_window.show()
		
		self.box = gtk.VBox(False, 0)
		self.scrolled_window.add_with_viewport(self.box)
		self.box.show()
		
		self.label = gtk.Label()
		self.box.pack_start(self.label, True, True, 0)
		self.label.set_selectable(True)
		self.label.show()
		
		self.close_button = gtk.Button(label="Close", stock=gtk.STOCK_CLOSE)
		self.close_button.connect("clicked", self.destroy)
		self.close_button.show()
		
		quitbox = gtk.HBox(False, 0)
		quitbox.pack_start(self.close_button, True, False, 0)
		quitbox.show()
		
		halign = gtk.Alignment(1, 0, 0, 0)
		halign.add(quitbox)
		halign.show()
		
		self.mainbox.pack_start(halign, False, False, 0)
		
	def ftp_details(self, host, user, password, directory, url):
	
		self.host = host
		self.user = user
		self.password = password
		self.directory = directory
		self.url = url
		
	def show_notification(self):
		pynotify.init("Uploading file...")
		notification = pynotify.Notification("KaeruFTPLoad", "Uploading files...", "dialog-info")
		notification.show()
 
		notification.set_urgency(pynotify.URGENCY_NORMAL)
		notification.set_timeout(pynotify.EXPIRES_NEVER)
	
	def show_error(self, message):
		self.window.set_size_request(300, 100)
		self.label.set_text(message)
		self.label.set_selectable(False)
		self.window.show()

	def destroy(self, widget, data=None):
		gtk.main_quit()
		
	def start_upload(self, file_names):
		
		if len(file_names) == 0:
			self.show_error("No files selected.")
		else:
			self.show_notification()
			ftp = ftp_uploader.ftp_uploader(self.host, self.user, self.password, self.directory, self.url)
			result = ftp.upload_files(file_names)
			
			if result == 0:
				self.show_error("Error connecting to the FTP server")
			elif result == 1:
				self.show_error("Error uploading files.")
			else:
				self.window.set_size_request(500, 200)
				self.label.set_text(result)
				self.window.show()

	def main(self, file_names):
		if len(file_names) == 0:
			chooser = file_chooser.file_chooser()
			file_names = chooser.get_files()
							
		self.start_upload(file_names)
			
		gtk.main()
