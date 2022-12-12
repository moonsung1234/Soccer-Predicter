
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

# make match list
match = []

for i, target_ct in enumerate(country) :
    for ct in country[i + 1:] :
        if not ct in play_map[target_ct]["country"] :
            match.append([target_ct, ct])

# get all match
result = []

def play(map, match_index) :
    if match_index == len(match) :
        result.append(map)

        return
    
    # win
    temp_map = copy.deepcopy(map)
    temp_map[match[match_index][0]]["win"] += 1
    temp_map[match[match_index][1]]["lose"] += 1

    play(temp_map, match_index + 1)

    # lose
    temp_map = copy.deepcopy(map)
    temp_map[match[match_index][0]]["lose"] += 1
    temp_map[match[match_index][1]]["win"] += 1

    play(temp_map, match_index + 1)

    # draw
    temp_map = copy.deepcopy(map)
    temp_map[match[match_index][0]]["draw"] += 1
    temp_map[match[match_index][1]]["draw"] += 1

    play(temp_map, match_index + 1)

play(play_map, 0)

# get match we want
final = []

def print_map(map) :
    temp_str = ""

    for ct in map.keys() :
        temp_str += f'{ct} win : {map[ct]["win"]} lose : {map[ct]["lose"]} draw : {map[ct]["draw"]} \n'

    print(temp_str)

for result_map in result :
    result_cts = sorted(result_map.keys(), key=lambda x : result_map[x]["win"] * 3 + result_map[x]["draw"], reverse=True)

    if result_cts[0] == target_country or result_cts[1] == target_country :
        final.append(result_map)

        print_map(result_map)

print(len(match), len(result), len(final))
    