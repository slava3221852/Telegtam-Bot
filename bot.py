import telebot
import config
import time
import vk

array = [None]
bot = telebot.TeleBot(config.token)

def posting():
    try:
        vk_api = vk.API(vk.AuthSession(app_id = 6087806 , user_login = '380921312218', user_password = '3221852q'))
        while True:
            post = vk_api.wall.get(owner_id=-45745333, count=1, offset=1)[1]
            if post['marked_as_ads'] == 0 and post['attachment']['type'] == 'photo' and post['id'] != array[0]:
                array[0] = post['id']
                bot.send_photo('@Ukrainians_4ch', vk_api.wall.get(owner_id=-45745333, count=1, offset=1)[1]['attachment']['photo']['src_big'])
                time.sleep(2)
    except Exception as e:
        posting()
        
posting()
