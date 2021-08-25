### 위클리 챌린지 > 2주차
def is_only_maxmin(score, student_score):
    # print(score, max(student_score), min(student_score), student_score, student_score.count(score))
    if max(student_score) == score and student_score.count(score) == 1:
        return True

    if min(student_score) == score and student_score.count(score) == 1:
        return True

    return False

def get_grade(score):
    if 90 <= score:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 50 <= score < 70:
        return 'D'
    else:
        return 'F'

def solution(scores):
    score_sum = []
    for student_no in range(len(scores)):
        student_score = [scores[idx][student_no] for idx in range(len(scores))]

        if is_only_maxmin(student_score[student_no], student_score):
            score = (sum(student_score) - student_score[student_no]) / (len(student_score)-1)
        else:
            score = sum(student_score) / len(student_score)
        score_sum.append(score)

    answer = ''.join(list(map(lambda x: get_grade(x), score_sum)))
    return answer

if __name__ == "__main__":
    scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]

    print(solution(scores))