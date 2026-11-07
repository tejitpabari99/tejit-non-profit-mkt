"""Build docs/nonprofit-guide.pdf, the illustrated guide for nonprofit staff.

Needs reportlab and Pillow (third-party, not stdlib). It is not used in CI;
run it by hand after changing the text or the images in docs/guide-images/.

    python3 scripts/build_guide_pdf.py
"""
from pathlib import Path

from PIL import Image
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    Image as RLImage, KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle,
)

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "nonprofit-guide.pdf"
IMG = ROOT / "docs" / "guide-images"
ICON = ROOT / "plugin" / ".claude-plugin" / "icon.png"
REPO = "https://github.com/tejitpabari99/tejit-np-plugin"
INSTALL = REPO + "/blob/main/docs/install.md"
ISSUES = REPO + "/issues"

INK = colors.HexColor("#222222")
ACCENT = colors.HexColor("#1F5FA8")
LINK = "#1F5FA8"

body = ParagraphStyle("body", fontName="Helvetica", fontSize=13, leading=19, textColor=INK, spaceAfter=8)
h1 = ParagraphStyle("h1", parent=body, fontName="Helvetica-Bold", fontSize=30, leading=34, alignment=TA_CENTER, spaceAfter=4)
sub = ParagraphStyle("sub", parent=body, fontSize=17, leading=22, alignment=TA_CENTER, textColor=ACCENT, spaceAfter=14)
h2 = ParagraphStyle("h2", parent=body, fontName="Helvetica-Bold", fontSize=20, leading=24, textColor=ACCENT, spaceBefore=12, spaceAfter=8)
step = ParagraphStyle("step", parent=body, fontName="Helvetica-Bold", fontSize=15, leading=20, spaceBefore=6, spaceAfter=6)


def a(url, text=None):
    return f'<a href="{url}" color="{LINK}"><u>{text or url}</u></a>'


def pic(name, max_w, max_h):
    p = IMG / name
    w, h = Image.open(p).size
    k = min(max_w / w, max_h / h)
    im = RLImage(str(p), width=w * k, height=h * k)
    im.hAlign = "LEFT"
    return im


def step_block(n, text, image=None, max_w=6.8 * inch, max_h=3.2 * inch):
    items = [Paragraph(f"{n}. {text}", step)]
    if image:
        items += [pic(image, max_w, max_h), Spacer(1, 10)]
    return KeepTogether(items)


def build():
    doc = SimpleDocTemplate(
        str(OUT), pagesize=letter, leftMargin=0.85 * inch, rightMargin=0.85 * inch,
        topMargin=0.7 * inch, bottomMargin=0.7 * inch,
        title="Tejit's Non Profit Tools: a quick guide for your team", author="",
        subject="How to add and use Tejit's Non Profit Tools",
    )
    s = []
    icon = RLImage(str(ICON), width=0.9 * inch, height=0.9 * inch)
    icon.hAlign = "CENTER"
    s += [icon, Spacer(1, 6), Paragraph("Tejit's Non Profit Tools", h1),
          Paragraph("A quick guide for your team", sub)]
    s += [Paragraph("What this is", h2), Paragraph(
        "Free, open-source helpers for AI assistants that take repetitive work off a nonprofit team's plate. "
        "The first tool is <b>Partner Event Finder</b>. It finds your partners' fundraising events and adds them "
        "to a shared Google Calendar. Each step is explained in plain words.", body)]
    s += [Paragraph("Add it in Claude", h2)]
    c1 = [Paragraph("1. Click your name, then click <b>Settings</b>.", step), pic("step-1.png", 3.4 * inch, 3.9 * inch)]
    c2 = [Paragraph("2. Click <b>Customize</b>.", step), pic("step-2.png", 1.7 * inch, 3.9 * inch)]
    t = Table([[c1, c2]], colWidths=[4.4 * inch, 2.4 * inch])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0)]))
    s += [t, PageBreak()]
    s.append(step_block(3, "Click <b>Plugins</b>, then <b>Add</b>, then <b>Add marketplace</b>.", "step-3.png"))
    s.append(step_block(4, "Click <b>Add from a repository</b>.", "step-4.png"))
    s.append(step_block(5, "Type <b>tejitpabari99/tejit-np-plugin</b>, keep <b>Sync automatically</b> on, then click <b>Sync</b>.", "step-5.png", max_h=2.6 * inch))
    s.append(KeepTogether([
        step_block(6, "If you see an <b>Install</b> button for Tejit's Non Profit Tools, click it."),
        step_block(7, "Start a new chat and say <b>\"Tejit's non profit tools\"</b>."),
    ]))
    s.append(Paragraph(
        "Please add it this way, rather than copying files, so you get updates and fixes automatically.", body))
    s.append(Paragraph("Using a different AI tool? See " + a(INSTALL) + ".", body))

    s.append(KeepTogether([
        Paragraph("Star it on GitHub", h2),
        Paragraph("Please star the project at " + a(REPO) + ". It helps you:", body),
        Paragraph("&bull; Keep track of it and see what is changing.", body),
        Paragraph("&bull; Report problems and share ideas (by filing issues).", body),
        Paragraph("New versions arrive on their own once <b>Sync automatically</b> is on, and the GitHub page shows "
                  "what changed. It is all open source, so all the code can be seen any time. "
                  "You need a free GitHub account to star it. Your AI assistant can help you create one.", body),
    ]))
    s.append(KeepTogether([
        Paragraph("Report a problem or share an idea", h2),
        Paragraph("Once the plugin is added, just say <b>\"share feedback\"</b> (or <b>\"report a problem\"</b>) in a chat. "
                  "Your assistant asks a few questions, shows you the report, then files it after your yes. "
                  "Reports are public, so private details are never included. You do not need a GitHub account; "
                  "it can go by email instead.", body),
    ]))
    doc.build(s)


if __name__ == "__main__":
    build()
    print("wrote", OUT)
