from PySide6.QtGui import QContextMenuEvent
from ressources.paths import Paths
from PySide6.QtWidgets import QTreeView, QAbstractItemView, QMenu, QTreeWidgetItem
from PySide6.QtCore import QDir, Qt, QFile, QFileInfo, QUrl, QDirIterator, QFlag, QModelIndex
from fileexplorer.model import Model
import shutil

class File_explorer(QTreeView):
    def __init__(self, parent):
        super().__init__(parent)
        # instances / attibutes
        self.base_path = Paths.sounds
        #self.base_path = Paths.toputfolders
        
        #logic
        self.set_model_path(self.base_path)
        
        #display menu on right click
        self.context_menu = QMenu(self)
        action_refresh = self.context_menu.addAction('refresh')
        action_refresh.triggered.connect(self.handle_action_refresh)
        
        self.menu_item = QMenu(self)
        action_delete = self.menu_item.addAction('delete')
        action_delete.triggered.connect(self.handle_action_delete)
        
        
    # functions

    def set_model_path(self, path):
        self.model = Model()
        self.model.setRootPath(path)
        self.setModel(self.model)
        self.setRootIndex(self.model.index(path))
        # print(self.model.supportedDropActions())
        
    def dragEnterEvent(self, event):
        event.accept()
        print('drag in treeview')

    def dropEvent(self, event):
        #objective  : handle all operation to do on drop event
        #parameters : self=File_explorer, event= drop event's event
        path = event.mimeData().urls()[0].toLocalFile()
        
        try : #if the drag's 'source' element has no widget source(outside the window)
            event.source().objectName()
        except : #if there is an error
            print('error')
            print('event has no source')
            self.copy_folder_v2(path, f'{self.base_path}\\{QDir(path).dirName()}')
        else : #if there is no error
            print('no errors')
            print('event has a source')
            
        #self.set_model_path(path)
             
    def copy_folder(self, from_dir, to_dir, copy_and_remove=False):  # kind of fail using QDirIterator   
        # https://forum.qt.io/topic/105993/copy-folder-qt-c/5   
        # make the copy of the main folder too
        # odesn't work if we copy the same folder inside this folder
        
        
        # QDir(to_dir).mkdir(QDir(from_dir).dirName())
        # to_dir = f'{to_dir}\\copy{QDir(from_dir).dirName()}'
        
        
        # arr_from_dir = []
        # arr_from_dir.append(from_dir)
        # dir = None
        
        # while len(arr_from_dir) != 0: # tant qu'il y a des dossiers
        #     # print(f'arr_from_dir : {arr_from_dir}')
        #     it = QDirIterator(arr_from_dir[0], QDirIterator.IteratorFlag.NoIteratorFlags)
        #     dir = QDir(from_dir)
        #     abs_source_path_length = len(dir.absoluteFilePath(from_dir))
        #     print(f'list : {arr_from_dir}')
            
        #     while it.hasNext(): # tant qu'il y a des elements dans le dossier concerne
                
        #         it.next()
        #         file_info = it.fileInfo()
        #         print(f'file info : {file_info}')
                
        #         if file_info.fileName() != '.' and file_info.fileName() != '..': # filter dot and dotdot  
        #             sub_path_structure     = file_info.absoluteFilePath()[abs_source_path_length:] #pb
        #             constructed_abs_path = to_dir + sub_path_structure
        #             print(f'file_info.absoluteFilePath() : {file_info.absoluteFilePath()}')
        #             print(f'dir.absoluteFilePath(from_dir) : {dir.absoluteFilePath(from_dir)}')
        #             print(f'sub_path_structure : {sub_path_structure}')
        #             print(f'constructed_abs_path : {constructed_abs_path}')

        #             if file_info.isDir() == True:
        #                 print('is a folder')
        #                 # dir.mkpath(constructed_abs_path) #create folder
        #                 # arr_from_dir.append(file_info.absoluteFilePath()) #new from_dir
                        
        #             elif file_info.isFile() == True:
        #                 QFile.remove(constructed_abs_path) #to make work copy()
        #                 QFile.copy(file_info.absoluteFilePath(), constructed_abs_path)
                        
        #     arr_from_dir.pop(0) #remove already treated folder's path
            
        # if copy_and_remove == True: #cut and paste option
        #     dir.removeRecursively()   
        pass

    def copy_folder_v2(self, from_dir, to_dir):
        shutil.copytree(from_dir, to_dir) # copytree() for a lot of folder, copy for one file()
        
    def contextMenuEvent(self, event):
        #objective  : display a menu on rightclick
        #parameters : self=File_explorer, event=event return by the function
        indexes = self.selectedIndexes()
        file_paths = []
        
        if  len(indexes) != 0: #at least one item selected
            self.menu_item.exec(event.globalPos()) #set the menu display at the globalpos position
            
            for i in range(0, len(indexes), 4):
                file_paths.append(self.model.filePath(self.selectedIndexes()[i])) #get the path of the item
            file_paths.clear() #reset array for next right click
        else: #no item selected
            self.context_menu.exec(event.globalPos())
             
    def handle_action_refresh(self):
        print('action_resfresh triggered')
        
    def handle_action_delete(self):
        print('action_delete triggered')

        
            
        
        
        
    