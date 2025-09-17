def get_friends_favorite_candy_count(favorites):
    favorite_candies = {}
    for item in favorites:
        for candy in item[1]:
            favorite_candies[candy] = favorite_candies.get(candy, 0) + 1
    return favorite_candies

def create_new_candy_data_structure(data):
    candy_lovers = {}
    for item in data:
        for candy in item[1]:
            if candy not in candy_lovers:
                candy_lovers[candy] = []
            if item[0] not in candy_lovers[candy]:
                candy_lovers[candy].append(item[0])
                
    return candy_lovers
    

def get_friends_who_like_specific_candy(data, candy_name):
    candy_lovers = create_new_candy_data_structure(data)
    
    return tuple(candy_lovers[candy_name])

def create_candy_set(data):
    all_candies = set()
    candy_lovers = create_new_candy_data_structure(data)
    for candy in candy_lovers.keys():
        all_candies.add(candy)
    return all_candies
