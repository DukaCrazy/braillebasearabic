### - pip install braillebasearabic

# Arabic
### The algorithm behaves normally, as it does in any other language; however, we are not able to verify whether the braille generated for the Arabic library is correct.
"مكتبة برمجية طُوِّرت للتعامل مع نصوص برايل البسيطة والمعقدة 2026"

```python
from braille import *

bb = bba()
print()
print(bb.output_braille_txt("مكتبة برمجية طُوِّرت للتعامل مع نصوص برايل البسيطة والمعقدة 2026"))
```
Output: ⠍⠅⠞⠃⠡⠀⠃⠗⠍⠚⠊⠡⠀⠾⠥⠺⠠⠑⠗⠞⠀⠇⠇⠞⠷⠁⠍⠇⠀⠍⠷⠀⠝⠯⠺⠯⠀⠃⠗⠁⠊⠇⠀⠁⠇⠃⠎⠊⠾⠡⠀⠺⠁⠇⠍⠷⠟⠙⠡⠀⠼⠃⠚⠃⠋

# Announcement
- This package is part of an ecosystem called Braille Base. This name does not represent a company or business; it is an independent initiative aimed at providing registered braille tables for all of humanity.

- We constantly need help to register, update, and validate braille tables. There is still no official contact channel, but you can find new information on the blog braillebase.blogspot.com or brailletable.blogspot.com.

## Pre-registered Letters and Characters

- ا, ب, ت, ث, ج, ح, خ, د, ذ, ر, ز, س, ش, ص, ض, ط, ظ, ع, غ, ف, ق, ك, ل, م, ن, ه, و, ي;

- لا, ى, ة, ء, أ, إ, ؤ, ئ, آ;


-  َ,  ً ,  ِ ,  ٍ ,  ُ ,  ٌ ,  ْ ,  ّ ;

` Fatha = "\u064e"       # َ  , Tanween Al Fath = "\u064b"   # ً  , Kasra = "\u0650"       # ِ  `

` Tanween Al Kasr = "\u064d"   # ٍ  , Dhamma = "\u064f"       # ُ  , Tanween Al Dham = "\u064c"   # ٌ `  

` Sukoun = "\u0652"       # ْ  , Shaddah = "\u0651"      # ّ  `



## Special: Greek
- [Α] ,[Β] ,[Γ] ,[Δ] ,[Ε] ,[Ζ] ,[Η] ,[Θ] ,[Ι] ,[Κ] ,[Λ] ,[Μ] ,[Ν] ,[Ξ] ,[Ο] ,[Π] ,[Ρ] ,[Σ] ,[Τ] ,[Υ] ,[Φ] ,[Χ] ,[Ψ] ,[Ω];
- [α] ,[β] ,[γ] ,[δ] ,[ε] ,[ζ] ,[η] ,[θ] ,[ι] ,[κ] ,[λ] ,[μ] ,[ν] ,[ξ] ,[ο] ,[π] ,[ρ] ,[σ] ,[τ] ,[υ] ,[φ] ,[χ] ,[ψ] ,[ω] ,[ς];
