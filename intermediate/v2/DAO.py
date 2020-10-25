from abc import ABC
import pickle
import sys

class DAO(ABC):
    def __init__(self, datasource = ''):
        self.datasource = datasource
        self.objCache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()
    
    def  __dump(self):
        f = open(self.datasource, 'wb')
        pickle.dump(self.objCache, f)
        f.close()
    
    def __load(self):
        f = open(self.datasource, 'rb')
        self.objCache = pickle.load(f)
        f.close()

    def add(self, key, obj):
        if key in self.objCache.keys():
            return False
        self.objCache[key] = obj
        self.__dump()
        return True

    def remove(self, key):
        try:
            self.objCache.pop(key)
            self.__dump()
            return True
        except KeyError:
            print('Chave não encontrada', f = sys.stderr)
            return False

    def get(self, key):
        try:
            return self.objCache[key]
        except KeyError:
            print('Chave não encontrada', f = sys.stderr)
            return False

    def get_all(self):
        return self.objCache.items()

    def set_data_source(self, path: str):
        if '.pkl' not in path:
            path = path + '.pkl'
        f = open(path, 'wb')
        pickle.dump(self.objCache, f)
        f.close()
    

    def import_source(self, path: str):
        f = open(path, 'rb')
        objc = pickle.load(f)
        f.close()
        for cliente in objc.values():
            self.objCache[cliente.codigo] = cliente
        self.__dump()
