import glob
from nltk.sentiment import SentimentIntensityAnalyzer
import re
from datetime import datetime

file_paths = sorted(glob.glob("files/*.txt"))

analyzer = SentimentIntensityAnalyzer()

pos_value = []
neg_value = []
paths = []


def positive_negative():
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            contents = file.read().split('\n')
            scores = analyzer.polarity_scores(contents[0])
            pos_value.append(scores['pos'])
            neg_value.append(scores['neg'])
    return pos_value, neg_value


def date():
    for file_path in file_paths:
        paths.append(file_path + "\n")
    pattern = re.compile(r"10-\d{2}")
    findings = re.findall(pattern, str(paths))
    formatted_dates = []
    for date_string in findings:
        date_local = datetime.strptime(date_string, '%m-%d')
        formatted_date = date_local.strftime('%b %d')
        formatted_dates.append(formatted_date)
    return formatted_dates
