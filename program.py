#lets assume that we have grid of 3 by 3 showing our joystick 

# [ [TL] [T] [TR]
#   [L] [C] [R]
#]  [BL] [B] [BR]

#Legen T : Top C : Center R : right L:left

# Dictionary where the key is tuple of two integers 
# and the values are string that described the 
# postion in the grid 
NAME = {
    (0, 0): "top-left",
    (0, 1): "top",
    (0, 2): "top-right",
    (1, 0): "left",
    (1, 1): "center",
    (1, 2): "right",
    (2, 0): "bottom-left",
    (2, 1): "bottom",
    (2, 2): "bottom-right",
}


# This is the dictionary where shows that every each moves have what effect
# example your in center your postion is [1][1] and you wanna go up so the final 
#state is [0][1] so it shows that the up is (-1 , 0) it applies for all other moves as well
MOVES = {
    "up":    (-1,  0),
    "down":  ( 1,  0),
    "left":  ( 0, -1),
    "right": ( 0,  1),
}

# Grid bounds (3x3)
ROWS, COLS = 3, 3

def in_bounds(r , c) : 
    return 0 <= r < ROWS and 0<= c < COLS

def valid_moves_from(pos):
    """Return a dict of {direction: next_pos} for legal moves from pos."""
    r, c = pos
    moves = {}
    for direction, (dr, dc) in MOVES.items():
        nr, nc = r + dr, c + dc
        if in_bounds(nr, nc):
            moves[direction] = (nr, nc)
    return moves


def show_grid(pos):
    """Print the 3x3 grid and mark the current position with [*]."""
    r0, c0 = pos
    for r in range(ROWS):
        row_cells = []
        for c in range(COLS):
            label = NAME[(r, c)]
            # Keep labels short for a compact grid
            short = {
                "top-left":"TL", "top":"T", "top-right":"TR",
                "left":"L", "center":"C", "right":"R",
                "bottom-left":"BL", "bottom":"B", "bottom-right":"BR"
            }[label]
            if (r, c) == (r0, c0):
                row_cells.append(f"[{short}*]")  # mark current spot
            else:
                row_cells.append(f"[{short} ]")
        print(" ".join(row_cells))
    print()  # blank line

# --------- Step 4: FSM runner (one step) ---------
def step(pos, direction):
    """
    Try to move from pos using 'direction'.
    If the direction is invalid or goes off-grid, stay in place.
    Return the new position.
    """
    direction = direction.lower()
    legal = valid_moves_from(pos)
    if direction not in MOVES:
        print(f"Invalid input '{direction}'. Use: up/down/left/right.")
        return pos
    if direction not in legal:
        print(f"Blocked: cannot go '{direction}' from {NAME[pos]}.")
        return pos
    new_pos = legal[direction]
    print(f"{NAME[pos]} --({direction})--> {NAME[new_pos]}")
    return new_pos

if __name__ == "__main__":
    # Start at center (like a real joystick resting point)
    pos = (1, 1)  # (row=1, col=1) = center
    print("Starting at:", NAME[pos])
    show_grid(pos)

    # Example path to demonstrate movement
    demo_moves = ["up", "right", "right", "down", "down", "left", "left", "up", "up"]
    for mv in demo_moves:
        pos = step(pos, mv)
        show_grid(pos)

    # --------- Optional: Interactive mode ---------
    # Type moves yourself; type 'quit' to stop.
    print("Enter moves (up/down/left/right). Type 'quit' to exit.")
    while True:
        mv = input("> ").strip().lower()
        if mv in ("q", "quit", "exit"):
            print("Goodbye!")
            break
        pos = step(pos, mv)
        show_grid(pos)