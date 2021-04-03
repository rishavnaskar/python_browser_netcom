import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QAction, QApplication, QLineEdit, QMainWindow, QToolBar
import os
import socket


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        network_details_btn = QAction('Network Details', self)
        network_details_btn.triggered.connect(self.network_details_get)
        navbar.addAction(network_details_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def network_details_get(self):
        try:
            IPAddress = socket.gethostbyname(socket.gethostname())
            print("My IP address is: " + IPAddress)
            url = self.url_bar.text()
            url = url[url.find('w')+4: len(url)-1]
            print('cmd /k "tracert %s"' %url)
            os.system('cmd /k "tracert %s"' %url)
        except:
            print('Could not execute that')


app = QApplication(sys.argv)
QApplication.setApplicationName('My Killer Browser')
window = MainWindow()
app.exec_()
