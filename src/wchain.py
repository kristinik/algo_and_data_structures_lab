def find_max_chain_length(words):
    if not words:
        return 0

    chain_lengths = {}
    words.sort(key=len)


    for word in words:
        chain_lengths[word] = 1
        for i in range(len(word)):
            new_word = word[:i] + word[i + 1:]
            if new_word in chain_lengths:
                chain_lengths[word] = max(chain_lengths[word], chain_lengths[new_word] + 1)

    return max(chain_lengths.values())


def read_input(file_name):
        with open(file_name, 'r') as f:
            number_of_words_in_line = f.readline().strip()
            if not number_of_words_in_line:
                return []

            number_of_words_in_line = int(number_of_words_in_line)
            words = [f.readline().strip() for _ in range(number_of_words_in_line)]

        return words


def write_output(max_chain_length, filename):
        with open(filename, 'w') as output_file:
            output_file.write(str(max_chain_length))
