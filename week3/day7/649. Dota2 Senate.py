"""
649. Dota2 Senate

Dota2 세계에는 두 개의 정당이 있습니다. Radiant와 Dire입니다.

Dota2 의회는 이 두 정당에 속한 의원들로 구성되어 있습니다. 이제 의회는 Dota2 게임의 변경 사항을 결정하려고 합니다.

이 변경 사항에 대한 투표는 라운드 방식으로 진행됩니다. 각 라운드에서 각 의원은 다음 두 가지 권리 중 하나를 행사할 수 있습니다.

다른 의원의 권리를 박탈하기:
한 의원은 다른 의원 한 명이 현재 라운드와 이후 모든 라운드에서 모든 권리를 잃도록 만들 수 있습니다.
승리 선언하기:
아직 투표할 권리를 가진 의원들이 모두 자신과 같은 정당에 속해 있다면, 해당 의원은 승리를 선언하고 게임의 변경 사항을 결정할 수 있습니다.

문자열 senate가 주어집니다. 이 문자열은 각 의원이 어느 정당에 속해 있는지를 나타냅니다.

'R'은 Radiant
'D'는 Dire

를 의미합니다.

의원의 수가 n명이라면, 주어진 문자열의 길이 역시 n입니다.

투표 절차는 주어진 순서대로 첫 번째 의원부터 마지막 의원까지 진행됩니다. 마지막 의원까지 진행한 뒤에도 투표가 끝나지 않았다면 다시 처음부터 다음 라운드를 진행합니다.

권리를 잃은 의원은 이후 절차에서 건너뜁니다. 

모든 의원은 자신의 정당이 승리하도록 하기 위해 최적의 전략으로 행동한다고 가정합니다.

최종적으로 어느 정당이 승리를 선언하고 Dota2 게임의 변경 사항을 결정하게 될지 예측하세요.

결과로 다음 중 하나를 반환해야 합니다.

"Radiant"
"Dire"

# 의사코드 

1. 의원 하나당 행동은 다른 의원 투표권한 박탈 or 승리선언임.
2. 리스트 두개 선언해서, 끝에 length 비교하게 하고, past_party 기록하게 해서 하면 될것 같은데?
3. 만약 past_party와 현재 party가 다르다면 append를 못하게 해야할거고.
"""



# 이전 풀이: 인접한 정당만 비교하기 때문에 다음 라운드와 누적된 투표권 박탈을 처리하지 못한다.
# class Solution:
#     def predictPartyVictory(self, senate: str) -> str:
#         Radiant = 0
#         Dire = 0
#         past_party = ''
#
#         print(len(senate))
#
#         for i in range(len(senate)):
#             crt_party = senate[i]
#
#             if past_party != '' and past_party != crt_party:
#                 past_party = crt_party
#                 continue
#
#             if crt_party == 'R':
#                 Radiant += 1
#                 print(Radiant)
#             elif crt_party == 'D':
#                 Dire += 1
#                 print(Dire)
#
#             past_party = crt_party
#             print(crt_party)
#
#         return 'Radiant' if Radiant > Dire else 'Dire'
#
# print(Solution().predictPartyVictory("RRDDD"))


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        balance = 0

        while 'R' in senate and 'D' in senate:
            next_round = ''

            for party in senate:
                if party == 'R':
                    if balance >= 0:
                        next_round += 'R'
                    balance += 1
                else:
                    if balance <= 0:
                        next_round += 'D'
                    balance -= 1

            senate = next_round

        return 'Radiant' if senate[0] == 'R' else 'Dire'


print(Solution().predictPartyVictory("RRDDD"))
