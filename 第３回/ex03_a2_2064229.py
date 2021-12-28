scores = [76, 98, 80, 69, 49, 88, 71, 66, 82, 100]

for i in range(len(scores)):
    if scores[i] >= 90:
        scores[i] = 'S'
    elif scores[i] >= 80:
        scores[i] = 'A'
    elif scores[i] >= 70:
        scores[i] = 'B'
    elif scores[i] >= 60:
        scores[i] = 'C'
    else:
        scores[i] = 'F'

print(scores)
