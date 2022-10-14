notes = {
    "до": "до-о",
    "ре": "ре-э",
    "ми": "ми-и",
    "фа": "фа-а",
    "соль": "со-оль",
    "ля": "ля-а",
    "си": "си-и"
}

PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]


class Note:
    def __init__(self, note, is_long=False):
        self.time = is_long
        self.note = notes[note] if is_long else note

    def play(self):
        print(self.note)

    def __str__(self):
        return self.note


class LoudNote(Note):
    def __init__(self, note, is_long=False):
        super().__init__(note, is_long)
        self.note = self.note.upper()


class DefaultNote(Note):
    def __init__(self, note='до', is_long=False):
        super().__init__(note, is_long)


class NoteWithOctave(Note):
    def __init__(self, note, octave, is_long=False):
        super().__init__(note, is_long)
        self.octave = octave

    def __str__(self):
        return f'{self.note} ({self.octave})'