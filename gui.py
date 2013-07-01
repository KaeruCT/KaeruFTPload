import pygtk
pygtk.require('2.0')
import gtk
import file_chooser
import ftp_uploader
import pynotify
import gobject
import threading

class gui(threading.Thread):
    def __init__(self):
        super(gui, self).__init__()
        
        self.title = "FTP Upload"
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
        
        self.text_view = gtk.TextView()
        self.box.pack_start(self.text_view, True, True, 0)
        self.text_view.show()
        
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
        notification = pynotify.Notification("FTP Upload", "Uploading files...", "dialog-info")
        notification.show()
 
        notification.set_urgency(pynotify.URGENCY_NORMAL)
        notification.set_timeout(pynotify.EXPIRES_NEVER)
    
    def show_error(self, message):
        buffer = gtk.TextBuffer()
        buffer.set_text(message)
        self.window.set_size_request(300, 100)
        self.text_view.set_buffer(buffer)
        self.window.show()

    def destroy(self, widget, data=None):
        gtk.main_quit()
        
    def start_upload(self):
        self.show_notification()
        ftp = ftp_uploader.ftp_uploader(self.host, self.user, self.password, self.directory, self.url)
        result = ftp.upload_files(self.file_names)
        
        if result == 0:
            self.show_error("Error connecting to the FTP server")
        elif result == 1:
            self.show_error("Error uploading files.")
        else:
            buffer = gtk.TextBuffer()
            buffer.set_text(result)
            self.window.set_size_request(500, 200)
            self.text_view.set_buffer(buffer)
            self.window.show()
                
    def file_names(self, file_names):
        self.file_names = file_names
    
    def run(self):
        if not self.file_names:
            chooser = file_chooser.file_chooser()
            self.file_names = chooser.get_files()
            chooser.destroy()
            
        if not self.file_names:
            gobject.idle_add(self.destroy, None)
        else:
            gobject.idle_add(self.start_upload)
        
