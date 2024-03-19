from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass

class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!!")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")

class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket!")


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass

class Quack(QuackBehavior):
    def quack(self):
        print("Quack")

class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")

class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")



class Duck(ABC):
    def __init__(self):
        self.flyBehavior = FlyBehavior
        self.quackBehavior = QuackBehavior

    def performFly(self):
        self.flyBehavior.fly(self)

    def performQuack(self):
        self.quackBehavior.quack(self)

    def swim(self):
        print("All ducks float, even decoys!")

    def setFlyBehavior(self, fb: FlyBehavior):
        self.flyBehavior = fb

    def setQuackBehavior(self, qb: QuackBehavior):
        self.quackBehavior = qb

class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.flyBehavior = FlyWithWings
        self.quackBehavior = Quack

    def Mallard_voice(self):
        print("I'm a real Mallard duck")

class ModelDuck(Duck):
    def __init__(self):
        super().__init__()
        self.flyBehavior = FlyNoWay
        self.quackBehavior = Quack

    def voice(self):
        print("I'm a model duck")
class MiniDuckSimulator:
    def __init__(self):

        model = ModelDuck()
        model.performFly()
        model.performQuack()
        model.voice()
        model.setFlyBehavior(FlyRocketPowered)
        model.performFly()


m = MiniDuckSimulator()