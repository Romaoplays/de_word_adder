import csv
import pprint
import os

from pons_translator_module import (
    get_reverse_translation,
    get_translation,
    get_reverse_translation,
)
from der_die_das_module import get_article

# Creates csv file if it doesn't exist
try:
    csv_file = open("de_words.csv", encoding="utf-8-sig")
except FileNotFoundError:
    csv_file = open("de_words.csv", "w", encoding="utf-8-sig")
finally:
    csv_file.close()

# Gets translation from pons_traslator module
def get_word_input():
    print("\nType out word:")
    resposta = input()
    translated_words = get_translation(resposta)
    if len(translated_words[0]) == 1:
        print("\n!!!Translation not found!!!")
        return None
    elif len(translated_words[0]) < 6:
        f = len(translated_words[0]) - 1
    else:
        f = 5

    print("\nPossible translations: ")
    unduper_list = []
    for i in range(f):
        if translated_words[1][i + 1] not in unduper_list:
            if len(translated_words[1][i + 1]) < 50:
                print("- " + translated_words[1][i + 1])
                unduper_list.append(translated_words[1][i + 1])

    current_article = get_article(translated_words[0][1])

    if current_article != "":
        print("\n" + current_article + " " + translated_words[0][1])
        source = get_article(translated_words[0][1]) + " " + translated_words[0][1]
    else:
        print("\n" + translated_words[0][1])
        source = translated_words[0][1]

    target = translated_words[1][1]

    return source, target


def get_reverse_word_input():
    print("\nType out word:")
    resposta = input()
    translated_words = get_reverse_translation(resposta)
    if len(translated_words[0]) == 1:
        print("\n!!!Translation not found!!!")
        return None
    elif len(translated_words[0]) < 6:
        f = len(translated_words[0]) - 1
    else:
        f = 5

    print("\nPossible translations: ")
    unduper_list = []
    for i in range(f):
        if translated_words[1][i + 1] not in unduper_list:
            if len(translated_words[1][i + 1]) < 50:
                print("- " + translated_words[1][i + 1])
                unduper_list.append(translated_words[1][i + 1])

    target = translated_words[1][1]

    return target


while True:
    print(
        "\nWhat do you want to do?\n1 - Add Word (Wild)\n2 - Add Word (Book)\n3 - View Saved Words\n4 - Check Article\n5 - Reverse Translate"
    )
    resposta_inicial = input()

    if resposta_inicial == "1" or resposta_inicial == "2":
        words = get_word_input()
        if words is not None:
            print(
                "\n1 - Add First Translation\n2 - Discard Word\n3 - Add Own Translation"
            )
            resposta_add = input()
            words_list = list(words)

            if resposta_inicial == "2" and resposta_add == "1":
                print("\nBook page?")
                words_list.append("Pag. " + input())
            if resposta_add == "1":
                csv_file = open("de_words.csv", "a", encoding="utf-8-sig")
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(words_list)
                csv_file.close()
            if resposta_add == "3":
                print("\nType Own Translation: (2 - Cancel)")
                resposta_own_translation = input()
                if resposta_own_translation == "2":
                    print("\nCanceled!")
                else:
                    words_list = []
                    words_list.append(list(words)[0])
                    words_list.append(resposta_own_translation)
                    if resposta_inicial == "2":
                        print("\nBook page?")
                        words_list.append("Pag. " + input())
                    csv_file = open("de_words.csv", "a", encoding="utf-8-sig")
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow(words_list)
                    csv_file.close()
                    print("\nDone!")

    elif resposta_inicial == "3":
        csv_file = open("de_words.csv", "r", encoding="utf-8-sig")
        csv_reader = csv.reader(csv_file)
        csv_list = list(csv_reader)

        csv_list_cleaner = []
        for row in csv_list:
            if row != []:
                csv_list_cleaner.append(row)

        csv_list = csv_list_cleaner

        k = 0

        print("Saved words:\n")

        for i in range(len(csv_list)):
            try:
                print(f"W: {csv_list[i][0]}  T: {csv_list[i][1]} || {csv_list[i][2]}")
            except IndexError:
                print(f"W: {csv_list[i][0]}  T: {csv_list[i][1]}")

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
                csv_file = open("de_words.csv", "w", encoding="utf-8-sig")
                csv_file.close()
                break
            elif resposta_viewer == "ok":
                print("")
                for i in range(len(csv_list)):
                    if i <= k:
                        try:
                            print(
                                f"W: {csv_list[i][0]}  T: {csv_list[i][1]} || {csv_list[i][2]} ======= OK"
                            )
                        except IndexError:
                            print(
                                f"W: {csv_list[i][0]}  T: {csv_list[i][1]} ======= OK"
                            )
                    else:
                        try:
                            print(
                                f"W: {csv_list[i][0]}  T: {csv_list[i][1]} || {csv_list[i][2]}"
                            )
                        except IndexError:
                            print(f"W: {csv_list[i][0]}  T: {csv_list[i][1]}")
                k = k + 1

    elif resposta_inicial == "4":
        print("\nType out word:")
        resposta = input()
        translated_words = get_translation(resposta)
        if len(translated_words[0]) == 1:
            print("\nWord not found!!!")
        else:
            current_article = get_article(translated_words[0][1])

            if current_article == "":
                print("\nArticle not found/Non-existant")
            else:
                print("\n" + current_article + " " + resposta.capitalize())

    elif resposta_inicial == "5":
        get_reverse_word_input()

    else:
        print("!!!Please type one of the numbers above!!!")
