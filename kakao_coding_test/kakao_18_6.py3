import re
reHead = re.compile('<head>(?P<inner>.+)</head>',re.DOTALL) # head 규칙
reMeta = re.compile('<meta property="og:url" content="https://(?P<url>.+)"/>') # url 규칙
reBody = re.compile('<body>(?P<inner>.+)</body>',re.DOTALL) # body 규칙
reLink = re.compile('<a href="https://(?P<link>.*?)">',re.DOTALL) # link 규칙

db_dict = {}
"""
key = url
value = [num_of_out_link, [in_link_list], basic_score, index]
"""


def get_head_content(page):
    return reHead.search(page).group("inner")

def get_head_url(string):
    return reMeta.search(string).group("url")

def get_body_content(page):
    return reBody.search(page).group("inner")

def get_body_links(string):
    return [cursor.group('link') for cursor in reLink.finditer(string)]

def build_db(word, pages):
    """
    입력으로 받은 pages와 word를 통해 db_dict을 구성한다.
    """
    reAll = re.compile('[a-zA-Z]+')
    reWord = re.compile(word, re.IGNORECASE)
    
    for idx, page in enumerate(pages):
        all_words = reAll.findall(page)
        words = [w for w in all_words if reWord.match(w) and len(w) == len(word)]
        basic_score = len(words)
        url = get_head_url(get_head_content(page))
        out_links = get_body_links(get_body_content(page))
        for link in out_links:
            if not db_dict.get(link, False):
                db_dict[link] = [-1, [url], -1, -1]
            else:
                db_dict[link] = [db_dict[link][0], db_dict[link][1]+[url], db_dict[link][2], db_dict[link][3]]
        if not db_dict.get(url, False):
            db_dict[url] = [len(out_links), [], basic_score, idx]
        else:
            db_dict[url] = [len(out_links), db_dict[url][1], basic_score, idx]

def find_best():
    best_val = -1
    best_idx = -1
    for key, value in db_dict.items():
        basic_score = value[2]
        link_score = 0
        for link in value[1]:
            link_score += db_dict[link][2]/db_dict[link][0]
        if best_val < basic_score + link_score:
            best_val = basic_score + link_score
            best_idx = value[3]
        if best_val == basic_score + link_score and best_idx > value[3]:
            best_idx = value[3]
    return best_idx

def solution(word, pages):
    answer = 0
    build_db(word, pages)

    answer = find_best()

    return answer

