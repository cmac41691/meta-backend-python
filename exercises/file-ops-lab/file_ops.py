def read_file(file_name):
    with open(file_name, "r") as file:
        contents = file.read()
        print(contents)
        return contents


def read_file_into_list(file_name):
    with open(file_name, "r") as file:
        return file.readlines()


def write_first_line_to_file(file_contents, output_filename):
    if file_contents == "":
        first_line = ""
    else:
        first_line = file_contents.split("\n")[0]

    with open(output_filename, "w") as file:
        file.write(first_line)


def read_even_numbered_lines(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        even_lines = []

        for index, line in enumerate(lines, start=1):
            if index % 2 == 0:
                even_lines.append(line)

        return even_lines


def read_file_in_reverse(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        lines.reverse()
        print(lines)
        return lines