import vk
import csv
from multiprocessing import Pool
from threading import Thread

'''def add_to_dict(sex, bdate, city):
    users_data = {}
    try:
        users_data.update()'''

def get_members(groupid):  # Функция формирования базы участников сообщества в виде списка
    first = vk_api.groups.getMembers(group_id=groupid, v=5.92)  # Первое выполнение метода
    data = first['items']  # Присваиваем переменной первую тысячу id'шников
    count = first['count'] // 1000  # Присваиваем переменной количество тысяч участников
    # С каждым проходом цикла смещение offset увеличивается на тысячу
    # и еще тысяча id'шников добавляется к нашему списку.
    for i in range(1, count + 1):
        data = data + vk_api.groups.getMembers(group_id=groupid, v=5.92, offset=i*1000)['items']
    return data


def get_members_information(data):
    members_information = []
    for i in data:
        information = vk_api.users.get(user_ids=i, fields=['sex', 'has_photo'], v=5.92)
        user_data = {
            'sex': information[0]['sex'],
            'has_photo': information[0]['has_photo']
        }
        members_information.append(user_data)
        print(data.index(i))
    return members_information


def write_csv(members_information):
    with open('users_information.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(('sex', 'has_photo'))
        for i in range(len(members_information)):
            writer.writerow((members_information[i]['sex'],
                             members_information[i]['has_photo']))


if __name__ == '__main__':
    token = '1ecc15cc1ecc15cc1ecc15cc7d1ea38f3d11ecc1ecc15cc408c01add21016158250322a'
    session = vk.Session(access_token=token)
    vk_api = vk.API(session)
    members = get_members('zapiskisedogotestera')
    write_csv(get_members_information(members))