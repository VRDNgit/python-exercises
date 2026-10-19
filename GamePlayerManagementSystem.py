class Player:
    
    total_player = 0

    def __init__(self, username, health, score):
        self.username = username
        self.health = health
        self.score = score
        Player.total_player += 1

    def take_damage(self, damage):
        if damage <= 0:
            return "Invalid damage"
        elif damage > self.health:
            self.health = 0
            return f"health = {self.health}"
        else:
            self.health -= damage
            return f"health = {self.health}"

    @staticmethod
    def is_valid_score(score):
        if score >= 0:
            return True
        else:
            return False

    @classmethod
    def get_total_players(cls):
        return cls.total_player

player1 = Player("Shadow", 100, 50)
player2 = Player("Phoenix", 80, 120)

print(player1.take_damage(30))
print(player1.take_damage(100))
print(player2.take_damage(-5))

print(Player.is_valid_score(0))
print(Player.is_valid_score(-10))

print(Player.get_total_players())