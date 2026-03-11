from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "ki-implementierung-deutsche-unternehmen.pdf"
GITHUB_URL = "https://github.com/smxabc/ai-transformation-project"


def build_styles():
    font_dir = Path("/System/Library/Fonts/Supplemental")
    regular_font = font_dir / "Arial.ttf"
    bold_font = font_dir / "Arial Bold.ttf"
    pdfmetrics.registerFont(TTFont("DocSans", str(regular_font)))
    pdfmetrics.registerFont(TTFont("DocSans-Bold", str(bold_font)))
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="TitleBlock",
            parent=styles["Title"],
            fontName="DocSans-Bold",
            fontSize=22,
            leading=28,
            textColor=colors.HexColor("#12344d"),
            alignment=TA_LEFT,
            spaceAfter=10,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SectionHeading",
            parent=styles["Heading2"],
            fontName="DocSans-Bold",
            fontSize=13,
            leading=16,
            textColor=colors.HexColor("#12344d"),
            spaceBefore=8,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Body",
            parent=styles["BodyText"],
            fontName="DocSans",
            fontSize=10.5,
            leading=15,
            textColor=colors.HexColor("#1d2733"),
            spaceAfter=5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Meta",
            parent=styles["BodyText"],
            fontName="DocSans",
            fontSize=9,
            leading=12,
            textColor=colors.HexColor("#5b6b79"),
            spaceAfter=10,
        )
    )
    return styles


def bullet(text, styles):
    return Paragraph(f"- {text}", styles["Body"])


def section(title, paragraphs, styles, story):
    story.append(Paragraph(title, styles["SectionHeading"]))
    for item in paragraphs:
        story.append(item)
    story.append(Spacer(1, 3))


