def calculate_average(scores):
    return sum(scores) / len(scores)

def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

scores = [85, 90, 78]
avg = calculate_average(scores)

print("Average:", avg)
print("Grade:", grade(avg))