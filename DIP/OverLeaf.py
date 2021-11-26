# A abstração da classe Strategy
class Strategy(ABC):
    
    def execute(self, picture: np.array) -> np.array:
        return picture

    pass

# Algoritmo que adiciona a imagem o efeito Cinza
class Grayscale(Strategy):

    def execute(self, picture: np.array) -> np.array:
        # Implementação do método para conversão para escala cinza

    pass

# Algoritmo que adiciona a imagem o efeito Sharpen
class Sharpen(Strategy):

    def execute(self, picture: np.array) -> np.array:
        # Implementação do método para conversão a escala sharpen

    pass

# (...)