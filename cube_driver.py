from cube import *
import copy


# Solved_states: 1 or 2 solved states (for a single piece or an F2L pair)
# Example: (cube.UF, 0)  or  ((cube.FR, 0), (cube.DRF, 0))
# Moveset: List of allowed moves
# Max_length: stop when we reach this number of states
def generate_move_states(solved_states, moveset, max_length):
    move_states = {}
    for s in solved_states:
        move_states[s] = []

    while len(move_states) < max_length:
        new_move_states = copy.deepcopy(move_states)
        for state in move_states:  # type(state) is an edge or corner object
            for move in moveset:
                if type(move) is Move:
                    if type(state[1]) is int:
                        new_state = move_piece(state, move)
                    else:
                        new_state = (move_piece(state[0], move), move_piece(state[1], move))
                    if new_state not in new_move_states:
                        new_move_states[new_state] = move_states[state] + [move]
                else:
                    temp = copy.deepcopy(state)
                    for m in move:
                        if type(state[1]) is int:
                            new_state = move_piece(temp, m)
                        else:
                            new_state = (move_piece(temp[0], m), move_piece(temp[1], m))
                        temp = copy.deepcopy(new_state)
                    if new_state not in new_move_states:
                        new_move_states[new_state] = move_states[state] + move

        move_states = new_move_states
    return move_states


# Slot to solve: (edge_to_solve, orientation_state)
# Returns move list to solve slot
def solve_edge(cube, slot_to_solve, moveset, max_length):
    move_states = generate_move_states([slot_to_solve], moveset, max_length)
    for e in edges:
        edge = eval("cube.%s" % e)
        if edge.piece == slot_to_solve[0].slot:
            return cube.truncate(cube.invert(move_states[(edge, 0)]))
        elif edge.piece == flip(slot_to_solve[0].slot, True):
        	return cube.truncate(cube.invert(move_states[(edge, 1)]))


# Slot to solve: (corner_to_solve, orientation_state)
# Returns move list to solve slot
def solve_corner(cube, slot_to_solve, moveset, max_length):
    move_states = generate_move_states([slot_to_solve], moveset, max_length)
    for c in corners:
        corner = eval("cube.%s" % c)
        if corner.piece == slot_to_solve[0].slot:
            return cube.truncate(cube.invert(move_states[(corner, 0)]))
        elif corner.piece == twist(slot_to_solve[0].slot, True, -1):
            return cube.truncate(cube.invert(move_states[(corner, 2)]))
        elif corner.piece == twist(slot_to_solve[0].slot, True, 1):
            return cube.truncate(cube.invert(move_states[(corner, 1)]))


# Slots to solve: ((edge_to_solve, orientation_state), (corner_to_solve, orientation_state))
def solve_pair(cube, slots_to_solve, moveset, max_length):
    move_states = generate_move_states([slots_to_solve], moveset, max_length)
    edge_tuple = slots_to_solve[0]
    corner_tuple = slots_to_solve[1]
    for c in corners:
        corner = eval("cube.%s" % c)
        if corner.piece == slots_to_solve[1][0].slot:
            corner_tuple = (corner, 0)
        elif corner.piece == twist(slots_to_solve[1][0].slot, True, -1):
            corner_tuple = (corner, 2)
        elif corner.piece == twist(slots_to_solve[1][0].slot, True, 1):
            corner_tuple = (corner, 1)

    for e in edges:
        edge = eval("cube.%s" % e)
        if edge.piece == slots_to_solve[0][0].slot:
            edge_tuple = (edge, 0)
        elif edge.piece == flip(slots_to_solve[0][0].slot, True):
            edge_tuple = (edge, 1)

    return cube.truncate(cube.invert(move_states[(edge_tuple, corner_tuple)]))


def solve_DB(cube):
    slot_to_solve = (cube.DB, 0)
    moveset = cube.all_turn(cube.U) + cube.all_turn(cube.F) + cube.all_turn(cube.D) + cube.all_turn(cube.R) + cube.all_turn(cube.L) + cube.all_turn(cube.B)
    max_length = 24

    solution = solve_edge(cube, slot_to_solve, moveset, max_length)
    cube.apply_list_of_moves(solution)

    output_message = ""
    return solution


