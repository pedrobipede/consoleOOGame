import Character as chh
import Action as ac

ch1 = chh.Character('airez', 'bruiser', 100, 5, 5, 10, 15, 200)
ch2 = chh.Character('pedro', 'mage', 200, 4, 4, 8, 15, 200)

print("VENCEDOR!!!!! {}".format(ac.duel(ch1, ch2).toString()))
