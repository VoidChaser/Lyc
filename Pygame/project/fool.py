import os
import sys
import pygame
import random
import itertools
from functools import total_ordering

numses = {'нет': 0,
          '1': 1,
          '2': 2,
          '3': 3,
          '4': 4,
          '5': 5,
          '6': 6,
          '7': 7,
          '8': 8,
          '9': 9,
          '10': 10,
          'валет': 11,
          'дама': 12,
          'король': 13,
          'туз': 14}


def start_screen():
    intro_text = ["Представляю вам Карточную игру Дурак.",
                  "",
                  "Правила типичны, колода 36 карт, без джокеров,",
                  "В начале игры:",
                  "",
                  "Происходит перемешивание колоды.",
                  "На каждого игрока выдается 6 карт, при раздаче определеятся козырная масть.",
                  "**В качестве козыря при раздаче не ставятся тузы.**",
                  "P.s. Карты козырной масти ценятся в игре, так как любая карта козырной масти может",
                  "покрыть любую карту кроме козырных карт достоинством выше.",
                  "",
                  "Определение первого хода:",
                  "Первый ход определяется наличием козырей у игроков,",
                  " и/или их достоинством: у кого есть карта козырной масти",
                  "наивысшего достоинства, тот и ходит первым.",
                  "Правило определения первого хода работает при условии того,",
                  " что игроки начинают новый матч, в котором никто не успел проиграть;",
                  "Иначе, первым ходит тот, кто проиграл.",
                  "",
                  "При атаке:",
                  "Во время игры игроки по очереди выкладывают карты, атакуя друг-друга по-очереди.",
                  "Атака происходит любой картой из своей колоды",
                  "В ответ защищающийся игрок должен отбить карту противника картой козырной масти,",
                  "либо высшего достоинства",
                  "В противном случае, защищающийся обязан взять все оставшиеся карты со стола,",
                  " или взять сразу первую карту, если не может её отбить.",
                  "Защита происходит до того момента, как на столе окажутся 6 заверщенных пар карт,",
                  " - игроки останутся без карт, либо игрок в защите возьмёт карты, или отобъется.",
                  "После каждого хода игроки добирают карты до 6. Игрок, который атаковал берёт карты первый.",
                  "Если в конце игры оба игрока не могут полно добрать карты, то карты делятся пополам,",
                  " так, что больше карт достается тому, кто ходил последним."]

    screen = pygame.display.set_mode((800, 800))
    fon = pygame.transform.scale(load_image('sukno.jpg'), (800, 800))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 20)
    text_coord = 10
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('White'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 30
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


pygame.init()
size = WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class DeckCardCountError(Exception):
    pass


class QueueError(Exception):
    pass


@total_ordering
class Card:
    def __init__(self, num, suit):
        super().__init__()
        self.suit = suit
        self.str_num = num
        self.num = self.get_num()
        if self.num != 0:
            self.image = load_image(f'{self.str_num} {self.suit}.png')

        self.kozir = False  # Чтобы инициализировать когда козырь определен конкретную масть - тру

    # Реализация атаки в классе игры. - реакты на события Если на карту положить карту,
    # то она выдает стейт атаки. Тру - успешна - карта покрыта, фолс - нет.
    def attack(self, other_card):
        if self > other_card:
            return True
        else:
            return False

    def __repr__(self):
        return f'Карта {self.str_num} {self.suit}'

    def __str__(self):
        return f'{self.str_num} {self.suit}'

    def __eq__(self, other):
        if self.kozir:
            if other.kozir:
                if self.suit == other.suit and self.num == other.num:
                    return True
                else:
                    return False
            elif not other.kozir:
                return False

        elif not self.kozir:
            if other.kozir:
                return False
            elif not other.kozir:
                if self.suit == other.suit and self.num == other.num:
                    return True
                else:
                    return False

    def __lt__(self, other):
        if self.kozir:
            if other.kozir:
                if self.suit == other.kozir and self.num < other.num:
                    return True
                else:
                    return False
            elif not other.kozir:
                return False

        elif not self.kozir:
            if other.kozir:
                return True
            elif not other.kozir:
                if self.suit == other.suit and self.num < other.num:
                    return True
                else:
                    return False

    def get_num(self):
        return numses[self.str_num]

    def __hash__(self):
        return hash(self.num)


No_cards = Card('нет', 'козырей')
ruba = load_image('рубашка.png')


@total_ordering
class Hand:
    def __init__(self, name):
        self.name = name
        self.container = []
        self.hod = None
        self.count_cards = None
        self.kozirs_count = None
        self.highest_kozir = None

    def recount(self):
        global kozir
        self.count_cards = len(self.container)
        count = 0
        high_num = 0
        highest_card = No_cards
        for _ in self.container:
            if _.suit == kozir.suit:
                if _.num > high_num:
                    high_num = _.num
                    highest_card = _
                count += 1
        self.kozirs_count = count
        self.highest_kozir = highest_card

    def __iadd__(self, other):
        self.container += [other]
        self.container = sorted(self.container, key=lambda x: (x.suit, x.num))
        self.recount()
        return self

    def __eq__(self, other):
        if self.container == other.container:
            return True
        else:
            return False

    def __le__(self, other):
        if self.kozirs_count:
            if other.kozirs_count:
                if self.kozirs_count < other.kozirs_count:
                    return True
                else:
                    if self.highest_kozir < other.highest_kozir:
                        return True
                    else:
                        return False
            else:
                return False

        elif not self.kozirs_count:
            if other.kozirs_count:
                return True
            elif not self.kozirs_count:
                return False

    # Закинуть в класс игры.
    def __isub__(self, other):
        try:
            if self.hod is True:
                # что-нибудь для анимации выкидывания карты и реализация пула карт в активной области игрового поля
                attack_card = self.container.pop(other)
                print(f'Нападает карта {attack_card}')
            else:
                raise QueueError('Сейчас не ваш ход.')
            self.recount()
            return self
        except QueueError as exept:
            print(exept)

    def __delitem__(self, key):
        del self.container[key]

    def __len__(self):
        return len(self.container)

    def __getitem__(self, item):
        return self.container[item]

    def __iter__(self):
        return iter(self.container)

    def __repr__(self):
        return f"Колода {self.name}:\n Карт: {self.count_cards},\n карты: " + ', '.join(list(
            map(str, self.container))) + f',\n Козырей: {self.kozirs_count}, Наивысший козырь: {self.highest_kozir}'

    # def check_first_hod(self, *hands): - закинуть в класс игры
    # реализовать методы сравнения колод


suits = ['пик', 'черви', 'буби', 'крести']
nums = ['6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
start_deck = [a for a in itertools.product(nums, suits)]
deck = []
for _ in range(len(start_deck)):
    card = Card(start_deck[_][0], start_deck[_][1])
    deck.append(card)

shuffle_counter = random.randint(16, 30)
for _ in range(shuffle_counter):
    random.shuffle(deck)

kozir_pos = 12
kozir = deck[kozir_pos]
while kozir.num == 'туз':
    kozir_pos += 1
    kozir = deck[kozir_pos]

for _ in deck:
    if _.suit == kozir.suit:
        _.kozir = True

pc_hand = Hand('Pc')
player_hand = Hand('Player')
first_player_is_first = False
for _ in range(12):
    if first_player_is_first:
        if _ % 2 != 0:
            pc_hand += deck[_]
        else:
            player_hand += deck[_]
    else:
        if _ % 2 != 0:
            player_hand += deck[_]
        else:
            pc_hand += deck[_]

kozir_pos = 12
kozir = deck[kozir_pos]
while kozir.num == 'туз':
    kozir_pos += 1
    kozir = deck[kozir_pos]

print(f"Выбранный козырь: {kozir}")
print()

print(pc_hand)
print()

print(player_hand)
print()


class Card_sprite(pygame.sprite.Sprite):
    def __init__(self, card: Card, x, y, show=False):
        super().__init__(all_sprites, card_sprites)
        self.card = card
        self.shown = show
        self.card_image = card.image
        self.update()
        self.rect = self.card_image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def show_card(self):
        self.shown = not self.shown

    def update(self):
        if self.shown:
            self.image = self.card_image
        else:
            self.image = ruba
        # self.rect = self.image.get_rect()



HOD_X = 250


class Game:
    def __init__(self):
        self.hands = []
        self.bito = []
        self.cards = deck
        self.hod = 0
        self.hod_dict = {}
        self.win = False
        self.add_decks(pc_hand, player_hand)
        self.hodit = max(self.hands)
        print(f"\nПервым ходит: {self.hodit.name}")
        self.draw_decks()
        while not self.win:
            self.hoditb()
            pygame.display.flip()

    def add_decks(self, *args):
        self.hands.extend(args)

    def draw_decks(self):
        y = 60
        for hand in self.hands:
            # hand = self.hands[0]
            for _, it_card in enumerate(hand):
                # print(_ * WIDTH // hand.count_cards, it_card)
                if hand.name == 'Player':
                    new_card = Card_sprite(it_card, 80 // hand.count_cards + _ * WIDTH // hand.count_cards, y,
                                           show=True)
                    # print(new_card.rect.width)
                else:
                    new_card = Card_sprite(it_card, 80 // hand.count_cards + _ * WIDTH // hand.count_cards, y)
            y += 540
            print()

    def attack_card(self, attack_sprite: Card_sprite):
        # print(self.hodit)
        if self.hodit.name == 'Player':
            self.hodit = 'Pc'
        else:
            self.hodit = 'Player'
        self.hod_dict[attack_sprite.card] = None
        self.hod += 1

        print(self.hod_dict)


    def defend_card(self, defending_sprite: Card_sprite):
        defending_card = defending_sprite.card
        attacking_card = self.hod_dict[list(self.hod_dict.keys())[self.hod]]
        if defending_card > attacking_card:
            self.hod_dict[attacking_card] = defending_card
            self.hod += 1
        print(self.hod_dict)



    def hoditb(self):
        # hodit = True
        dragging = False
        print(type(self.hodit))
        try:
            if self.hodit.name == 'Player':
                while self.hodit.name == 'Player':
                    # cr_x, cr_y = c_x + w, c_y + h
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            terminate()
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            curr_x, curr_y = event.pos
                            _: Card_sprite
                            for _ in card_sprites:
                                card_x = _.rect.x
                                card_y = _.rect.y
                                if (card_x <= curr_x <= card_x + _.rect.width) and (
                                        card_y <= curr_y <= card_y + _.rect.height):
                                    shot_card = _.card
                                    shot_deck = list(filter(lambda x: _.card in x.container, self.hands))[0].name
                                    print(
                                        f'Попал в карту {shot_card} колоды'
                                        f' {shot_deck}')
                                    if shot_deck == 'Player':
                                        self.attack_card(_)
                                        # _.show_card()
                                        # _.update()
                                    # должна быть проверка чтобы не хватать карты другого игрока
                    # Реализовать перетаскивание
                    # Реализовать стейты атаки и защиты
                    # Реализовать зону для карт
                    # Реализовать выкладку карт и сдвиг карт при добавлении новых
                    # Реализовать интерфейс
                    # Реализовать ход/ выбор карты компьютером, метод выкладки карты для защиты, атаки.

                    screen.fill(pygame.Color('black'))
                    all_sprites.draw(screen)
                    card_sprites.draw(screen)
                    pygame.display.flip()
                print('Игрок сходил')
                # hodit = False

                self.hodit = list(filter(lambda x: x.name != 'Player', self.hands))[0]
                print(self.hodit)
            else:
                print('Компьютер сходил')
                self.hodit = list(filter(lambda x: x.name != 'Pc', self.hands))[0]
        except AttributeError as e:
            print(e)
    # Проблема выдает что self.hodit это строка

def terminate():
    pygame.quit()
    sys.exit()


class Cloth(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.image.fill(pygame.Color('#41ac43'))




FPS = 50
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
card_sprites = pygame.sprite.Group()
# c_x, c_y = 0, 0
# w, h = 10, 10

if __name__ == '__main__':
    pygame.display.set_caption('The fool')
    cloth = Cloth()
    game = Game()
    ranning = True
    # start_screen()
    while ranning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

        screen.fill(pygame.Color('black'))
        all_sprites.draw(screen)
        card_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
