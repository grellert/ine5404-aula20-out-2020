import PySimpleGUI as sg 

# View do padrão MVC
class ExportView:
    def __init__(self):
        self.__container = []
        self.__largura_resposta = 40 #aux. var
        self.__window = sg.Window('Exportação de clientes', self.__container ,font=('Helvetica', 14))

    def tela_consulta(self):
        linha0 = [sg.Text('Digite o nome do arquivo que quer salvar:')]
        linha1 = [sg.InputText('', key='caminho_export')]
        linha2 = [sg.Button('Exportar')]

        self.__container = [linha0, linha1, linha2]
        self.__window = sg.Window('Exportação de clientes', self.__container ,font=('Helvetica', 14))

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()

