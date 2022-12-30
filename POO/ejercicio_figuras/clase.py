class PerimetroArea:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    #metodos
    def perimetro(self):
        return (2 * self.base) + (2 * self.altura)