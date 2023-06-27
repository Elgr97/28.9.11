import pytest
import requests
from pydantic import BaseModel

#Тест на успешное создание нового пользователя

class AccessTokenRequest(BaseModel):
    access_token: str

class User(BaseModel):
    first_name: str
    last_name: str
    age: int

def test_create_new_user():
    url = "https://api.vk.com/method/users.get"
    params = {
        "access_token": "YOUR_TOKEN",
        "v": "5.131",
        "first_name": "John",
        "last_name": "Li",
        "age": 25
    }
    response = requests.post(url, params=params)
    user_data = response.json()["response"][0]
    user = User(**user_data)
    assert user.first_name == "John"
    assert user.last_name == "Li"
    assert user.age == 25


#Тест на обновление профиля пользователя
class UserUpdate(BaseModel):
    first_name: str
    last_name: str
    age: int

def test_update_user_profile():
    url = "https://api.vk.com/method/account.saveProfileInfo"
    params = {
        "access_token": "YOUR_TOKEN",
        "v": "5.131",
        "first_name": "Jane",
        "last_name": "Li",
        "age": 27
    }
    response = requests.post(url, params=params)
    user_data = response.json()["response"]
    user_update = UserUpdate(**params)
    assert user_data["first_name"] == user_update.first_name
    assert user_data["last_name"] == user_update.last_name
    assert user_data["age"] == user_update.age


#Тест на получение списка друзей пользователя
class Friend(BaseModel):
    id: int
    first_name: str
    last_name: str

def test_get_user_friends():
    url = "https://api.vk.com/method/friends.get"
    params = {
        "access_token": "YOUR_TOKEN",
        "v": "5.131"
    }
    response = requests.post(url, params=params)
    friends_data = response.json()["response"]["items"]
    friends = [Friend(**friend_data) for friend_data in friends_data]
    assert len(friends) > 0
    for friend in friends:
        assert friend.id > 0
        assert friend.first_name != ""
        assert friend.last_name != ""

#Тест на поиск пользователей по имени и фамилии
class UserSearch(BaseModel):
    id: int
    first_name: str
    last_name: str

def test_search_users():
    url = "https://api.vk.com/method/users.search"
    params = {
        "access_token": "YOUR_TOKEN",
        "v": "5.131",
        "q": "John Li",
        "fields": "id,first_name,last_name"
    }
    response = requests.post(url, params=params)
    users_data = response.json()["response"]["items"]
    users = [UserSearch(**user_data) for user_data in users_data]
    assert len(users) > 0
    for user in users:
        assert user.id > 0
        assert user.first_name != ""
        assert user.last_name != ""

#Тест на создание новой группы
class Group(BaseModel):
    id: int
    name: str

def test_create_new_group():
    url = "https://api.vk.com/method/groups.create"
    params = {
        "access_token": "YOUR_TOKEN",
        "v": "5.131",
        "title": "Test Group"
    }
    response = requests.post(url, params=params)
    group_data = response.json()["response"]
    group = Group(**group_data)
    assert group.id > 0
    assert group.name == "Test Group"

#Тест на присоединение пользователя к группе
class GroupJoin(BaseModel):
    member_id: int
    group_id: int

def test_join_group():
    url = "https://api.vk.com/method/groups.join"
    params = {
        "access_token": "YOUR_TOKEN",
        "v": "5.131",
        "group_id": "GROUP_ID"
    }
    response = requests.post(url, params=params)
    join_data = response.json()["response"]
    join = GroupJoin(**join_data)
    assert join.member_id > 0
    assert join.group_id == "GROUP_ID"

#Тест на получение списка новостей группы
class News(BaseModel):
    id: int
    text: str

def test_get_group_news():
    url = "https://api.vk.com/method/wall.get"
    params = {
        "access_token": "YOUR_ACCESS_TOKEN",
        "v": "5.131",
        "owner_id": "-GROUP_ID",
        "count": "10"
    }
    response = requests.post(url, params=params)
    news_data = response.json()["response"]["items"]
    news = [News(**news_data) for news_data in news_data]
    assert len(news) > 0
    for item in news:
        assert item.id > 0
        assert item.text != ""

#Тест на отправку сообщения пользователю 
class Message(BaseModel):
    id: int
    text: str

def test_send_message():
    url = "https://api.vk.com/method/messages.send"
    params = {
        "access_token": "YOUR_TOKEN",
        "v": "5.131",
        "user_id": "USER_ID",
        "message": "Hello, World!"
    }
    response = requests.post(url, params=params)
    message_data = response.json()["response"]
    message = Message(**message_data)
    assert message.id > 0
    assert message.text == "Hello, World!"

#Тест на получение списка сообщений пользователя
class Message(BaseModel):
    id: int
    text: str

def test_get_user_messages():
    url = "https://api.vk.com/method/messages.getHistory"
    params = {
        "access_token": "YOUR_TOKEN",
        "v": "5.131",
        "user_id": "USER_ID",
        "count": "10"
    }
    response = requests.post(url, params=params)
    messages_data = response.json()["response"]["items"]
    messages = [Message(**message_data) for message_data in messages_data]
    assert len(messages) > 0
    for item in messages:
        assert item.id > 0
        assert item.text != ""

#Тест на удаление пользователя
class UserDelete(BaseModel):
    id: int
    deactivated: str

def test_delete_user():
    url = "https://api.vk.com/method/account.delete"
    params = {
        "access_token": "YOUR_TOKEN",
        "v": "5.131"
    }
    response = requests.post(url, params=params)
    user_data = response.json()["response"]
    user_delete = UserDelete(**user_data)
    assert user_delete.id > 0
    assert user_delete.deactivated == "deleted"

  
