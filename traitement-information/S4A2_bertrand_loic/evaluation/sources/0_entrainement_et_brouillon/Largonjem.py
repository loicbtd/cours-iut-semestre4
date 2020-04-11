def is_jargonizable(word):
    if (word[0] != 'a'
            and word[0] != 'e'
            and word[0] != 'i'
            and word[0] != 'o'
            and word[0] != 'u'
            and word[0] != 'y'):
        return True
    return False


def jargonize(message):
    jargonized_message = ""
    for word in message.split():
        word = word.lower()
        if is_jargonizable(word):
            word = 'l'+word[1:]+word[0]+"em"
        jargonized_message += word + " "
    return jargonized_message


def main():
    message = "Jargon jargon jargon jargon"
    print(jargonize(message))


main()
