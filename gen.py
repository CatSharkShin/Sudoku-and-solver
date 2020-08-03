grid = [
        [2,3,4,7,5,0,9,0,0],
        [7,0,0,4,0,0,0,0,3],
        [1,0,0,0,0,0,0,4,5],
        [6,9,0,0,7,8,0,0,4],
        [0,7,1,0,0,0,8,5,0],
        [4,0,8,3,0,5,0,7,0],
        [8,4,0,0,0,3,0,0,7],
        [9,6,0,1,0,0,0,0,8],
        [5,0,0,7,0,2,9,0,0]
]
class Box:
    def __init__(self,value,x,y):
        self.value = value
        self.x = x
        self.y = y
        self.color = (190,190,190)
        self.locked = value != 0
class Board:
    def __init__(self):
        self.boxes = []
    def 
# [x,y] y=h x=v
def checkbox(x,y):
    start =  (x//3*3,y//3*3)
    dupe = False
    dupes = []
    print("Checking: "+str(grid[x][y])+" "+str(x)+","+str(y))
    for row in range(start[0],start[0]+3):
        for col in range(start[1],start[1]+3):
            #print(grid[row][col],end=' ')
            if grid[row][col] ==  grid[x][y] and x!=col and y!=col:
                dupe = True
                dupes.append((row,col))
                print("Box dupe found: "+str(grid[row][col])+" "+str(row)+","+str(col))
    for i in range(9):
        if grid[i][y] == grid[x][y] and x != i:
            print("Col dupe found: "+str(grid[i][y])+" "+str(i)+","+str(y))
            dupes.append((i,y))
        if grid[x][i] == grid[x][y] and y != i:
            print("Row dupe found: "+str(grid[x][i])+" "+str(x)+","+str(i))
            dupes.append((x,i))
    print(dupes)
    return dupe

def iterategrid():
    for col in range(len(grid)):
        for row in range(len(grid[col])):
            print(str(col)+","+str(row)+": "+str(grid[col][row]))
def main():
    print(checkbox(1,4))


if __name__ == '__main__':
    main()