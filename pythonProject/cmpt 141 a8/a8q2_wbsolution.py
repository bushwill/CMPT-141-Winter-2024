def reverse_phrase(sentence):
    sentence_list = sentence.split(" ")
    return reverse_phrase_recursive(sentence_list)

def reverse_phrase_recursive(sentence_list):
    if len(sentence_list)<1:
        return ""
    if len(sentence_list) == 1:
        return sentence_list[0]
    return reverse_phrase_recursive(sentence_list[1:]) + " " + sentence_list[0]




print(reverse_phrase("DO I CHOOSE YOU PIKACHU"))
