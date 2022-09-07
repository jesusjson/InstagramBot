from time import time
import random
import time
from instabot import Bot 
import settings


Jusername = settings.userinfo["username"]
Jpassword = settings.userinfo["password"]


bot = Bot(
    comment_delay = 10,
    max_comments_per_day = 200
)

bot.login(
    username = Jusername,
    password = Jpassword,
    use_cookie=False
)


def getUserMediaId(commendUserAccounts):
    list = []
    
    for x in commendUserAccounts:
        userId = bot.get_user_id_from_username(x)
        mediaId = bot.get_last_user_medias(userId, 2)
        result = mediaId[0]
        list.append(result)
    
    return list

def randomComments(comment):
    comments = random.choice(comment)
    return comments
    

def getComments(userMediaid,commendText):
    
    for x in userMediaid:
        bot.comment(x,commendText)
        print("[SYSTEM] Yorum gönderimi başarılı.")
        time.sleep(3)
    