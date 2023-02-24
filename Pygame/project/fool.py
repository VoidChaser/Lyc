import pygame
import os
import sys
import random
import itertools
from functools import total_ordering

pygame.init()
size = WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode(size)

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
    font = pygame.font.Font('Arial', 20)
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


# @total_ordering
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
                if self.num == other.num:
                    return True

        elif not self.kozir:
            if not other.kozir:
                if self.suit == other.suit:
                    if self.num == other.num:
                        return True

        return False
        # Ретёрн прерывает выполнение функции. Когда условие выполняется - выполнение прервется на значении - тру,
        # в остальных значениях, - фолс.

    def __lt__(self, other):
        if self.kozir:
            if other.kozir:
                if self.num < other.num:
                    return True

        elif not self.kozir:
            if other.kozir:
                return True
            elif not other.kozir:
                if self.suit == other.suit:
                    if self.num < other.num:
                        return True

        return False

    def __ge__(self, other):
        if self.kozir:
            if other.kozir:
                if self.num > other.num:
                    return True

        elif not self.kozir:
            if other.kozir:
                return False
            elif not other.kozir:
                if self.suit == other.suit:
                    if self.num > other.num:
                        return True

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

    def pop(self, index):
        item_to_ret = self.container.pop(index)
        return item_to_ret

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

    def __isub__(self, other):
        try:
            if self.hod is True:
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

    def __index__(self, element):
        return self.container.index(element)

    def index(self, element):
        return self.container.index(element)

    def __iter__(self):
        return iter(self.container)

    def pop(self, index):
        to_pop_item = self.container.pop(index)
        return to_pop_item

    def __repr__(self):
        return f"Колода {self.name}:\n Карт: {self.count_cards},\n карты: " + ', '.join(list(
            map(str, self.container))) + f',\n Козырей: {self.kozirs_count}, Наивысший козырь: {self.highest_kozir}'


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
        card.image = self

    def show_card(self):
        self.shown = not self.shown

    def update(self):
        if self.shown:
            self.image = self.card_image
        else:
            self.image = ruba


HOD_X = 250


