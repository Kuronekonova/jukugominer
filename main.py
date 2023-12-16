import os
KANA = """あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽどゅゃょッアイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲンガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポョュャっ"""
NUMBERS = '0123456789'
JPNUMBERS = "０１２３４５６７８９"
ENNALPHACHARS = """~!@#$%^&*()_+:"|<>?;'\,./-""" # NALPHA: non-alphabetic (for example, 'a' is alphabetic, but ; is not.)
JPNALPHACHARS = """～～＠＃＄％＾＆＊（）＿＋｛｝：”｜＜＞？「」；’￥、。・/*-—.…"""
ENNUMS = '0123456789'
JPNUMS = "０１２３４５６７８９"
nonAlphabeticCharacters = ENNALPHACHARS + JPNALPHACHARS + ENNUMS +  JPNUMS
adderVar = ""
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
        jpFileContentsString = ' '.join((' '.join(jpFile.readlines())).splitlines()) # turn text file's text into one line
    for i in range(len(jpFileContentsString)):
        if(jpFileContentsString[i] in nonAlphabeticCharacters or jpFileContentsString[i] in KANA):
            jpFileContentsString = jpFileContentsString.replace(jpFileContentsString[i], ' ')
    
    
    for i in range(len(jpFileContentsString) - 1):
        if(jpFileContentsString[i] != ' '):
            adderVar += jpFileContentsString[i]  
            if(jpFileContentsString[i + 1] == ' '):
                jukugoList.append(adderVar)
                adderVar = ""
    createFile = int(input("""Would you like to save these Jukugo into a text file?
1. Yes
2. No""" + '\n' + 'Your choice: '))
    match createFile:
        case 1:
            while(True):
                jukugoFileName = str(input("Mined Jukugo File Name: "))
                if(jukugoFileName[len(jukugoFileName) - 4:len(jukugoFileName)] == '.txt'):
                    break
                else:
                    print("Please make sure to include the file's extension (.txt for text files, etc.)!")
                    os.system('pause')
                    os.system('cls')                
            with open(jukugoFileName, 'w', encoding='utf8') as jukugoFile:
                for i in range(len(jukugoList)):
                    jukugoFile.write(jukugoList[i] + '\n')
            print("Successfully created {}.".format(jukugoFileName))
            os.system('pause')
            os.system('cls')
        case 2:
            exit()



