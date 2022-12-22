from badgeuse_psql import Badgeuse_psql
from badgeuse_scan import Scan_Raspberry
import time

scan_raspberry = Scan_Raspberry()
badgeuse_psql = Badgeuse_psql()


x = 0
while x < 5:
    data = scan_raspberry.read_card()
    if badgeuse_psql.root(data):
        print("L'admin a arrêté le programme")
        break 
    elif badgeuse_psql.check(data):
        badgeuse_psql.card_c(data)
        badgeuse_psql.commit()
        print("Vous pouvez passer")
    else:
        if badgeuse_psql.waiting():
            badgeuse_psql.add_card(data)
            badgeuse_psql.card_c(data)
            badgeuse_psql.commit()

            print("Carte ajouté, vous pouvez passer")
        else:
            print("Votre carte n'est pas valable")
    x += 1
    time.sleep(2.5)

badgeuse_psql.stop()
print("END")

