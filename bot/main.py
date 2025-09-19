"""
Main menu and orchestration for the entertainment bot.
Uses functions from recommendations, games, utils.
"""
from bot.recommendations import recommend
from bot.games import rock_paper_scissors, guess_number
from bot.external import tell_joke
from bot.utils import print_header, ask_choice, clear_console
from termcolor import cprint

def start_bot():
    clear_console()
    print_header("ENTERTAINMENT BOT")
    while True:
        cprint("\nГоловне меню:", "cyan")
        print("1) Рекомендації (фільми/музика/ігри)")
        print("2) Анекдот / Цікава історія")
        print("3) Ігри")
        print("4) Запустити Гру: Хто хоче стати мільйонером?")
        print("0) Вихід")
        choice = ask_choice("Введіть номер опції: ", ["0","1","2","3","4"])
        if choice == "0":
            cprint("Бувайте! 👋", "green")
            break
        elif choice == "1":
            recommend()
        elif choice == "2":
            tell_joke()
        elif choice == "3":
            show_games_menu()
        elif choice == "4":
            # ланкуємо гру мільйонер як підмодуль
            from millionaire.game import play_millionaire
            play_millionaire()

def show_games_menu():
    while True:
        cprint("\nМеню ігор:", "cyan")
        print("1) Камінь-ножиці-папір")
        print("2) Вгадай число")
        print("0) Назад")
        choice = ask_choice("Ваш вибір: ", ["0","1","2"])
        if choice == "0":
            break
        elif choice == "1":
            rock_paper_scissors()
        elif choice == "2":
            guess_number()

