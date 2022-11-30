
import copy

# input country
country = input("같은 조에 속한 나라들을 입력해주세요. (ex : A, B, C, D) : ")
country = list(map(lambda x : str.strip(x), str.split(country, ",")))
play_map = {}

for ct in country :
    play_map[ct] = {}
    play_map[ct]["win"] = 0
    play_map[ct]["lose"] = 0
    play_map[ct]["draw"] = 0
    play_map[ct]["country"] = []

# input play info
play_info = input("나라별 경기 기록을 입력해주세요. (ex :  A : B = 0 : 0, C : D = 2 : 0, ...) : ")

# preprocessing

if not str.strip(play_info) == "" :
    play_info = list(map(lambda x : str.strip(x), str.split(play_info, ",")))
    
    for info in play_info :
        info = list(map(lambda x : str.strip(x), str.split(info, "=")))
        ct1, ct2 = list(map(lambda x : str.strip(x), str.split(info[0], ":")))
        sc1, sc2 = list(map(lambda x : int(x), str.split(info[1], ":")))

        if ct1 in country and ct2 in country :
            play_map[ct1]["country"].append(ct2)
            play_map[ct2]["country"].append(ct1)

            if sc1 > sc2 :
                play_map[ct1]["win"] += 1
                play_map[ct2]["lose"] += 1
            
            elif sc1 < sc2 :
                play_map[ct1]["lose"] += 1
                play_map[ct2]["win"] += 1

            else :
                play_map[ct1]["draw"] += 1
                play_map[ct2]["draw"] += 1

        else :
            print("입력하신 기록 중 존재하지 않는 국가가 있습니다.")

# input country that you want to know the rank
target_country = str.strip(input("원하는 국가를 입력해주세요. : "))
result = []

def print_map(map) :
    string = ""
    
    for ct in map.keys() :
        string += "{0} win:{1} lose:{2} draw:{3} \n".format(ct, map[ct]["win"], map[ct]["lose"], map[ct]["draw"])

    print(string)

def save(map) :
    for ct in map.keys() :
        if len(map[ct]["country"]) != len(country) - 1 :
            return

    result.append(map)

def play(map, ct) :
    if len(map[ct]["country"]) == len(country) :

        return map, ct

    for _ct in country :
        if not _ct == ct and not _ct in map[ct]["country"] :
            # win
            temp_map = copy.deepcopy(map)
            temp_map[ct]["win"] += 1
            temp_map[_ct]["lose"] += 1
            temp_map[ct]["country"].append(_ct)
            temp_map[_ct]["country"].append(ct)

            temp_map, temp_ct = play(temp_map, _ct)

            save(temp_map)

            # lose
            temp_map = copy.deepcopy(map)
            temp_map[ct]["lose"] += 1
            temp_map[_ct]["win"] += 1
            temp_map[ct]["country"].append(_ct)
            temp_map[_ct]["country"].append(ct)

            temp_map, temp_ct = play(temp_map, _ct)

            save(temp_map)

            # draw
            temp_map = copy.deepcopy(map)
            temp_map[ct]["draw"] += 1
            temp_map[_ct]["draw"] += 1
            temp_map[ct]["country"].append(_ct)
            temp_map[_ct]["country"].append(ct)

            temp_map, temp_ct = play(temp_map, _ct)

            save(temp_map)

    return map, ct

# play
play(
    copy.deepcopy(play_map),
    target_country
)

print(result, len(result))
