from __future__ import print_function, unicode_literals
from tabulate import tabulate
from PyInquirer import prompt
import os
import json

OSBOT_BOTS_PATH = os.path.expanduser("~") + "\\OSBot\\Data\\bots.json"


def prettify_bot_info(bots: list[dict]) -> list[dict]:
    key_order = [
        "banned",
        "email",
        "username",
        "password",
        "pin",
        "description",
        "verified",
    ]

    pretty_bots = []

    for bot in bots:

        pretty_bot = {}
        for key in key_order:
            if key == "banned":
                pretty_bot[key] = bot.get(key, False)
                continue

            if key in bot:
                pretty_bot[key] = bot[key]
            else:
                pretty_bot[key] = ""

        for key, value in bot.items():
            if key not in pretty_bot.keys():
                pretty_bot[key] = value

        pretty_bots.append(pretty_bot)

    return pretty_bots


def prettify_bots(bots: list[dict]) -> None:
    with open(OSBOT_BOTS_PATH, "w") as json_file:
        json.dump(prettify_bot_info(bots), json_file, indent=4)


def display_bots(bots: list[dict]) -> None:
    print(tabulate(prettify_bot_info(bots), headers="keys", tablefmt="rounded_grid"))


def create_acc_list(bots: list[dict]) -> list[dict]:
    bots_list = []
    for bot in bots:
        username = bot.get("username", "No username")
        description = bot.get("description", "No description")
        banned = bot.get("banned", False)

        bot_info = {
            "name": f'{username} - {description if description != "" else "No description"}',
            "disabled": "Banned" if banned else "",
        }
        bots_list.append(bot_info)

    return bots_list


def find_bot(username: str, bots: list[dict]) -> dict:
    for bot in bots:
        if bot.get("username", "No username") == username:
            return bot
    return {}


def write_bot_script(accounts: list[str]) -> None:
    BAT_PATH = f"{os.getcwd()}\\launch_bots.bat"
    OSBOT_PATH = os.path.expanduser("~") + "\\Desktop\\osbot.jar"
    JAVA_PATH = '"C:\\Java\\jre1.8.0_301\\bin\\java.exe"'
    OSBOT_USERNAME = "fcgod1"
    OSBOT_PASS = "#@goO21fwg1@YU&d"

    with open(BAT_PATH, "w", encoding="UTF-8") as launch_file:
        pass

    for account in accounts:
        chosen_bot = find_bot(account.split(" - ")[0], bots)
        email = chosen_bot["email"]
        password = chosen_bot["password"]

        with open(BAT_PATH, "a", encoding="UTF-8") as launch_file:
            launch_file.write(
                f'{JAVA_PATH} -jar {OSBOT_PATH} -login "{OSBOT_USERNAME}:{OSBOT_PASS}" -bot "{email}:{password}:0000"\n'
            )


with open(OSBOT_BOTS_PATH) as bots_file:
    bots = json.loads(bots_file.read())

start_questions = [
    {
        "type": "list",
        "name": "process",
        "message": "What do you want to do?",
        "choices": ["Display bots", "Prettify bots file", "Run bots"],
    }
]

start_answers = prompt(start_questions)
if start_answers["process"] == start_questions[0]["choices"][0]:
    display_bots(bots)
    os._exit(-1)
if start_answers["process"] == start_questions[0]["choices"][1]:
    prettify_bots(bots)
    os._exit(-1)
else:
    bot_questions = [
        {
            "type": "checkbox",
            "name": "accounts",
            "message": "Choose your bot account(s):",
            "choices": create_acc_list(bots),
        }
    ]
    bot_answers = prompt(bot_questions)
    write_bot_script(bot_answers["accounts"])
    os._exit(0)
