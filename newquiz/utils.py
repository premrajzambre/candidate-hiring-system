def get_rank(score_percentage):
    ranks = [
        [100, "Impressive!", "Wow! You are a genius."],
        [75, "Well done!", "You know more than most people!"],
        [50, "Not bad!", "Please improve your performance."],
        [25, "Uh oh!", "You seriously need to work on yourself"],
        [0, "Not good!", "You are too bad"],
    ]

    for rank in ranks:
        if rank[0] <= score_percentage:
            return {'title': rank[1], 'description': rank[2]}

    raise ValueError("Invalid score %s" % score_percentage)
