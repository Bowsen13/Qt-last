import os, sys

class Paths:
          
    base     = os.path.dirname(__file__)
    ui_files = os.path.join(base,"ui")
    images   = os.path.join(base,"images")
    icons    = os.path.join(images,'icons')
    datas    = os.path.join(base,"images")
    sounds   = os.path.join(base,"sounds")
    toputfolders = os.path.join(base,'toputfolders')
    toonlyfolders = os.path.join(base,'toonlyfolders')
    totestcopy2 = os.path.join(base,'totestcopy2')
    totestcopy = os.path.join(base,'totestcopy')
    
    # File loaders.
    @classmethod
    def ui_file(cls, filename):
        return os.path.join(cls.ui_files, filename)
    @classmethod
    def icon(cls, filename):
        return os.path.join(cls.icons, filename)
    @classmethod
    def image(cls, filename):
        return os.path.join(cls.images, filename)
    @classmethod
    def data(cls, filename):
        return os.path.join(cls.data, filename)
    @classmethod
    def sound(cls, filename):
        return os.path.join(cls.sounds, filename)
    @classmethod
    def toputfolder(cls, filename):
        return os.path.join(cls.toputfolders, filename)
    @classmethod
    def toonlyfolder(cls, filename):
        return os.path.join(cls.toonlyfolders, filename)