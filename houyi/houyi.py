from game.game import Game


class HouYi(Game):
    def __init__(self):
        super().__init__(1000, 200)
        self.defense = 100

    def houyiFight(self,enemy_hp, enemy_power,):
        while True:
            self.hp =self.hp+ self.defense - enemy_power
            enemy_hp = enemy_hp - self.power
            print(f"我的血量{self.hp}")
            print(f"敌人的血量{enemy_hp}")
            print(enemy_hp)
            if self.hp <=0:
                print("我输了")
                break
            elif enemy_hp<=0:
                print("敌人输了")
                break



hp = 1000
power = 200
game = HouYi()
game.houyiFight(hp, power)