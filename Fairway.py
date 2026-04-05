import random
import time

print("ОБРАТИТЕ ВНИМАНИЕ!!!")
print("Дорогие пользователи! Нашу игру нужно запускать через программу поддерживающую Python. К примеру Idle,PyCharm,Visual Studio Code.")
print("Спасибо за понимание. Приятной игры!")
print(f'\nВы - охотник на монстров. Жители одного странного маленького городка на окраине попросили вас освободить их дома от нечисти за хорошую плату, на что вы согласились. За каждый дом вы')
print('будете получать по 50 золотых. Какие монстры и секреты этого города вас ждут? Со временем вы')
print('всё узнаете. Но какой ценой?')

player: str = "😃"
wall: str = "⬛"
free: str = "⬜"
enemy: str = "👾"
key: str = "🔑"
lock: str = "🔒"
door: str = "🚪"
potion: str = "❤️"

p_hp: float = 100
max_hp: float = 100
gold: int = 0
p_damage: float = 20
m_dmg_mult: float = 1.0
esc_chns: float = 0.4
inventory: list = []
house_cleared: int = 0
current_house: int = 1
game_running: bool = True
player_exited: bool = False
p_x: int = 1
p_y: int = 1

houses: str = '''
1  /\\     2   /\\     3   /\\
  /  \\       /  \\       /  \\
 /____\\     /____\\     /____\\
 |    |     |    |     |    |
 | [] |     | [] |     | [] |
 |____|     |____|     |____|
'''
print(houses)

house1_map: list = [
    ['⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛'],
    ['⬛',player,'⬜','⬜','⬛','⬜','⬜','⬜','⬜','⬜','👾','⬜','⬜','⬜','⬛'],
    ['⬛','⬛','⬛','⬜','⬛','⬜','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬜','⬛'],
    ['⬛','🔑','⬜','⬜','❤️','⬜','⬜','👾','⬜','⬜','⬜','⬜','⬛','⬜','⬛'],
    ['⬛','⬛','⬛','⬛','⬛','⬛','⬜','⬛','⬛','⬛','⬛','⬜','⬛','⬜','⬛'],
    ['⬛','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬛','⬜','⬛','⬜','⬛','⬜','⬛'],
    ['⬛','⬜','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬜','⬛','⬜','⬛','⬜','⬛'],
    ['⬛','👾','⬛','⬜','⬜','⬜','⬜','⬜','⬜','👾','⬜','⬜','⬛','⬜','⬛'],
    ['⬛','⬜','⬛','⬜','⬛','⬛','⬛','⬜','⬛','⬛','⬛','⬛','⬛','⬜','⬛'],
    ['⬛','⬜','⬜','⬜','❤️','⬜','⬜','⬜','⬛','⬜','⬜','⬜','⬜','⬜','⬛'],
    ['⬛','⬛','⬛','⬛','⬛','⬜','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛'],
    ['⬛','⬜','⬜','👾','⬜','⬜','⬛','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬛'],
    ['⬛','⬜','⬛','⬛','⬛','⬛','⬛','⬜','⬛','⬛','⬛','⬛','⬛','⬜','⬛'],
    ['⬛','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬛','🚪','🔒','⬜','⬜','⬜','⬛'],
    ['⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛'],
]

