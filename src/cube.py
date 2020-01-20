from constants import *


class Edge:
    # Slot = 2-tuple
    # Piece = 2-tuple
    def eo(self):  # Edge orientation property for top layer
        if self.piece[0] == 0:
            return 0
        return 1

    def __init__(self, slot, indices):
        self.slot = slot
        self.piece = slot
        self.indices = indices

    def __str__(self):
        return faces[self.piece[0]] + faces[self.piece[1]]

    def __hash__(self):
        return hash(self.piece)

    def __eq__(self, other):
        return self.piece == other.piece or self.piece == flip(other.piece, True)


class Corner:
    # Slot = 3-tuple
    # Piece = 3-tuple
    def co(self):  # Corner orientation property
        if self.piece[0] == 0:
            return 0
        if self.piece[1] == 0:
            return 1
        return 2

    def __init__(self, slot, indices):
        self.slot = slot
        self.piece = slot
        self.indices = indices

    def __str__(self):
        return faces[self.piece[0]] + faces[self.piece[1]] + faces[self.piece[2]]

    def __hash__(self):
        return hash(self.piece)

    def __eq__(self, other):
        return self.piece == other.piece or self.piece == twist(other.piece, True, 1) or self.piece == twist(other.piece, True, -1)


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

    def __str__(self):
        return self.name


# Example Input: "URUFULUB"  (String)
# Example Output: "[self.UR, self.UF, self.UL, self.UB]"  (String)
def build_string_from_list(string):
    length = len(string) // 4

    result = "["
    for i in range(4):
        result += "self.%s, " % string[i * length: (i + 1) * length]
    result += "]"
    return result


# Example Input: (cube.UF, 1), cube.F
# Example Output: (cube.FR, 0)
def move_piece(piece, move):
    slot = piece[0]  # The edge or corner object
    new_slot = piece[0]  # The new slot after the move

    orientation_state = piece[1]  # The current orientation state of the piece
    new_orientation_state = piece[1]  # The new orientation state after the move

    for i in range(move.turns):
        if slot in move.edge_cycle:
            # The slot is affected by the move
            slot_index = move.edge_cycle.index(slot)
            new_slot = move.edge_cycle[(slot_index + 1) % 4]
            if move.flip:
                new_orientation_state = 1 - orientation_state

        elif slot in move.corner_cycle:
            slot_index = move.corner_cycle.index(slot)
            new_slot = move.corner_cycle[(slot_index + 1) % 4]
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

        slot = new_slot
        orientation_state = new_orientation_state

    return new_slot, new_orientation_state


# Flips an edge.
def flip(t, f):
    if len(t) > 2:
        return t

    if f:
        return t[1], t[0]
    return t


# Twists a corner.
def twist(t, tw, twist_amt):
    if len(t) < 3:
        return t

    if tw:
        if twist_amt == 1:
            # Twist counterclockwise
            return t[2], t[0], t[1]
        else:
            # Twist clockwise
            return t[1], t[2], t[0]
    return t


# Turns a move object into an integer.
def to_int(move):
    m = ["U", "R", "F", "D", "L", "B", "Ui", "Ri", "Fi", "Di", "Li", "Bi"]
    return m.index(move.name)


# Turns a list of move objects into a string.
def stringify(list_moves):
    result = ""
    for m in list_moves:
        result += str(m) + " "

    return result


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
        for i in range(move.turns):
            self.cycle_edges(move.edge_cycle, move.flip)
            self.cycle_corners(move.corner_cycle, move.twist)

    def apply_list_of_moves(self, list_moves):
        for m in list_moves:
            self.apply_move(m)

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
        temp = slots[-1].piece
        for i in range(3, 0, -1):
            if slots[i].slot[0] == slots[i - 1].slot[0]:
                slots[i].piece = twist(slots[i - 1].piece, t, -1)
            else:
                slots[i].piece = twist(slots[i - 1].piece, t, 1)

        if slots[0].slot[0] == slots[-1].slot[0]:
            slots[0].piece = twist(temp, t, -1)
        else:
            slots[0].piece = twist(temp, t, 1)

    # Invert a single move.
    def invert_move(self, move):
        inverted_name = move.name
        if len(move.name) == 1:
            inverted_name = move.name + "i"
        elif move.name[-1] == 'i':
            inverted_name = move.name[0]

        return eval("self.%s" % inverted_name)

    # Double a single move.
    def double_move(self, move):
        doubled_name = move.name + "2"
        return eval("self.%s" % doubled_name)

    # Halve a single move.
    def halve_move(self, move):
        halved_name = move.name[0]
        return eval("self.%s" % halved_name)

    # Inverts a list of moves.
    def invert(self, list_moves):
        result = []
        for move in list_moves[::-1]:
            result.append(self.invert_move(move))

        return result

    def all_turn(self, move):
        return [move, self.invert_move(move), self.double_move(move)]

    # Truncates a list of moves (removes unnecessary moves)
    def truncate(self, list_moves):
        new_list = self.truncate_helper(list_moves)
        if len(list_moves) == len(new_list):
            return new_list
        return self.truncate(new_list)

    def truncate_helper(self, list_moves):
        if len(list_moves) <= 1:
            return list_moves

        if list_moves[0].name[0] == list_moves[1].name[0]:
            total_turns = (list_moves[0].turns + list_moves[1].turns) % 4
            if total_turns == 0:
                return self.truncate_helper(list_moves[2:])

            new_index = faces.index(list_moves[0].name[0]) * 3 + total_turns - 1
            new_move = eval("self.%s" % moves[new_index])
            list_moves[1] = new_move
            return self.truncate_helper(list_moves[1:])
        else:
            return [list_moves[0]] + self.truncate_helper(list_moves[1:])

    # Generate conjugates given moves A and B.
    def generate_conjugate(self, move_a, move_b):
        return [[move_a, move_b, self.invert_move(move_a)], [move_a, self.double_move(move_b), self.invert_move(move_a)], [move_a, self.invert_move(move_b), self.invert_move(move_a)]]
