import PySimpleGUI as sg 
import Cliente
from BaseView import BaseView

# View do padrão MVC
class ClienteView(BaseView):
    def __init__(self, controlador):
        super().__init__("Consulta de clientes", controlador)
        self.__largura_resposta = 40 #aux. var

    def tela_consulta(self):
        linha0 = [sg.Text('Digite o código ou o nome do cliente e clique na ação desejada:')]
        linha1 = [sg.Text('Código:'), sg.InputText('', key='codigo')]
        linha2 = [sg.Text('Nome:'), sg.InputText('', key='nome')]
        linha3 = [sg.Button('Cadastrar'), sg.Button('Consultar'), sg.Button('Remover')]
        linha3 += [sg.Button('Listar'), sg.Button('Exportar'), sg.Button('Importar')]
        linha4 = [sg.Text('', size=(self.__largura_resposta, 1), key='resultado')]
        
        self.__container = [linha0, linha1, linha2, linha3, linha4]
        self.update_layout(self.__container)


    def prepara_area_texto(self, nlinhas):
        self.window.Element('resultado').set_size((self.__largura_resposta, nlinhas))

    def mostra_resultado(self, resultado): 
        nlinhas = resultado.count("\n")+1
        self.prepara_area_texto(nlinhas)
        self.window.Element('resultado').Update(resultado)

    def limpa_dados(self):
        self.window.Element('nome').Update('')
        self.window.Element('codigo').Update('')