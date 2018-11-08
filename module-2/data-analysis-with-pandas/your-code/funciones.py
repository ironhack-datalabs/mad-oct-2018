

def create_diff_grades(grades=['A', 'B', 'C', 'D', 'E'], pluses=['++', '+', '', '-', '--']): 
    return [g+p for g in grades for p in pluses][::-1] + ['']

def grade(s, l_grades=create_diff_grades()): 
    res = 0
    if (s.strip() in l_grades) and (len(s.strip()) > 0):   
        res = l_grades.index(s.strip())
    return int(res)