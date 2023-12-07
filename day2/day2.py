import os
def check_validity(game: str) :

    newls = game.strip().split(",")
    print(newls)
    #print(game)

    
def main():
    max_count = {"red": 12, "blue": 13, "yellow": 13} 
    sum_id = 0

    pwd = os.getcwd() 
    file = open(pwd + "/day2/test1.txt")

    for line in file:
        print(line)
        game, x = line.split(":",maxsplit=1)
        idx = int(game.strip("Game"))
        x = x.replace(",","").replace(";","").replace(" ","")
        print(x)
        ridx = x.find('red')
        print(ridx)

if __name__ == '__main__':
    main()