house2_map: list = [
    ['⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛'],
    ['⬛',player,'⬜','⬛','⬜','⬜','⬜','⬛','⬜','⬜','⬜','⬛','⬜','⬜','⬛'],
    ['⬛','⬛','⬜','⬛','⬛','⬛','⬜','⬛','⬛','⬛','⬜','⬛','⬛','⬜','⬛'],
    ['⬛','⬜','⬜','⬛','❤️','⬜','⬜','⬜','👾','⬜','⬜','⬛','⬜','⬜','⬛'],
    ['⬛','⬛','⬜','⬛','⬛','⬛','⬜','⬛','⬛','⬛','⬜','⬛','⬛','⬜','⬛'],
    ['⬛','⬜','⬜','⬜','⬜','⬜','⬜','⬛','⬜','⬜','⬜','⬛','⬜','⬜','⬛'],
    ['⬛','⬛','⬛','⬛','⬛','⬛','⬜','⬛','⬛','⬛','⬜','⬛','⬛','⬜','⬛'],
    ['⬛','👾','⬜','⬜','⬜','⬜','⬜','⬛','⬜','⬜','⬜','⬛','⬜','⬜','⬛'],
    ['⬛','⬛','⬛','⬛','⬛','⬛','⬜','⬛','⬛','⬛','⬜','⬛','⬛','⬜','⬛'],
    ['⬛','⬜','⬜','⬜','⬜','⬜','⬜','⬛','⬜','⬜','⬜','⬜','❤️','⬜','⬛'],
    ['⬛','⬛','⬛','⬛','⬛','⬛','⬜','⬛','⬛','⬛','⬜','⬛','⬛','⬜','⬛'],
    ['⬛','⬜','⬜','👾','⬜','⬜','⬜','⬛','🔑','⬜','⬜','⬛','⬜','⬜','⬛'],
    ['⬛','⬛','⬛','⬛','⬛','⬛','⬜','⬛','⬛','⬛','⬜','⬛','⬛','⬜','⬛'],
    ['⬛','⬜','⬜','⬜','⬜','⬜','⬜','⬛','⬜','⬜','⬜','⬛','🚪','🔒','⬛'],
    ['⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛'],
]

house3_map: list = [
    ['⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛'],
    ['⬛',player,'⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','👾','⬜','⬜','⬜','⬛'],
    ['⬛','⬛','⬛','⬛','⬛','⬜','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬜','⬛'],
    ['⬛','⬜','⬜','⬜','❤️','👾','⬜','👾','⬜','⬜','⬛','🔑','⬛','⬜','⬛'],
    ['⬛','⬜','⬛','⬛','⬛','⬛','⬜','⬛','⬛','⬜','⬛','⬜','⬛','⬜','⬛'],
    ['⬛','⬜','⬜','⬜','❤️','⬜','⬜','⬛','⬜','⬜','⬛','⬜','⬜','⬜','⬛'],
    ['⬛','⬛','⬜','⬛','⬛','⬛','⬛','⬛','⬛','⬜','⬛','⬜','⬛','⬜','⬛'],
    ['⬛','👾','⬜','⬜','⬛','⬜','⬜','⬜','⬜','👾','⬛','⬜','⬛','⬜','⬛'],
    ['⬛','⬜','⬛','⬜','⬛','⬛','⬛','⬜','⬛','⬜','⬛','⬜','⬛','⬛','⬛'],
    ['⬛','⬜','⬛','⬜','⬜','⬜','⬜','⬜','⬛','⬜','⬜','⬜','❤️','⬜','⬛'],
    ['⬛','⬛','⬛','⬛','⬛','⬜','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛'],
    ['⬛','⬜','⬜','👾','⬜','⬜','⬛','⬜','⬜','⬜','⬜','⬜','❤️','⬜','⬛'],
    ['⬛','⬜','⬛','⬛','⬛','⬛','⬛','⬜','⬛','⬛','⬛','⬛','⬛','⬜','⬛'],
    ['⬛','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬛','🚪','🔒','⬜','⬜','⬜','⬛'],
    ['⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛'],
]

class EnemyClass:
    def __init__(self, x, y, name, health, damage):
        self.x, self.y, self.name, self.health, self.damage = x, y, name, health, damage
    
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, dmg):
        self.health -= dmg
    
    def get_attack_damage(self):
        base = random.randint(self.damage - 5, self.damage + 5)
        return int(base * m_dmg_mult)

class PotionClass:
    def __init__(self, x, y, heal_amount):
        self.x, self.y, self.heal_amount = x, y, heal_amount

class KeyClass:
    def __init__(self, x, y):
        self.x, self.y = x, y

class LockClass:
    def __init__(self, x, y):
        self.x, self.y, self.is_open = x, y, False

class DoorClass:
    def __init__(self, x, y):
        self.x, self.y = x, y

enemies, potions, keys, locks, doors = [], [], [], [], []
current_map = []

def auto_save():
    s = open("save.txt", "w", encoding="utf-8")
    s.write(str(p_hp) + "\n")
    s.write(str(gold) + "\n")
    s.write(str(house_cleared) + "\n")
    s.write(str(current_house) + "\n")
    s.write(str(p_damage) + "\n")
    for item in inventory:
        s.write(item + "\n")
    s.close()
    print("\n📝 [ПРОГРЕСС СОХРАНЕН]")
    
