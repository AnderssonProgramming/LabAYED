def get_lines():

    print("Numero de casos")
    cases = int(input("Digite el número de casos: "))

    cases_list = []
    for i in range(cases):

        print("CASO", i+1)
        print("Líneas")
        lines_number = int(input("Escriba el número de lineas: "))
        lines_list = []
        for j in range(lines_number):
            line = input("Escriba la linea: ")
            lines_list.append(line.split())

        cases_list.append(lines_list)
    # print(cases)
    return cases_list

def show_decoded_messaged_by_cases(list_cases):
    index = 1
    for case in list_cases:
        decodded_message = word_list(case)
        print("Case #", index)
        for message in decodded_message:
            print("".join(message))
        print("")
        index += 1

def word_list(lines):
    decoded_message_list = []
    for line in lines:
        decoded_word = []
        # index nos dirá que letra extraer y nos dara la posición de la misma en el string
        index = 0
        #if len(line) >= index:
        for word in line:
            if len(word) > index:
                decoded_word.append(word[index])
                index += 1
        decoded_message_list.append(decoded_word)

    #print(decoded_message_list)
    return decoded_message_list

# def show_decodded_message(decodded_message_list):
def main():
    lines_cases = get_lines()
    show_decoded_messaged_by_cases(lines_cases)
main()