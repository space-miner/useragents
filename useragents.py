import csv
import random
import os


filename = os.path.dirname(os.path.realpath(__file__))+'/useragents.csv'
user_agent_csv = open(filename, 'r')
ser_agent_reader = csv.reader(user_agent_csv)
user_agent_list = [row for row in user_agent_reader]


def load_header():
    return {'User-Agent': random.choice(user_agent_list)[0]}
