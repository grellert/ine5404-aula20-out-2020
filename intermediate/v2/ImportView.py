import PySimpleGUI as sg 
import Cliente
from BaseView import BaseView

# View do padrão MVC
class ImportView(BaseView):
    def __init__(self, controlador):
        super().__init__("Importação de clientes", controlador)

    def tela_consulta(self):
        self.__container =  [[sg.In(key="caminho_import") ,sg.FileBrowse(file_types=(("*.pkl"),))],
                            [sg.Button("importar")] ]

        self.update_layout(self.__container)

