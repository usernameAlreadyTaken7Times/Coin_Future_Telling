from bs4 import BeautifulSoup
import requests


def get_hex_link(num):
    """return the weblink for the given number's hexagram"""
    if isinstance(num, int) and 1 <= num <= 64:
        pass
    else:
        print('Check your input. The input should be a number and between 1-64.')

    # the hex_weblink
    hex_num = [4103, 4105, 4106, 4107, 4108, 4109,
               4110, 4111, 4112, 4113, 4126, 4127,
               4140, 4141, 4142, 4143, 4144, 4145,
               4146, 4147, 4148, 4149, 4150, 4152,
               4153, 4159, 4164, 4167, 4168, 4169,
               4170, 4171, 4172, 4173, 4174, 4175,
               4176, 4177, 4179, 4180, 4181, 4182,
               4183, 4184, 4185, 4186, 4187, 4188,
               4189, 4190, 4192, 4193, 4194, 4195,
               4196, 4197, 4198, 4200, 4212, 4244,
               4255, 4256, 4257, 4263]
    url = "https://www.zhouyi.cc/zhouyi/yijing64/" + str(hex_num[num - 1]) + ".html"

    return url


def get_webpage(link):
    """This function aims to retrieve the website contents for further parsing.
    :param str link: The website's url link.
    """
    # test if link valid
    if isinstance(link, str):
        pass
    else:
        print('Please check your input link, format error.')
        raise AttributeError

    # retrieve the website content
    response = requests.get(link)

    # set the format of the website sourcecode as 'utf-8' to avoid undesired charset questions
    response.encoding = 'utf-8'

    return response


def webpage_parsing_all(text_input):
    """This function aims to parse the website's future-telling trigram content as .html format,
    and then get the text chapters with all information of this hexagram.
    :param str text_input: The web-link you want to parse.
    """

    soup = BeautifulSoup(text_input, 'html.parser')

    # divide all div chapters to search text
    part = soup.select('div')
    part_name_list = []  # store chapter name
    part_content_list = []  # store chapter contents

    for part_num in range(len(part)):

        # find title for chapters
        if part[part_num].attrs.get('class') == ['guatt', 'cf', 'f14', 'fb', 'tleft']:
            part_name_list.append(part[part_num])
        # find content for chapters
        if part[part_num].attrs.get('class') == ['gualist', 'tleft', 'f14', 'lh25']:
            part_content_list.append(part[part_num])

    # prepare the chapter names for storing
    chp_name = []
    for chp_num in range(0, 7):
        chp_name.append(part_name_list[chp_num].text)

    # prepare the chapter contents for storing
    chp_content = []
    for chp_num in range(0, 7):
        # set an empty list to store the texts for one specific chapter
        chp_text = part_content_list[chp_num].text.split('\r\n')

        # deal with the sentence splitting inside a chapter
        chp_text_bkp = []
        for stc_num in range(len(chp_text)):

            # delete the undesired space in the first record
            if stc_num == 0:
                if ' ' in chp_text[stc_num]:
                    chp_text[stc_num] = chp_text[stc_num].replace(' ', '')

            # split the text into paragraphs
            if '\n' in chp_text[stc_num] and '\n\n' not in chp_text[stc_num]:
                list_temp = chp_text[stc_num].split('\n')  # here just assume only one '\n' will be in the record
                chp_text_bkp.append(list_temp[0])
                chp_text_bkp.append('-------------------------------------')
                chp_text_bkp.append(list_temp[1])
            elif '\n\n' in chp_text[stc_num]:
                list_temp = chp_text[stc_num].split('\n')  # here just assume only one '\n\n' will be in the record
                chp_text_bkp.append(list_temp[0])
                chp_text_bkp.append('-------------------------------------')
                chp_text_bkp.append(list_temp[2])
            else:
                chp_text_bkp.append(chp_text[stc_num])

        chp_content.append(chp_text_bkp)

    # reformat the article in the way chapter_name & chapter_content
    text = ''
    for chp_num in range(0, 7):
        text = (text + '\n**************************************\n' + str(chp_name[chp_num])
                + '\n***************************************\n')
        text = text + ''.join((chp_content[chp_num][i] + '\n') for i in range(len(chp_content[chp_num])))

    return text


