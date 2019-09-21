from constants import *


class Edge:
    # Slot = 2-tuple
    # Piece = 2-tuple
    def __init__(self, slot, indices):
        self.slot = slot
        self.piece = slot
        self.indices = indices


class Corner:
    # Slot = 3-tuple
    # Piece = 3-tuple
    def __init__(self, slot, indices):
        self.slot = slot
        self.piece = slot
        self.indices = indices


class Move:
    # Turns: Number of clockwise 90-degree turns
    # Edge_cycle: The edges to cycle clockwise
    # Corner_cycle: The corners to cycle clockwise
    # Flip: Whether the move changes the orientation of the edges
    # The name of the move
    def __init__(self):
        self.turns = 1
        self.edge_cycle = []
        self.corner_cycle = []
        self.flip = False
        self.twist = False
        self.name = ""


# Example Input: "URUFULUB"  (String)
# Example Output: "[self.UR, self.UF, self.UL, self.UB]"  (String)
def build_string_from_list(string):
    length = len(string) // 4

    result = "["
    for i in range(4):
        result += "self.%s, " % string[i * length: (i + 1) * length]
    result += "]"
    return result


# Example Input: (cube.UR, 1), cube.F
# Example Output: (cube.FR, 0)
def move_piece(piece, move):
    slot = piece[0]  # The edge or corner object
    new_slot = piece[0]  # The new slot after the move

    orientation_state = piece[1]  # The current orientation state of the piece
    new_orientation_state = piece[1]  # The new orientation state after the move

    if slot in move.edge_cycle:
        # The slot is affected by the move
        slot_index = move.edge_cycle.index(slot)
        new_slot = move.edge_cycle[slot_index - 1]
        if move.flip:
            new_orientation_state = 1 - orientation_state

    elif slot in move.corner_cycle:
        slot_index = move.corner_cycle.index(slot)
        new_slot = move.corner_cycle[slot_index - 1]
        if move.twist:
            if slot.slot[0] == new_slot.slot[0]:
                if new_orientation_state == 0:
                    new_orientation_state = 2
                else:
                    new_orientation_state -= 1
            else:
                if new_orientation_state == 2:
                    new_orientation_state = 0
                else:
                    new_orientation_state += 1

    return new_slot, new_orientation_state


def flip(t, f):
    if f:
        return t[1], t[0]
    return t


def twist(t, tw, twist_amt):
    if tw:
        if twist_amt == 1:
            # Twist counterclockwise
            return t[2], t[0], t[1]
        else:
            # Twist clockwise
            return t[1], t[2], t[0]
    return t


class Cube:
    def __init__(self):  # Constructor
        # Initialize the edge slots
        for e in edges:
            eval_string = "self.%s = Edge((%s, %s), %s)" % (e, e[0], e[1], e)
            exec(eval_string)

        # Initialize the corner slots
        for c in corners:
            eval_string = "self.%s = Corner((%s, %s, %s), %s)" % (c, c[0], c[1], c[2], c)
            exec(eval_string)

        # Initialize the moves (18 moves in 6 groups)
        for i in range(18):
            eval_string = "self.%s = Move()" % moves[i]  # Construct the move object
            exec(eval_string)

            eval_string = "self.%s.turns = %d" % (moves[i], i % 3 + 1)  # Initialize the turns
            exec(eval_string)

            edge_cycle = eval(moves[i - i % 3] + "_edge_cycle")
            eval_string = "self.%s.edge_cycle = %s" % (moves[i], build_string_from_list(edge_cycle))
            exec(eval_string)  # Initialize the edge cycle

            corner_cycle = eval(moves[i - i % 3] + "_corner_cycle")
            eval_string = "self.%s.corner_cycle = %s" % (moves[i], build_string_from_list(corner_cycle))
            exec(eval_string)  # Initialize the corner cycle

            flip = eval(moves[i - i % 3] + "_flip")
            eval_string = "self.%s.flip = %s" % (moves[i], flip)
            exec(eval_string)  # Initialize the flip

            twist = eval(moves[i - i % 3] + "_twist")
            eval_string = "self.%s.twist = %s" % (moves[i], twist)
            exec(eval_string)  # Initialize the twist

            eval_string = "self.%s.name = \"%s\"" % (moves[i], moves[i])
            exec(eval_string)  # Initialize the name

    # Given a move object, applies the move to the cube, changing the piece variables of the
    # edge and corner objects.
    # move: a move object
    def apply_move(self, move):
        self.cycle_edges(move.edge_cycle, move.flip)
        self.cycle_corners(move.corner_cycle, move.twist)

    # Given a slots list of 4 edges, cycles the piece variables of the objects in the list.
    # slots: list of 4 edges
    def cycle_edges(self, slots, f):
        temp = slots[-1].piece  # Store the piece variable of the last object in the list
        for i in range(3, 0, -1):
            slots[i].piece = flip(slots[i - 1].piece, f)

        slots[0].piece = flip(temp, f)

    # Given a slots list of 4 edges, cycles the piece variables of the objects in the list.
    # slots: list of 4 edges
    def cycle_corners(self, slots, t):
        temp = slots[-1].piece  # Store the piece variable of the last object in the list
        for i in range(3, 0, -1):
            if slots[i].piece[0] == slots[i - 1].piece[0]:
                slots[i].piece = twist(slots[i - 1].piece, t, -1)
            else:
                slots[i].piece = twist(slots[i - 1].piece, t, 1)

        if slots[0].piece[0] == temp[0]:
            slots[0].piece = twist(temp, t, -1)
        else:
            slots[0].piece = twist(temp, t, 1)
