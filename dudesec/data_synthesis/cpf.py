from random import choice


def generateCpf():
    

    list_cpf = [random.randint(0,9) for i in range(9)]
    sum_digit_one = 0
    sum_digit_two = 0
    count_one = len(list_cpf) + 1
    count_two = len(list_cpf) + 2
    
    for i in range(count_two):
        if count_one >= 2:
            sum_digit_one += list_cpf[i] * count_one
        if count_one == 2:
            if sum_digit_one % 11 > 2:
                list_cpf.append(abs((sum_digit_one * 10) % 11))
            else:
                list_cpf.append(0)

        if count_two >= 2:
            sum_digit_two += list_cpf[i] * count_two
        if count_two == 2:
            if sum_digit_two % 11 > 2:
                list_cpf.append(abs((sum_digit_two * 10) % 11))
            else:
                list_cpf.append(0)

        count_one -= 1
        count_two -= 1
    
    string_cpf = ''.join(str(elem) for elem in list_cpf)
    
    return f"{string_cpf[:3]}.{string_cpf[3:6]}.{string_cpf[6:9]}-{string_cpf[9:]}"
