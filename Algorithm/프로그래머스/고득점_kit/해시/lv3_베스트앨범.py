from collections import defaultdict

def solution(genres, plays):
    dic = defaultdict(list)
    for i in range(len(genres)):
        dic[genres[i]].append((i, plays[i]))

    genres_order = []
    for key in dic:
        # s == 장르의 총 play 합
        s = sum([j[1] for j in dic[key]])
        genres_order.append((key, s))

    genres_order.sort(key= lambda x: -x[1])

    answer = []
    # 장르의 총 play 수가 높은 순으로 반복
    for k, v in genres_order:
        # 장르 내에서 play 수가 많은 2개를 뽑아 answer에 추가
        temp = sorted(dic[k], key=lambda x: -x[1])[:2]
        for idx, plays in temp:
            answer.append(idx)

    return answer


v = solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
print(v)


# 다른풀이
# 가독성은 떨어지는데 테크니컬하다
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer


# 가독성 좋은 코드
# 아래 album class의 __lt__ 등 함수들은 클래스 크기 비교를 위한 내장함수를 오버라이딩 한 것이다.

def solution(genres, plays):
    answer = []
    dic = {}
    album_list = []
    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
        album_list.append(album(genres[i], plays[i], i))

    dic = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)
    album_list = sorted(album_list, reverse=True)



    while len(dic) > 0:
        play_genre = dic.pop(0)
        print(play_genre)
        cnt = 0;
        for ab in album_list:
            if play_genre[0] == ab.genre:
                answer.append(ab.track)
                cnt += 1
            if cnt == 2:
                break

    return answer

class album:
    def __init__(self, genre, play, track):
        self.genre = genre
        self.play = play
        self.track = track

    def __lt__(self, other):
        return self.play < other.play
    def __le__(self, other):
        return self.play <= other.play
    def __gt__(self, other):
        return self.play > other.play
    def __ge__(self, other):
        return self.play >= other.play
    def __eq__(self, other):
        return self.play == other.play
    def __ne__(self, other):
        return self.play != other.play