# ['2872903512970063631_8657972632', '2625143484099432565_8657972632']
# ['2922189592421606754_8657972632', '2872903512970063631_8657972632', '2625143484099432565_8657972632']
import settings
import jesu


########################### PROPORTİES ########################################
userAccounts = settings.comments["commentUserAccounts"]
comment = settings.comments["sendComments"]
commentFile = jesu.randomComments(comment)
userMedıaId = jesu.getUserMediaId(userAccounts)
########################### PROPORTİES ########################################


print("""  
############# KWRGN BOT İŞLEM #############
          1 - Yorum reklam sistem 
      
          0 - Sistem Kapat
          [?] Lütfen sistemi [0] ile kapatınız aksi taktirde doğacak hatalardan hizmetimiz sorumlu değildir!
      """)
########################### FUNCTİONS ########################################
while True:
    sec = int(input("[?] "))
    if sec == 1:
        jesu.getComments(userMedıaId,commentFile)
    elif sec == 0:
        exit()
########################### FUNCTİONS ########################################

