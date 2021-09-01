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

    data[4] = int(data[4])
    for lang in [data[0], '-']:
        for job in [data[1], '-']:
            for career in [data[2], '-']:
                for food in [data[3], '-']:
                    info_db[lang][job][career][food].append(data)

    # for lang in [data[0], '-']:
    #     for job in [data[1], '-']:
    #         for career in [data[2], '-']:
    #             for food in [data[3], '-']:
    #                 info_db[lang][job][career][food].sort(key=lambda x: x[4])

def search_data(info_db, data):
    result = 0

    lang, job, career, food, score = data
    score = int(score)

    info_db[lang][job][career][food].sort(key=lambda x: x[4])
    search_data = info_db[lang][job][career][food]
    for i in range(len(search_data)):
        if search_data[i][4] >= score:
            result = len(search_data[i:])
            break

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