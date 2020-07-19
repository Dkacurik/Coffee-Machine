# Write your code here
import math
# print('Starting to make a coffee')
# print('Grinding coffee beans')
# print('Boiling water')
# print('Mixing boiled water with crushed coffee beans')
# print('Pouring coffee into the cup')
# print('Pouring some milk into the cup')
# print('Coffee is ready!')

# print('Write how many cups of coffee you will need:')
# numberOfCups = int(input())
# print('For ' + str(numberOfCups) + ' cups of coffee you will need:')
# print(str(numberOfCups * 200) + ' ml of water')
# print(str(numberOfCups * 50) + ' ml of milk')
# print(str(numberOfCups * 15) + ' g of coffee beans')

# def canMakeCups(w, m, cb):
#     possibleCups = [w / 200, m / 50, cb / 15]
#     possibleCups.sort()
#
#     return math.floor(possibleCups[0])
#
#
# print('Write how many ml of water the coffee machine has:')
# water = int(input())
# print('Write how many ml of milk the coffee machine has:')
# milk = int(input())
# print('Write how many grams of coffee beans the coffee machine has:')
# coffeeBeans = int(input())
# print('Write how many cups of coffee you will need:')
# numberOfCups = int(input())
#
# posibbleCups = canMakeCups(water, milk, coffeeBeans)
#
# if(numberOfCups * 200 > water or numberOfCups * 50 > milk or numberOfCups * 15 > coffeeBeans):
#     print('No, I can make only ' + str(posibbleCups) + ' cups of coffee')
# elif(numberOfCups * 200 <= water or numberOfCups * 50 <= milk or numberOfCups * 15 < coffeeBeans):
#     if(posibbleCups > 0):
#         print('Yes, I can make that amount of coffee (and even ' + str(posibbleCups - numberOfCups) + ' more than that)')
#
#     else:
#         print('Yes, I can make that amount of coffee')

class Machine:
    def __init__(self):
        self.machineWater = 400
        self.machineMilk = 540
        self.machineCoffeeBeans = 120
        self.machineCups = 9
        self.machineMoney = 550

    def printStats(self):
        print('\nThe coffee machine has:')
        print(str(self.machineWater) + ' of water')
        print(str(self.machineMilk) + ' of milk')
        print(str(self.machineCoffeeBeans) + ' of coffee beans')
        print(str(self.machineCups) + ' of disposable cups')
        print('$' + str(self.machineMoney) + ' money')

    def withdrawMoney(self):
       print('I gave you $' + str(self.machineMoney))
       self.machineMoney = 0

    def fillMachine(self):
        print('Write how many ml of water do you want to add:')
        newWater = int(input())
        self.machineWater = self.machineWater + newWater
        print('Write how many ml of milk do you want to add:')
        newMilk = int(input())
        self.machineMilk = self.machineMilk + newMilk
        print('Write how many grams of coffee beans do you want to add:')
        newCoffeBeans = int(input())
        self.machineCoffeeBeans = self.machineCoffeeBeans + newCoffeBeans
        print('Write how many disposable cups of coffee do you want to add:')
        newCups = int(input())
        self.machineCups = self.machineCups + newCups

class Coffee:
    # machine = Machine()
    def __init__(self, machine):
        self.machine = machine
        print('constructor')

    def makeCoffee(self, w, m, cb, p):
        state = 0
        if(machine.machineWater - w >= 0):
            state = 1
            machine.machineWater = machine.machineWater - w
        else:
            state = 0
            print('Sorry, not enough water!')
        if(machine.machineMilk - m > 0 and state == 1):
            machine.machineMilk = machine.machineMilk - m
        else:
            state = 0
        if(machine.machineCoffeeBeans - cb > 0 and state == 1):
            machine.machineCoffeeBeans = machine.machineCoffeeBeans - cb
        else:
            state = 0
        if(machine.machineCups - 1 >= 0 and state == 1):
            state = 1
            machine.machineCups = machine.machineCups - 1
        else:
            state = 0
        if(state == 1):
            print('I have enough resources, making you a coffee!')
            machine.machineMoney = machine.machineMoney + p

    def makeEspresso(self):
        self.makeCoffee(250,0,16,4)

    def makeLatte(self):
        self.makeCoffee(350,75,20,7)

    def makeCappuccino(self):
        self.makeCoffee(200,100,12,6)



machine = Machine()
coffee = Coffee(machine)
state = ''
while(state != 'exit'):
    print('\nWrite action (buy, fill, take, remaining, exit):')
    state = input()
    if(state == 'buy'):
        print('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        typeOfCoffee = input()
        if(typeOfCoffee == 'back'):
            continue
        elif(int(typeOfCoffee) == 1):
            coffee.makeEspresso()
        elif(int(typeOfCoffee) == 2):
            coffee.makeLatte()
        elif(int(typeOfCoffee) == 3):
            coffee.makeCappuccino()
    elif(state == 'take'):
        machine.withdrawMoney()
    elif(state == 'fill'):
        machine.fillMachine()
    elif(state == 'remaining'):
        machine.printStats()


