def create_db():
    # cpp, java, python, - 4   4
    # frontend, backend, - 3   12
    # junior, senior, -    3   36
    # chicken, pizza, -    3   108
    # score
    info_db = dict()
    for lang in ['cpp', 'java', 'python', '-']:
        info_db[lang] = dict()
        for job in ['frontend', 'backend', '-']:
            info_db[lang][job] = dict()
            for career in ['junior', 'senior', '-']:
                info_db[lang][job][career] = dict()
                for food in ['chicken', 'pizza', '-']:
                    info_db[lang][job][career][food] = []

    return info_db


def insert_data(info_db, data):
    # data = [lang, job, career, food, score]

    lang_range = [data[0], '-'] if data[0] != '-' else [data[0]]
    job_range = [data[1], '-'] if data[1] != '-' else [data[1]]
    career_range = [data[2], '-'] if data[2] != '-' else [data[2]]
    food_range = [data[3], '-'] if data[3] != '-' else [data[3]]

    data[4] = int(data[4])
    for lang in lang_range:
        for job in job_range:
            for career in career_range:
                for food in food_range:
                    info_db[lang][job][career][food].append(data[4])


def search_data(info_db, data):
    result = 0

    lang, job, career, food, score = data
    score = int(score)

    info_db[lang][job][career][food].sort()

    from bisect import bisect_left
    search_index = bisect_left(info_db[lang][job][career][food], score)
    result = len(info_db[lang][job][career][food][search_index:])


    return result

def solution(info, query):
    answer = []

    # 지원자 정보 테이블 생성
    info_db = create_db()

    # 지원자 정보 테이블 삽입
    for applicant_data in info:
        applicant = applicant_data.split(' ')
        insert_data(info_db, applicant)

    for query_data in query:
        data = list(filter(lambda x: x != 'and', query_data.split(' ')))
        answer.append(search_data(info_db, data))

    return answer

if __name__ == "__main__":
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

    print(solution(info, query))