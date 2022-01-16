dict1 = {"<addressee>": "друг", "<how>": "Срочно",  "<offer>": "получили уникальную возможность выиграть",
         "<what>": "уникальный денежный приз", "<amount>": "$120,000",
         "<further action>": "подтверждения получения приза", "<urgency>": "незамедлительно",
         "<sendwhat>": "взнос участника лотереи", "<howmuch>": "$30",  "<complementary>": "С наилучшими пожеланиями,",
         "<sender>": "Президент международного фонда честных лотерей"
         }
dict2 = {"<addressee>": "John", "<how>": "С радостью",  "<offer>": "удостоены чести претендовать на",
         "<what>": "долю наследства шейха Ваканды", "<amount>": "$97,000",
         "<further action>": "инициации процесса подачи документов", "<urgency>": "в кратчайший срок",
         "<sendwhat>": "регистрационную пошлину", "<howmuch>": "$100",  "<complementary>": "С нетерпением жду ответа,",
         "<sender>": "Верховный нотариус Ваканды"
         }
template = "\n\n\n\tДорогой <addressee>!\n\n\t<how> спешу сообщить вам, что вы <offer> <what> в размере <amount>." \
            "\n Для <further action>, пожалуйста, <urgency> отправьте <sendwhat> <howmuch>\n на счет " \
            "555-xxxxxxxxxxxxxxxx в Нигерийском коммерческом банке. \n\n <complementary> \n <sender>"


def interpolate(stri, **kwargs):
    for item in kwargs:
        stri = stri.replace(item, kwargs[item])
    print(stri)
    return None


if __name__ == "__main__":
    interpolate(template, **dict1)
    interpolate(template, **dict2)
