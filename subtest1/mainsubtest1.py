import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QSplitter
from mainwindow_ui import Ui_MainWindow
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import Qt

class MainWindow(QMainWindow ,Ui_MainWindow):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)
        self.show()
        
        self.add_splitter()
        #self.connect_pb()
        
        self.pb_cart_1.clicked.connect(self.play_audio1)
        self.pb_cart_2.clicked.connect(self.play_audio2)
        
        
    def add_splitter(self):
        widget = QWidget()
        hlayout = QVBoxLayout()
        splitter = QSplitter()
        
        widget_1 = self.frame_sub_main
        widget_2 = self.frame_treeview
        
        splitter.addWidget(widget_2)
        splitter.addWidget(widget_1)
        splitter.setOrientation(Qt.Orientation.Horizontal)
        hlayout.addWidget(splitter)
        widget.setLayout(hlayout)
        self.setCentralWidget(widget) 
        
    def play_audio1(self):
        print('pad1 clicked')
        print(f'pad file : {self.pb_cart_1.file}')
        player.setSource(self.pb_cart_1.file)
        print(f'player source : {player.source()}')
        player.play()
        
    def play_audio2(self):
        print('pad 2 clicked')
        print(f'pad file : {self.pb_cart_2.file}')
        player.setSource(self.pb_cart_2.file)
        print(f'player source : {player.source()}')
        player.play()
     
     
     
     
if __name__ == "__main__":
    # classes's instances  
      
    app = QApplication(sys.argv)
    
    
    
    window = MainWindow()  
    player = QMediaPlayer()
    audio_output = QAudioOutput()
    audio_output.setVolume(1)
    player.setAudioOutput(audio_output)
    
    # launch app
    app.exec()