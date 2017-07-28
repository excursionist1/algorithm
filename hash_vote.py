voted = {}
value = voted.get('tom')
voted = {}
def check_voter(name):
    if voted.get(name):
        print('get out!')
    else:
        voted[name] = True
        print('come on!')

check_voter('tom')
check_voter('james')
check_voter('tom')
check_voter('james')
