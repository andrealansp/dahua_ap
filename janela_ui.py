# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\a.alves\Desktop\Projetos\dahua_app\janela.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1024, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(1024, 500))
        Dialog.setMaximumSize(QtCore.QSize(1024, 600))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\a.alves\\Desktop\\Projetos\\dahua_app\\favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(430, 460, 181, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.qpb_processo = QtWidgets.QProgressBar(Dialog)
        self.qpb_processo.setGeometry(QtCore.QRect(450, 410, 561, 23))
        self.qpb_processo.setProperty("value", 24)
        self.qpb_processo.setObjectName("qpb_processo")
        self.pontoLabel = QtWidgets.QLabel(Dialog)
        self.pontoLabel.setGeometry(QtCore.QRect(30, 10, 80, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pontoLabel.setFont(font)
        self.pontoLabel.setObjectName("pontoLabel")
        self.pontoComboBox = QtWidgets.QComboBox(Dialog)
        self.pontoComboBox.setGeometry(QtCore.QRect(30, 50, 391, 39))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pontoComboBox.sizePolicy().hasHeightForWidth())
        self.pontoComboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pontoComboBox.setFont(font)
        self.pontoComboBox.setObjectName("pontoComboBox")
        self.resultadoLabel = QtWidgets.QLabel(Dialog)
        self.resultadoLabel.setGeometry(QtCore.QRect(450, 10, 136, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.resultadoLabel.setFont(font)
        self.resultadoLabel.setObjectName("resultadoLabel")
        self.qte_resultado = QtWidgets.QPlainTextEdit(Dialog)
        self.qte_resultado.setGeometry(QtCore.QRect(450, 50, 551, 351))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.qte_resultado.setFont(font)
        self.qte_resultado.setObjectName("qte_resultado")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 140, 391, 298))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.qpb_pegar_seriais = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qpb_pegar_seriais.sizePolicy().hasHeightForWidth())
        self.qpb_pegar_seriais.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.qpb_pegar_seriais.setFont(font)
        self.qpb_pegar_seriais.setObjectName("qpb_pegar_seriais")
        self.verticalLayout.addWidget(self.qpb_pegar_seriais)
        self.qpb_set_automantain = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qpb_set_automantain.sizePolicy().hasHeightForWidth())
        self.qpb_set_automantain.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.qpb_set_automantain.setFont(font)
        self.qpb_set_automantain.setObjectName("qpb_set_automantain")
        self.verticalLayout.addWidget(self.qpb_set_automantain)
        self.qpb_get_aicode = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qpb_get_aicode.sizePolicy().hasHeightForWidth())
        self.qpb_get_aicode.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.qpb_get_aicode.setFont(font)
        self.qpb_get_aicode.setObjectName("qpb_get_aicode")
        self.verticalLayout.addWidget(self.qpb_get_aicode)
        self.qpb_get_firmewares = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qpb_get_firmewares.sizePolicy().hasHeightForWidth())
        self.qpb_get_firmewares.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.qpb_get_firmewares.setFont(font)
        self.qpb_get_firmewares.setObjectName("qpb_get_firmewares")
        self.verticalLayout.addWidget(self.qpb_get_firmewares)
        self.qpb_configurar_fonte = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.qpb_configurar_fonte.setFont(font)
        self.qpb_configurar_fonte.setObjectName("qpb_configurar_fonte")
        self.verticalLayout.addWidget(self.qpb_configurar_fonte)
        self.qpb_cancelar_operacao = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.qpb_cancelar_operacao.setFont(font)
        self.qpb_cancelar_operacao.setObjectName("qpb_cancelar_operacao")
        self.verticalLayout.addWidget(self.qpb_cancelar_operacao)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 100, 391, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.resultadoLabel_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.resultadoLabel_2.setFont(font)
        self.resultadoLabel_2.setObjectName("resultadoLabel_2")
        self.horizontalLayout.addWidget(self.resultadoLabel_2)
        self.qcb_todas_cameras = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.qcb_todas_cameras.setObjectName("qcb_todas_cameras")
        self.horizontalLayout.addWidget(self.qcb_todas_cameras)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "DAHUA GET DATA"))
        self.label.setText(_translate("Dialog", "Desenvolvido por André Alves"))
        self.pontoLabel.setText(_translate("Dialog", "Ponto"))
        self.resultadoLabel.setText(_translate("Dialog", "Resultado"))
        self.qpb_pegar_seriais.setText(_translate("Dialog", "Coletar Seriais"))
        self.qpb_set_automantain.setText(_translate("Dialog", "Configurar Auto Maintain"))
        self.qpb_get_aicode.setText(_translate("Dialog", "Coletar Info Auto register"))
        self.qpb_get_firmewares.setText(_translate("Dialog", "Coletar Firmewares"))
        self.qpb_configurar_fonte.setText(_translate("Dialog", "Configurar Fontes"))
        self.qpb_cancelar_operacao.setText(_translate("Dialog", "Cancelar Operação"))
        self.resultadoLabel_2.setText(_translate("Dialog", "Ações"))
        self.qcb_todas_cameras.setText(_translate("Dialog", "Aplicar em todas as câmeras"))