def load_house(n):
    global current_map, p_x, p_y, enemies, potions, keys, locks, doors, current_house
    current_house = n
    current_map = []
    
    if n == 1:
        for row in house1_map:
            current_map.append(list(row))
    elif n == 2:
        for row in house2_map:
            current_map.append(list(row))
    elif n == 3:
        for row in house3_map:
            current_map.append(list(row))
    
    enemies, potions, keys, locks, doors = [], [], [], [], []
    
    for y, row in enumerate(current_map):
        for x, item in enumerate(row):
            if item == player:
                p_x, p_y = x, y
            elif item == enemy:
                if n == 1:
                    enemies.append(EnemyClass(x, y, "Гоблин", 40, 10))
                elif n == 2:
                    enemies.append(EnemyClass(x, y, "Орк", 55, 15))
                elif n == 3:
                    enemies.append(EnemyClass(x, y, "Тролль", 70, 20))
            elif item == potion:
                potions.append(PotionClass(x, y, 30))
            elif item == key:
                keys.append(KeyClass(x, y))
            elif item == lock:
                locks.append(LockClass(x, y))
            elif item == door:
                doors.append(DoorClass(x, y))

def battle(m):
    global p_hp
    print("\n" + "=" * 40)
    print(f"⚔️ БОЙ С {m.name.upper()}! ⚔️")
    print("=" * 40)
    
    while m.is_alive() and p_hp > 0:
        print(f"\n💚 Ваше здоровье: {int(p_hp)} | ❤️ {m.name}: {m.health}")
        print("Выберите действие (введите цифру):")
        print("  1. Атаковать")
        print("  2. Использовать зелье")
        print("  3. Убежать")
        print("-" * 20)
        choice = input("👉 Ваш выбор: ")
        
        if choice == "1":
            dmg = random.randint(int(p_damage - 5), int(p_damage + 5))
            m.take_damage(dmg)
            print(f"⚔️ Вы нанесли {dmg} урона!")
            if m.is_alive():
                monster_dmg = m.get_attack_damage()
                p_hp -= monster_dmg
                print(f"👹 {m.name} нанес {monster_dmg} урона!")
        elif choice == "2":
            if "зелье" in inventory:
                inventory.remove("зелье")
                p_hp = min(max_hp, p_hp + 40)
                print("💊 Вы использовали зелье! Восстановлено 40 HP!")
                if m.is_alive():
                    monster_dmg = m.get_attack_damage()
                    p_hp -= monster_dmg
                    print(f"👹 {m.name} нанес {monster_dmg} урона!")
            else:
                print("❌ У вас нет зелий!")
        elif choice == "3":
            if random.random() < esc_chns:
                print("🏃 Вы успешно сбежали!")
                return True
            else:
                monster_dmg = m.get_attack_damage()
                p_hp -= monster_dmg
                print(f"👹 Не удалось убежать! {m.name} нанес {monster_dmg} урона!")
        else:
            print("❌ Неверный выбор! Пожалуйста, введите цифру 1, 2 или 3")
    
    return p_hp > 0

