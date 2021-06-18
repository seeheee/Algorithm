from collections import defaultdict
from operator import itemgetter

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    music_dic = defaultdict(lambda: 0)

    for g, p in zip(genres, plays):
        music_dic[g] += p

    genre_rank = [genre for genre, play in sorted(music_dic.items(), key=itemgetter(1), reverse=True)]


    total_dict = defaultdict(lambda: [])

    # {'classic': [(500, 0), (150, 2), (800, 3)], 'pop': [(600, 1), (2500, 4)]}
    for i, genre_play_tuple in enumerate(zip(genres, plays)):
        total_dict[genre_play_tuple[0]].append((genre_play_tuple[1], i))

    answer = []
    for g in genre_rank:
        list1 = sorted(total_dict[g], key=itemgetter(0), reverse=True)
        # [(2500, 4), (600, 1)]
        # [(800, 3), (500, 0), (150, 2)]

        if len(list1) > 1:
            answer.append(list1[0][1])
            answer.append(list1[1][1])
        else:
            answer.append(list1[0][1])

    return answer


print(solution(genres, plays))