def webpage_parsing_part(text_input, chp_num_text):
    """This function aims to parse the website's future-telling trigram content as .html format,
    and then get only the text chapters of the related hexagram.
    :param str text_input: The web-link you want to parse,
    :param int chp_num_text: the chapter number of the chosen paragraph, should be in range (0,7)
    """

    if isinstance(chp_num_text, int) and 0 <= chp_num_text <= 6:
        pass
    else:
        print('Please check your input chapter number.')

    soup = BeautifulSoup(text_input, 'html.parser')

    # divide all div chapters to search text
    part = soup.select('div')
    part_name_list = []  # store chapter name
    part_content_list = []  # store chapter contents

    for part_num in range(len(part)):

        # find title for chapters
        if part[part_num].attrs.get('class') == ['guatt', 'cf', 'f14', 'fb', 'tleft']:
            part_name_list.append(part[part_num])
        # find content for chapters
        if part[part_num].attrs.get('class') == ['gualist', 'tleft', 'f14', 'lh25']:
            part_content_list.append(part[part_num])

    # prepare the chapter names for storing
    chp_name = []
    for chp_num in range(0, 7):
        chp_name.append(part_name_list[chp_num].text)

    # prepare the chapter contents for storing
    chp_content = []
    for chp_num in range(0, 7):
        # set an empty list to store the texts for one specific chapter
        chp_text = part_content_list[chp_num].text.split('\r\n')

        # deal with the sentence splitting inside a chapter
        chp_text_bkp = []
        for stc_num in range(len(chp_text)):

            # delete the undesired space in the first record
            if stc_num == 0:
                if ' ' in chp_text[stc_num]:
                    chp_text[stc_num] = chp_text[stc_num].replace(' ', '')

            # split the text into paragraphs
            if '\n' in chp_text[stc_num] and '\n\n' not in chp_text[stc_num]:
                list_temp = chp_text[stc_num].split('\n')  # here just assume only one '\n' will be in the record
                chp_text_bkp.append(list_temp[0])
                chp_text_bkp.append('-------------------------------------')
                chp_text_bkp.append(list_temp[1])
            elif '\n\n' in chp_text[stc_num]:
                list_temp = chp_text[stc_num].split('\n')  # here just assume only one '\n\n' will be in the record
                chp_text_bkp.append(list_temp[0])
                chp_text_bkp.append('-------------------------------------')
                chp_text_bkp.append(list_temp[2])
            else:
                chp_text_bkp.append(chp_text[stc_num])

        chp_content.append(chp_text_bkp)

    # reformat the article in the way chapter_name & chapter_content
    text = ''

    text = (text + '\n**************************************\n' + str(chp_name[chp_num_text])
            + '\n***************************************\n')
    text = text + ''.join((chp_content[chp_num_text][i] + '\n') for i in range(len(chp_content[chp_num_text])))

    str_begin = str(chp_name[chp_num_text]).find('第')
    str_end = str(chp_name[chp_num_text]).find('爻')
    if str_end == -1:
        str_end = str(chp_name[chp_num_text]).find('卦')

    return text, str(chp_name[chp_num_text])[str_begin: str_end+1]


def to_txt(path, name, text):
    """This function aims to write the text into a txt file.
    :param str path: The path of the txt file,
    :param str name: the name of the txt file,
    :param str text: the to-be-witten text.
    """

    # os.getcwd()

    with open(path + name, "w") as f:
        print(text, file=f)
    f.close()


