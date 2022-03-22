from plurality import Plurality

p = Plurality(['laura', 'camille', 'erica'])

election = p.vote('laura')
election = p.vote('camille')
election = p.vote('erica')
election = p.vote('laura')

print(p.showWinner())

