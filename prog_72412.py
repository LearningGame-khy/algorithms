def is_passed(person_info, q):
    for idx in range(len(person_info)-1):
        if q[idx] == '-':
            continue

        if person_info[idx] != q[idx]:
            return False

    if int(person_info[-1]) < int(q[-1]):
        return False

    return True


def solution(info, query):
    answer = []

    for q in query:
        result = 0
        q = list(filter(lambda x: x != 'and', q.split(' ')))
        for person in info:
            person_info = person.split(' ')
            if is_passed(person_info, q):
                result += 1

        answer += [result]

    return answer

if __name__ == "__main__":
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

    print(solution(info, query))