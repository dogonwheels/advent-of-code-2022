def parseStrategy(line):
    opponent_move = {"A": "rock", "B": "paper", "C": "scissors"}
    score_for_result = {"X": 0, "Y": 3, "Z": 6}

    tokens = line.split()
    return {"opponent": opponent_move[tokens[0]], "score": score_for_result[tokens[1]]}


def scoreStrategy(round):
    # if opponent plays X, and player wants Y points - what should they play?
    move_for_points = {
        "rock": {0: "scissors", 3: "rock", 6: "paper"},
        "paper": {0: "rock", 3: "paper", 6: "scissors"},
        "scissors": {0: "paper", 3: "scissors", 6: "rock"},
    }
    played_scores = {"rock": 1, "paper": 2, "scissors": 3}

    # choose the move that will result in the desired score
    move = move_for_points[round["opponent"]][round["score"]]

    return played_scores[move] + round["score"]


input = open("2/input").readlines()

strategy = list(map(parseStrategy, input))
scores = list(map(scoreStrategy, strategy))

print(sum(scores))
