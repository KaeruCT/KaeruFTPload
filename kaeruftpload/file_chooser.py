
import pygtk
pygtk.require('2.0')
import gtk

class file_chooser:
	def __init__(self):
		self.chooser = gtk.FileChooserDialog(title="Select file(s) to upload",
			action = gtk.FILE_CHOOSER_ACTION_OPEN,
			buttons = (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
				gtk.STOCK_OPEN,gtk.RESPONSE_OK))
				
		self.chooser.set_select_multiple(True)

	def get_files(self):
		response = self.chooser.run()
		if response == gtk.RESPONSE_OK:
			file_names = self.chooser.get_filenames()
		else:
			file_names = []
			
		self.chooser.destroy()
		return file_names
