from lib.panda import Panda
panda = Panda(serial="WIFI", claim=False)
while True:
    print (panda.can_recv())

