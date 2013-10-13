# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pointstopaths.ui'
#
# Created: Sat Aug  4 08:17:08 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PointsToPaths(object):
    def setupUi(self, PointsToPaths):
        PointsToPaths.setObjectName(_fromUtf8("PointsToPaths"))
        PointsToPaths.resize(424, 517)
        PointsToPaths.setWindowTitle(QtGui.QApplication.translate("PointsToPaths", "PointsToPaths", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout_6 = QtGui.QVBoxLayout(PointsToPaths)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.tabWidget = QtGui.QTabWidget(PointsToPaths)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab1)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.tab1)
        self.label_3.setText(QtGui.QApplication.translate("PointsToPaths", "Input point layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.inShape = QtGui.QComboBox(self.tab1)
        self.inShape.setObjectName(_fromUtf8("inShape"))
        self.verticalLayout_3.addWidget(self.inShape)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_4 = QtGui.QLabel(self.tab1)
        self.label_4.setEnabled(True)
        self.label_4.setText(QtGui.QApplication.translate("PointsToPaths", "Point group field (string or integer)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        self.attrField = QtGui.QComboBox(self.tab1)
        self.attrField.setObjectName(_fromUtf8("attrField"))
        self.verticalLayout_4.addWidget(self.attrField)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_5 = QtGui.QLabel(self.tab1)
        self.label_5.setToolTip(_fromUtf8(""))
        self.label_5.setText(QtGui.QApplication.translate("PointsToPaths", "Point order field (numeric or datetime string)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.orderField = QtGui.QComboBox(self.tab1)
        self.orderField.setToolTip(QtGui.QApplication.translate("PointsToPaths", "date string or integer", None, QtGui.QApplication.UnicodeUTF8))
        self.orderField.setObjectName(_fromUtf8("orderField"))
        self.verticalLayout_2.addWidget(self.orderField)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_6 = QtGui.QLabel(self.tab1)
        self.label_6.setText(QtGui.QApplication.translate("PointsToPaths", "Date format (required if order field is a datetime string)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.dateFormat = QtGui.QLineEdit(self.tab1)
        self.dateFormat.setEnabled(True)
        self.dateFormat.setObjectName(_fromUtf8("dateFormat"))
        self.verticalLayout.addWidget(self.dateFormat)
        self.label = QtGui.QLabel(self.tab1)
        self.label.setText(QtGui.QApplication.translate("PointsToPaths", "Example:  if datetime string = 2011-01-01T00:01", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.tab1)
        self.label_2.setText(QtGui.QApplication.translate("PointsToPaths", "                      then format = %Y-%m-%dT%H:%M", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setContentsMargins(-1, 6, -1, -1)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_9 = QtGui.QLabel(self.tab1)
        self.label_9.setText(QtGui.QApplication.translate("PointsToPaths", "Gap period (in minutes if order field is a datetime string)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_7.addWidget(self.label_9)
        self.gapPeriod = QtGui.QLineEdit(self.tab1)
        self.gapPeriod.setInputMethodHints(QtCore.Qt.ImhNone)
        self.gapPeriod.setObjectName(_fromUtf8("gapPeriod"))
        self.verticalLayout_7.addWidget(self.gapPeriod)
        self.verticalLayout_5.addLayout(self.verticalLayout_7)
        self.horizontalGroupBox = QtGui.QGroupBox(self.tab1)
        self.horizontalGroupBox.setTitle(QtGui.QApplication.translate("PointsToPaths", "Output shapefile", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalGroupBox.setObjectName(_fromUtf8("horizontalGroupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.outShape = QtGui.QLineEdit(self.horizontalGroupBox)
        self.outShape.setObjectName(_fromUtf8("outShape"))
        self.horizontalLayout.addWidget(self.outShape)
        self.btnBrowse = QtGui.QPushButton(self.horizontalGroupBox)
        self.btnBrowse.setText(QtGui.QApplication.translate("PointsToPaths", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBrowse.setObjectName(_fromUtf8("btnBrowse"))
        self.horizontalLayout.addWidget(self.btnBrowse)
        self.verticalLayout_5.addWidget(self.horizontalGroupBox)
        self.tabWidget.addTab(self.tab1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.textBrowser = QtGui.QTextBrowser(self.tab_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 381, 251))
        self.textBrowser.setHtml(QtGui.QApplication.translate("PointsToPaths", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">%d      Day of the month as a decimal number</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">%f       Microsecond as a decimal number</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">%H      Hour (24-hour clock) as a decimal number</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">%I        Hour (12-hour clock) as a decimal number</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">%j        Day of the year as a decimal number</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">%m     Month as a decimal number</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">%M     Minute as a decimal number</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">%p      Locale’s equivalent of either AM or PM</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">%S      Second as a decimal number</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">%y      Year without century as a decimal number</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">%Y      Year with century as a decimal number</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">%z      UTC offset in the form +HHMM or -HHMM    </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(10, 290, 361, 91))
        self.label_7.setText(QtGui.QApplication.translate("PointsToPaths", "This information was acquired from the Python Software Foundation, v2.7 Documentation. For more details about Python date formatting, visit:\n"
"\n"
"http://docs.python.org/library/datetime.html", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 351, 461))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setText(QtGui.QApplication.translate("PointsToPaths", "PointsToPaths is intended to help in processing data collected from animal tracking devices (though it may be useful for many other applications). This tool takes a string or integer field to group points by common values within that field.  The points in each group translate to the verticies of a line, and the order of the verticies is determined by a numeric field or a string field representing a date.\n"
"\n"
"Each group of verticies can be divided into multiple lines by specifying a gap period. The gap period will end a line if the difference in the order value between two consecutive points exceeds the gap value. If the order field is a datetime, then the gap units are in minutes.\n"
"\n"
"This plugin is based largely on the Points2One plugin written by Pavol Kapusta and Goyo Diaz as well as ftools written by Carson Farmer.\n"
"\n"
"If you find this plugin helpful or have ideas about\n"
"how it might be improved, please let me know.\n"
"\n"
"Cyrus:  cyrusnhiatt@gmail.com", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.verticalLayout_6.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(PointsToPaths)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_6.addWidget(self.buttonBox)

        self.retranslateUi(PointsToPaths)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PointsToPaths.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PointsToPaths.reject)
        QtCore.QMetaObject.connectSlotsByName(PointsToPaths)
        PointsToPaths.setTabOrder(self.outShape, self.btnBrowse)
        PointsToPaths.setTabOrder(self.btnBrowse, self.buttonBox)

    def retranslateUi(self, PointsToPaths):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QtGui.QApplication.translate("PointsToPaths", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("PointsToPaths", "Date Format Reference", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("PointsToPaths", "About", None, QtGui.QApplication.UnicodeUTF8))