def solve_DL(cube):
    slot_to_solve = (cube.DL, 0)
    moveset = cube.all_turn(cube.U) + cube.all_turn(cube.F) + cube.all_turn(cube.R) + cube.all_turn(cube.L)
    max_length = 22

    solution = solve_edge(cube, slot_to_solve, moveset, max_length)
    cube.apply_list_of_moves(solution)

    output_message = ""
    return solution


def solve_DR(cube):
    slot_to_solve = (cube.DR, 0)
    moveset = cube.all_turn(cube.U) + cube.all_turn(cube.F) + cube.all_turn(cube.R) + cube.generate_conjugate(cube.L, cube.U) + cube.generate_conjugate(cube.Bi, cube.U)
    max_length = 20

    solution = solve_edge(cube, slot_to_solve, moveset, max_length)
    cube.apply_list_of_moves(solution)

    output_message = ""
    return solution


def solve_DF(cube):
    slot_to_solve = (cube.DF, 0)
    moveset = cube.all_turn(cube.U) + cube.all_turn(cube.F) + cube.generate_conjugate(cube.L, cube.U) + cube.generate_conjugate(cube.Li, cube.U) + \
              cube.generate_conjugate(cube.R, cube.U) + cube.generate_conjugate(cube.Ri, cube.U) + \
              cube.generate_conjugate(cube.B, cube.U) + cube.generate_conjugate(cube.Bi, cube.U)
    max_length = 18

    solution = solve_edge(cube, slot_to_solve, moveset, max_length)
    cube.apply_list_of_moves(solution)

    output_message = ""
    return solution


def solve_BL_pair(cube):
    slot_to_solve = ((cube.BL, 0), (cube.DLB, 0))
    moveset = cube.all_turn(cube.U) + \
              cube.generate_conjugate(cube.R, cube.U) + cube.generate_conjugate(cube.Ri, cube.U) + \
              cube.generate_conjugate(cube.L, cube.U) + cube.generate_conjugate(cube.Li, cube.U) + \
              cube.generate_conjugate(cube.F, cube.U) + cube.generate_conjugate(cube.Fi, cube.U) + \
              cube.generate_conjugate(cube.B, cube.U) + cube.generate_conjugate(cube.Bi, cube.U)
    max_length = 384

    solution = solve_pair(cube, slot_to_solve, moveset, max_length)
    cube.apply_list_of_moves(solution)

    output_message = ""
    return solution


def solve_BR_pair(cube):
    slot_to_solve = ((cube.BR, 0), (cube.DBR, 0))
    moveset = cube.all_turn(cube.U) + \
              cube.generate_conjugate(cube.R, cube.U) + cube.generate_conjugate(cube.Ri, cube.U) + \
              cube.generate_conjugate(cube.Li, cube.U) + \
              cube.generate_conjugate(cube.F, cube.U) + cube.generate_conjugate(cube.Fi, cube.U) + \
              cube.generate_conjugate(cube.B, cube.U)
    max_length = 294

    solution = solve_pair(cube, slot_to_solve, moveset, max_length)
    cube.apply_list_of_moves(solution)

    output_message = ""
    return solution


def solve_FL_pair(cube):
    slot_to_solve = ((cube.FL, 0), (cube.DFL, 0))
    moveset = cube.all_turn(cube.U) + \
              cube.generate_conjugate(cube.R, cube.U) + \
              cube.generate_conjugate(cube.Li, cube.U) + \
              cube.generate_conjugate(cube.F, cube.U) + cube.generate_conjugate(cube.Fi, cube.U)
    max_length = 216

    solution = solve_pair(cube, slot_to_solve, moveset, max_length)
    cube.apply_list_of_moves(solution)

    output_message = ""
    return solution