def shop():
    global p_hp, max_hp, gold, inventory, p_damage, m_dmg_mult, esc_chns, player
    shopping = True
    while shopping:
        print("\n" + "=" * 40)
        print("🏪 ЛАВКА КУЗНЕЦА ТОМАСА 🏪")
        print(f"💰 Ваше золото: {gold}")
        print("-" * 40)
        print("Выберите действие (введите цифру):")
        print("1. ❤️ Лечебное зелье (20 золота)")
        print("2. 🛡️ Увеличить Макс. HP +20 (40 золота)")
        print("3. ⚔️ Заточить меч (+10 к урону) (50 золота)")
        print("4. 🥧 Пирог от бабушки Агаты (рандомный эффект) (60 золота)")
        print("0. 🚪 Выйти из лавки")
        print("=" * 40)
        choice = input("👉 Ваш выбор: ")
        
        if choice == "1":
            if gold >= 20:
                gold -= 20
                inventory.append("зелье")
                print("✅ Вы купили зелье!")
            else:
                print("❌ Недостаточно золота!")
        elif choice == "2":
            if gold >= 40:
                gold -= 40
                max_hp += 20
                p_hp += 20
                print(f"✅ Макс. HP теперь {int(max_hp)}!")
            else:
                print("❌ Недостаточно золота!")
        elif choice == "3":
            if gold >= 50:
                gold -= 50
                p_damage += 10
                print("✅ Меч стал острее!")
            else:
                print("❌ Недостаточно золота!")
        elif choice == "4":
            if gold >= 60:
                gold -= 60
                print("ТОМАС: Осторожнее с этой штукой!")
                effect = random.randint(1, 4)
                if effect == 1:
                    max_hp = int(max_hp * 1.7)
                    p_hp = min(p_hp, max_hp)
                    p_damage = p_damage / 2 + 4
                    player = '🐢'
                    print(f"🐢 Тебе попалась начинка с зельем черепахи. Теперь твоё HP {int(p_hp)}. Твой урон понизился.")
                elif effect == 2:
                    max_hp = 15
                    p_hp = 15
                    p_damage += 10
                    m_dmg_mult = 0.33
                    player = '🐶'
                    print(f"🐶 Тебе попалась начинка с зельем мопса. Теперь твоё HP равно 15 ед. Враги наносят в 3 раза меньше урона!")
                elif effect == 3:
                    max_hp = 10
                    p_hp = 10
                    p_damage /= 3
                    esc_chns = 1.0
                    player = '🐰'
                    print("🐰 Тебе попалась начинка с зельем зайца. Теперь ты можешь убежать в любой момент! Но HP = 10.")
                else:
                    max_hp = 70
                    p_hp = min(p_hp, 70)
                    p_damage += 10
                    player = '😡'
                    print("🔥 Тебе попалась начинка с зельем берсерка. Теперь твои HP равны 70 ед., а урон на 10 ед. больше!")
            else:
                print("❌ Недостаточно золота!")
        elif choice == "0":
            shopping = False
            print("👋 Удачи в бою, охотник!")
        else:
            print("❌ Неверный выбор! Пожалуйста, введите цифру 0, 1, 2, 3 или 4")

open("save.txt", "a", encoding="utf-8").close()

print("\n" + "=" * 50)
print("ЗАГРУЗКА ИГРЫ")
print("=" * 50)
f_check = open("save.txt", "a", encoding="utf-8")
f_check.close()

while True:
    ans = input("Загрузить игру? (да/нет): ").lower()

    if ans == "да":
        f = open("save.txt", "r", encoding="utf-8")
        lines = f.readlines()
        f.close()

        if len(lines) < 5:
            print("❌ Ошибка: Сохранений не обнаружено! Пожалуйста, выберите нет (новая игра).")
        else:
            p_hp = float(lines[0][:-1])
            gold = int(lines[1][:-1])
            house_cleared = int(lines[2][:-1])
            current_house = int(lines[3][:-1])
            p_damage = float(lines[4][:-1])
            
            inventory = []
            if len(lines) > 5:
                for i in range(5, len(lines)):
                    item = lines[i][:-1]
                    if item != "":
                        inventory.append(item)
            
            load_house(current_house)
            print("✅ Загрузка завершена!")
            break

    elif ans == "нет":
        load_house(1)
        print("🚀 Начинаем новое приключение!")
        break
    else:
        print(f"Вы хотите сломать нашу программу? То есть мы над ней старались, а вы с нами так?! Ладно. \nПОЖАЛУЙСТА ВВЕДИТЕ ДА ИЛИ НЕТ.")
time.sleep(2)

start_time = time.time()

