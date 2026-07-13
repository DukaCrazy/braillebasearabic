from braillebase import BrailleBase

class BrailleBaseArabic(BrailleBase):
    def __init__(self):

        """
        """
        super().__init__()
        self.setting_braille_rules_uppercase("⠨", "⠐") 

        #Alphabet Arabic
        self.append_braille_letter("ا", ["⠁"], 3) 
        self.append_braille_letter("ب", ["⠃"], 3) 
        self.append_braille_letter("ت", ["⠞"], 3) 
        self.append_braille_letter("ث", ["⠹"], 3) 
        self.append_braille_letter("ج", ["⠚"], 3) 
        self.append_braille_letter("ح", ["⠱"], 3) 
        self.append_braille_letter("خ", ["⠭"], 3) 
        self.append_braille_letter("د", ["⠙"], 3) 
        self.append_braille_letter("ذ", ["⠮"], 3) 
        self.append_braille_letter("ر", ["⠗"], 3) 
        self.append_braille_letter("ز", ["⠵"], 3) 
        self.append_braille_letter("س", ["⠎"], 3) 
        self.append_braille_letter("ش", ["⠩"], 3) 
        self.append_braille_letter("ص", ["⠯"], 3) 
        self.append_braille_letter("ض", ["⠫"], 3) 
        self.append_braille_letter("ط", ["⠾"], 3) 
        self.append_braille_letter("ظ", ["⠿"], 3) 
        self.append_braille_letter("ع", ["⠷"], 3) 
        self.append_braille_letter("غ", ["⠣"], 3) 
        self.append_braille_letter("ف", ["⠋"], 3) 
        self.append_braille_letter("ق", ["⠟"], 3) 
        self.append_braille_letter("ك", ["⠅"], 3) 
        self.append_braille_letter("ل", ["⠇"], 3) 
        self.append_braille_letter("م", ["⠍"], 3) 
        self.append_braille_letter("ن", ["⠝"], 3) 
        self.append_braille_letter("ه", ["⠓"], 3) 
        self.append_braille_letter("و", ["⠺"], 3) 
        self.append_braille_letter("ي", ["⠊"], 3) 
        #Additional shapes for some letters and “hamzas”
        self.append_braille_letter("لا", ["⠧"], 3) 
        self.append_braille_letter("ى", ["⠕"], 3) 
        self.append_braille_letter("ة", ["⠡"], 3) 
        self.append_braille_letter("ء", ["⠄"], 3) 
        self.append_braille_letter("أ", ["⠌"], 3) 
        self.append_braille_letter("إ", ["⠨"], 3) 
        self.append_braille_letter("ؤ", ["⠳"], 3) 
        self.append_braille_letter("ئ", ["⠽"], 3) 
        self.append_braille_letter("آ", ["⠜"], 3) 
        #Diacritical Signs
        self.append_braille_letter("\u064e", ["⠂"], 3) 
        self.append_braille_letter("\u064b", ["⠆"], 3) 
        self.append_braille_letter("\u0650", ["⠑"], 3) 
        self.append_braille_letter("\u064d", ["⠔"], 3) 
        self.append_braille_letter("\u064f", ["⠥"], 3) 
        self.append_braille_letter("\u064c", ["⠢"], 3) 
        self.append_braille_letter("\u0652", ["⠒"], 3) 
        self.append_braille_letter("\u0651", ["⠠"], 3) 

        #letras min
        self.append_braille_letter("a", ["⠁"]) 
        self.append_braille_letter("b", ["⠃"]) 
        self.append_braille_letter("c", ["⠉"]) #2026/05/18
        self.append_braille_letter("d", ["⠙"]) #2026/05/18
        self.append_braille_letter("e", ["⠑"]) #2026/05/18
        self.append_braille_letter("f", ["⠋"]) #2026/05/18
        self.append_braille_letter("g", ["⠛"]) #2026/05/18
        self.append_braille_letter("h", ["⠓"]) #2026/05/18
        self.append_braille_letter("i", ["⠊"]) #2026/05/18
        self.append_braille_letter("j", ["⠚"]) #2026/05/18
        self.append_braille_letter("k", ["⠅"]) #2026/05/18
        self.append_braille_letter("l", ["⠇"]) #2026/05/18
        self.append_braille_letter("m", ["⠍"]) #2026/05/18
        self.append_braille_letter("n", ["⠝"]) #2026/05/18
        self.append_braille_letter("o", ["⠕"]) #2026/05/18
        self.append_braille_letter("p", ["⠏"]) #2026/05/18
        self.append_braille_letter("q", ["⠟"]) #2026/05/18
        self.append_braille_letter("r", ["⠗"]) #2026/05/18
        self.append_braille_letter("s", ["⠎"]) #2026/05/18
        self.append_braille_letter("t", ["⠞"]) #2026/05/18
        self.append_braille_letter("u", ["⠥"]) #2026/05/18
        self.append_braille_letter("v", ["⠧"]) #2026/05/18
        self.append_braille_letter("w", ["⠺"]) #2026/05/18
        self.append_braille_letter("x", ["⠭"]) #2026/05/18
        self.append_braille_letter("y", ["⠽"]) #2026/05/18
        self.append_braille_letter("z", ["⠵"]) #2026/05/18

       #letras maiusc
        self.append_braille_letter("A", ["⠁"],1)
        self.append_braille_letter("B", ["⠃"],1)
        self.append_braille_letter("C", ["⠉"],1)
        self.append_braille_letter("D", ["⠙"],1)
        self.append_braille_letter("E", ["⠑"],1)
        self.append_braille_letter("F", ["⠋"],1)
        self.append_braille_letter("G", ["⠛"],1)
        self.append_braille_letter("H", ["⠓"],1)
        self.append_braille_letter("I", ["⠊"],1)
        self.append_braille_letter("J", ["⠚"],1)
        self.append_braille_letter("K", ["⠅"],1)
        self.append_braille_letter("L", ["⠇"],1)
        self.append_braille_letter("M", ["⠍"],1)
        self.append_braille_letter("N", ["⠝"],1)
        self.append_braille_letter("O", ["⠕"],1)
        self.append_braille_letter("P", ["⠏"],1)
        self.append_braille_letter("Q", ["⠟"],1)
        self.append_braille_letter("R", ["⠗"],1)
        self.append_braille_letter("S", ["⠎"],1)
        self.append_braille_letter("T", ["⠞"],1)
        self.append_braille_letter("U", ["⠥"],1)
        self.append_braille_letter("V", ["⠧"],1)
        self.append_braille_letter("W", ["⠺"],1)
        self.append_braille_letter("X", ["⠭"],1)
        self.append_braille_letter("Y", ["⠽"],1)
        self.append_braille_letter("Z", ["⠵"],1)

        #number
        self.append_braille_letter("⠼", ["⠼"]) #2026/06/05
        self.append_braille_letter("1", ["⠁"]) #2026/06/05
        self.append_braille_letter("2", ["⠃"]) #2026/06/05
        self.append_braille_letter("3", ["⠉"]) #2026/06/05
        self.append_braille_letter("4", ["⠙"]) #2026/06/05
        self.append_braille_letter("5", ["⠑"]) #2026/06/05
        self.append_braille_letter("6", ["⠋"]) #2026/06/05
        self.append_braille_letter("7", ["⠛"]) #2026/06/05
        self.append_braille_letter("8", ["⠓"]) #2026/06/05
        self.append_braille_letter("9", ["⠊"]) #2026/06/05
        self.append_braille_letter("0", ["⠚"]) #2026/06/05  

        self.append_braille_letter("...", ["⠄", "⠄", "⠄"])
        self.append_braille_letter("…", ["⠄", "⠄", "⠄"])
        self.append_braille_letter("———", ["⠤", "⠤", "⠤"])
        