def solve_FR_pair(cube):
    slot_to_solve = ((cube.FR, 0), (cube.DRF, 0))
    moveset = cube.all_turn(cube.U) + \
              cube.generate_conjugate(cube.R, cube.U) + \
              cube.generate_conjugate(cube.Fi, cube.U)
    max_length = 150

    solution = solve_pair(cube, slot_to_solve, moveset, max_length)
    cube.apply_list_of_moves(solution)

    output_message = ""
    return solution


def cycle(b):
    return [b[-1]] + b[:-1]


def cycle_of(a, b):
    if a == b:
        return 0

    temp = copy.deepcopy(b)
    for i in range(1, 4):
        temp = cycle(temp)
        if a == temp:
            return 4 - i

    return -1


def solve_EO(cube):
    # Algorithms
    ADJ_EDGES = [cube.F, cube.U, cube.R, cube.Ui, cube.Ri, cube.Fi]
    OPP_EDGES = [cube.F, cube.R, cube.U, cube.Ri, cube.Ui, cube.Fi]

    solution = []
    orientations = [cube.UB.eo(), cube.UR.eo(), cube.UF.eo(), cube.UL.eo()]
    print(orientations)

    cycle_number = cycle_of(orientations, [0, 1, 1, 0])
    if cycle_number >= 0:
        solution += [cube.U] * cycle_number + ADJ_EDGES

    cycle_number = cycle_of(orientations, [0, 1, 0, 1])
    if cycle_number >= 0:
        solution += [cube.U] * cycle_number + OPP_EDGES

    if orientations == [1, 1, 1, 1]:
        solution += ADJ_EDGES + [cube.U] + OPP_EDGES

    cube.apply_list_of_moves(solution)
    return cube.truncate(solution)


def solve_CO(cube):
    # Algorithms
    SUNE = [cube.R, cube.U, cube.Ri, cube.U, cube.R, cube.U2, cube.Ri]
    ANTISUNE = cube.invert(SUNE)
    T = [cube.R, cube.U, cube.Ri, cube.Ui, cube.Li, cube.U, cube.R, cube.Ui, cube.Ri, cube.L]
    L = cube.invert(T)
    U = [cube.R2, cube.D, cube.Ri, cube.U2, cube.R, cube.Di, cube.Ri, cube.U2, cube.Ri]
    Pi = [cube.R, cube.U2, cube.R2, cube.Ui, cube.R2, cube.Ui, cube.R2, cube.U2, cube.R]
    H = SUNE + SUNE

    solution = []
    orientations = [cube.UBL.co(), cube.URB.co(), cube.UFR.co(), cube.ULF.co()]

    cycle_number = cycle_of(orientations, [1, 1, 1, 0])
    if cycle_number >= 0:
        solution += [cube.U] * cycle_number + SUNE

    cycle_number = cycle_of(orientations, [2, 0, 2, 2])
    if cycle_number >= 0:
        solution += [cube.U] * cycle_number + ANTISUNE

    cycle_number = cycle_of(orientations, [1, 0, 0, 2])
    if cycle_number >= 0:
        solution += [cube.U] * cycle_number + T

    cycle_number = cycle_of(orientations, [0, 1, 0, 2])
    if cycle_number >= 0:
        solution += [cube.U] * cycle_number + L

    cycle_number = cycle_of(orientations, [0, 0, 1, 2])
    if cycle_number >= 0:
        solution += [cube.U] * cycle_number + U

    cycle_number = cycle_of(orientations, [2, 1, 2, 1])
    if cycle_number >= 0:
        solution += [cube.U] * cycle_number + H

    cycle_number = cycle_of(orientations, [2, 2, 1, 1])
    if cycle_number >= 0:
        solution += [cube.U] * cycle_number + Pi

    cube.apply_list_of_moves(solution)
    return cube.truncate(solution)


def solve_CP_1(cube):
    slot_to_solve = (cube.ULF, 0)
    moveset = cube.all_turn(cube.U)
    max_length = 4

    solution = solve_corner(cube, slot_to_solve, moveset, max_length)
    cube.apply_list_of_moves(solution)

    output_message = ""
    return solution


