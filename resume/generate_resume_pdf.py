from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
    KeepTogether,
    KeepInFrame,
)
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from pathlib import Path

OUTPUT = "Joefel-Mal-ang-Lato-Resume.pdf"
PHOTO = Path("profile-photo.jpg")

# ---------- PAGE ----------
PAGE_W, PAGE_H = A4

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    rightMargin=12 * mm,
    leftMargin=12 * mm,
    topMargin=11 * mm,
    bottomMargin=10 * mm,
)

# ---------- EDITORIAL PALETTE ----------
INK = colors.HexColor("#2f2a25")
MUTED = colors.HexColor("#756d64")
SOFT = colors.HexColor("#a39a90")
PAPER = colors.HexColor("#f5f0e8")
PANEL = colors.HexColor("#ebe3d8")
LINE = colors.HexColor("#cfc4b7")
ACCENT = colors.HexColor("#8b6f57")
ACCENT_DARK = colors.HexColor("#6f5745")
WHITE = colors.white

# ---------- STYLES ----------
styles = getSampleStyleSheet()

name_style = ParagraphStyle(
    "EditorialName",
    parent=styles["Normal"],
    fontName="Times-Bold",
    fontSize=31,
    leading=33,
    textColor=INK,
    spaceAfter=2,
)

role_style = ParagraphStyle(
    "EditorialRole",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=10.8,
    leading=14,
    textColor=ACCENT_DARK,
    spaceAfter=4,
)

contact_style = ParagraphStyle(
    "EditorialContact",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.5,
    leading=11.2,
    textColor=MUTED,
)

section_style = ParagraphStyle(
    "EditorialSection",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=10.2,
    leading=13,
    textColor=INK,
    spaceBefore=0,
    spaceAfter=8,
)

body_style = ParagraphStyle(
    "EditorialBody",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=9.5,
    leading=13.2,
    textColor=INK,
    spaceAfter=7,
)

project_title_style = ParagraphStyle(
    "EditorialProjectTitle",
    parent=body_style,
    fontName="Helvetica-Bold",
    fontSize=10.2,
    leading=12.5,
    textColor=INK,
    spaceAfter=2,
)

project_role_style = ParagraphStyle(
    "EditorialProjectRole",
    parent=body_style,
    fontName="Helvetica",
    fontSize=8.8,
    leading=11.7,
    textColor=SOFT,
    spaceAfter=2,
)

small_style = ParagraphStyle(
    "EditorialSmall",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.7,
    leading=11,
    textColor=MUTED,
)

sidebar_heading_style = ParagraphStyle(
    "EditorialSidebarHeading",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=9.3,
    leading=12,
    textColor=INK,
    spaceAfter=3,
)

sidebar_body_style = ParagraphStyle(
    "EditorialSidebarBody",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.6,
    leading=11,
    textColor=INK,
)

footer_style = ParagraphStyle(
    "EditorialFooter",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=7.0,
    leading=8,
    textColor=SOFT,
)

# ---------- HELPERS ----------
def P(text, style=body_style):
    return Paragraph(text, style)


def editorial_section(title):
    return [
        Paragraph(title.upper(), section_style),
        Table(
            [[""]],
            colWidths=[122 * mm],
            rowHeights=[0.45 * mm],
            style=TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), LINE),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]),
        ),
        Spacer(1, 5),
    ]


def sidebar_section(title):
    return [
        Paragraph(title.upper(), sidebar_heading_style),
        Table(
            [[""]],
            colWidths=[39 * mm],
            rowHeights=[0.4 * mm],
            style=TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), ACCENT),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]),
        ),
        Spacer(1, 5),
    ]


story = []

# ---------- HEADER ----------
photo_flowable = Spacer(1, 1)

if PHOTO.exists():
    try:
        photo = Image(str(PHOTO), width=36 * mm, height=36 * mm)
        photo.hAlign = "RIGHT"
        photo_flowable = photo
    except Exception:
        pass

header_text = [
    Paragraph("JOEFEL MAL-ANG LATO", name_style),
    Paragraph("PROGRAMMER / WEB DEVELOPER", role_style),
    Paragraph(
        "Cebu, Philippines &nbsp;&nbsp;•&nbsp;&nbsp; "
        "09610414212 &nbsp;&nbsp;•&nbsp;&nbsp; "
        "joefellato215@gmail.com",
        contact_style,
    ),
]

header = Table(
    [[header_text, photo_flowable]],
    colWidths=[145 * mm, 30 * mm],
    rowHeights=[38 * mm],
)

header.setStyle(
    TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ])
)

story.append(header)

story.append(
    Table(
        [[""]],
        colWidths=[178 * mm],
        rowHeights=[0.7 * mm],
        style=TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), ACCENT),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]),
    )
)

story.append(Spacer(1, 6))

# ---------- MAIN CONTENT ----------
main = []

# PROFILE
main.extend(editorial_section("Profile"))

profile = (
    "Programmer and Web Developer with a strong interest in building practical, "
    "responsive, and user-focused websites and web applications. Experienced in "
    "developing modern web interfaces, working with programming technologies, and "
    "turning ideas into functional digital solutions. Passionate about continuous "
    "learning, problem-solving, and using technology to create useful products and "
    "improve real-world processes."
)

main.append(P(profile))
main.append(Spacer(1, 4))

