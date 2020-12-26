import csv
import pprint
import os

from pons_translator_module import get_translation

# Creates csv file if it doesn't exist
try:
    csv_file = open("de_words.csv")
except FileNotFoundError:
    csv_file = open("de_words.csv", "w")
finally:
    csv_file.close()

# Gets translation from pons_traslator module
def get_word_input():
    print("\nType out word:")
    resposta = input()
    translated_words = get_translation(resposta)
    print("\nPossible translations: ")
    unduper_list = []
    for i in range(5):
        if translated_words[1][i + 1] not in unduper_list:
            print("- " + translated_words[1][i + 1])
            unduper_list.append(translated_words[1][i + 1])

    source = translated_words[0][1]
    target = translated_words[1][1]

    return source, target


while True:
    print(
        "\nWhat do you want to do?\n1 - Add word (Wild)\n2 - Add word (Book)\n3 - View Saved words"
    )
    resposta_inicial = input()

    if resposta_inicial == "1" or resposta_inicial == "2":
        words = get_word_input()
        print("\n1 - Add \n2 - Discard")
        resposta_add = input()
        words_list = list(words)

        if resposta_inicial == "2" and resposta_add == "1":
            print("\nBook page?")
            words_list.append("Pag. " + input())

        if resposta_add == "1":
            csv_file = open("de_words.csv", "a")
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(words_list)
            csv_file.close()

    elif resposta_inicial == "3":
        csv_file = open("de_words.csv", "r")
        csv_reader = csv.reader(csv_file)
        csv_list = list(csv_reader)

        csv_list_cleaner = []
        for row in csv_list:
            if row != []:
                csv_list_cleaner.append(row)

        csv_list = csv_list_cleaner

        k = 0

        for row in csv_list:
            print(row)

        print(f"Total: {len(csv_list)} words")

        while True:
            print("\n'exit','ok','del' ")
            resposta_viewer = input()
            if resposta_viewer == "exit":
                csv_file.close()
                break
            elif resposta_viewer == "del":
                csv_file.close()
                os.remove("de_words.csv")
                print("\nThe file has been cleared!")
                csv_file = open("de_words.csv", "w")
                csv_file.close()
                break
            elif resposta_viewer == "ok":
                for i in range(len(csv_list)):
                    if i <= k:
                        print(str(csv_list[i]) + " OK")
                    else:
                        print(csv_list[i])
                k = k + 1
