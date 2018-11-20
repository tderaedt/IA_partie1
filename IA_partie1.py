# Tomy Deraedt, BA1 INFO , groupe 2 #

from random import random, choice
def eps_greedy(M):
    r = random()                # r est un chiffre random entre 0 et 1
    if r >= eps :               # si r est plus petit ou égale à eps faire ce qui suis/ eps-greedy
        all_probas = list()     # crée une liste vide pour toute les probabilitée
        for i in range(len(M)):
            all_probas.append(M[i][1])
        max_proba = max(all_probas)        # probalité max trouvé entre autre grâce à la fonction max
        all_choices = list()
        for i in range(len(M)):
            if max_proba == M[i][1] :
                all_choices.append(M[i][0])
        max_choice = choice(all_choices)
        s_max = max_choice
        return s_max
    else :
        s,p = choice(M)

    return max_choices


# Stratégie d'apprentissage


from eps_greedy
def Monte_carlo(alpha,r,Psi) :
    Psi = (1-int(alpha**i)*(Psi+alpha*i)*r)

    if r = 1:
        win
    else :
        loose
    return r


def TD(0),(alpha,p,s,r): # "Temporal Difference leraning : s = état après coup / ***continuer
    last = [s_max,max_proaba]
    last = ((1-alpha)*last+alpha*r)
        while partie != "win"
            if r == 1 :
                partie ="win"
            else :
                 partie = "loose"


def Qlearning(alpha,p,s,r) : # same of TD
    last =[s_max,max_proba]
    last = ((1 - alpha)*last+alpha + ps*
    partie = "win"

    while partie != "win"
        if r = 1:
            partie = "win"
        else :
            r = 0
            partie = loose


        # FONCTION A IMPLEMENTER

def makeMove(M,last,strategy,eps,alpha) :
    M[]                                  # list avec s un mouvement possible pour le joueur(=> état après coup possible) p = estimation actuelle de la probalité de gagner à partir de cet états
    last = s_max,max_proba]                         # s = état après coup précédent par le joueur/ p = le m^^eme que pour "M"/ if player haven't play "last" = None
    stategy = Monte_carlo or TD or Qlearning           # strategie d'apprentissage
    eps = eps in eps_greedy                                              # ensemble epsylon
    alpha =                                            # learning rate/ valeur de akoha dans l'apprentissage
    if M[]= (0,0) :
        Move = stategy
    return Move

def endGame(won,history,strategy,alpha):
    r = (0 or 1)
    if won :
        r = 1
    else :
        r = 0
        if strategy == TD or strategy == Qlearning :
            history[-1][1] = (1 - alpha) * history[-1][1]+ alpha*r
            or Monte_carlo for i in range(len(history)):
                history[-1][1] = (1 - (alpha**1))* history[-1][1]+ (alpha**1)*r
    return None