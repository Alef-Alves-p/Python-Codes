# Complete the function so that it finds the average of the three scores passed to it and returns 
# the letter value associated with that grade.

def get_grade(s1, s2, s3):
    # Code here
    numbs = [s1, s2, s3]
    score = sum(numbs) / len(numbs)
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 90:
        return "B"
    elif 70 <= score <= 80:
        return "C"
    elif 60 <= score <= 70:
        return "D"
    elif 0 <= score <= 60:
        return "F"

print(get_grade(70, 90, 40))
print(get_grade(30, 36, 45))
print(get_grade(98, 44, 12))
print(get_grade(150, 21, 50))
print(get_grade(96, 54, 74))
