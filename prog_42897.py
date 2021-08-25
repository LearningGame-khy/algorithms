### 코딩테스트 연습 > 동적계획법 > 도둑질
# 인접한 집들은 방범장치로 연결되어 있으므로, 인접한 두 집을 털면 경보가 울림
# 도둑이 훔칠 수 있는 돈의 최대값은 ?
# 집은 3 <= 집수 <= 1,000,000
# 돈은 0 <= 돈 <= 1,000
def solution(money):
    # 1. 0번 집을 터는 경우, 마지막 집은 털지못함 => range(2, len(money)-1)
    # 2. 0번 집을 안터는 경우, 마지막 집은 경우에 따라 텀 => range(2, len(money))
    # 2가지에 대한 값을 구해야함
    dp0 = [0 for _ in range(len(money))]
    dp1 = [0 for _ in range(len(money))]

    # 1번 케이스
    dp0[0] = money[0]

    # 1, 2번 케이스를 두 번 돌리면 비효율적이니 한번에
    for i in range(1, len(money)-1):
        dp0[i] = max(dp0[i-1], dp0[i-2]+money[i])
        dp1[i] = max(dp1[i-1], dp1[i-2]+money[i])

    # 2번 케이스는 끝까지 확인해야하므로 마지막 값 탐색
    dp1[-1] = max(dp1[-2], dp1[-3]+money[-1])

    answer = max(dp0[-2], dp1[-1])
    return answer

if __name__ == "__main__":
    money = [1, 2, 3, 1]

    print(solution(money))