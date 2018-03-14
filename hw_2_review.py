import os
import string

positive_path = "C:\Users\\15169\Desktop\\txt_sentoken\\pos"
negative_path = "C:\Users\\15169\Desktop\\txt_sentoken\\neg"

file_number_limit = 1000

sentence_to_test = 'I like this movie very much'


def loadData(folder_path, limit):
    data_arr = []
    for root, dirs, files in os.walk(folder_path, topdown=False):
        counter = 0
        for name in files:
            if counter >= limit:
                break
            file_path = os.path.join(root, name)
            data_arr.extend(open(file_path, 'r').readlines())
            counter += 1
    return data_arr

positive_data = loadData(positive_path, file_number_limit)
negative_data = loadData(negative_path, file_number_limit)

mega_positive = ''.join(positive_data).replace('\n', '')
mega_negative = ''.join(negative_data).replace('\n', '')

clean_mega_positive = mega_positive.translate(None, string.punctuation).lower()
clean_mega_negative = mega_negative.translate(None, string.punctuation).lower()


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

clean_mega_pos_dict = word_count(mega_positive)
clean_mega_neg_dict = word_count(mega_negative)


def total_prob(sentence, mega_text, dictionary):
    tokens = sentence.lower().split()
    probability = 1
    total_lenth = len(mega_text)
    for word in tokens:
        if word in dictionary:
            value = dictionary[word]
        else:
            print 'not found word'
            print word
            value = 0

        probability = probability * (value / float(total_lenth))

    return probability


pos_prob = total_prob(sentence_to_test, clean_mega_positive, clean_mega_pos_dict)
neg_prob = total_prob(sentence_to_test, clean_mega_negative, clean_mega_neg_dict)

print pos_prob
print neg_prob
