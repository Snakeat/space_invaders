class Stats():
    """"score info"""

    def __init__(self):
        """"stats initialisation"""
        self.reset_stats()
        self.run_game = True 
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """"stats update"""
        self.guns_left = 2
        self.score = 0