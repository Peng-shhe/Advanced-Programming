class Role:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.hp_max = 150
        self.hp = 150
        self.mp_max = 100
        self.mp = 100
        self.offense = 35
        self.spirit = 20
        self.defense = 40
        self.speed = 30
        self.luck = 30
        self.is_alive = True
        self.is_defending = False
        
        #普攻
        def attack(self, target):
            
            pass
        
        #施法
        def cast(self, target,skill):
            
            pass
        
        #防御
        def defend(self):
            pass
        
        #升级
        def levelUp(self):
            self.level += 1
            pass
        
        #结束回合
        def endturn(self):
            pass
        
        #治疗
        def heal(self,amount):
            self.hp += amount
            if self.hp > self.hp_max:
                self.hp = self.hp_max
        #可替换：
        #self.hp = min(self.hp_max,self.hp)    
            
        #回蓝
        def restoreMP(self,amount):
            self.mp += amount
            if self.mp > self.mp_max:
                self.mp = self.mp_max
        #可替换：
        #self.mp = min(self.mp_max,self.mp)
        
        
        
        