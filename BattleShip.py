class Player:
    def __init__(self,player_name,player_gameboard,opponent_gameboard,ships):
        self.player_name = player_name
        self.player_gameboard = player_gameboard
        self.opponent_gameboard = opponent_gameboard
        self.ships = ships


class PlayerGameBoard:
    def __init__(self,gameboard):
        self.gameboard = gameboard
        
    def printPlayerGameBoard(self):
        print("Player Gamezboard")
        print("    0   1   2   3   4   5   6   7   8   9")
        keys = ["0","1","2","3","4","5","6","7","8","9"]
        for coord_y,key in enumerate(keys):
            row = key
            for coord_x in range(0,10):
                if self.gameboard[coord_y][coord_x] == 0:
                    row += "   ~"
                elif self.gameboard[coord_y][coord_x] == 1:
                    row += "   {}".format("o")
                elif self.gameboard[coord_y][coord_x] == 2:
                    row += "   {}".format("x")
            print(row)
    def updatePlayerGameBoard(self,ships):
        for ship in ships:
            for x in range(0,ship.length):
                if ship.hits[x] == 0:
                    self.gameboard[ship.cords[x][0]][ship.cords[x][1]] = 1
                    continue
                elif ship.hits[x] == 1:
                    self.gameboard[ship.cords[x][0]][ship.cords[x][1]] = 2
                    continue
    def checkWinner(self):
        for y in range(0,10):
            for x in range(0,10):
                if self.gameboard[y][x] == 1 :
                    return False
        print("FUck u palyer 2")
        return False

class OpponentGameBoard:
    def __init__(self,gameboard):
        self.gameboard = gameboard
        
    def printOpponentGameBoard(self):
        print("Opponent Gameboard")
        print("    0   1   2   3   4   5   6   7   8   9")
        keys = ["0","1","2","3","4","5","6","7","8","9"]
        for coord_y,key in enumerate(keys):
            row = key
            for coord_x in range(0,10):
                if self.gameboard[coord_y][coord_x] == 0:
                    row += "   ~"
                elif self.gameboard[coord_y][coord_x] == 1:
                    row += "   {}".format("H")
                elif self.gameboard[coord_y][coord_x] == 2:
                    row += "   {}".format("M")
            print(row)
            
    def updateHit(self,coord):
        self.gameboard[coord[0]][coord[1]] = 1
        
    def updateMiss(self,coord):
        self.gameboard[coord[0]][coord[1]] = 2
        
            
class Ship:
    
    def __init__(self, length, cords): #inializes object
        self.length = length
        self.hits = [0]*length
        self.cords = cords
        
        
    def isSunk(self): #checks if the ship is sunk
        count = 0
        for x in self.hits:
            if x==1:
                count+=1
        if count==self.length:
            return True
        else:
            return False
        
    def damage(self, cord): #uses the cord to determine what part of the ship was hit
        for x in range(0, self.length):
            if cord==self.cords[x]:
                self.hits[x]=1
                
def shoot(opponent_ships,opponent_gameboard):
    print("Position your cannons")
    cannon_position = [int(input("Which row will you attack?")),int(input("Which column will you attack?"))]
    for ship in opponent_ships:
        for coords in ship.cords:
            if cannon_position == coords:
                ship.damage(coords)
                if ship.isSunk():
                    print('You sunk a ship!')
                else:
                    print('You hit a ship!')
                opponent_gameboard.updateHit(cannon_position)
                return [opponent_ships,opponent_gameboard]
            else:
                continue
    print('Your shot missed the enemy ships.')
    opponent_gameboard.updateMiss(cannon_position)
    return [opponent_ships,opponent_gameboard]


