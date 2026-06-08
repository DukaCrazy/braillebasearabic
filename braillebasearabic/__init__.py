from braillebase import BrailleBase

class BrailleBaseArabic(BrailleBase):
    def __init__(self):

        """
        """
        super().__init__()
        self.setting_braille_rules01("⠨", "⠐") 

        #Alphabet Arabic
        self.append_braille_letter("ا", ["⠁"]) 
        self.append_braille_letter("ب", ["⠃"]) 
        self.append_braille_letter("ت", ["⠞"]) 
        self.append_braille_letter("ث", ["⠹"]) 
        self.append_braille_letter("ج", ["⠚"]) 
        self.append_braille_letter("ح", ["⠱"]) 
        self.append_braille_letter("خ", ["⠭"]) 
        self.append_braille_letter("د", ["⠙"]) 
        self.append_braille_letter("ذ", ["⠮"]) 
        self.append_braille_letter("ر", ["⠗"]) 
        self.append_braille_letter("ز", ["⠵"]) 
        self.append_braille_letter("س", ["⠎"]) 
        self.append_braille_letter("ش", ["⠩"]) 
        self.append_braille_letter("ص", ["⠯"]) 
        self.append_braille_letter("ض", ["⠫"]) 
        self.append_braille_letter("ط", ["⠾"]) 
        self.append_braille_letter("ظ", ["⠿"]) 
        self.append_braille_letter("ع", ["⠷"]) 
        self.append_braille_letter("غ", ["⠣"]) 
        self.append_braille_letter("ف", ["⠋"]) 
        self.append_braille_letter("ق", ["⠟"]) 
        self.append_braille_letter("ك", ["⠅"]) 
        self.append_braille_letter("ل", ["⠇"]) 
        self.append_braille_letter("م", ["⠍"]) 
        self.append_braille_letter("ن", ["⠝"]) 
        self.append_braille_letter("ه", ["⠓"]) 
        self.append_braille_letter("و", ["⠺"]) 
        self.append_braille_letter("ي", ["⠊"]) 
        #Additional shapes for some letters and “hamzas”
        self.append_braille_letter("لا", ["⠧"]) 
        self.append_braille_letter("ى", ["⠕"]) 
        self.append_braille_letter("ة", ["⠡"]) 
        self.append_braille_letter("ء", ["⠄"]) 
        self.append_braille_letter("أ", ["⠌"]) 
        self.append_braille_letter("إ", ["⠨"]) 
        self.append_braille_letter("ؤ", ["⠳"]) 
        self.append_braille_letter("ئ", ["⠽"]) 
        self.append_braille_letter("آ", ["⠜"]) 
        #Diacritical Signs
        self.append_braille_letter("\u064e", ["⠂"]) 
        self.append_braille_letter("\u064b", ["⠆"]) 
        self.append_braille_letter("\u0650", ["⠑"]) 
        self.append_braille_letter("\u064d", ["⠔"]) 
        self.append_braille_letter("\u064f", ["⠥"]) 
        self.append_braille_letter("\u064c", ["⠢"]) 
        self.append_braille_letter("\u0652", ["⠒"]) 
        self.append_braille_letter("\u0651", ["⠠"]) 

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
        self.append_special_braille_lettr_rules01("A", ["⠁"])
        self.append_special_braille_lettr_rules01("B", ["⠃"])
        self.append_special_braille_lettr_rules01("C", ["⠉"])
        self.append_special_braille_lettr_rules01("D", ["⠙"])
        self.append_special_braille_lettr_rules01("E", ["⠑"])
        self.append_special_braille_lettr_rules01("F", ["⠋"])
        self.append_special_braille_lettr_rules01("G", ["⠛"])
        self.append_special_braille_lettr_rules01("H", ["⠓"])
        self.append_special_braille_lettr_rules01("I", ["⠊"])
        self.append_special_braille_lettr_rules01("J", ["⠚"])
        self.append_special_braille_lettr_rules01("K", ["⠅"])
        self.append_special_braille_lettr_rules01("L", ["⠇"])
        self.append_special_braille_lettr_rules01("M", ["⠍"])
        self.append_special_braille_lettr_rules01("N", ["⠝"])
        self.append_special_braille_lettr_rules01("O", ["⠕"])
        self.append_special_braille_lettr_rules01("P", ["⠏"])
        self.append_special_braille_lettr_rules01("Q", ["⠟"])
        self.append_special_braille_lettr_rules01("R", ["⠗"])
        self.append_special_braille_lettr_rules01("S", ["⠎"])
        self.append_special_braille_lettr_rules01("T", ["⠞"])
        self.append_special_braille_lettr_rules01("U", ["⠥"])
        self.append_special_braille_lettr_rules01("V", ["⠧"])
        self.append_special_braille_lettr_rules01("W", ["⠺"])
        self.append_special_braille_lettr_rules01("X", ["⠭"])
        self.append_special_braille_lettr_rules01("Y", ["⠽"])
        self.append_special_braille_lettr_rules01("Z", ["⠵"])

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
        
