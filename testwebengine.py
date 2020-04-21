import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
# use the QtWebEngineWidgets
from PyQt5.QtWebEngineWidgets import *
# start my_app




class WebPage(QWebEnginePage):

    def __init__(self, parent):
        QWebEnginePage.__init__(self, parent)
        #self.settings().setAttribute(QWebEngineSettings.DeveloperExtrasEnabled, True)
    def javaScriptConsoleMessage(self, msg, lineNumber, sourceID,foo):
        print("JsConsole(%s:%s): %s" % (sourceID, lineNumber, msg))



my_app = QApplication(sys.argv)
# open webpage
my_web = QWebEngineView()
page = WebPage(my_web)
my_web.setPage(page)
filehtml =os.path.join( os.path.dirname(os.path.abspath(__file__)), "timeline-full-height.html")
#filehtml =os.path.join( os.path.dirname(os.path.abspath(__file__)), "react-calendar-timeline-demo/index.html")
my_web.load(QUrl("file:///%s" % (filehtml.replace("\\","/"))))
print(filehtml)
my_web.show()
# sys exit function
sys.exit(my_app.exec_())