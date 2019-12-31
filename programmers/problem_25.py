'''
오픈채팅방 (카카오)
https://programmers.co.kr/learn/courses/30/lessons/42888

채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 record가 매개변수로 주어질 때, 모든 기록이 처리된 후,
최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return 하도록 solution 함수를 완성하라.

record는 다음과 같은 문자열이 담긴 배열이며, 길이는 1 이상 100,000 이하이다.
모든 유저는 [유저 아이디]로 구분한다.
[유저 아이디] 사용자가 [닉네임]으로 채팅방에 입장 - Enter [유저 아이디] [닉네임] (ex. Enter uid1234 Muzi)
[유저 아이디] 사용자가 채팅방에서 퇴장 - Leave [유저 아이디] (ex. Leave uid1234)
[유저 아이디] 사용자가 닉네임을 [닉네임]으로 변경 - Change [유저 아이디] [닉네임] (ex. Change uid1234 Muzi)
첫 단어는 Enter, Leave, Change 중 하나이다. 
각 단어는 공백으로 구분되어 있으며, 알파벳 대문자, 소문자, 숫자로만 이루어져있다.
유저 아이디와 닉네임은 알파벳 대문자, 소문자를 구별한다.
유저 아이디와 닉네임의 길이는 1 이상 10 이하이다.
채팅방에서 나간 유저가 닉네임을 변경하는 등 잘못 된 입력은 주어지지 않는다.
'''

def solution(records):
    answer = []
    name_table = {}
    actionList = {'Leave': '님이 나갔습니다.', 'Enter': '님이 들어왔습니다.'}
    caseList = []
    for record in records:
        record = record.split(' ')
        action = record[0]
        if action != 'Leave':
            name_table[record[1]] = record[2]
        if action != 'Change':
            caseList.append((action, record[1]))
    
    for action, id in caseList:
        answer.append(name_table[id] + actionList[action]) 
    return answer
    

if __name__ == '__main__':
    input = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    target = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
    result = solution(input)
    print(result)
    print(result == target)