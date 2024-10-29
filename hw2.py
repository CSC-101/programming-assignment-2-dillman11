import data

# Write your functions for each part in the space below.

# Part 1
def create_rectangle(point1:data.Point, point2:data.Point) -> data.Rectangle:
    new_rect = data.Rectangle(data.Point(0,0), data.Point(0,0))
    if point1.x > point2.x:
        new_rect.bottom_right.x = point1.x
        new_rect.top_left.x = point2.x
    else:
        new_rect.bottom_right.x = point2.x
        new_rect.top_left.x = point1.x
    if point1.y < point2.y:
        new_rect.bottom_right.y = point1.y
        new_rect.top_left.y = point2.y
    else:
        new_rect.bottom_right.y = point2.y
        new_rect.top_left.y = point1.y
    return new_rect


# Part 2
def shorter_duration_than(duration1:data.Duration, duration2:data.Duration) -> bool:
    if duration1.minutes < duration2.minutes:
        return True
    elif duration1.minutes == duration2.minutes and duration1.seconds < duration2.seconds:
        return True
    else:
        return False

# Part 3
def songs_shorter_than(songs:list[data.Song],duration:data.Duration) -> list[data.Song]:
    short_songs = []
    for song in songs:
        if song.duration.minutes < duration.minutes:
            short_songs.append(song)
        elif song.duration.minutes == duration.minutes and song.duration.seconds < duration.seconds:
            short_songs.append(song)
    return short_songs


# Part 4
def running_time(songs:list[data.Song], playlist:list[int]) -> data.Duration:
    total = data.Duration(0, 0)
    for idx in playlist:
        total.minutes += songs[idx].duration.minutes
        total.seconds += songs[idx].duration.seconds
    total.minutes += total.seconds//60
    total.seconds %= 60
    return total


# Part 5
def validate_route(city_links:list[list[str]],route:list[str]) -> bool:
    for idx in range(len(route)-1):
        link = [route[idx], route[idx+1]]
        reverse_link = [route[idx+1],route[idx]]
        if link not in city_links and reverse_link not in city_links:
            return False
    return True


# Part 6
def longest_repetition(integers:list[int]) -> int or None:
    if integers == []:
        return None
    max_count = 0
    max_idx = 0
    count = 0
    for idx in range(len(integers)-1):
        if integers[idx] == integers[idx+1]:
            count += 1
        else:
            if count > max_count:
                max_count = count
                max_idx = idx - count
            count = 0
    if count > max_count:
        max_idx = len(integers)-1-count
    return max_idx


