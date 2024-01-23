from typing import Optional, Union
from PySide6.QtCore import QModelIndex, QObject, QPersistentModelIndex, Qt, QFlag
from PySide6.QtWidgets import QFileSystemModel


class Model(QFileSystemModel):
    def __init__(self):
        super().__init__()
        
    def flags(self, index: QModelIndex | QPersistentModelIndex):
        if index.isValid() == False:
            return Qt.ItemFlag.ItemIsDropEnabled
        
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsDropEnabled | Qt.ItemFlag.ItemIsDragEnabled
        