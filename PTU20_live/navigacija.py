import os
from datetime import datetime

print(os.getcwd())
os.chdir('PTU20_live')
print(os.getcwd())

if os.path.exists("labas.txt"):
    with open("labas.txt", "r") as labas_f:
        for line in labas_f:
            print(line, end="")
    print()
else:
    print('file is not there')

if not os.path.exists("siuksles"):
    os.makedirs('siuksles')
    with open("siuksles/siuksle", "w") as siuksle:
        siuksle.write("xxx")
else:
    if os.path.exists("siuksles/siuksle"):
        os.remove("siuksles/siuksle")
    os.rmdir('siuksles')

os.chdir('..')
print(os.getcwd())
main_dir_content = os.listdir()
for item in main_dir_content:
    item_st = os.stat(item)
    print(f"{item[:29]:30} {item_st.st_size:>9} "
          f"{datetime.fromtimestamp(item_st.st_ctime)}")

if os.path.exists("README.md"):
    readme_stats = os.stat("README.md")
    print(readme_stats.st_size)
    print(datetime.fromtimestamp(readme_stats.st_ctime))