class Game:
    def __init__(self):
        self.first_round_user = None
        self.hodit = None
        self.hands, self.bito = [], []
        self.cards = deck
        self.hod_dict = {}
        self.hod = 0
        self.win = False
        self.add_decks(pc_hand, player_hand)
        self.init_and_draw_decks()


    def get_index_user_name(self, pos=-1):
        if not self.hod_dict:
            return None

        last_dict_hod = list(self.hod_dict.keys())[pos]
        return self.get_involved_hand(last_dict_hod).name

        # Изменил возвращаемое значение функции на именно имя ключа из словаря, как имени пользователя, а не значения.

    def get_last_user_name(self):
        return self.get_index_user_name()

    def get_first_user_name(self):
        return self.get_index_user_name(0)

    def add_decks(self, *args):
        self.hands.extend(args)

    def init_and_draw_decks(self):
        y = 60
        for hand in self.hands:
            for _, it_card in enumerate(hand):
                if hand.name == 'Player':
                    Card_sprite(it_card, 80 // hand.count_cards + _ * WIDTH // hand.count_cards, y,
                                show=True)
                else:
                    Card_sprite(it_card, 80 // hand.count_cards + _ * WIDTH // hand.count_cards, y)
            y += 540
            print()

    def draw_decks(self):
        y = 60
        for hand in self.hands:
            for _, it_card in enumerate(hand):
                if hand.name == 'Player':
                    it_card.image.rect.move(80 // hand.count_cards + _ * WIDTH // hand.count_cards, y)
                else:
                    it_card.image.rect.move(80 // hand.count_cards + _ * WIDTH // hand.count_cards, y)
                    it_card.image.shown = False
            y += 540
            print()

    def begin_round(self, first_hod=False):
        # global cloth

        # В идеале, чисто, перед тем, как начинать раунд,
        # должны все по очереди добирать карт до 6, и должны перерисовываться колоды.
        if all_hod_used_cards:
            for _ in all_hod_used_cards:
                used_hand = game.get_involved_hand(_)
                used_hand.pop(used_hand.index(_))

        self.draw_decks()

        self.hod_dict = {}
        if not first_hod:
            self.hodit = list(filter(lambda x: x != self.hodit, self.hands))[0]
            print(f"\nХодит: {self.hodit.name}\n")
        else:
            self.hodit = max(self.hands)
            print(f"\nПервым ходит {self.hodit.name}:\n")
        self.first_round_user = self.hodit.name
        interface_sprites.update(self.first_round_user)

    def end_round(self):
        pass

    # Должны убираться карты, раздаваться по порядку недостающие карты. Обновляться бито.

    def attack_card(self, attack_card: Card):
        if self.hodit.name == 'Player':
            taken_card_sprite = player_hand[player_hand.container.index(attack_card)].image
        else:
            taken_card_sprite = pc_hand[pc_hand.container.index(attack_card)].image
            taken_card_sprite.show_card()
        self.hod_dict[attack_card] = None
        taken_card_sprite.update()


    def defend_card(self, defending_card: Card):
        if self.hodit.name == 'Player':
            self.hodit = 'Pc'
        else:
            defending_card.image.show_card()
        self.hod_dict[list(self.hod_dict.keys())[-1]] = defending_card
        defending_card.image.update()


    def get_involved_hand(self, card):
        return list(filter(lambda x: card in x, self.hands))[0]


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
interface_sprites = pygame.sprite.Group()
card_sprites = pygame.sprite.Group()

Card_sprite(kozir, 720, 300,
            show=True)


class Interface_Sprite(pygame.sprite.Sprite):
    def __init__(self, text, x, y, text_changable=False, font_size=25):
        super().__init__(all_sprites, interface_sprites)
        self.text = text
        self.text_changable = text_changable
        self.font_size = font_size
        self.x, self.y = x, y

        self.image = pygame.Surface((WIDTH, HEIGHT))

        self.font = pygame.font.Font(None, font_size)
        self.image = self.font.render(self.text, False, (pygame.Color(255, 255, 255)))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.update()

    # low_font = pygame.font.Font('Arial', 10)
    # middle_font = pygame.font.Font('Arial', 20)

    def redraw_text(self):
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image = self.font.render(self.text, False, (pygame.Color(255, 255, 255)))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x, self.y

    def update(self, new_text=None):
        if self.text_changable:
            if new_text is not None:
                self.text = new_text
        self.redraw_text()


def formated_hod_return():
    return f'Сейчас ходит: {game.hodit.name}'


if __name__ == '__main__':
    pygame.display.set_caption('The fool')
    cloth = Cloth()
    game = Game()

    all_hod_used_cards = list()
    game.begin_round(first_hod=True)
    running = True
    # start_screen()
    # Пока проект не доделан заставка закомментирована.
    game_name = Interface_Sprite('Дурак by tr', 330, 5)
    pc_hand_name = Interface_Sprite('Колода Pc', 30, 30, font_size=30)
    player_hand_name = Interface_Sprite('Колода Player', 15, 570, font_size=30)
    # hod_indicator = Interface_Sprite('Ходит:', 600, 30, font_size=30)

    while not game.win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            # Поправил потому что последняя карта это та, которую будут класть,
            # в иных случаях надо смотреть на первую карту.
            fair_play = True
            all_hod_used_cards = [*list(game.hod_dict.keys()), *list(game.hod_dict.values())]
            all_hod_used_cards = list(filter(lambda x: x is not None, all_hod_used_cards))
            if game.hodit.name == 'Player':
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    curr_x, curr_y = event.pos
                    _: Card_sprite
                    for _ in card_sprites:
                        card_x = _.rect.x
                        card_y = _.rect.y
                        if (card_x <= curr_x <= card_x + _.rect.width) and (
                                card_y <= curr_y <= card_y + _.rect.height):
                            shot_card = _.card
                            shot_deck_name = list(filter(lambda x: _.card in x.container, game.hands))[0].name
                            # Несостыковка. Похоже что использование pop для выкидывания
                            # использованной уже карты из учёта карт для выбора - плохая идея,
                            # и стоит учитывать то, что использованные карты выбирать не нужно,-
                            # путём их убирания из possible_cards_to_..., а после уж и методом pop.
                            print(
                                f'Выбрана карта {shot_card} колоды'
                                f' {shot_deck_name}')
                            if shot_deck_name == 'Player':
                                if game.first_round_user == 'Player' or game.first_round_user is None:
                                    # if shot_card
                                    if shot_card not in all_hod_used_cards:
                                        game.attack_card(shot_card)
                                        print(f'Игрок атакует картой {shot_card}.\n')
                                    else:
                                        print(f'Картой {shot_card} уже ходили.')
                                        fair_play = False
                                    # Если первым ходил, игрок, то в раунде игрок будет только атаковать.
                                    # Поэтому убрал условие.

                                elif game.first_round_user == 'Pc':
                                    pc_played_card = list(game.hod_dict.keys())[-1]
                                    if shot_card > pc_played_card:
                                        if shot_card not in all_hod_used_cards:
                                            game.defend_card(shot_card)
                                            print(f'Игрок защищается от {pc_played_card} картой {shot_card}.\n')
                                        else:
                                            print(f'Картой {shot_card} уже ходили.')
                                            fair_play = False
                                    else:
                                        print(f'Этой картой нельзя защититься.'
                                              f' Она меньше по значению либо не подходит по масти.')
                                        fair_play = False

                            else:
                                print('Вы не выбрали вашу карту')
                                fair_play = False
                            if fair_play:
                                print('Игрок сходил\n')

                                # hodit = False
                                game.hodit = list(filter(lambda x: x.name != 'Player', game.hands))[0]
                                print()
            else:

                if game.first_round_user == 'Pc' or game.first_round_user is None:
                    card_to_attack = min(list(filter(lambda x: x not in all_hod_used_cards, pc_hand)),
                                         key=lambda x: x.num)
                    game.attack_card(card_to_attack)
                    print(f'Компьютер атакует картой {card_to_attack}.\n')

                elif game.first_round_user == 'Player':
                    player_played_card = list(game.hod_dict.keys())[-1]
                    possible_cards_to_defend = list(
                        filter(lambda x: x > player_played_card and x not in all_hod_used_cards, pc_hand))

                    if possible_cards_to_defend:
                        card_to_defend = min(possible_cards_to_defend)
                        game.defend_card(card_to_defend)
                        print(f'Компьютер защищается от {player_played_card} картой {card_to_defend}.\n')

                    else:
                        print(f'Компьютер берёт.\n')
                        game.begin_round()
                        # Берёт.

                print('Компьютер сходил\n')
                print(f'Состояние раунда на данный момент:\n {game.hod_dict}')
                game.hodit = list(filter(lambda x: x.name != 'Pc', game.hands))[0]
                print(f'\nХодит {game.hodit.name}:\n')

                print()

        screen.fill(pygame.Color('black'))
        all_sprites.update()
        all_sprites.draw(screen)
        card_sprites.draw(screen)
        interface_sprites.draw(screen)
        pygame.display.flip()

    # TODO: Реализовать зону для карт.
    #     Реализовать интерфейс.
    #     Реализовать выкладку карт и сдвиг карт при добавлении новых.
    #     Реализовать набор карт со стола. Разбивку словаря с картами на их список,
    #     добор этих карт в руку игрока или пк, дорисовку их потом.
    #     А также обновление статусов рубашек карт.
    #     Реализовать функцию добора.
    #     Реализовать ветвление в нажатие на кнопку брать, если нет возможных для хода карт,
    #     и проверку на то, что игрок может сходить.
    #     Реализовать экземпляр класса карт/интерфейсов - бито,
    #     которое является одной картой с цифрой,- количеством карт, оставшихся в колоде.
    #     В случае отсутствия таких, кроме козыря - убирать. Плюс учесть то, что козырь тоже часть бито.
    #     Баг: Карта, которой сходил компьютер всё еще числится в колоде.
    #     Доделать индикатор хода и его апдтейт
    #     Баг: Индикатор хода не работает и не обновляет значение.
    #     Баг: Туда же и баг со спрайтами, которые не обновляются.
    #     Баг спрайтов - остаются старые после реинициализации хода.
    #     Баг по ресурсам изображений: 9 буби = 9 черви.

    #     Проблема: Карта, которую убрали из колоды методом поп - нужна при определении последнего юзера хода.
    #     Решение: Переопределить метод определения последнего юзера хода так,
    #     чтобы последняя карта там не учавствовала. - решено. - готово.
    #     Проблема в методе сравнения - решена. - готово.
    #     Баг: Последнее значение для хода меняется на первое для следующего -> не создается новая запись в словаре,
    #     а меняется последняя - Исправлен. - готово.
    #     Должна быть проверка чтобы не хватать карты другого игрока - готово.
    #     Реализовать перетаскивание - Не нужно. Сделал через тапы. - готово.
    #     Реализовать стейты атаки и защиты - готово.
    #     Реализовать ход/ выбор карты компьютером, метод выкладки карты для защиты, атаки. - готово.
    #     Проблема выдает что self.hodit это строка - готово.
    #     def check_first_hod(self, *hands): - закинуть в класс игры - готово.
    #     реализовать методы сравнения колод - готово.

    pygame.quit()
