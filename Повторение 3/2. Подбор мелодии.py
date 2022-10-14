from functools import total_ordering

notes = {
    "до": "до-о",
    "ре": "ре-э",
    "ми": "ми-и",
    "фа": "фа-а",
    "соль": "со-оль",
    "ля": "ля-а",
    "си": "си-и"
}

alt_notes = {
    "до-о": "до",
    "ре-э": "ре",
    "ми-и": "ми",
    "фа-а": "фа",
    "со-оль": "соль",
    "ля-а": "ля",
    "си-и": "си"
}

notes_nums = {"до": 0,
              "ре": 1,
              "ми": 2,
              "фа": 3,
              "соль": 4,
              "ля": 5,
              "си": 6,
              }

long_notes_nums = {
    "до-о": 0,
    "ре-э": 1,
    "ми-и": 2,
    "фа-а": 3,
    "со-оль": 4,
    "ля-а": 5,
    "си-и": 6,
}

N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


@total_ordering
class Note:
    def __init__(self, note, is_long=False):
        self.time = is_long
        self.note = note
        self.timeness = notes_nums[alt_notes[self.note]] if self.note in list(alt_notes.keys())\
            else notes_nums[
            self.note]

    def play(self):
        print(self.note)

    def __str__(self):
        return self.note if not self.time else notes[self.note]

    def __eq__(self, other):
        if self.timeness == other.timeness:
            return True
        return False

    def __lt__(self, other):
        if self.timeness < other.timeness:
            return True
        return False

    def __lshift__(self, other):
        note = alt_notes[self.note] if self.note in list(alt_notes.keys()) else self.note
        index = list(notes_nums.keys()).index(note)
        evd_num = (index - other)
        note = list(notes_nums.keys())[evd_num % 7]
        return Note(note, self.time)

    def __rshift__(self, other):
        note = alt_notes[self.note] if self.note in list(alt_notes.keys()) else self.note
        index = list(notes_nums.keys()).index(note)
        evd_num = (index + other)
        note = list(notes_nums.keys())[evd_num % 7]
        return Note(note, self.time)

    def get_interval(self, other):
        n1, n2 = self.timeness, other.timeness
        sub = INTERVALS[abs((n2 - n1)) % 7]
        return sub

    def __repr__(self):
        return self.note if not self.timeness else notes[self.note]


class Melody:
    def __init__(self, *note: list):
        self.notes = note[0] if note else []
        semi_res = list(map(lambda x: x.note if not x.time else notes[x.note], self.notes))

    def __str__(self):
        if self.notes:
            semi_res = list(map(lambda x: x.note if not x.time else notes[x.note], self.notes))
            semi_res[0] = semi_res[0].capitalize()
            return ', '.join(semi_res)
        return ''

    def __repr__(self):
        if self.notes:
            semi_res = list(map(lambda x: x.note if not x.time else notes[x.note], self.notes))
            semi_res[0] = semi_res[0].capitalize()
            return ', '.join(semi_res)
        return ''

    def append(self, other):
        self.notes = self.notes + [other]

    def replace_last(self, other):
        self.notes = self.notes[:-1] + [other]

    def remove_last(self):
        self.notes = self.notes[:-1]

    def clear(self):
        self.notes = []

    def __len__(self):
        return len(self.notes)

    def __lshift__(self, other):
        if self.notes:
            if all(list(map(lambda x: (x.timeness - other) >= 0, self.notes))):
                notes = list(map(lambda x: x.__lshift__(other), self.notes))
                return Melody(notes)
        return Melody(self.notes)

    def __rshift__(self, other):
        if self.notes:
            if all(list(map(lambda x: (x.timeness + other) <= 6, self.notes))):
                notes = list(map(lambda x: x.__rshift__(other), self.notes))
                return Melody(notes)
        return Melody(self.notes)