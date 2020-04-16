def check(deck,fr,to):
    #print(deck[fr.y][fr.x]["text"])
    if deck[fr.y][fr.x]["text"]==chr(9823):     #black pawn
        if to.y<=fr.y:
            return False
        elif fr.y == 1:
            if (to.y-fr.y)>2:
                return False
            elif ((to.y-fr.y)==2 and len(deck[to.y][to.x]["text"])==1):
                return False
        elif (to.y-fr.y)!=1:
            return False
        elif (len(deck[to.y][to.x]["text"])==1 and
              ord(deck[to.y][to.x]["text"])<9818 and
              ((to.x-fr.x)**2)**0.5 != 1):
            return False
        if (len(deck[to.y][to.x]["text"])==0 and fr.x != to.x):
            return False
    elif deck[fr.y][fr.x]["text"]==chr(9817):   #white pawn
        if to.y>=fr.y:
            return False
        elif fr.y == 6:
            if (fr.y-to.y)>2:
                return False
            elif ((fr.y-to.y)==2 and len(deck[to.y][to.x]["text"])==1):
                return False
        elif (fr.y-to.y)!=1:
            return False
        elif (len(deck[to.y][to.x]["text"])==1 and
              ord(deck[to.y][to.x]["text"])>=9818 and
              ((to.x-fr.x)**2)**0.5 != 1):
            return False
        if (len(deck[to.y][to.x]["text"])==0 and fr.x != to.x):
            return False

    elif deck[fr.y][fr.x]["text"]==chr(9820):   #black rook
        if not (to.x == fr.x or to.y == fr.y):
            return False
    elif deck[fr.y][fr.x]["text"]==chr(9814):   #white rook
        if not (to.x == fr.x or to.y == fr.y):
            return False
    elif deck[fr.y][fr.x]["text"]==chr(9822):   #black knight
        pass
    elif deck[fr.y][fr.x]["text"]==chr(9816):   #white knight
        pass
    elif deck[fr.y][fr.x]["text"]==chr(9821):   #black bishop
        pass
    elif deck[fr.y][fr.x]["text"]==chr(9815):   #white bishop
        pass
    elif deck[fr.y][fr.x]["text"]==chr(9818):   #black king
        pass
    elif deck[fr.y][fr.x]["text"]==chr(9813):   #white king
        pass
    elif deck[fr.y][fr.x]["text"]==chr(9819):   #black queen
        pass
    elif deck[fr.y][fr.x]["text"]==chr(9812):   #white queen
        pass
    return True
