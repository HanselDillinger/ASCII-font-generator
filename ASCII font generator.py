"""
ASCII font generator
"""

import os

try:
    import pyfiglet
    from termcolor import colored
    import colorama
    from PIL import Image
    from PIL import ImageDraw
except ImportError as ImpErr:
    raise ImportError("Import couldn't find module, or couldn't find name" +\
                      "in module {}".format(ImpErr))

colorama.init()


class FontGenerator:
    # fonts from pyfiglet
    font_list = [
        "3-d", "3x5", "5lineoblique", "acrobatic", "alligator", "alligator2", "alphabet", "avatar", "banner",
        "banner3-D",
        "banner3", "banner4", "barbwire", "basic", "bell", "big", "bigchief", "binary", "block", "bubble", "bulbhead",
        "calgphy2", "caligraphy", "catwalk", "chunky", "coinstak", "colossal", "computer", "contessa", "contrast",
        "cosmic",
        "cosmike", "cricket", "cyberlarge", "cybermedium", "cybersmall", "diamond", "digital", "doh", "doom",
        "dotmatrix",
        "drpepper", "eftichess", "eftifont", "eftipiti", "eftirobot", "eftitalic", "eftiwall", "eftiwater", "epic",
        "fender", "fourtops", "fuzzy", "goofy", "gothic", "graffiti", "hollywood", "invita", "isometric1", "isometric2",
        "isometric3", "isometric4", "italic", "ivrit", "jazmine", "jerusalem", "katakana", "kban", "larry3d", "lcd",
        "lean",
        "letters", "linux", "lockergnome", "madrid", "marquee", "maxfour", "mike", "mini", "mirror", "mnemonic",
        "morse",
        "moscow", "nancyj-fancy", "nancyj-underlined", "nancyj", "nipples", "ntgreek", "o8", "ogre", "pawp", "peaks",
        "pebbles", "pepper", "poison", "puffy", "pyramid", "rectangles", "relief", "relief2", "rev", "roman", "rot13",
        "rounded", "rowancap", "rozzo", "runic", "runyc", "sblood", "script", "serifcap", "shadow", "short", "slant",
        "slide", "slscript", "small", "smisome1", "smkeyboard", "smscript", "smshadow", "smslant", "smtengwar", "speed",
        "stampatello", "standard", "starwars", "stellar", "stop", "straight", "tanja", "tengwar", "term", "thick",
        "thin",
        "threepoint", "ticks", "ticksslant", "tinker-toy", "tombstone", "trek", "tsalagi", "twopoint", "univers",
        "usaflag",
        "weird"]

    def __init__(self):
        """
        Program introduction
        """

        os.system("cls")
        print(colored(pyfiglet.figlet_format("ASCII fonts generator",
                                             font="slant"), "blue"))
        print("ver. 1.0.0")
        os.system("pause")
        self.menu()

    def menu(self):
        """
        Set a font
        """

        # main loop
        while True:
            
            while True:
                os.system("cls")
                print(colored("Choose a font (0 - 145) (':e' - exit, ':f' - font names).\n", "grey", "on_white"))

                try:
                    command = input(">")
                    if command == ":e":
                        return
                    elif command == ":f":
                        os.system("cls")
                        for i, font in enumerate(self.font_list):
                            print(str(i) + ") " + font)
                        os.system("pause")
                        continue
                    if (int(command) >= 0 and int(command) <= 145):
                        break
                except ValueError:
                    continue

            self.introduction_and_generation(int(command))

    def introduction_and_generation(self, font_num):
        """
        Font example.
        It also accepts user text.
        """

        while True:
            os.system("cls")
            print(colored(self.font_list[font_num], "green", "on_blue") + "\n")
            print(pyfiglet.figlet_format("Sample Text", font=self.font_list[font_num]))

            print("Type ':b' to return to the menu.")
            text = str(input("Please enter your text: "))

            # Back to main menu
            if text == ":b":
                return

            # If user didn't type anything
            if not text:
                continue

            ascii_text = pyfiglet.figlet_format(text, font=self.font_list[font_num])
            print(ascii_text)

            # Loop until user type a correct command
            while True:
                print(colored("Save? t/i/b (text/image/back)", "white", "on_green"))
                command = str(input("Please enter a char : "))

                if command == "b" or command == "t" or command == "i":
                    if command == "b":
                        break

                    name = str(input("File name: "))
                    if command == "t":
                        file = open(name + ".txt", "w")
                        file.write(ascii_text)
                        file.close()
                    elif command == "i":
                        img = Image.new("RGB", (1, 1), (255, 255, 255))
                        d = ImageDraw.Draw(img)
                        text_width, text_height = d.textsize(ascii_text)
                        img = img.resize((text_width, text_height))
                        d = ImageDraw.Draw(img)
                        d.text((0, 0), ascii_text, (0, 0, 0))
                        img.save(name + ".png")

                    print(colored("Done!", "green"))
                    os.system("pause")
                    break


def main():
    font_generator = FontGenerator()


if __name__ == "__main__":
    main()

__ver__ = "1.0.0"
