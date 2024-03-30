import sys
input = sys.stdin.readline

N = int(input())   # 채팅방의 기록 수 N
chat_room, emoticon = set(), 0
for i in range(N):
    chat = input().strip()
    if chat == 'ENTER':
        emoticon += len(chat_room)
        chat_room = set()
    else:
        chat_room.add(chat)
emoticon += len(chat_room)

print(emoticon)