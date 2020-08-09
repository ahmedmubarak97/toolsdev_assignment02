import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance


def maya_main_window():
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window), QtWidgets.QWidget)


class SmartSaveUI(QtWidgets.QDialog):

    def __init__(self):
        super(SmartSaveUI, self).__init__(parent=maya_main_window())
        self.setWindowTitle("Smart Save")
        self.resize(500, 200)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.title_lbl = QtWidgets.QLabel("Smart Save")
        self.title_lbl.setStyleSheet("font: bold 20px")
        self.dir_lbl = QtWidgets.QLabel("Directory")
        self.dir_linedit = QtWidgets.QLineEdit()
        self.incandsave_btn = QtWidgets.QPushButton("Incremenet and Save")
        self.browse_btn = QtWidgets.QPushButton("Browse...")
        self.save_btn = QtWidgets.QPushButton("Save")
        self.cancel_btn = QtWidgets.QPushButton("Cancel")
        self.desc_lbl = QtWidgets.QLabel("Descriptor")
        self.desc_linedit = QtWidgets.QLineEdit("main")
        self.version_lbl = QtWidgets.QLabel("Version")
        self.version_spinbox = QtWidgets.QSpinBox()
        self.version_spinbox.setValue(1)
        self.ext_lbl = QtWidgets.QLabel("Extension")
        self.ext_linedit = QtWidgets.QLineEdit("ma")

    def create_layout(self):
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.title_lbl)

        self.dir_lay = QtWidgets.QHBoxLayout()
        self.dir_lay.addWidget(self.dir_lbl)
        self.dir_lay.addWidget(self.dir_linedit)
        self.dir_lay.addWidget(self.browse_btn)

        self.desc_lay = QtWidgets.QHBoxLayout()
        self.desc_lay.addWidget(self.desc_lbl)
        self.desc_lay.addWidget(self.desc_linedit)

        self.version_lay = QtWidgets.QHBoxLayout()
        self.version_lay.addWidget(self.version_lbl)
        self.version_lay.addWidget(self.version_spinbox)

        self.ext_lay = QtWidgets.QHBoxLayout()
        self.ext_lay.addWidget(self.ext_lbl)
        self.ext_lay.addWidget(self.ext_linedit)

        self.desc_lay = QtWidgets.QHBoxLayout()
        self.desc_lay.addWidget(self.desc_lbl)
        self.desc_lay.addWidget(self.desc_linedit)

        self.bottom_btn_lay = QtWidgets.QHBoxLayout()
        self.bottom_btn_lay.addWidget(self.incandsave_btn)
        self.bottom_btn_lay.addWidget(self.save_btn)
        self.bottom_btn_lay.addWidget(self.cancel_btn)

        self.main_layout.addLayout(self.dir_lay)
        self.main_layout.addLayout(self.desc_lay)
        self.main_layout.addLayout(self.version_lay)
        self.main_layout.addLayout(self.ext_lay)
        self.main_layout.addStretch()
        self.main_layout.addLayout(self.bottom_btn_lay)
        self.setLayout(self.main_layout)