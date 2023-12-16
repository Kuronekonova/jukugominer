import os, time
os.system('mode 80, 10')
KANA = """あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽどゅゃょッアイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲンガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポョュャっ"""
NUMBERS = '0123456789'
JPNUMBERS = "０１２３４５６７８９"
ENNALPHACHARS = """~!@#$%^&*()_+:"|<>?;'\,./-""" # NALPHA: non-alphabetic (for example, 'a' is alphabetic, but ; is not.)
JPNALPHACHARS = """～～＠＃＄％＾＆＊（）＿＋｛｝：”｜＜＞？「」；’￥、。・/*-—.…"""
ENNUMS = '0123456789'
JPNUMS = "０１２３４５６７８９"
nonAlphabeticCharacters = ENNALPHACHARS + JPNALPHACHARS + ENNUMS +  JPNUMS
jukugoList = []

while(True):
    while(True):
        jpFileName = str(input("JP Text File: "))
        if(jpFileName[len(jpFileName) - 4:len(jpFileName)] == '.txt'):
            break
        elif(jpFileName == "EXIT"):
            print("Closing...")
            exit()
        else:
            print("Please make sure to include the file's extension (.txt for text files, etc.)!")
            os.system('pause')
            os.system('cls')
    with open(jpFileName, 'r', encoding='utf8') as jpFile:
        jpFileContentsString = ' '.join((' '.join(jpFile.readlines())).splitlines()) # turn file's text into one line
    for i in range(len(jpFileContentsString)):
        if(jpFileContentsString[i] in nonAlphabeticCharacters or jpFileContentsString[i] in KANA):
            jpFileContentsString = jpFileContentsString.replace(jpFileContentsString[i], ' ')    
    jukugoList = [jukugo for jukugo in (jpFileContentsString.replace(' ', '\n')).splitlines() if jukugo != '']
    while(True):
        jukugoFileName = str(input("Mined Jukugo File Name: "))
        if(jukugoFileName[len(jukugoFileName) - 4:len(jukugoFileName)] == '.txt'):
            break
        else:
            print("Please make sure to include the file's extension (.txt for text files, etc.)!")
            os.system('pause')
            os.system('cls')    
    print(f'Creating {jukugoFileName} file...')
    time.sleep(2)
    with open(jukugoFileName, 'w', encoding='utf8') as jukugoFile:
        for i in range(len(jukugoList)):
            jukugoFile.write(jukugoList[i] + '\n')
    print(f"Successfully created {jukugoFileName}.")
    os.system('pause')
    os.system('cls')
