from itertools import permutations
import os


def generateWorldList(word_size, profile, path):

    if isinstance(profile, dict):
        birthdate_yy = profile["birthdate"][-2:]
        birthdate_yyy = profile["birthdate"][-3:]
        birthdate_yyyy = profile["birthdate"][-4:]
        birthdate_xd = profile["birthdate"][1:2]
        birthdate_xm = profile["birthdate"][3:4]
        birthdate_dd = profile["birthdate"][:2]
        birthdate_mm = profile["birthdate"][2:4]
        bd_list = [birthdate_yy,birthdate_yyy,
        birthdate_yyyy,birthdate_xd,birthdate_xm,
        birthdate_dd,birthdate_mm,]

        name_lastname_list = [profile["name"], profile["lastname"], profile["nickname"]]
        for name  in name_lastname_list:
            if name.capitalize() not in name_lastname_list: name_lastname_list.append(name.capitalize())
            if name.upper() not in name_lastname_list: name_lastname_list.append(name.upper())
            if name.lower() not in name_lastname_list: name_lastname_list.append(name.lower())
        output_list = bd_list + name_lastname_list
        combination_list = []

        for i in range(word_size):
            combination_list += permutations(output_list, i+1)

        if not os.path.exists(path):
            output_file = open(path, 'w')
            for word in combination_list:
                output_file.write('{}\n'.format(''.join(word)))