class ElevadorJahNoUltimoAndarException(Exception):
    def __init__(self):
        Exception.__init__(self, 'O elevador ja esta no ultimo andar!')

