import pytest
from candy_problem.candy_problem import * 



def test_friends_favorite_candy_count():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "laffy taffy"]],
        [ "Bob", ["milky way", "lollipop"]],
        [ "Arlene", ["milky way", "laffy taffy"]],
        [ "Carlie", ["nerds"]]
    ]

    # Act
    favorite_candies = get_friends_favorite_candy_count(friend_favorites)
    
    # Assert
    assert favorite_candies == {"lollipop" : 2, "laffy taffy": 2, "milky way": 2, "nerds": 1}

def test_create_candy_data_structure_type():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "laffy taffy"]],
        [ "Bob", ["milky way", "lollipop"]],
        [ "Arlene", ["milky way", "laffy taffy"]],
        [ "Carlie", ["nerds"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert type(new_candy_data) == dict

# Add your own assertions to the test below
def test_create_candy_data_structure_values():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "laffy taffy"]],
        [ "Bob", ["milky way", "lollipop"]],
        [ "Arlene", ["milky way", "laffy taffy"]],
        [ "Carlie", ["nerds"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert len(new_candy_data) == 4


def test_get_friends_who_like_specific_candy():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "laffy taffy"]],
        [ "Bob", ["milky way", "lollipop"]],
        [ "Arlene", ["milky way", "laffy taffy"]],
        [ "Carlie", ["nerds"]]
    ]
    candy_name = "lollipop"

    # Act
    friends = get_friends_who_like_specific_candy(friend_favorites, candy_name)
    
    # Assert
    assert friends == ("Sally", "Bob")

def test_create_candy_set():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "laffy taffy"]],
        [ "Bob", ["milky way", "lollipop"]],
        [ "Arlene", ["milky way", "laffy taffy"]],
        [ "Carlie", ["nerds"]]
    ]

    # Act
    all_candies = create_candy_set(friend_favorites)
    
    # Assert
    assert  all_candies == {"lollipop", "laffy taffy", "milky way", "nerds"}
