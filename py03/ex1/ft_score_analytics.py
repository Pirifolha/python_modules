#!/usr/bin/env python3

import sys


def score_analytics():
    scores: list[int] = []
    for arg in sys.argv[1:]:
        try:
            value = int(arg)
            scores.append(value)
        except ValueError:
            print(f"Invalid score: {arg}")
            return
    print("=== Player Score Analytics ===")
    if len(scores) < 1:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py"
            " <score1> <score2> ..."
        )
        return
    players: int = len(scores)
    total_score: int = sum(scores)
    high_score: int = max(scores)
    lowest_score: int = min(scores)
    average_score: float = total_score / players
    score_range: int = high_score - lowest_score
    print(f"Scores processed: {scores}")
    print(f"Total players: {players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {lowest_score}")
    print(f"Score range: {score_range}")


score_analytics()
