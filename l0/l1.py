import pandas as pd
music = [["Thousand Foot Krutch", "We are"],
         ["Panic! At The Disco", "One of Dr*nks"],
         ["Ava", "Famy"],
         ["Double Life", "SKYFLAME"],
         ["Like a Player", "Madonna"]]

entries = ["track","artist"]

playlist = pd.DataFrame(data=music, columns=entries)
print(playlist)