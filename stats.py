class Stats():
    # отслеживание статистики
    def __init__(self):
        """ициирует статитстику"""
        self.reset_stats()
        self.run_game = True
        with open('record.txt', 'r') as f:
            self.record = int(f.readline())


    def reset_stats(self):
        """статистика изменяющаяся во время игры"""
        self.guns_left = 3
        self.score = 0



