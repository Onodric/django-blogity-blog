import datetime
import re
import math

from django.utils.html import strip_tags


def count_words(html_string):
    """
    A helper function to get a wordcount from a string of html

    :param html_string:
        A tagged html string
    :return:
        the word count of that string minus the tags
    """
    word_string = strip_tags(html_string)
    word_list = re.findall(r'\w+', word_string)
    word_count = len(word_list)
    return word_count


def get_read_time(html_string):
    """
    A helper function to get a read time of a given html string

    :param html_string:
        A tagged html string
    :return:
        The average read time of the article as an integer in minutes
    """
    count = count_words(html_string)
    # the average reader of English reads at 200-260 wpm
    read_rate = 200.0
    read_time_min = math.ceil(count/read_rate)
    read_time = str(datetime.timedelta(minutes=read_time_min))
    return read_time