while game_running and p_hp > 0:
    print("\n" + "=" * 50)
    for row in current_map:
        print("".join(row))
    print("-" * 50)
    print("❤️ - зелье здоровья | 🔑 - ключ | 🔒 - замок | 🚪 - дверь")
    print(f"❤️ HP: {int(p_hp)}/{int(max_hp)} | 🎒 Инвентарь: {inventory} | 🏠 Домов: {house_cleared}/3 | 💰 Золото: {gold}")
    print("=" * 50)
    
    print("Управление (введите букву):")
    print("  W - вверх | S - вниз | A - влево | D - вправо | Q - выход")
    print("-" * 30)
    while True:
        move = input("👉 Ваш ход: ").lower()
        nx, ny = p_x, p_y

        if move == "w":
            ny -= 1
            break
        elif move == "s":
            ny += 1
            break
        elif move == "a":
            nx -= 1
            break
        elif move == "d":
            nx += 1
            break
        elif move == "q":
            auto_save()
            print("Выход из игры... Прогресс сохранён!")
            player_exited = True
            game_running = False
            break
        else:
            print("Вы поломать или поиграть?! Пожалуйста, введите W, A, S, D для движения или Q для выхода")
    
    if 0 <= ny < len(current_map) and 0 <= nx < len(current_map[0]):
        target = current_map[ny][nx]
        step_ok = False
        
        if target == free:
            step_ok = True
        elif target == wall:
            print("❌ Стена! Нельзя пройти.")
        elif target == potion:
            for p in potions:
                if p.x == nx and p.y == ny:
                    inventory.append("зелье")
                    current_map[ny][nx] = free
                    potions.remove(p)
                    step_ok = True
                    print("[+] Вы нашли зелье! 💊")
                    break
        elif target == key:
            for k in keys:
                if k.x == nx and k.y == ny:
                    inventory.append("Ключ")
                    current_map[ny][nx] = free
                    keys.remove(k)
                    step_ok = True
                    print("[+] Вы нашли ключ! 🔑")
                    break
        elif target == lock:
            locked_found = False
            for l in locks:
                if l.x == nx and l.y == ny and not l.is_open:
                    locked_found = True
                    if "Ключ" in inventory:
                        inventory.remove("Ключ")
                        l.is_open = True
                        current_map[ny][nx] = free
                        print("[+] Замок открыт!")
                        step_ok = True
                    else:
                        print("❌ Заперто! Нужен ключ!")
                    break
            if not locked_found:
                step_ok = True
        elif target == enemy:
            for e in enemies:
                if e.x == nx and e.y == ny:
                    if battle(e):
                        if e.health <= 0:
                            current_map[ny][nx] = free
                            enemies.remove(e)
                            print("👹 Монстр повержен!")
                        step_ok = True
                    break
        elif target == door:
            print("\n🚪 Вы подошли к двери...")
            if len(enemies) == 0:
                gold += 50
                print(f"💰 +50 золота! Всего золота: {gold}")
                auto_save()
                shop()
                house_cleared += 1
                if house_cleared < 3:
                    load_house(house_cleared + 1)
                    print(f"\n🏠 Вы переходите к дому {house_cleared + 1}!")
                else:
                    game_running = False
            else:
                print(f"⚠️ Монстры остались! Осталось {len(enemies)} монстров. Награды не будет.")
        else:
            step_ok = True
        
        if step_ok and game_running:
            current_map[p_y][p_x] = free
            p_x, p_y = nx, ny
            current_map[p_y][p_x] = player
    else:
        print("❌ Нельзя выйти за пределы карты!")

if player_exited:
    print("\n👋 Игра завершена по вашему желанию. Возвращайтесь!")
elif p_hp <= 0:
    print("\n" + "=" * 50)
    print("💀 ТЫ ПОГИБ... И НЕ СПАС ГОРОД... 💀")
    print("=" * 50)
    print("Старушка Агата плачет. Кузнец Томас грустит.")
elif house_cleared >= 3:
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    print("\n" + "=" * 60)
    print("🎉 ПОБЕДА! 🎉")
    print("=" * 60)
    print(f"⏱️ Время: {minutes} мин {seconds} сек")
    print(f"💰 Всего заработано: {gold} золотых")
    print("""
Жители города благодарят вас!
Старушка Агата испекла пирог.
Кузнец Томас выковал меч в вашу честь.

НО...
В последний момент из портала вылетает СВИТОК.
На нём написано: "Это только начало. Жди нас."

Ваше приключение только начинается...
""")
elif house_cleared < 3 and not player_exited:
    print("\n🏚️ КОНЦОВКА: ТРУСЛИВЫЙ ОХОТНИК 🏚️")
    print("Вы вышли из домов, оставив часть монстров. Томас выгнал вас из города.")
