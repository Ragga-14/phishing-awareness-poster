"""Exports the phishing poster to a single PowerPoint slide (poster style).
Install first:  pip install python-pptx
Run:            python build_pptx.py
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

NAVY = RGBColor(0x0B, 0x12, 0x20)
CARD = RGBColor(0x13, 0x1C, 0x31)
CYAN = RGBColor(0x22, 0xD3, 0xEE)
RED = RGBColor(0xFF, 0x4D, 0x6D)
GREEN = RGBColor(0x34, 0xD3, 0x99)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.33), Inches(7.5)
slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank

bg = slide.background.fill
bg.solid()
bg.fore_color.rgb = NAVY


def box(x, y, w, h, fill=CARD):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.fill.background()
    return shape


def text(x, y, w, h, lines, size=14, color=WHITE, bold=False):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = line
        p.font.size = Pt(size)
        p.font.bold = bold
        p.font.color.rgb = color


# Title
text(0.5, 0.2, 12.3, 1, ["THINK BEFORE YOU CLICK"], 44, WHITE, True)
text(0.5, 1.0, 12.3, 0.6, ["Phishing: the #1 social engineering attack on organizations"], 20, CYAN)

# Panel 1: What it is
box(0.5, 1.8, 4.0, 2.4)
text(0.7, 1.9, 3.6, 0.5, ["WHAT IS PHISHING?"], 18, CYAN, True)
text(0.7, 2.4, 3.6, 1.8, ["Fake emails, SMS or calls pretending to be a trusted source to steal passwords, money or data."], 14)

# Panel 2: How it works
box(4.7, 1.8, 4.0, 2.4)
text(4.9, 1.9, 3.6, 0.5, ["HOW IT WORKS"], 18, RED, True)
text(4.9, 2.4, 3.6, 1.8, ["1. Bait: convincing message", "2. Pressure: urgency/fear", "3. Click: fake link/attachment", "4. Steal: credentials/malware", "5. Breach: network access"], 14)

# Panel 3: Red flags
box(8.9, 1.8, 3.9, 2.4)
text(9.1, 1.9, 3.5, 0.5, ["RED FLAGS"], 18, RED, True)
text(9.1, 2.4, 3.5, 1.8, ["Misspelled sender domain", "Urgent threats", "Generic greeting", "Unexpected attachment", "Mismatched links"], 14)

# Panel 4: Protect yourself
box(0.5, 4.4, 7.0, 1.9)
text(0.7, 4.5, 6.6, 0.5, ["HOW TO PROTECT YOURSELF"], 18, GREEN, True)
text(0.7, 5.0, 6.6, 1.3, ["STOP and think  |  CHECK sender and hover links", "VERIFY through official channels  |  REPORT to IT", "Use MFA and keep systems updated"], 15)

# Panel 5: Placement
box(7.7, 4.4, 5.1, 1.9)
text(7.9, 4.5, 4.7, 0.5, ["WHERE TO DISPLAY THIS POSTER"], 18, CYAN, True)
text(7.9, 5.0, 4.7, 1.3, ["Office desks and open-plan areas", "Break room / cafeteria", "Lift lobbies, reception, HR training rooms", "Finance and admin departments"], 14)

# Footer
footer = box(0.5, 6.5, 12.3, 0.7, RED)
text(0.7, 6.58, 11.9, 0.5, ["Suspect phishing? Do NOT click. Report to IT Security: security@yourorganization.com"], 18, WHITE, True)

# Optional image if you downloaded one
img = os.path.join("assets", "hero-phishing-hook.png")
if os.path.exists(img):
    slide.shapes.add_picture(img, Inches(11.3), Inches(0.2), height=Inches(1.4))

prs.save("Phishing_Awareness_Poster.pptx")
print("Saved Phishing_Awareness_Poster.pptx")