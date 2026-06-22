from braillebase import BrailleBase

class BrailleBaseArabic(BrailleBase):
    def __init__(self):

        """
        """
        super().__init__()
        self.setting_braille_rules_uppercase("⠨", "⠐") 

        #Alphabet Arabic
        self.append_special_braille_letter_rules_RTL("ا", ["⠁"]) 
        self.append_special_braille_letter_rules_RTL("ب", ["⠃"]) 
        self.append_special_braille_letter_rules_RTL("ت", ["⠞"]) 
        self.append_special_braille_letter_rules_RTL("ث", ["⠹"]) 
        self.append_special_braille_letter_rules_RTL("ج", ["⠚"]) 
        self.append_special_braille_letter_rules_RTL("ح", ["⠱"]) 
        self.append_special_braille_letter_rules_RTL("خ", ["⠭"]) 
        self.append_special_braille_letter_rules_RTL("د", ["⠙"]) 
        self.append_special_braille_letter_rules_RTL("ذ", ["⠮"]) 
        self.append_special_braille_letter_rules_RTL("ر", ["⠗"]) 
        self.append_special_braille_letter_rules_RTL("ز", ["⠵"]) 
        self.append_special_braille_letter_rules_RTL("س", ["⠎"]) 
        self.append_special_braille_letter_rules_RTL("ش", ["⠩"]) 
        self.append_special_braille_letter_rules_RTL("ص", ["⠯"]) 
        self.append_special_braille_letter_rules_RTL("ض", ["⠫"]) 
        self.append_special_braille_letter_rules_RTL("ط", ["⠾"]) 
        self.append_special_braille_letter_rules_RTL("ظ", ["⠿"]) 
        self.append_special_braille_letter_rules_RTL("ع", ["⠷"]) 
        self.append_special_braille_letter_rules_RTL("غ", ["⠣"]) 
        self.append_special_braille_letter_rules_RTL("ف", ["⠋"]) 
        self.append_special_braille_letter_rules_RTL("ق", ["⠟"]) 
        self.append_special_braille_letter_rules_RTL("ك", ["⠅"]) 
        self.append_special_braille_letter_rules_RTL("ل", ["⠇"]) 
        self.append_special_braille_letter_rules_RTL("م", ["⠍"]) 
        self.append_special_braille_letter_rules_RTL("ن", ["⠝"]) 
        self.append_special_braille_letter_rules_RTL("ه", ["⠓"]) 
        self.append_special_braille_letter_rules_RTL("و", ["⠺"]) 
        self.append_special_braille_letter_rules_RTL("ي", ["⠊"]) 
        #Additional shapes for some letters and “hamzas”
        self.append_special_braille_letter_rules_RTL("لا", ["⠧"]) 
        self.append_special_braille_letter_rules_RTL("ى", ["⠕"]) 
        self.append_special_braille_letter_rules_RTL("ة", ["⠡"]) 
        self.append_special_braille_letter_rules_RTL("ء", ["⠄"]) 
        self.append_special_braille_letter_rules_RTL("أ", ["⠌"]) 
        self.append_special_braille_letter_rules_RTL("إ", ["⠨"]) 
        self.append_special_braille_letter_rules_RTL("ؤ", ["⠳"]) 
        self.append_special_braille_letter_rules_RTL("ئ", ["⠽"]) 
        self.append_special_braille_letter_rules_RTL("آ", ["⠜"]) 
        #Diacritical Signs
        self.append_special_braille_letter_rules_RTL("\u064e", ["⠂"]) 
        self.append_special_braille_letter_rules_RTL("\u064b", ["⠆"]) 
        self.append_special_braille_letter_rules_RTL("\u0650", ["⠑"]) 
        self.append_special_braille_letter_rules_RTL("\u064d", ["⠔"]) 
        self.append_special_braille_letter_rules_RTL("\u064f", ["⠥"]) 
        self.append_special_braille_letter_rules_RTL("\u064c", ["⠢"]) 
        self.append_special_braille_letter_rules_RTL("\u0652", ["⠒"]) 
        self.append_special_braille_letter_rules_RTL("\u0651", ["⠠"]) 

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
        self.append_special_braille_letter_rules_uppercase("A", ["⠁"])
        self.append_special_braille_letter_rules_uppercase("B", ["⠃"])
        self.append_special_braille_letter_rules_uppercase("C", ["⠉"])
        self.append_special_braille_letter_rules_uppercase("D", ["⠙"])
        self.append_special_braille_letter_rules_uppercase("E", ["⠑"])
        self.append_special_braille_letter_rules_uppercase("F", ["⠋"])
        self.append_special_braille_letter_rules_uppercase("G", ["⠛"])
        self.append_special_braille_letter_rules_uppercase("H", ["⠓"])
        self.append_special_braille_letter_rules_uppercase("I", ["⠊"])
        self.append_special_braille_letter_rules_uppercase("J", ["⠚"])
        self.append_special_braille_letter_rules_uppercase("K", ["⠅"])
        self.append_special_braille_letter_rules_uppercase("L", ["⠇"])
        self.append_special_braille_letter_rules_uppercase("M", ["⠍"])
        self.append_special_braille_letter_rules_uppercase("N", ["⠝"])
        self.append_special_braille_letter_rules_uppercase("O", ["⠕"])
        self.append_special_braille_letter_rules_uppercase("P", ["⠏"])
        self.append_special_braille_letter_rules_uppercase("Q", ["⠟"])
        self.append_special_braille_letter_rules_uppercase("R", ["⠗"])
        self.append_special_braille_letter_rules_uppercase("S", ["⠎"])
        self.append_special_braille_letter_rules_uppercase("T", ["⠞"])
        self.append_special_braille_letter_rules_uppercase("U", ["⠥"])
        self.append_special_braille_letter_rules_uppercase("V", ["⠧"])
        self.append_special_braille_letter_rules_uppercase("W", ["⠺"])
        self.append_special_braille_letter_rules_uppercase("X", ["⠭"])
        self.append_special_braille_letter_rules_uppercase("Y", ["⠽"])
        self.append_special_braille_letter_rules_uppercase("Z", ["⠵"])

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
        
