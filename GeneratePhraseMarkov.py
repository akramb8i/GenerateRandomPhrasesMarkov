import sys
import random
import collections


def readfile(file_name):     # read the input file

    with open(file_name) as f:
        contents = f.read()
    return contents


def creatwords(file_content, prefix):   # reading file content and storing words in a dictionary


    dict = collections.defaultdict(list)
    words = file_content.split(' ')
    start = prefix

    for word in words[start:]:
        key = ' '.join(words[start - prefix:start])
        dict[key].append(word)

        start += 1

    return dict


def generateoutput(dict, output_len):        # generating the output sentences

    current_words = random.choice(list(dict.keys())).split(' ')  # random starting words
    output = ' '.join(current_words) + ' '

    for i in range(output_len):
        try:
            key = ' '.join(current_words)
            random_words = random.choice(dict[key])
            output += random_words + ' '

            for word in range(len(current_words)):
                current_words[word] = current_words[(word + 1) % len(current_words)]
            current_words[-1] = random_words

        except KeyError:
            return output
    return output


if __name__ == '__main__':
    file_content = readfile(sys.argv[1])   # get the text file name
    prefix_len = creatwords(file_content, int(sys.argv[2]))    # number of prefix from cmd
    output_sentences = generateoutput(prefix_len, int(sys.argv[3]))    # output sentence length
    print(output_sentences)