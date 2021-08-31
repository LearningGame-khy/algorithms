### 메뉴 리뉴얼
# 2 <= orders <= 20  2 <= orders.item <= 10
# 1 <= course <= 10
# answer 오름차순, 동일할경우 모두 배열에 담아서
from itertools import combinations

def solution(orders, course):
    answer = []
    temp = []

    for order in orders:
        order = sorted(order)
        order = list(order)
        for course_cnt in course:
            for menu in combinations(order, course_cnt):
                new_menu = ''.join(menu)
                temp.append(new_menu)

    check = {}
    for menu in temp:
        if menu not in check:
            check[menu] = 1
        else:
            check[menu] += 1

    for course_cnt in course:
        max = 0
        temp = []
        for menu in check.keys():
            if len(menu) != course_cnt or check[menu] < 2:
                continue

            if check[menu] > max:
                temp = []
                max = check[menu]
                temp.append(menu)

            elif check[menu] == max:
                temp.append(menu)

        answer += temp

    return sorted(answer)

if __name__ == "__main__":
    orders = ["XYZ", "XWY", "WXA"]
    course = [2,3,4]

    print(solution(orders, course))