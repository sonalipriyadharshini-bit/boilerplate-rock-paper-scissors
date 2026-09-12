def player(prev_play, opponent_history=[]):

    # Reset history when a new game starts
    if prev_play == "":
        opponent_history.clear()

    # Store opponent's previous move
    if prev_play:
        opponent_history.append(prev_play)

    # First move
    if len(opponent_history) == 0:
        return "R"

    # --------------------------------
    # STEP 1: Try to find patterns
    # --------------------------------

    prediction = None

    # Try different pattern lengths
    for pattern_length in range(5, 0, -1):

        # We need enough moves to create a pattern
        if len(opponent_history) <= pattern_length:
            continue

        # Get the opponent's most recent pattern
        pattern = tuple(opponent_history[-pattern_length:])

        # Store possible next moves
        next_moves = []

        # Search the history for the same pattern
        for i in range(len(opponent_history) - pattern_length):

            old_pattern = tuple(
                opponent_history[i:i + pattern_length]
            )

            # If the same pattern occurred before
            if old_pattern == pattern:

                # Get the move that came after the pattern
                next_move = opponent_history[
                    i + pattern_length
                ]

                next_moves.append(next_move)

        # If we found the pattern before
        if len(next_moves) > 0:

            # Count each possible next move
            rock = next_moves.count("R")
            paper = next_moves.count("P")
            scissors = next_moves.count("S")

            # Predict the most common next move
            if rock >= paper and rock >= scissors:
                prediction = "R"

            elif paper >= rock and paper >= scissors:
                prediction = "P"

            else:
                prediction = "S"

            break

    # --------------------------------
    # STEP 2: If no pattern was found
    # --------------------------------

    if prediction is None:

        recent_moves = opponent_history[-10:]

        rock = recent_moves.count("R")
        paper = recent_moves.count("P")
        scissors = recent_moves.count("S")

        if rock >= paper and rock >= scissors:
            prediction = "R"

        elif paper >= rock and paper >= scissors:
            prediction = "P"

        else:
            prediction = "S"

    # --------------------------------
    # STEP 3: Beat the prediction
    # --------------------------------

    if prediction == "R":
        return "P"

    elif prediction == "P":
        return "S"

    else:
        return "R"