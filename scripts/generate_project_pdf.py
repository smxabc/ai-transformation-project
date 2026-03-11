from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "ai-readiness-blueprint-portfolio.pdf"


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="TitleBlock",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
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
            fontName="Helvetica-Bold",
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
            fontName="Helvetica",
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
            fontName="Helvetica",
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
    story.append(Paragraph("AI Readiness Blueprint for German Enterprises", styles["TitleBlock"]))
    story.append(
        Paragraph(
            "Portfolio dossier for applications, interviews, and GitHub presentation",
            styles["Meta"],
        )
    )
    story.append(
        Paragraph(
            "This document describes a repository that shows how enterprise digitalization and AI enablement can be structured for German mid-sized firms and large corporations.",
            styles["Body"],
        )
    )

    section(
        "Project Summary",
        [
            Paragraph(
                "The project is a public blueprint for assessing enterprise readiness for digitalization and AI. It combines management framing with practical delivery artifacts such as maturity models, assessment templates, governance checklists, and transformation roadmaps.",
                styles["Body"],
            )
        ],
        styles,
        story,
    )

    section(
        "What The Repository Covers",
        [
            bullet("Current-state analysis of IT landscape, processes, delivery model, and data foundations", styles),
            bullet("Digitalization and AI maturity model across strategy, operations, governance, and enablement", styles),
            bullet("Target operating model for AI-ready organizations", styles),
            bullet("Use-case portfolio and prioritization logic based on business value, feasibility, and risk", styles),
            bullet("Governance framework for security, compliance, and responsible AI implementation", styles),
            bullet("KPI-driven decision model and transformation roadmap for 12 to 24 months", styles),
        ],
        styles,
        story,
    )

    section(
        "Strategic Thesis",
        [
            Paragraph(
                "AI readiness is not a standalone technology initiative. It is an enterprise capability program. Sustainable AI implementation requires process quality, data ownership, integration standards, operating governance, and measurable delivery outcomes.",
                styles["Body"],
            )
        ],
        styles,
        story,
    )

    table_data = [
        ["Capability", "What the project demonstrates"],
        ["Strategy", "Translation of broad transformation goals into a coherent enterprise model"],
        ["Architecture", "Assessment and target-state logic for systems, data, and integrations"],
        ["Execution", "Roadmaps, scorecards, and program steering artifacts"],
        ["Governance", "Responsible AI, security, compliance, and risk framing"],
        ["Communication", "Public GitHub presentation suitable for portfolio use"],
    ]
    table = Table(table_data, colWidths=[45 * mm, 120 * mm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#12344d")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
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
    section("What This Shows About My Work", [table], styles, story)

    section(
        "Example Use Cases Covered By The Blueprint",
        [
            bullet("AI readiness model for a German industrial mid-sized company", styles),
            bullet("Governed AI scaling model for a corporate or group structure", styles),
            bullet("Project and portfolio redesign toward measurable outcome steering", styles),
            bullet("Tooling and operating choices tied to business capabilities and constraints", styles),
        ],
        styles,
        story,
    )

    section(
        "Case Study Snapshot",
        [
            bullet("Mid-sized company scenario: ERP-centered environment with Excel-heavy coordination, fragmented knowledge, and the need for fast value realization", styles),
            bullet("Corporate scenario: multi-business-unit environment with heterogeneous systems, stronger governance constraints, and the need for scalable standards", styles),
            bullet("Both variants are translated into concrete assessment, governance, and rollout logic inside the repository", styles),
        ],
        styles,
        story,
    )

    section(
        "Why The Project Is Relevant",
        [
            Paragraph(
                "The repository is built around a practical market reality: many companies want to use AI, but lack the operational foundation to do so responsibly. The project addresses this gap by linking digitalization, architecture, governance, and management decisions in one system.",
                styles["Body"],
            )
        ],
        styles,
        story,
    )

    section(
        "Resume Summary",
        [
            Paragraph(
                "Developed a public strategy repository that explains how to assess enterprise IT landscapes, define AI-ready operating models, prioritize use cases, establish governance, redesign project management, and steer transformation through KPI-based decisions.",
                styles["Body"],
            )
        ],
        styles,
        story,
    )

    section(
        "Repository Reference",
        [
            Paragraph(
                "Main repository files include README, executive summary, maturity model, assessment framework, operating model, use-case portfolio, governance guidance, KPI model, roadmap, templates, and case studies.",
                styles["Body"],
            )
        ],
        styles,
        story,
    )

    section(
        "Suggested Interview Framing",
        [
            bullet("How would I assess an enterprise before suggesting AI initiatives?", styles),
            bullet("How do I connect management priorities with implementation decisions?", styles),
            bullet("What governance and KPI logic is needed before scaling AI?", styles),
        ],
        styles,
        story,
    )

    return story


def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(colors.HexColor("#5b6b79"))
    canvas.drawRightString(195 * mm, 12 * mm, f"Page {doc.page}")
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
