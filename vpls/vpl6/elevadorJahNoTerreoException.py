class ElevadorJahNoTerreoException(Exception):
    def __init__(self):
        Exception.__init__(self, "Elevador ja esta no terreo!")