def get_hex_num_yao(hex_yao_list):
    """Use the input hexagram's six Yaos order and return the corresponding hexagram.
    :param list hex_yao_list: The order of the Yaos for this hexagram, in the form of [0, 1, 0, 1, 1, 1],
    :return: the number of this hexagram.
    """

    # calculate the binary number for this hexagram
    binary_num_hex = int(''.join(str(hex_yao_list[i]) for i in range(len(hex_yao_list))), 2)

    # dic to convert the binary list to hexagram
    hex_order_list = [2, 23, 8, 20, 16, 35, 45, 12,
                      15, 52, 39, 53, 62, 56, 31, 33,
                      7, 4, 29, 59, 40, 64, 47, 6,
                      46, 18, 48, 57, 32, 50, 28, 44,
                      24, 27, 3, 42, 51, 21, 17, 25,
                      36, 22, 63, 37, 55, 30, 49, 13,
                      19, 41, 60, 61, 54, 38, 58, 10,
                      11, 26, 5, 9, 34, 14, 43, 1]

    return hex_order_list[binary_num_hex]


def set_hex(num_list):
    """Use the numbers of heads when three coins are flipped for six times as input,
     and return the corresponding hexagram and the Change Yao.
     :param list num_list: The list for heads of the six flips for the three coins;
     """

    def set_yao(num):
        """Use the number of heads when three coins are flipped for one time as input,
         and get the Yin/Yang result and weather there is a change Yao involved.
        :param int num: The heads of one flip with three coins;
        :return: the Yin/Yang result and weather it is a changed Yao;
        """

        yao = -1  # default yao=-1
        yao_changed = False  # weather a change Yao is involved

        # here, assume the inputted number is valid
        if num == 0:
            yao = 1
            yao_changed = True
        elif num == 1:
            yao = 0
            yao_changed = False
        elif num == 2:
            yao = 1
            yao_changed = False
        elif num == 3:
            yao = 0
            yao_changed = True

        return yao, yao_changed

    # here the numbers are already tested and they should be valid
    change_yao_num = 0  # default number of the change Yao
    change_yao_index = [0, 0, 0, 0, 0, 0]
    hexagram = [-1, -1, -1, -1, -1, -1]  # default hexagram

    # loop to get result
    for i in range(len(num_list)):
        rlt = set_yao(num_list[i])
        hexagram[i] = rlt[0]
        if rlt[1]:
            change_yao_index[i] = 1
            change_yao_num += 1

    return hexagram, change_yao_num, change_yao_index


def get_changed_hex(hex_yao_list, change_yao_index):
    """Use the original hexagram and the change Yaos to get the changed hexagram.
    """
    changed_hex = hex_yao_list.copy()

    for i in range(0, 6):
        if change_yao_index[i] == 1:
            if hex_yao_list[i] == 0:
                changed_hex[i] = 1
            else:
                changed_hex[i] = 0

    return changed_hex


def instruction_format_1(text_1, title_1):
    """This function aims to improve the typesetting for the output result when there is one part of text involved.
    """
    text_part_0 = ('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$\t\t\t\t卦象详解\t\t\t\t '
                   '$\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')
    text_part_1 = '--------------------------------------\n'
    text_part_2 = '卦象需要用爻辞\n- 【' + title_1 + '】解释。爻辞如下：\n'
    text_part_3 = text_1
    text_part_4 = '\n--------------------------------------'

    text = text_part_0 + text_part_1 + text_part_2 + text_part_3 + text_part_4

    return text


def instruction_format_2(text_1, text_2, title_1, title_2):
    """This function aims to improve the typesetting for the output result when there are two parts of texts involved.
    First the important one, then the not important one.
    """
    text_part_0 = ('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$\t\t\t\t卦象详解\t\t\t\t '
                   '$\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')
    text_part_1 = '--------------------------------------\n'
    text_part_2 = '卦象需要用两个爻辞共同解释，但具有主次之分。应以其中\n- 【' + title_1 + '】为主，以\n- 【' + title_2 + '】为辅。两种爻辞分列如下：\n'
    text_part_3 = text_1
    text_part_4 = '\n--------------------------------------'
    text_part_5 = text_2
    text_part_6 = '\n--------------------------------------'

    text = text_part_0 + text_part_1 + text_part_2 + text_part_3 + text_part_4 + text_part_5 + text_part_6

    return text


