from abc import ABC, abstractmethod

class Estrategia(ABC):
    @abstractmethod
    def executar_estrategia_inicial(self):
        pass

    @abstractmethod
    def executar_estrategia_final(self):
        pass

class Nuclear(Estrategia): 
    def executar_estrategia_inicial(self):
        print("Recuar tropas; Propor cooperação econômica.")

    def executar_estrategia_final(self):
        print("Desarmar o inimigo")


class GrandeExercito(Estrategia):
    def executar_estrategia_inicial(self):
        print("Atacar pelo norte; Vizinho atacar pelo sul.")
        
    def executar_estrategia_final(self):
        print("Dividir benefícios; Dividir custo de reconstrução.")


class Fragil(Estrategia):
    def executar_estrategia_inicial(self):
        print("Plantar evidências; Lançar bombas; Derrubar governo.")
    
    def executar_estrategia_final(self):
        print("Estabelecer um governo amigo.")


class Guerra:
    def __init__(self, tipo_de_inimigo):
        if tipo_de_inimigo == "Nuclear":
            self.estrategia = Nuclear()
        elif tipo_de_inimigo == "Grande Exército":
            self.estrategia = GrandeExercito()
        elif tipo_de_inimigo == "Frágil":
            self.estrategia = Fragil()
        else:
            raise ValueError("Força inimiga inválida")

    def iniciarGuerra(self):
        print("Guerra declarada")
        self.estrategia.executar_estrategia_inicial()

    def finalizarGuerra(self):
        print("Guerra concluída")
        self.estrategia.executar_estrategia_final()

def main():
    simulacao = Guerra("Grande Exército")

    simulacao.iniciarGuerra()

    simulacao.finalizarGuerra()

if __name__ == "__main__":
    main()
    