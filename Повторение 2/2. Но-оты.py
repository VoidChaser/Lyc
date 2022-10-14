notes = {
    "до": "до-о",
    "ре": "ре-э",
    "ми": "ми-и",
    "фа": "фа-а",
    "соль": "со-оль",
    "ля": "ля-а",
    "си": "си-и"
}


class Note:
    def __init__(self, note: str, time=False):
        self.time = time
        self.note = notes[note] if time else note

    def play(self):
        print(self.note)

    def __str__(self):
        return self.note