def get_instructions(hex_yao_list, change_yao_num, change_yao_index):
    """Return the corresponding explanation to the hexagram.

    """

    print_text = ''

    if change_yao_num == 0:
        # no change_yao, use default hexagram explanation

        hex_num = get_hex_num_yao(hex_yao_list)
        link = get_hex_link(hex_num)

        result = webpage_parsing_part(get_webpage(link).text, 0)
        print_text = instruction_format_1(result[0], result[1])

    elif change_yao_num == 1:
        # one changed Yao, use this changed Yao's explanation

        # determine which Yao is changed
        changed_yao = change_yao_index.index(1) + 1

        hex_num = get_hex_num_yao(hex_yao_list)
        link = get_hex_link(hex_num)

        result = webpage_parsing_part(get_webpage(link).text, changed_yao)
        print_text = instruction_format_1(result[0], result[1])

    elif change_yao_num == 2:
        # two changed Yaos, use both explanations to explain, but based more on the upper one

        # determine which two Yaos are changed
        changed_yao_order = [i for i, x in enumerate(change_yao_index) if x == 1]

        hex_num = get_hex_num_yao(hex_yao_list)
        link = get_hex_link(hex_num)

        result_1 = webpage_parsing_part(get_webpage(link).text, changed_yao_order[0] + 1)
        result_2 = webpage_parsing_part(get_webpage(link).text, changed_yao_order[1] + 1)  # as main
        print_text = instruction_format_2(result_2[0], result_1[0], result_2[1], result_1[1])

    elif change_yao_num == 3:
        # three changed Yaos, use the original hexagram's explanation as the main part,
        # and the changed hexagram's explanation as the supplement

        # get the changed hexagram
        changed_hex_list = get_changed_hex(hex_yao_list, change_yao_index)

        hex_num_1 = get_hex_num_yao(hex_yao_list)
        link_1 = get_hex_link(hex_num_1)

        hex_num_2 = get_hex_num_yao(changed_hex_list)
        link_2 = get_hex_link(hex_num_2)

        result_1 = webpage_parsing_part(get_webpage(link_1).text, 0)  # as main
        result_2 = webpage_parsing_part(get_webpage(link_2).text, 0)
        print_text = instruction_format_2(result_1[0], result_2[0], result_1[1], result_2[1])

    elif change_yao_num == 4:
        # four changed Yaos, use the two unchanged Yao's explanations to explain, but base more on the below one

        # determine which two Yaos are unchanged
        unchanged_yao_order = [i for i, x in enumerate(change_yao_index) if x == 0]

        hex_num = get_hex_num_yao(hex_yao_list)
        link = get_hex_link(hex_num)

        result_1 = webpage_parsing_part(get_webpage(link).text, unchanged_yao_order[0] + 1)  # as main
        result_2 = webpage_parsing_part(get_webpage(link).text, unchanged_yao_order[1] + 1)
        print_text = instruction_format_2(result_1[0], result_2[0], result_1[1], result_2[1])

    elif change_yao_num == 5:
        # five changed Yaos, use the changed hexagram's unchanged Yao's explanation

        # determine which Yao is unchanged
        unchanged_yao = change_yao_index.index(0) + 1

        # get the changed hexagram
        changed_hex_list = get_changed_hex(hex_yao_list, change_yao_index)

        hex_num = get_hex_num_yao(changed_hex_list)
        link = get_hex_link(hex_num)

        result = webpage_parsing_part(get_webpage(link).text, unchanged_yao)
        print_text = instruction_format_1(result[0], result[1])

    elif change_yao_num == 6:
        # six Yaos are all changed, use the changed hexagram's explanation

        # get the changed hexagram
        changed_hex_list = get_changed_hex(hex_yao_list, change_yao_index)

        hex_num = get_hex_num_yao(changed_hex_list)
        link = get_hex_link(hex_num)

        result = webpage_parsing_part(get_webpage(link).text, 0)
        print_text = instruction_format_1(result[0], result[1])

    return print_text
