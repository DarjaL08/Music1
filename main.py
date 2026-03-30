from music21 import stream, note
from music21 import environment
from music21 import metadata
from music21 import instrument
import random

us = environment.UserSettings()
us['musicxmlPath'] = '/Applications/MuseScore 4.app/Contents/MacOS/mscore'

language = input('Please enter the language you would like to use: ')
if language == 'English':
    alphabet = ["a", "b", "c", "d", "e",
                "f","g", "h", "i", "j",
                "k", "l", "m", "n", "o",
                "p", "q", "r", "s", "t",
                "u", "v", "w", "x", "y",
                "z",]
elif language == 'Latvian':
        alphabet = ["a", "ā", "b", "c", "č", "d",
                       "e", "ē", "f", "g", "ģ", "h",
                       "i", "ī", "j", "k", "ķ", "l",
                       "ļ", "m", "n", "ņ", "o", "p",
                       "r", "s", "š", "t", "u", "ū",
                       "v", "z", "ž"]

elif language == 'Russian':
        alphabet = ["а", "б", "в", "г", "д", "е", "ё",
                       "ж", "з", "и", "й", "к", "л", "м",
                       "н", "о", "п", "р", "с", "т", "у",
                       "ф", "х", "ц", "ч", "ш", "щ", "ъ",
                       "ы", "ь", "э", "ю", "я"]

def correct_name(name, alphabet):
        for letter in name:
            if letter not in alphabet:
             return None
        return name

def name_to_index(name, alphabet: list):
    indexes= []
    for letter in name:
        indexes.append(alphabet.index(letter))
    return indexes

def music(indexes, name):
    melody = stream.Score()
    part1 = stream.Part()
    part2 = stream.Part()
    melody.insert(0, metadata.Metadata())
    melody.metadata.title = f"{name}"
    melody.metadata.composer = "DL"
    part1.insert(0, instrument.Violoncello())
    part2.insert(0, instrument.Piano())
    score = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    vowels = set(list("aeiouy") + list("āēīū") + list("аеёиоуыэюя"))

    for i, ch in zip(indexes, name):
        if ch in vowels:
            octave = 4
            velocity = 80
            length = random.choice([0.5, 0.75, 1, 1.5])
        else:
                octave = 3
                velocity = 70
                length = random.choice([0.5, 0.75, 1, 1.5])
                notas = random.choice([
                            [0,2,4],
                            [0,4,2],
                            [0,1,2]
                          ])
        for nota in notas:
            pitch = score[(i + nota) % 7] + str(octave + ((i + nota) // 7) % 2)
            n = note.Note(pitch)
            n.volume.velocity = velocity
            n.quarterLength = length
        part1.append(n)
    melody.append(part1)
    return melody

while True:
    name = input('Please give me you Name: ')
    name = name.lower()
    name= name.replace(' ', '')
    result = correct_name(name, alphabet)
    if result is None:
        print('Sorry, your name was not recognised')
    else:
        res = name_to_index(result, alphabet)
        mel = music(res, name)
        mel.show()
        break













