


def translate(text,translation_map):
    #use raw input and split the sentence into a list of words
    input_list = text.split()
    output_list = []

    #iterate the input words and append translation
    #(or word if no translation) to the output
    for word in input_list:
        translation = translation_map.get(word)
        output_list.append(translation if translation else word)

    #convert output list back to string
    return ' '.join(output_list)