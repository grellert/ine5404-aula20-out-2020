import PySimpleGUI as sg 
import Cliente

# View do padrão MVC
class ImportView:
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__container = []
        self.__largura_resposta = 40 #aux. var
        self.__window = sg.Window('Importação de clientes', self.__container ,font=('Helvetica', 14))

    def tela_consulta(self):
        print('?')
        self.__container =  [[sg.In(key="caminho_import") ,sg.FileBrowse(file_types=(("*.pkl"),))],
                            [sg.Button("importar")] ]

        self.__window = sg.Window('Exportação de clientes', self.__container ,font=('Helvetica', 14))

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()

