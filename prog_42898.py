### 코딩테스트 연습 > DP > 등굣길
# 1. 오른쪽 / 아래 만 사용해서 최단경로 구하기
# 2. 구한 최단경로 / 1,000,000,007의 나머지를 출력
# * 입력값: m, n, puddles(2차원배열) => 출력값: 최단경로수
# * m, n이 동시에 1이 되는 경우, 집과 학교가 물에 잠긴 경우는 없음
def is_water(x, y, route_score):
    if route_score[y][x] == -1:
        return True
    return False

def solution(col, row, puddles):
    # 집-학교 공간 생성
    route_score = [[0 for _ in range(col)] for _ in range(row)]

    # 물웅덩이 좌표 입력
    for x, y in puddles:
        route_score[y-1][x-1] = -1

    # 집-학교 거리 계산
    # 출발점 1 지정
    # 이동한 칸에서 나타날 수 있는 경로 수 = 왼쪽칸 + 위쪽칸 -> 이동할 수 있는게 오른쪽이랑 아래밖에 없으므로
    route_score[0][0] = 1
    for y in range(row):
        for x in range(col):
            if is_water(x, y, route_score) or (x == 0 and y == 0):
                continue
            # print(f'route_score[{y}][{x}] = {route_score[y - 1][x]} + {route_score[y][x - 1]}')
            if x == 0:
                if not is_water(x, y-1, route_score):
                    route_score[y][x] += route_score[y-1][x]
            elif y == 0:
                if not is_water(x-1, y, route_score):
                    route_score[y][x] += route_score[y][x-1]
            else:
                a = route_score[y-1][x] if not is_water(x, y-1, route_score) else 0
                b = route_score[y][x-1] if not is_water(x-1, y, route_score) else 0
                route_score[y][x] = a+b

    return route_score[-1][-1]

if __name__ == '__main__':
    m, n, puddles = 4, 3, [[2, 2]]

    print(solution(m, n, puddles))
