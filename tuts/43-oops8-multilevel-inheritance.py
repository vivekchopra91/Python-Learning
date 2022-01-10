class Hera_pheri:
    daroo = 10

class Hera_pheri_2(Hera_pheri):
    shortcut_scheme = 5
    daroo = 5
    def rich(self):
        return f"Yes there is a scheme to multiply your money : {self.shortcut_scheme} number of times."

class Phir_hera_pheri(Hera_pheri_2):
    shortcut_scheme = 10
    girl = "anuradha"
    def rich(self):
        return f"Yes, with this scheme, you can multiply your money : {self.shortcut_scheme} number of times a week."

babu_rao = Hera_pheri()
raju = Hera_pheri_2()
shyam = Phir_hera_pheri()

print(raju.rich())
print(shyam.daroo)
print(raju.daroo)
print(babu_rao.daroo)
# print(babu_rao.girl)            # will be error, since multilevel follows chronological order. 