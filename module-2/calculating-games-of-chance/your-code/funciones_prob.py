def odds(p):
    return(p/(1-p))

def prob(succ, total): 
    return succ/total

def print_prob(p): 
    return '{:.2f}%'.format(100 * p)

def print_odd(a, s): 
    return '{} : {}'.format(a, s-a)
