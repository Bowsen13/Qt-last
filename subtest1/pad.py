from PySide6.QtGui import QContextMenuEvent, QDragEnterEvent, QDropEvent, QKeyEvent
from PySide6.QtWidgets import QPushButton

class Pad(QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Datas
        self.file = ''
        self.tag = 'pad'
        self.infos = {'obj' : self,
                      'tag' : self.tag}
        #text
        #Behaviour
     
    
    # Behaviour
        
    def dragEnterEvent(self, event):
        event.accept()
    
    def dropEvent(self, event):
        self.file = event.mimeData().text()
        print(f'Dropped in pad : {self.file}')
        
        
