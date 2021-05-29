#encoding utf-8
num_note = input("Entrez le nombre de note à saisir:")
num_note = float(num_note)
fin_boucle = "moyenne"
Yt=0
i=1
while i<=num_note:
    Yi=input("Veuillez entrez votre note:")
    Yi=float(Yi)
    Yt=Yt+Yi
    i=i+1
moyenne = Yt/num_note
text = "Tu as {} de moyenne."
print(text.format(moyenne))