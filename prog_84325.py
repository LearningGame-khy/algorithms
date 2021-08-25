### 위클리 챌린지 > 4주차
def solution(table, languages, preference):
    table_score = []
    for job_info in table:
        job_name, *job_language = job_info.split(' ')

        score = []
        for idx, language in enumerate(languages):
            # 직업 언어 선호도 점수화
            if language in job_language:
                score.append((5 - job_language.index(language)) * preference[idx])
            else:
                score.append(0)

        table_score.append([sum(score), job_name])

    # 점수순으로 내림차순, 이름 사전순으로 오름차순 정렬
    table_score = sorted(table_score, key=lambda x: (-x[0], x[1]))
    return table_score[0][1]

if __name__ == "__main__":
    # table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
    # languages = ["PYTHON", "C++", "SQL"]
    # preference = [7, 5, 5]

    table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
    languages = ["JAVA", "JAVASCRIPT"]
    preference = [7, 5]

    print(solution(table, languages, preference))