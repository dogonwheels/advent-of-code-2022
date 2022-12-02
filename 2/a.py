def parseRound(line):
    opponent_move = {"A": "rock", "B": "paper", "C": "scissors"}
    player_move = {"X": "rock", "Y": "paper", "Z": "scissors"}

    tokens = line.split()
    return {"opponent": opponent_move[tokens[0]], "player": player_move[tokens[1]]}


def scoreRound(round):
    played_scores = {"rock": 1, "paper": 2, "scissors": 3}

    round_scores = {
        "rock": {"rock": 3, "paper": 0, "scissors": 6},
        "paper": {"rock": 6, "paper": 3, "scissors": 0},
        "scissors": {"rock": 0, "paper": 6, "scissors": 3},
    }

    played = played_scores[round["player"]]
    result = round_scores[round["player"]][round["opponent"]]

    return played + result


input = open("2/input").readlines()

rounds = list(map(parseRound, input))
scores = list(map(scoreRound, rounds))

print(sum(scores))