def solve_CP_2(cube):
    A_PERM = [cube.Ri, cube.F, cube.Ri, cube.B2, cube.R, cube.Fi, cube.Ri, cube.B2, cube.R2]

    slot_to_solve = (cube.UFR, 0)
    moveset = [A_PERM, cube.invert(A_PERM)]
    max_length = 3

    solution = solve_corner(cube, slot_to_solve, moveset, max_length)
    cube.apply_list_of_moves(solution)

    output_message = ""
    return solution


def solve_CP_3(cube):
    R_PERM = [cube.Ri, cube.U2, cube.R, cube.U2, cube.Ri, cube.F, cube.R, cube.U, cube.Ri, cube.Ui, cube.Ri, cube.Fi, cube.R2, cube.Ui]

    slot_to_solve = (cube.URB, 0)
    moveset = [R_PERM]
    max_length = 2

    solution = solve_corner(cube, slot_to_solve, moveset, max_length)
    cube.apply_list_of_moves(solution)

    output_message = ""
    return solution


def solve_EP_1(cube):
    U_PERM = [cube.R, cube.Ui, cube.R, cube.U, cube.R, cube.U, cube.R, cube.Ui, cube.Ri, cube.Ui, cube.R2]

    slot_to_solve = (cube.UB, 0)
    moveset = [[cube.U] + U_PERM + [cube.Ui], [cube.Ui] + U_PERM + [cube.U], [cube.Ui] + cube.invert(U_PERM) + [cube.U], [cube.U] + cube.invert(U_PERM) + [cube.Ui]]
    max_length = 4

    solution = solve_edge(cube, slot_to_solve, moveset, max_length)
    cube.apply_list_of_moves(solution)

    output_message = ""
    return solution


def solve_EP_2(cube):
    U_PERM = [cube.R, cube.Ui, cube.R, cube.U, cube.R, cube.U, cube.R, cube.Ui, cube.Ri, cube.Ui, cube.R2]

    slot_to_solve = (cube.UF, 0)
    moveset = [U_PERM, cube.invert(U_PERM)]
    max_length = 3

    solution = solve_edge(cube, slot_to_solve, moveset, max_length)
    cube.apply_list_of_moves(solution)

    output_message = ""
    return solution


def to_matrix(cube):
    matrix = []
    for i in range(6):
        matrix.append([[0, 0, 0]] * 3)

    for e in edges:
        for i in range(2):
            exec_string = "matrix["
            exec_string += e[i] + "]"
            index = eval("cube.%s.indices[i]" % e)
            exec_string += "[%d][%d]" % (index[0], index[1])
            exec_string += " = %d" % (eval("cube.%s.piece[i]" % e))
            exec(exec_string)

    for c in corners:
        for i in range(3):
            exec_string = "matrix["
            exec_string += c[i] + "]"
            index = eval("cube.%s.indices[i]" % c)
            exec_string += "[%d][%d]" % (index[0], index[1])
            exec_string += " = %d" % (eval("cube.%s.piece[i]" % c))
            exec(exec_string)
    return matrix


def to_cube(matrix):
    cube = Cube()

    for e in edges:
        indices = []
        for i in range(2):
            exec_string = "cube.%s.indices" % e
            exec_string += "[%d]" % i
            index = eval(exec_string)

            exec_string = "matrix"
            exec_string += "[%d]" % eval("cube.%s.slot[%d]" % (e, i))
            exec_string += "[%d]" % index[0]
            exec_string += "[%d]" % index[1]

            indices.append(eval(exec_string))
        exec_string = "cube.%s.piece = indices[0], indices[1]" % e
        exec(exec_string)


    for c in corners:
        indices = []
        for i in range(3):
            exec_string = "cube.%s.indices" % c
            exec_string += "[%d]" % i
            index = eval(exec_string)

            exec_string = "matrix"
            exec_string += "[%d]" % eval("cube.%s.slot[%d]" % (c, i))
            exec_string += "[%d]" % index[0]
            exec_string += "[%d]" % index[1]

            indices.append(eval(exec_string))
        exec_string = "cube.%s.piece = indices[0], indices[1], indices[2]" % c
        exec(exec_string)
    return cube
