class ProjetorAdapter:
    def __init__(self, projetor):
        self.projetor = projetor

    def liga(self):
        if isinstance(self.projetor, ProjetorSamsung):
            self.projetor.Ligar()
        elif isinstance(self.projetor, ProjetorLG):
            self.projetor.Habilitar(0)

class ProjetorSamsung:
    def Ligar(self):
        print("Projetor Samsung ligado")

class ProjetorLG:
    def Habilitar(self, timer):
        if timer == 0:
            print("Projetor LG ligado imediatamente")
        else:
            print("Projetor LG ligado após", timer, "minutos")

class SistemaControleProjetores:
    def init(self, projetor):
        projetor.liga()


sistema = SistemaControleProjetores()

projetor_samsung = ProjetorSamsung()
adapter_samsung = ProjetorAdapter(projetor_samsung)
sistema.init(adapter_samsung)

projetor_lg = ProjetorLG()
adapter_lg = ProjetorAdapter(projetor_lg)
sistema.init(adapter_lg)