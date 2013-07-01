#!/usr/bin/env python2
import ConfigParser
import os.path
import sys
import gui
import gtk
import gobject

if __name__ == "__main__":

    gobject.threads_init()

    config = ConfigParser.ConfigParser()
    conf_file = os.path.abspath(os.path.dirname(__file__)+"/kaeruftpload.conf")
    
    config.read(conf_file)
    
    host = config.get("config", "host");
    user = config.get("config", "user");
    password = config.get("config", "password");
    directory = config.get("config", "directory");
    url = config.get("config", "url");
    
    if not sys.argv == None:
        file_names = sys.argv
        del file_names[0]
    else:
        file_names = []

    gui = gui.gui()
    gui.ftp_details(host, user, password, directory, url)
    gui.file_names(file_names)
    gui.run()
    
    gtk.main()
