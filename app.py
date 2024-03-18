import random
import sys
from time import sleep

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

from classes.helpers import Funcoes


class Janela(QDialog):
    def __init__(self) -> None:
        super(Janela, self).__init__()
        loadUi("janela.ui", self)
        self.cancelar = True
        self._portas = [9050, 9051, 9052, 9053, 9060, 9061, 9070, 9071, 9072, 9073]
        self._help = Funcoes(self)
        self._sites = self._help.pegalistaip()
        self.inicializarformulario()

    """ Propriedades da classe Janela """

    @property
    def sites(self):
        return self._sites

    @sites.setter
    def sites(self, value):
        self._sites = value

    @property
    def portas(self):
        return self._portas

    @portas.setter
    def portas(self, value):
        self._portas = value

    @property
    def cancelar(self):
        return self._cancelar

    @cancelar.setter
    def cancelar(self, value):
        self._cancelar = not value

    def inicializarformulario(self) -> None:
        """Método para Iniciar os Slots and Signals
        Não retorna dados.
        """
        self.carrega_dados()
        self.open()
        self.qpb_processo.setValue(0)
        self.qpb_pegar_seriais.clicked.connect(self.carregar_seriais)
        self.qpb_set_automantain.clicked.connect(self.definir_automantain)
        self.qpb_get_aicode.clicked.connect(self.pegar_portas_autoregister)
        self.qpb_get_firmewares.clicked.connect(self.pegar_firmewares)
        self.qpb_configurar_fonte.clicked.connect(self.definir_fontes)
        self.qpb_cancelar_operacao.clicked.connect(self.cancelar_operacao)

    def open(self) -> None:
        self.show()

    def carrega_dados(self) -> None:
        """Esse método carrega o ComboBox com os dados carregados na propriedade sites"""
        for opcao in self.sites:
            self.pontoComboBox.addItem(f"{opcao}")

    def carregar_seriais(self) -> None:
        """Slot que carrega os dados dos seriais."""
        self._help.coletar_seriais()

    def definir_automantain(self) -> None:
        """Slot que carrega os dados dos seriais"""
        self._help.setar_reset_cameras_contexto()

    def pegar_portas_autoregister(self) -> None:
        """Slot que carrega os dados das portas do auto register"""
        self._help.coletar_auto_register()

    def pegar_firmewares(self) -> None:
        """Slot que carrega os dados dos firmewares das câmeras"""
        self._help.coletar_firmewares()

    def definir_fontes(self) -> None:
        """Slot que configura as fontes para os fluxo principal e fluxo secundário."""
        self._help.setar_fontes()

    def cancelar_operacao(self) -> None:
        self.cancelar = self.cancelar
        print(self.cancelar)


app = QApplication(sys.argv)
janela = Janela()
target = janela.open()
sys.exit(app.exec_())
