from ClienteView import ClienteView
from ExportView import ExportView
from ImportView import ImportView
from Cliente import Cliente
from ClienteDAO import ClienteDAO
import PySimpleGUI as sg 

class ClienteController:
    def __init__(self):
        self.__telaCliente = ClienteView(self)
        self.__telaExport = ExportView(self)
        self.__telaImport = ImportView(self)
        self.__clienteDAO = ClienteDAO()

        sg.theme('Reddit')

    def inicia(self):
        self.__telaCliente.tela_consulta()
        
        # Loop de eventos
        rodando = True
        export_active = False
        import_active = False
        resultado = ''
        while rodando:
            if export_active:
                export_active = self.handle_export()
            elif import_active:
                import_active = self.handle_import()
            else:
                event, values = self.__telaCliente.le_eventos()

                if event == sg.WIN_CLOSED:
                    self.__telaCliente.fim()
                    break
                else:
                    try:
                        if event == 'Cadastrar':
                            codigo = int(values['codigo'])
                            nome = values['nome']
                            resultado = self.adiciona_cliente(codigo, nome)
                        elif event == 'Consultar':
                            codigo = self.get_codigo(values)
                            resultado = self.busca_codigo(codigo)
                        elif event == 'Remover':
                            codigo = self.get_codigo(values)
                            resultado = self.remove_cliente(codigo)
                        elif event == 'Listar':
                            resultado = self.clientes_to_string()
                        elif event == 'Exportar':
                            self.__telaExport.tela_consulta()
                            export_active = True 
                        elif event == 'Importar':
                            self.__telaImport.tela_consulta()
                            import_active = True 


                    except ValueError:
                        resultado = 'Código deve ser um número inteiro!'
                    except KeyError:
                        resultado = 'Valor não cadastrado!'
                    except NameError:
                        resultado = 'Digite ao menos um campo!'

                if resultado != '':
                    dados = str(resultado)
                    self.__telaCliente.mostra_resultado(dados)
                    self.__telaCliente.limpa_dados()


    # se o cadastro não existir, levanta key error
    def busca_codigo(self, codigo):
        return self.__clienteDAO.get(codigo)
    
    def busca_nome(self, nome):
        for key, val in self.__clientes.items():
            if val.nome == nome:
                return key 

        raise KeyError

    # retona código, buscando pelo nome se necessários
    # se o cadastro não existir, levanta NameError
    def get_codigo(self, values):
        if values['codigo'] != '':
            codigo = int(values['codigo'])
        elif values['nome'] != '':
            codigo = self.busca_nome(values['nome'])
        return codigo

    # cria novo OBJ cliente e adiciona ao dict
    def adiciona_cliente(self, codigo, nome):
        if nome == '':
            return 'Campo nome vazio!'
        elif self.__clienteDAO.add(Cliente(codigo, nome)):
            return 'Cliente adicionado com sucesso'
        else:
            return 'Código já cadastrado!'

    # remove cliente do dict
    def remove_cliente(self, codigo):
        if self.__clienteDAO.remove(codigo):
            return 'Cliente removido com sucesso'
        else:
            return 'Código não cadastrado!'

    def clientes_to_string(self):
        clientes = [_[1] for _ in self.__clienteDAO.get_all()]
        return '\n'.join([str(c) for c in clientes])

    def handle_export(self):
        event_exp, values_exp = self.__telaExport.le_eventos()

        export_active = True

        if event_exp == sg.WIN_CLOSED:
            self.__telaExport.fim()
            export_active = False
        elif event_exp == 'Exportar':
                path = values_exp['caminho_export']
                self.__clienteDAO.set_data_source(path)
                self.__telaExport.fim()
                export_active = False

        return export_active

    def handle_import(self):
        event_exp, values_exp = self.__telaImport.le_eventos()

        import_active = True

        if event_exp == sg.WIN_CLOSED:
            self.__telaImport.fim()
            import_active = False
        elif event_exp == 'importar':
                path = values_exp['caminho_import']
                self.__clienteDAO.import_source(path)
                self.__telaImport.fim()
                import_active = False

        return import_active