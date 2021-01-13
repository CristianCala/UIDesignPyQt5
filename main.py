# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       main.py
# Autores:      Cristian Cala Sierra
# License:      MIT License
# ----------------------------------------------------------------------------
import sys
from vista import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import (QRect)
from PyQt5.QtWidgets import  (QApplication, QMainWindow, QLineEdit, QPushButton,
	QFrame,QLabel,QCheckBox, QGraphicsDropShadowEffect)


class main(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self)
		self.setWindowTitle("Main Ui")
		self.setFixedSize(800, 600)
		self.setStyleSheet(estiloFondo)

		self.initUi()

	def initUi(self):


		globalFont = (QtGui.QFont("Roboto", 16, QtGui.QFont.Bold))
		titulofont = (QtGui.QFont("Roboto", 20, QtGui.QFont.Bold))
		font_line = (QtGui.QFont("Roboto", 12, QtGui.QFont.Bold))
		fontCondiciones = (QtGui.QFont("Roboto", 11, QtGui.QFont.Bold))

		self.frameizquierda = QFrame(self)
		self.frameizquierda.setStyleSheet(estiloFrame)
		self.frameizquierda.setGeometry(QRect(0,0,400,600))
		self.sombra = QGraphicsDropShadowEffect()
		self.sombra.setBlurRadius(100)
		self.frameizquierda.setGraphicsEffect(self.sombra)

		self.encabezado = QLabel(self)
		self.encabezado.setStyleSheet(estiloTitulo)
		self.encabezado.setGeometry(QRect(460,50,200,100))
		self.encabezado.setText("REGISTRO")
		self.encabezado.setFont(titulofont)
		self.encabezado.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

		self.boton1 = QPushButton(self)
		self.boton1.setStyleSheet(estiloR)
		self.boton1.setGeometry(QRect(650,10,70,30))
		self.boton1.setFont(fontCondiciones)
		self.boton1.setText("registro")
		self.sombra3 = QGraphicsDropShadowEffect()
		self.sombra3.setBlurRadius(100)
		self.boton1.setGraphicsEffect(self.sombra3)

		self.boton2 = QPushButton(self)
		self.boton2.setStyleSheet(estiloD)
		self.boton2.setGeometry(QRect(720,10,70,30))
		self.boton2.setFont(fontCondiciones)
		self.boton2.setText("inicio")
		self.sombra4 = QGraphicsDropShadowEffect()
		self.sombra4.setBlurRadius(100)
		self.boton2.setGraphicsEffect(self.sombra4)

		self.nombre = QLabel(self)
		self.nombre.setStyleSheet(estiloNombre)
		self.nombre.setGeometry(QRect(450,100,100,100))
		self.nombre.setText("NOMBRE")
		self.nombre.setFont(globalFont)
		self.nombre.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

		self.nombre_edit = QLineEdit(self)
		self.nombre_edit.setStyleSheet(estiloLine)
		self.nombre_edit.setFont(font_line)
		self.nombre_edit.setGeometry(QRect(460, 165,100,30))
		self.nombre_edit.setPlaceholderText("Nombre")

		self.apellido = QLabel(self)
		self.apellido.setStyleSheet(estiloNombre)
		self.apellido.setGeometry(QRect(625,100,100,100))
		self.apellido.setText("APELLIDO")
		self.apellido.setFont(globalFont)
		self.apellido.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

		self.apellido_edit = QLineEdit(self)
		self.apellido_edit.setStyleSheet(estiloLine)
		self.apellido_edit.setFont(font_line)
		self.apellido_edit.setGeometry(QRect(630,165,100,30))
		self.apellido_edit.setPlaceholderText("Apellido")

		self.contrasena = QLabel(self)
		self.contrasena.setStyleSheet(estiloNombre)
		self.contrasena.setFont(globalFont)
		self.contrasena.setGeometry(QRect(450,200,150,100))
		self.contrasena.setText("CONTRASEÑA")
		self.contrasena.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

		self.contrasena_edit = QLineEdit(self)
		self.contrasena_edit.setStyleSheet(estiloLine)
		self.contrasena_edit.setFont(font_line)
		self.contrasena_edit.setGeometry(QRect(460,265,300,30))
		self.contrasena_edit.setPlaceholderText("Contraseña")

		self.email = QLabel(self)
		self.email.setStyleSheet(estiloNombre)
		self.email.setFont(globalFont)
		self.email.setGeometry(QRect(465,300,100,100))
		self.email.setText("Email")

		self.email_edit = QLineEdit(self)
		self.email_edit.setStyleSheet(estiloLine)
		self.email_edit.setFont(font_line)
		self.email_edit.setGeometry(QRect(465,365,300,30))
		self.email_edit.setPlaceholderText("Email@ejemplo.com")

		self.chequer = QCheckBox(self)
		self.chequer.setGeometry(QRect(465,400,20,30))
		self.chequer.setStyleSheet(estiloCheck)

		self.condiciones = QLabel(self)
		self.condiciones.setStyleSheet(estilo_condiciones)
		self.condiciones.setFont(fontCondiciones)
		self.condiciones.setText("Aceptar términos y condiciones")
		self.condiciones.setGeometry(QRect(490,365,250,100))

		self.btn_registro = QPushButton(self)
		self.btn_registro.setStyleSheet(estiloBoton)
		self.btn_registro.setGeometry(QRect(460,450,300,50))
		self.btn_registro.setFont(globalFont)
		self.btn_registro.setText("Registrarse")
		self.sombra2 = QGraphicsDropShadowEffect()
		self.sombra2.setBlurRadius(100)
		self.btn_registro.setGraphicsEffect(self.sombra2)

		self.copyrigth = QLabel(self)
		self.copyrigth.setStyleSheet(estilo_condiciones)
		self.copyrigth.setFont(fontCondiciones)
		self.copyrigth.setText("by Cristian Cala ❤️")
		self.copyrigth.setGeometry(QRect(660,530,150,100))

if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = main()
	interface.show()
	app.exec_()