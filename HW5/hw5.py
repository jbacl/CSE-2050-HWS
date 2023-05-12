def solveable(p_idxs, k_idx):
    """Returns True (false) if all pawn locations can be capture by sequential knight moves"""
    # 1) Base case - is the puzzle solved?
    if p_idxs == set():
        return True
    # 2) Find all valid_moves
    all_valid_moves = valid_moves(k_idx)
    bool = False
       # 3) Try all valid_moves
    for move in all_valid_moves:
        if move in p_idxs:
            p_idxs.remove(move)
            outcome = solveable(p_idxs, move)
            if outcome is True:
                bool = True
                break
            else:
                p_idxs.add(move)
                continue
   
    # 4) If nothing worked in step 3, there's no solution with the knight in this position
    return bool or len(p_idxs) == 0



def valid_moves(k_idx):
    """Returns set of all valid moves from k_idx, assuming an 8x8 chess board"""
    y_val = k_idx[0]
    x_val = k_idx[1]

    y_list = [-2, -2, -1, -1, 1, 1, 2, 2]
    x_list = [-1, 1, -2, 2, -2, 2, -1, 1]

    valid_moves_set = set()

    for i in range(len(y_list)):
        if y_val + y_list[i] < 0 or y_val + y_list[i] > 7:
            pass
        elif x_val + x_list[i] > 7 or x_val + x_list[i] < 0:
            pass
        else:
            valid_moves_set.add((y_val + y_list[i]), (x_val + x_list[i]))
    
    return valid_moves_set
