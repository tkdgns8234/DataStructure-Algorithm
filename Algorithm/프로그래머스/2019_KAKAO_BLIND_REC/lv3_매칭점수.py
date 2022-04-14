# 내가 만든 로직
# 1. 기본점수 + 외부링크 수 구해놓기 + 링크 구하기
# 2. dict[링크] = (idx, 기본점수, 링크점수의 합, 링크 수) <- 링크 수를 빼먹었다 다시 넣음
# 구현이 꼬여서 오래걸리고 길어진 이유
# 1. 처음에 링크점수 때문에 topologysort 를 사용해아한다고 생각했다.(잘못생각함)
# 2. 링크점수를 구하는 방법을 잘못 생각하고 진행했다.
# 성공은 했다!!!, 하지만 1시간 40분이나 걸렸고, 예상 외로 변수가 많이 생겨 너무 코드도 정리가 안됐다.

# 다른 사람의 코드를 참고해보자

def get_page_url(page):
    URL_TAG = "<meta property=\"og:url\" content=\""

    url = ""
    idx = str(page).find(URL_TAG) + len(URL_TAG)
    while page[idx] != "\"":
        url += page[idx]
        idx += 1
    return url

def get_normal_score(word, page):
    word = word.upper()
    page = page.upper()
    count = 0
    start_idx = 0

    for i in range(1, len(page)):
        if not str(page[i]).isalpha():
            # 단어별 갯수 count
            if word == page[start_idx:i]:
                count += 1
            start_idx = i+1
    return count


def get_link_score(pages, score):
    LINK_TAG = "<a href=\""
    for i, page in enumerate(pages):
        linked_score = 0
        idx = str(page).find(LINK_TAG) + len(LINK_TAG) # 찾고자 하는 string이 없는 경우 -1 리턴
        while idx > len(LINK_TAG):
            link = ""
            while page[idx] != "\"":
                link += page[idx]
                idx += 1
            # 해당 링크에 i 인덱스 기본점수 + 링크 수 더해
            if link in score.keys():
                for key in score.keys():
                    if score[key][0] == i:
                        score[link][2] += score[key][1]/score[key][3]

            idx = str(page).find(LINK_TAG, idx) + len(LINK_TAG)

def get_outer_link_count(page):
    LINK_TAG = "<a href=\""

    link_count = 0
    idx = str(page).find(LINK_TAG) + len(LINK_TAG)  # 찾고자 하는 string이 없는 경우 -1 리턴
    while idx > len(LINK_TAG):
        link_count += 1
        idx = str(page).find(LINK_TAG, idx) + len(LINK_TAG)
    return link_count

def get_score_info(word, pages, score):

    for idx, page in enumerate(pages):
        url = get_page_url(page)
        n_score = get_normal_score(word, page)
        outer_link_count = get_outer_link_count(page)
        score[url] = [idx, n_score, 0, outer_link_count]

    get_link_score(pages, score)


def solution(word, pages):
    score = dict()
    get_score_info(word, pages, score)

    answer = 0
    max_val = 0
    for key in score.keys():
        idx, normal_s, link_s = score[key][0], score[key][1], score[key][2]
        if max_val < normal_s + link_s:
            max_val = normal_s + link_s
            answer = idx
        elif max_val == normal_s + link_s:
            answer = min(answer, idx)

    return answer
#
v = solution('Muzi', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"])
print(v)


# 훨씬 간결하고 좋은 풀이
# 나와 다른 점
# 1. split을 사용해 문자를 찾는다
# 2. 구조화가 잘되어있다. (난 링크점수 구하는 방법을 초반에 잘못 이해해서 꼬였다)
# 3. 링크 점수를 구하는 방법
# 4. 정답을 구하는 방법 (sort 이용)
def getScore(word, page):
    import re
    return re.sub('[^a-z]+', '.', page.lower()).split('.').count(word.lower())

def solution(word, pages):
    webpages = {}
    for i, page in enumerate(pages):
        pagetitle = page.split('<meta property=\"og:url\" content=\"')[1].split('\"')[0]
        links = []
        for link_long in page.split('a href=\"')[1:]:
            links.append(link_long.split('\"')[0])
        webpages[pagetitle] = [i, getScore(word, page), links, 0] #3은 링크점수

    for page in webpages.values():
        for target in page[2]:
            try:
                webpages[target][3] += page[1] / len(page[2])
            except:
                pass
    answer = []
    print(webpages)
    for page in webpages.values():
        answer.append([page[0], page[1] + page[3]])

    answer.sort(key=lambda x:x[0])
    return sorted(answer, key=lambda x:x[1], reverse=True)[0][0]