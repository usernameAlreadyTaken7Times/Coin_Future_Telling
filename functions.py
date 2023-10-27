from bs4 import BeautifulSoup
import requests


def get_link(num):
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

    return text


def to_txt(path, text):
    """This function aims to write the text into a txt file.
    :param str path: The path of the txt file,
    :param str text: the to-be-witten text.
    """

    with open(path, "w") as f:
        print(text, file=f)
    f.close()


def set_hex(num_1, num_2, num_3, num_4, num_5, num_6):
    """Use the numbers of heads when three coins are flipped for six times as input,
     and return the corresponding hexagram and the Change Yao."""

    # here the numbers are already tested andb they should be valid
    Yao = 0



rsp = get_webpage("https://www.zhouyi.cc/zhouyi/yijing64/4103.html")
txt = webpage_parsing_part(rsp.text, 3)
to_txt(r"C:\Users\86781\OneDrive\桌面\0.txt", txt)
pass
