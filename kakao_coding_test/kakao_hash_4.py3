def solution(genres, plays):
    song_dict = {}
    count_dict = {}
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        song_dict[genre] = song_dict.get(genre, []) + [i]
        count_dict[genre] = count_dict.get(genre, 0) + play
    
    answer = []
    
    sorted_count = sorted(list(count_dict.items()), key=lambda x: x[1], reverse=True)
    for i in range(len(sorted_count)):
        songs = song_dict[sorted_count[i][0]]
        sorted_songs = sorted(songs, key=lambda x: plays[x], reverse=True)
        for j in range(len(sorted_songs)):
            answer.append(sorted_songs[j])
            if j == 1:
                break
    
    return answer