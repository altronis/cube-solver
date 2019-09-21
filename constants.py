# Face constants
U = 0
R = 1
F = 2
D = 3
L = 4
B = 5

# 6 Faces
faces = ["U", "R", "F", "D", "L", "B"]

# 12 Edge objects
edges = ["UR", "UF", "UL", "UB", "DR", "DF", "DL", "DB", "FR", "FL", "BR", "BL"]

# 8 Corner objects
corners = ["UFR", "URB", "UBL", "ULF", "DFL", "DRF", "DBR", "DLB"]

# 18 Moves
moves = ["U", "U2", "Ui", "R", "R2", "Ri", "F", "F2", "Fi",
         "D", "D2", "Di", "L", "L2", "Li", "B", "B2", "Bi"]

# Edge cycles
U_edge_cycle = "URUFULUB"
R_edge_cycle = "URBRDRFR"
F_edge_cycle = "UFFRDFFL"
D_edge_cycle = "DRDBDLDF"
L_edge_cycle = "ULFLDLBL"
B_edge_cycle = "UBBLDBBR"

# Corner cycles
U_corner_cycle = "UFRULFUBLURB"
R_corner_cycle = "UFRURBDBRDRF"
F_corner_cycle = "ULFUFRDRFDFL"
D_corner_cycle = "DRFDBRDLBDFL"
L_corner_cycle = "UBLULFDFLDLB"
B_corner_cycle = "URBUBLDLBDBR"

# Flips (edge orientation)
U_flip = False
R_flip = False
F_flip = True
D_flip = False
L_flip = False
B_flip = True

# Twists (corner orientation)
U_twist = False
R_twist = True
F_twist = True
D_twist = False
L_twist = True
B_twist = True

# Edge indices
UR = ((1, 2), (1, 0))
UL = ((1, 0), (1, 2))
UF = ((2, 1), (0, 1))
UB = ((0, 1), (2, 1))

DR = ((1, 0), (1, 2))
DL = ((1, 2), (1, 0))
DF = ((2, 1), (2, 1))
DB = ((0, 1), (0, 1))

FR = ((1, 2), (2, 1))
FL = ((1, 0), (2, 1))
BR = ((1, 2), (0, 1))
BL = ((1, 0), (0, 1))

# Corner indices
UFR = ((2, 2), (0, 2), (2, 0))
URB = ((0, 2), (0, 0), (2, 2))
UBL = ((0, 0), (2, 0), (0, 2))
ULF = ((2, 0), (2, 2), (0, 0))

DRF = ((2, 0), (2, 0), (2, 2))
DFL = ((2, 2), (2, 0), (2, 0))
DBR = ((0, 0), (0, 2), (0, 2))
DLB = ((0, 2), (0, 0), (0, 0))
