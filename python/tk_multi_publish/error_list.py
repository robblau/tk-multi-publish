"""
Copyright (c) 2013 Shotgun Software, Inc
----------------------------------------------------
"""

import tank
from tank.platform.qt import QtCore, QtGui

class ErrorItem(QtGui.QWidget):
    """
    """
    def __init__(self, parent=None):
        """
        Construction
        """
        QtGui.QWidget.__init__(self, parent)
    
        # set up the UI
        from .ui.error_item import Ui_ErrorItem
        self._ui = Ui_ErrorItem() 
        self._ui.setupUi(self)

class ErrorList(QtGui.QWidget):
    """
    """
    def __init__(self, tasks, parent=None):
        """
        Construction
        """
        QtGui.QWidget.__init__(self, parent)
        
        self._tasks = tasks
        for task in self._tasks:
            task.modified.connect(self._on_task_modified)
        
        self._error_widgets = []
            
        # set up the UI
        from .ui.error_list import Ui_ErrorList
        self._ui = Ui_ErrorList() 
        self._ui.setupUi(self)
        
        # add a layout:
        layout = QtGui.QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(2,2,2,2)
        self._ui.item_frame.setLayout(layout)
        
        # update ui
        self._update_ui()
        
    def _on_task_modified(self):
        self._populate_errors()
        
    def _populate_errors(self):

        for widget in self._error_widgets:
            widget.setParent(None)
            widget.deleteLater()
        self._error_widgets = []
        
        layout = self._ui.item_frame.layout()
        for task in self._tasks:
            for pp_error in task.pre_publish_errors:
                item = ErrorItem(self._ui.item_frame)
                layout.addWidget(item)
                self._error_widgets.append(item)
                
        self._update_ui()
    
    def _update_ui(self):
        self.setVisible(len(self._error_widgets) > 0)





