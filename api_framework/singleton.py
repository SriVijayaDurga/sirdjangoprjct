import os
from jproperties import Properties

CONSTANT_PATH = os.environ.get('CONSTANTPATH')
print(CONSTANT_PATH)
configs = Properties()

with open(CONSTANT_PATH, 'rb') as config_file:
    configs.load(config_file)


class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance is None:
            Singleton.__instance = configs
        return Singleton.__instance


constants = Singleton.getInstance()


def getConstant(key):
    return constants.get(key).data