# PROJECTS
main.extend(editorial_section("Projects & Practical Experience"))

projects = [
    (
        "Prometheus Market",
        "E-commerce / Full-Stack Web Application",
        "Developed a full-stack e-commerce platform with product management, "
        "inventory intelligence, order management, customer features, analytics, "
        "authentication, and responsive web interfaces using Python, Flask, "
        "JavaScript, SQLite, HTML5, and CSS3.",
    ),
    (
        "Miguel Lechon",
        "Client Project • Business Website / Web Application",
        "Designed and developed a responsive business website for Miguel Lechon, "
        "a local lechon business, as a client project. Built the website to present "
        "products and pricing clearly, improve customer inquiries and ordering, and "
        "provide a mobile-friendly experience across devices. Implemented frontend "
        "and backend functionality using HTML5, CSS3, JavaScript, Python, and Flask.",
    ),
    (
        "Oculus AI",
        "AI Assistant / Python Project",
        "Developed a Python-based AI assistant project focused on voice interaction, "
        "automation, and practical assistant functionality.",
    ),
    (
        "Personal Portfolio",
        "Responsive Web Development",
        "Built a responsive personal portfolio website to showcase projects, "
        "technical skills, and professional work.",
    ),
]

for title, subtitle, description in projects:
    main.extend([
        Paragraph(title, project_title_style),
        Paragraph(subtitle, project_role_style),
        Paragraph(description, body_style),
        Spacer(1, 5),
    ])

# EDUCATION
main.extend(editorial_section("Education"))

main.extend([
    Paragraph(
        "Colegio De San Antonio De Padua (CSAP)",
        project_title_style,
    ),
    Paragraph(
        "Computer Engineering — Undergraduate",
        project_role_style,
    ),
    Paragraph(
        "Degree Not Completed",
        small_style,
    ),
])

# ---------- SIDEBAR ----------
sidebar = []

sidebar.extend(sidebar_section("Contact"))

sidebar.append(
    Paragraph(
        "Cebu, Philippines<br/>"
        "09610414212<br/>"
        "joefellato215@gmail.com",
        sidebar_body_style,
    )
)

sidebar.append(Spacer(1, 10))

sidebar.extend(sidebar_section("Skills"))

skills = [
    "HTML5",
    "CSS3",
    "JavaScript",
    "Python",
    "Flask",
    "Git",
    "GitHub",
    "Responsive Web Design",
    "UI/UX Design",
    "REST APIs",
    "SQLite",
    "Web Application Development",
]

for skill in skills:
    sidebar.append(
        Paragraph(
            "• " + skill,
            sidebar_body_style,
        )
    )

sidebar.append(Spacer(1, 10))

sidebar.extend(sidebar_section("Reference"))

sidebar.append(
    Paragraph(
        "<b>Marlon C. Gacrama</b><br/>"
        "Friend<br/>"
        "maruronu@gmail.com<br/>"
        "(+63) 939-681-0206",
        sidebar_body_style,
    )
)

sidebar.append(Spacer(1, 10))

sidebar.extend(sidebar_section("Education"))

sidebar.append(
    Paragraph(
        "<b>CSAP</b><br/>"
        "Computer Engineering<br/>"
        "Undergraduate<br/>"
        "Degree Not Completed",
        sidebar_body_style,
    )
)

# ---------- TWO COLUMN BODY ----------
sidebar_frame = KeepInFrame(
    39 * mm,
    255 * mm,
    sidebar,
    mode="shrink",
)

main_frame = KeepInFrame(
    122 * mm,
    255 * mm,
    main,
    mode="shrink",
)

body_table = Table(
    [[sidebar_frame, main_frame]],
    colWidths=[43 * mm, 131 * mm],
    hAlign="LEFT",
)

body_table.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), PANEL),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (0, 0), 5 * mm),
        ("RIGHTPADDING", (0, 0), (0, 0), 4 * mm),
        ("TOPPADDING", (0, 0), (0, 0), 6 * mm),
        ("BOTTOMPADDING", (0, 0), (0, 0), 6 * mm),
        ("LEFTPADDING", (1, 0), (1, 0), 7 * mm),
        ("RIGHTPADDING", (1, 0), (1, 0), 0),
        ("TOPPADDING", (1, 0), (1, 0), 1 * mm),
        ("BOTTOMPADDING", (1, 0), (1, 0), 0),
        ("LINEAFTER", (0, 0), (0, 0), 0.5, LINE),
    ])
)

story.append(body_table)

# ---------- FOOTER ----------
story.append(Spacer(1, 5))

footer = Table(
    [[
        Paragraph(
            "PROFESSIONAL RESUME  •  JOEFEL MAL-ANG LATO",
            footer_style,
        )
    ]],
    colWidths=[178 * mm],
)

footer.setStyle(
    TableStyle([
        ("LINEABOVE", (0, 0), (-1, -1), 0.5, LINE),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ])
)

story.append(footer)

# ---------- PAGE BACKGROUND ----------
def draw_background(canvas_obj, doc_obj):
    canvas_obj.saveState()
    canvas_obj.setFillColor(PAPER)
    canvas_obj.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas_obj.restoreState()


doc.build(
    story,
    onFirstPage=draw_background,
)

print("PDF CREATED:", OUTPUT)
print("SIZE:", Path(OUTPUT).stat().st_size, "bytes")
