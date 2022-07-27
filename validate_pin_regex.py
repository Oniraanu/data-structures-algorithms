import re


def validate_pin(pin):
    # return true or false
    my_pin = range(1, len(pin))
    length_pin = len(pin)
    a = re.findall(r'[a-zA-Z]+', pin)
    # if length_pin == 6 or length_pin == 4:
    #
    # else:
    #     for i in my_pin:
    #         if i == a:
    #             return False
    # return True
    for i in my_pin:
        if length_pin == 6 or length_pin == 4:
            if i in a:
                return False
            else:
                return True
        return


print(validate_pin("a123"))
