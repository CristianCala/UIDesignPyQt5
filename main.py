import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import (QFont, QIcon, QPalette, QBrush, QColor, QPixmap,
						 QRegExpValidator, QImage)
from PyQt5.QtCore import (Qt, QDir, pyqtSignal, QFile, QByteArray,QIODevice,QBuffer,QDate, QTime, QSize, QTimer, QRect, QRegExp, QTranslator,QLocale,
						  QLocale, QLibraryInfo, QFileInfo, QDir,QPropertyAnimation,QTranslator,QAbstractAnimation, QLocale)
from PyQt5.QtWidgets import  (QApplication, QMainWindow, QWidget, QDialog, QTableWidget, QMenu, 
							 QTableWidgetItem, QAbstractItemView, QLineEdit, QPushButton,
							 QActionGroup, QAction, QMessageBox, QFrame, QStyle, QGridLayout,
							 QVBoxLayout, QHBoxLayout, QLabel, QToolButton, QGroupBox,
							 QDateEdit, QComboBox, QCheckBox, QTextEdit, QRadioButton, QScrollArea, QFileDialog,QGraphicsEffect, QVBoxLayout, 
							 QGraphicsDropShadowEffect, QGraphicsBlurEffect)


class main(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self)
		self.setWindowTitle("Main Ui")
		# self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
		self.setFixedSize(800, 600)
		# self.setStyleSheet("QMainWindow{\n"
		# "background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(220,20,60,1), stop:1 rgba(102,0,0,1));\n"
		# "border-radius: 22px;"
		# "}\n"
		# "")
		self.setStyleSheet("QMainWindow{\n"
		"background-image: url(ui.png);"
		"}\n"
		"")
		self.initUi()


	def initUi(self):
		print("pana")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = main()
	interface.show()
	app.exec_()