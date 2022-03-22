class Plurality:

    def __init__ (self, candidatos, ):
        self.candidatos = candidatos #array

    def vote(self, nomeVoto):
        #check if name is in array
        inArray = False
        for element in self.candidatos:
                if element == nomeVoto:
                    inArray = True
        if inArray:
           
            # create dict with the candidates and the votes for each one
            candidatosVotos = dict.fromkeys(self.candidatos, 0)

            #add vote
            candidatosVotos[nomeVoto] += 1
            
            return candidatosVotos
            

        else:
            return 'invalid vote'

    def showWinner(candidatosVotos):
        winner = max(candidatosVotos, key = candidatosVotos.get)
        return winner 