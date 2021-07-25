import uart
import numpy as np
import random


def get_exp(iteration=10):
    count = [0, 0, 0, 0, 0]  # anger, happy, normal, sad, null
    for z in range(iteration):
        print(z)
        raw_exp = uart.read_uart()
        if np.array_equal(raw_exp, np.array([0, 0, 0, 0])):
            count[4] += 1
        elif np.argmax(raw_exp) == 0:
            count[0] += 1
        elif np.argmax(raw_exp) == 1:
            count[1] += 1
        elif np.argmax(raw_exp) == 2:
            count[2] += 1
        elif np.argmax(raw_exp) == 3:
            count[3] += 1
    if np.argmax(count) == 0:
        current_exp = 'You look angry 👿'
    elif np.argmax(count) == 1:
        current_exp = 'You look happy 😍'
    elif np.argmax(count) == 2:
        current_exp = 'You look normal 😐'
    elif np.argmax(count) == 3:
        current_exp = 'You look sad 😢'
    elif np.argmax(count) == 4:
        current_exp = 'No expression detected'
    print('Exp stat: ', count)
    return current_exp


def find_exp(text, user_id):
    return get_exp()


def recommond_music(text, user_id):  # text => 接收到的訊息字串;   user_id => User的Line ID
    current_exp = get_exp()
    if current_exp == 'You look angry 👿':
        link = 'https://www.youtube.com/watch?v=bP9gMpl1gyQ&ab_channel=TheSoulofWind'
    elif current_exp == 'You look happy 😍':
        link = 'https://www.youtube.com/watch?v=xoastiYx9JU&ab_channel=Hung-yiLee'
    elif current_exp == 'You look normal 😐':
        link = 'https://www.youtube.com/watch?v=USoC8AqirVA&ab_channel=%E7%BE%8E%E9%A3%9F%E4%BD%9C%E5%AE%B6%E7%8E%8B%E5%88%9A'
    elif current_exp == 'You look sad 😢':
        link = 'https://www.youtube.com/watch?v=AuBxCuik5Pg&ab_channel=UnusualVideos'
    else:
        link = 'https://www.youtube.com/watch?v=_R1PBhaZrZo&ab_channel=ClassicMrBean'
    return link


def recommond_meme(text, user_id):
    links = ['https://i.imgur.com/pEaWv9x.jpg?2',
             'https://i.imgur.com/bXqHpvM.jpg',
             'https://i.imgur.com/qlGTsoy.jpg',
             'https://i.imgur.com/GoeWqwA.jpg',
             'https://i.imgur.com/haEgnmg.jpg',
             'https://i.imgur.com/VNUFxbE.jpg',
             'https://i.imgur.com/ZydjYfT.jpg',
             'https://i.imgur.com/WMYiPkH.jpg',
             'https://i.imgur.com/gU6KQh2.jpg',
             'https://i.imgur.com/GIPwmGw.jpg',
             'https://i.imgur.com/8aibSQr.png',
             'https://i.imgur.com/2nILxHw.jpg',
             'https://i.imgur.com/ANq1FPm.jpg',
             'https://i.imgur.com/ngoWuIq.jpg',
             'https://i.imgur.com/032CeQf.jpg',
             'https://i.imgur.com/rgbmTDJ.jpg',
             'https://i.imgur.com/nsa0Cr0.jpg',
             'https://i.imgur.com/t4ErW9o.jpg',
             'https://i.imgur.com/6brudMi.jpg',
             'https://i.imgur.com/pmKDJm9.jpg'
             ]
    seed = random.randint(0, len(links) - 1)
    return links[seed]
