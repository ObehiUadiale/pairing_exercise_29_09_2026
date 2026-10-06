def recipe(participants):
    if participants == []:
        return ""

    if len(participants) == 1:
        return participants[0]


    if len(participants) == 2:
        return f"{participants[0]} & {participants[1]}"

    if len(participants) >= 3:
       return f"{', '.join(participants[:-1])} & {participants[-1]}"