def createShips():
    print("Where do you want to place Aircraft carrier? length 5")
    aircraft=[int(input("x = ")),int(input("y = "))]
    air_orien=input("What orientation for Aircraft carrier? u, d, l, or r")
    
    print("Where do you want to place Battleship? length 4")
    battle=[int(input("x = ")),int(input("y = "))]
    battle_orien=input("What orientation for Battleship? u, d, l, or r")
    
    print("Where do you want to place Submarine? length 3")
    submarine=[int(input("x = ")),int(input("y = "))]
    sub_orien=input("What orientation for Submarine? u, d, l, or r")
    
    print("Where do you want to place Destoryer? length 3")
    destroyer=[int(input("x = ")),int(input("y = "))]
    destroyer_orien=input("What orientation for Destroyer? u, d, l, or r")
    
    print("Where do you want to place Patrol Boat? length 2")
    patrol=[int(input("x = ")),int(input("y = "))]
    patrol_orien=input("What orientation for Patrol Boat? u, d, l, or r")
    
    shipCords=[aircraft, battle, submarine, destroyer, patrol]
    orien =[air_orien,battle_orien,sub_orien,destroyer_orien,patrol_orien]
    ships =[Ship(5,[[0,0],[0,0],[0,0],[0,0],[0,0]]), \
            Ship(4,[[0,0],[0,0],[0,0],[0,0]]), \
            Ship(3,[[0,0],[0,0],[0,0]]), \
            Ship(3,[[0,0],[0,0],[0,0]]), \
            Ship(2,[[0,0],[0,0]])]  
            
    for x in range(0,5):
        count=0
        if orien[x]== "U" :
            w=shipCords[x]
            while(count<ships[x].length):
                y=w[0]
                y=y-count
                ships[x].cords[count]=[y,w[1]]
                count+=1
                
        elif orien[x]== "R":
            w=shipCords[x]
            while(count<ships[x].length):
                y=w[1]
                y=y+count
                ships[x].cords[count]=[w[0],y]
                count+=1
                
        elif orien[x]== "D":
            w=shipCords[x]
            while(count<ships[x].length):
                y=w[0]
                y=y+count
                ships[x].cords[count]=[y,w[1]]
                count+=1
                
        elif orien[x]== "L":
            w=shipCords[x]
            while(count<ships[x].length):
                y=w[1]
                y=y-count
                ships[x].cords[count]=[w[0],y]
                count+=1
        
    return ships

#def checkWinner(ships):
    #count = 0
    #for ship in ships:
        #if (ship.isSunk == True):
            #count+=1
    #if(count==len(ships)):
        #return True
    #else:
        #return False
    
#Game Begins
#Creating gameboard
p1_gb = []
p2_gb = []
o1_gb = []
o2_gb = []
ls = [p1_gb,p2_gb,o1_gb,o2_gb]
for gb in ls:
    for numbers in range(0,10):
        gb.append([0,0,0,0,0,0,0,0,0,0])      
p1_gb = PlayerGameBoard(p1_gb)
p2_gb = PlayerGameBoard(p2_gb)
o1_gb = OpponentGameBoard(o1_gb)
o2_gb = OpponentGameBoard(o2_gb)
#Creating ships
p1_gb.printPlayerGameBoard()
print("Player 1 place your ships!")
p1ships=createShips()
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
p1_gb.printPlayerGameBoard()
print("Player 2 place your ships!")
p2ships=createShips()
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
print("\n","\n","\n","\n","\n","\n",)
#Updating Ships onto gameboard
p2_gb.updatePlayerGameBoard(p2ships)
p1_gb.updatePlayerGameBoard(p1ships)
#Putting together player object
p1_name = input('what your name good sir?: ')
p2_name = input('what your name good sir?: ')
player1 = Player(p1_name,p1_gb,o1_gb,p1ships)
player2 = Player(p2_name,p2_gb,o2_gb,p2ships)
playerTurn=1
x = 0
while x == 0:
    print("Turn :" + str(playerTurn) + "\n")
    if playerTurn != 1:
        pass
    if(playerTurn%2==1):
        p1_gb.updatePlayerGameBoard(p1ships)
        print("Player 1's turn!")
        o1_gb.printOpponentGameBoard()
        p1_gb.printPlayerGameBoard()
        shoot(p2ships, o1_gb)
        #p2_gb.checkWinner()
        if p2_gb.checkWinner() == True:
            break
        else:
            playerTurn+=1
            continue

            
    elif(playerTurn%2==0):
        p2_gb.updatePlayerGameBoard(p2ships)
        print("Player 2's turn!")
        o2_gb.printOpponentGameBoard()
        p2_gb.printPlayerGameBoard()
        shoot(p1ships, o2_gb)

        #p1_gb.checkWinner()
        if p1_gb.checkWinner() == True:
            break
        else:
            playerTurn+=1
            continue
    
  