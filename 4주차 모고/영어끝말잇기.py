def solution(n, words):
    speek_person = []

    for w in words:
        if not speek_person:
            speek_person.append(w)

        elif w not in speek_person and speek_person[-1][-1] == w[0]:
            speek_person.append(w)

        elif speek_person[-1][-1] != w[0] or w in speek_person:
            return [(len(speek_person) % n) + 1, (len(speek_person) // n) + 1]

    if len(speek_person) == len(words):
        return [0,0]