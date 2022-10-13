from frog import HighScores

scores = [10, 30, 90, 30, 100, 20, 10, 0, 30, 40, 95, 70, 70]
highscores = HighScores(scores)
print(highscores.personal_top_three())
