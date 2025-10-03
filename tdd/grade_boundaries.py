import warnings

def calc_grade(p_mark):

    mark_dict = {'Max':500,'A*':450,'A':400,'B':300,'C':250,'D':150,'E':50,'U':0}
    try:
        p_mark = int(p_mark)
    except ValueError:
        warnings.warn('Please enter a number for the score')
        return None
    if p_mark > 500 or p_mark < 0:
        warnings.warn('Please enter a number in the valid range of marks 0-500')
        return None
    grade_bounds = list(mark_dict.items())
    for i in range(len(grade_bounds)):
        grade, mark_req = grade_bounds[i]
        if p_mark >= mark_req and grade != 'Max':
            return grade
    return 'U'

print(calc_grade(250.1))