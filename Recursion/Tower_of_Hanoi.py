def moveDisk(poleA, poleC):
    print("moving disk from", poleA, "to", poleC)

def moveTower(height, poleA, poleB, poleC):
    if height >= 1:
        moveTower(height-1, poleA, poleC, poleB)
        moveDisk(poleA, poleC)
        moveTower(height-1, poleB, poleA, poleC)

moveTower(3, 'A', 'B', 'C')  # 2^n - 1 steps