def build_story(styles):
    story = []
    story.append(Paragraph("Blueprint zur KI-Implementierung in deutschen Unternehmen", styles["TitleBlock"]))
    story.append(
        Paragraph(
            "Strategisches Projektdossier",
            styles["Meta"],
        )
    )
    story.append(
        Paragraph(
            "Dieses Dokument beschreibt ein Repository, das zeigt, wie Digitalisierung und KI-Einführung in deutschen Mittelständlern und Konzernen strukturiert aufgebaut werden können.",
            styles["Body"],
        )
    )

    section(
        "Projektüberblick",
        [
            Paragraph(
                "Das Projekt ist ein Blueprint für die Analyse und den Aufbau von KI-Readiness in Unternehmen. Es verbindet Management-Perspektive mit konkreten Umsetzungsartefakten wie Reifegradmodellen, Assessment-Templates, Governance-Checklisten und Transformations-Roadmaps.",
                styles["Body"],
            )
        ],
        styles,
        story,
    )

    section(
        "Inhalte des Repositorys",
        [
            bullet("Ist-Analyse von IT-Landschaft, Prozessen, Delivery-Modell und Datengrundlagen", styles),
            bullet("Reifegradmodell für Digitalisierung und KI über Strategie, Operations, Governance und Enablement", styles),
            bullet("Ziel-Operating-Model für KI-fähige Organisationen", styles),
            bullet("Use-Case-Portfolio und Priorisierungslogik anhand von Business Value, Machbarkeit und Risiko", styles),
            bullet("Governance-Framework für Security, Compliance und verantwortungsvolle KI-Implementierung", styles),
            bullet("KPI-basiertes Entscheidungsmodell und Transformations-Roadmap für 12 bis 24 Monate", styles),
        ],
        styles,
        story,
    )

    section(
        "Strategische These",
        [
            Paragraph(
                "KI-Readiness ist keine isolierte Technologieinitiative. Sie ist ein unternehmensweites Fähigkeitsprogramm. Nachhaltige KI-Implementierung braucht Prozessqualität, Datenverantwortung, Integrationsstandards, Betriebs-Governance und messbare Umsetzungsergebnisse.",
                styles["Body"],
            )
        ],
        styles,
        story,
    )

    table_data = [
        ["Baustein", "Beitrag des Projekts"],
        ["Strategie", "Übersetzung breiter Transformationsziele in ein konsistentes Unternehmensmodell"],
        ["Architektur", "Logik für Ist-Analyse und Zielbild von Systemen, Daten und Integrationen"],
        ["Umsetzung", "Roadmaps, Scorecards und Artefakte für die Programmsteuerung"],
        ["Governance", "Einordnung von verantwortungsvoller KI, Security, Compliance und Risiko"],
        ["Steuerung", "Verknüpfung von Management-Entscheidungen mit messbaren Ergebnissen"],
    ]
    table = Table(table_data, colWidths=[45 * mm, 120 * mm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#12344d")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "DocSans-Bold"),
                ("FONTNAME", (0, 1), (-1, -1), "DocSans"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("LEADING", (0, 0), (-1, -1), 12),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#c7d2db")),
                ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#f7f9fb")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    section("Projektlogik im Überblick", [table], styles, story)

    section(
        "Beispielhafte Handlungsfelder",
        [
            bullet("KI-Readiness-Modell für einen deutschen industriellen Mittelständler", styles),
            bullet("Governed-AI-Skalierungsmodell fuer Konzern- oder Gruppenstrukturen", styles),
            bullet("Neuausrichtung von Projekt- und Portfoliosteuerung in Richtung messbarer Ergebnisse", styles),
            bullet("Tool- und Betriebsentscheidungen entlang von Geschäftsfähigkeiten und Restriktionen", styles),
        ],
        styles,
        story,
    )

    section(
        "Fallstudien-Snapshot",
        [
            bullet("Mittelstands-Szenario: ERP-zentrierte Umgebung mit Excel-lastiger Koordination, fragmentiertem Wissen und Bedarf an schneller Wertrealisierung", styles),
            bullet("Konzern-Szenario: Multi-Business-Unit-Umfeld mit heterogenen Systemen, höheren Governance-Anforderungen und Bedarf an skalierbaren Standards", styles),
            bullet("Beide Varianten werden im Repository in konkrete Assessment-, Governance- und Rollout-Logik übersetzt", styles),
        ],
        styles,
        story,
    )

    section(
        "Warum das Projekt relevant ist",
        [
            Paragraph(
                "Das Repository adressiert eine konkrete Marktrealität: Viele Unternehmen wollen KI nutzen, haben aber noch nicht die operative Grundlage für verantwortungsvolle Skalierung. Das Projekt verbindet deshalb Digitalisierung, Architektur, Governance und Management-Entscheidungen in einem gemeinsamen Modell.",
                styles["Body"],
            )
        ],
        styles,
        story,
    )

    section(
        "Kernaussage",
        [
            Paragraph(
                "Der Blueprint beschreibt, wie Unternehmenslandschaften analysiert, KI-fähige Operating Models definiert, Use Cases priorisiert, Governance etabliert und Transformationen über KPI-basierte Entscheidungen gesteuert werden können.",
                styles["Body"],
            )
        ],
        styles,
        story,
    )

    section(
        "Repository-Referenz",
        [
            Paragraph(
                "Zu den zentralen Inhalten gehören README, Executive Summary, Reifegradmodell, Assessment-Framework, Operating Model, Use-Case-Portfolio, Governance-Leitfaden, KPI-Modell, Roadmap, Templates und Fallstudien.",
                styles["Body"],
            )
        ],
        styles,
        story,
    )

    section(
        "Leitfragen für die Anwendung",
        [
            bullet("Wie sollte ein Unternehmen bewertet werden, bevor KI-Initiativen gestartet werden?", styles),
            bullet("Wie lassen sich Management-Prioritäten mit Umsetzungsentscheidungen verbinden?", styles),
            bullet("Welche Governance- und KPI-Logik ist vor der Skalierung von KI notwendig?", styles),
        ],
        styles,
        story,
    )

    return story


def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("DocSans", 9)
    canvas.setFillColor(colors.HexColor("#5b6b79"))
    canvas.drawString(18 * mm, 16 * mm, GITHUB_URL)
    canvas.drawRightString(195 * mm, 12 * mm, f"Seite {doc.page}")
    canvas.linkURL(GITHUB_URL, (18 * mm, 14.5 * mm, 120 * mm, 18.5 * mm), relative=0)
    canvas.restoreState()


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    styles = build_styles()
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
    )
    story = build_story(styles)
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(OUTPUT)


if __name__ == "__main__":
    main()
