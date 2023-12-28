def average_characters_per_line(file_path):
    total_characters = 0
    total_lines = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            total_characters += len(line)
            total_lines += 1

    if total_lines == 0:
        return 0  # Avoid division by zero

    average_characters = total_characters / total_lines
    return average_characters

# Replace 'your_file.txt' with the path to your text file
file_path = 'data/urdu_eng_text.txt'
result = average_characters_per_line(file_path)

print(f"Average characters per line: {result:.2f}")
