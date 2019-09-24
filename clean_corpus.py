import re

SPECIAL_CHARACTERS_REGEX = re.compile(r"[.,]")

def calculate_number_of_lines(input_file_path):
    lines_count = 0
    with open(input_file_path, "r", encoding="utf-8") as input_file:
        for line in input_file:
            lines_count += 1
    return lines_count


def filter_special_characters(text):
    filtered_text = text
    special_characters = re.findall(SPECIAL_CHARACTERS_REGEX, text)
    for special_character in special_characters:
        filtered_text = filtered_text.replace(special_character, '')
    return filtered_text


def main():
    input_file_path = "data/B.txt"
    output_file_path = "data/B-filtered.txt"
    number_of_lines = calculate_number_of_lines(input_file_path)
    with open(input_file_path, "r", encoding='utf-8') as file_input, open(output_file_path, "w", encoding='utf-8') as file_output:
        counter = 0
        for line in file_input:
            counter += 1
            percentage = (counter / number_of_lines) * 100
            print('{}% {}/{}'.format(percentage, counter, number_of_lines))
            filtered_line = filter_special_characters(line)
            file_output.write(filtered_line)


if __name__ == "__main__":
    main()
