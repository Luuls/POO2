class ComandoInvalidoException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Este comando eh invalido!');
