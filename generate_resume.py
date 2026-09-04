import os
import shutil
import base64
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def build_pdf(target_path):
    # Standard Letter: 612 x 792 pt.
    # Left & Right margins: 40pt -> Available width = 532pt
    doc = SimpleDocTemplate(
        target_path,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=38,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    name_style = ParagraphStyle(
        'NameStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=21,
        leading=25,
        alignment=1, # Center
        textColor=colors.HexColor('#111111'),
        spaceAfter=5
    )

    contact_style = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        alignment=1, # Center
        textColor=colors.HexColor('#222222')
    )

    section_header_style = ParagraphStyle(
        'SectionHeaderStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13,
        textColor=colors.HexColor('#111111'),
        spaceBefore=12,
        spaceAfter=2,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor('#1f2937'),
        spaceAfter=2
    )

    skill_label_style = ParagraphStyle(
        'SkillLabelStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor('#111111')
    )

    skill_val_style = ParagraphStyle(
        'SkillValStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor('#1f2937')
    )

    project_title_style = ParagraphStyle(
        'ProjectTitleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#111111'),
        spaceBefore=6,
        spaceAfter=2,
        keepWithNext=True
    )

    tech_stack_style = ParagraphStyle(
        'TechStackStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#374151'),
        spaceAfter=3,
        keepWithNext=True
    )

    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.2,
        leading=13.2,
        leftIndent=15,
        firstLineIndent=-10,
        textColor=colors.HexColor('#1f2937'),
        spaceAfter=2.5
    )

    edu_title_style = ParagraphStyle(
        'EduTitleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.8,
        leading=14,
        textColor=colors.HexColor('#111111')
    )

    edu_sub_style = ParagraphStyle(
        'EduSubStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.2,
        leading=13.5,
        textColor=colors.HexColor('#374151')
    )

    edu_right_style = ParagraphStyle(
        'EduRightStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        alignment=2, # Right
        textColor=colors.HexColor('#111111')
    )

    story = []

    # 1. Header
    story.append(Paragraph("DHARMENDRA KUMAR", name_style))
    contact_text = (
        'Noida, Uttar Pradesh &nbsp;|&nbsp; '
        '+91 7790891845 &nbsp;|&nbsp; '
        '<a href="mailto:dharmendra70003@gmail.com" color="#111111">dharmendra70003@gmail.com</a>'
    )
    story.append(Paragraph(contact_text, contact_style))
    links_text = (
        '<a href="https://linkedin.com/in/dharmendra-kumar-925770222" color="#1d4ed8">LinkedIn</a> &nbsp;|&nbsp; '
        '<a href="https://github.com/dharmendra779089" color="#1d4ed8">GitHub</a> &nbsp;|&nbsp; '
        '<a href="https://dharmendra779089.github.io" color="#1d4ed8">Portfolio</a>'
    )
    story.append(Paragraph(links_text, contact_style))
    story.append(Spacer(1, 8))

    def add_section_header(title):
        story.append(Paragraph(title, section_header_style))
        story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor('#111111'), spaceBefore=2, spaceAfter=6))

    # 2. Summary
    add_section_header("SUMMARY")
    summary_p = (
        "Python Developer with hands-on experience building backend applications and database-driven systems. "
        "Experienced with Python, SQL, PostgreSQL, debugging, authentication, and problem solving."
    )
    story.append(Paragraph(summary_p, body_style))
    story.append(Spacer(1, 3))

    # 3. Technical Skills
    add_section_header("TECHNICAL SKILLS")
    skills_data = [
        [Paragraph("Languages:", skill_label_style), Paragraph("Python, SQL, C++, C", skill_val_style)],
        [Paragraph("Backend &amp; Web:", skill_label_style), Paragraph("Python, CRUD, Authentication, JWT", skill_val_style)],
        [Paragraph("Databases:", skill_label_style), Paragraph("PostgreSQL, JSON", skill_val_style)],
        [Paragraph("Libraries &amp; Tools:", skill_label_style), Paragraph("OpenCV, MediaPipe, PyAutoGUI", skill_val_style)],
        [Paragraph("Developer Tools:", skill_label_style), Paragraph("Git, GitHub, GitHub Actions, VS Code, Jupyter Notebook, Vercel, Render, Cursor, GitHub Copilot", skill_val_style)],
        [Paragraph("Core Skills:", skill_label_style), Paragraph("Problem Solving, Debugging, Database Optimization, Role-Based Access Control", skill_val_style)],
    ]
    skills_table = Table(skills_data, colWidths=[122, 410])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 3))

    # 4. Projects
    add_section_header("PROJECTS")
    
    # Project 1
    p1_title = '<b>Hospital Appointment &amp; Queue Management</b> &nbsp;|&nbsp; <a href="https://haqms-frontend-qk7k.onrender.com/" color="#1d4ed8"><u>Live Demo</u></a>'
    story.append(Paragraph(p1_title, project_title_style))
    story.append(Paragraph("Tech Stack: Node.js, PostgreSQL, Prisma ORM, JWT", tech_stack_style))
    story.append(Paragraph("• &nbsp;Engineered a secure appointment system, utilizing Prisma ORM and JWT to implement role-based access and prevent SQL injection.", bullet_style))
    story.append(Paragraph("• &nbsp;Optimized database performance by resolving N+1 query issues, reducing report-generation calls from O(n × 5) to O(3).", bullet_style))
    story.append(Paragraph("• &nbsp;Ensured data integrity using atomic database transactions and improved scalability via database-level pagination.", bullet_style))
    story.append(Spacer(1, 5))

    # Project 2
    p2_title = '<b>Student Management System</b> &nbsp;|&nbsp; <a href="https://github.com/dharmendra779089" color="#1d4ed8"><u>Live Demo</u></a>'
    story.append(Paragraph(p2_title, project_title_style))
    story.append(Paragraph("Tech Stack: Python, JavaScript, HTML, CSS, JSON, Render", tech_stack_style))
    story.append(Paragraph("• &nbsp;Built a Python web application to manage student records with robust CRUD operations and server-side business logic.", bullet_style))
    story.append(Paragraph("• &nbsp;Implemented lightweight JSON-based data persistence for efficient record retrieval and state updates.", bullet_style))
    story.append(Paragraph("• &nbsp;Developed a responsive HTML/CSS/JS frontend and deployed the full-stack application on Render.", bullet_style))
    story.append(Spacer(1, 3))

    # 5. Achievements & Leadership
    add_section_header("ACHIEVEMENTS &amp; LEADERSHIP")
    story.append(Paragraph(
        "• &nbsp;<b>100 Days of Code — Udemy:</b> Built 100+ Python mini-projects focused on clean code, scripting, problem solving, and data manipulation.",
        bullet_style
    ))
    story.append(Paragraph(
        "• &nbsp;<b>Startup &amp; Incubation Cell — PSIT:</b> Led student engagement initiatives and facilitated technical peer-mentorship programs supporting campus entrepreneurial activities.",
        bullet_style
    ))
    story.append(Spacer(1, 3))

    # 6. Education
    add_section_header("EDUCATION")
    edu_data = [
        [
            Paragraph("<b>Pranveer Singh Institute of Technology (PSIT)</b>", edu_title_style),
            Paragraph("Kanpur, Uttar Pradesh &nbsp;|&nbsp; 2021–2025", edu_right_style)
        ],
        [
            Paragraph("Bachelor of Technology in Computer Science &amp; Engineering", edu_sub_style),
            Paragraph("", edu_right_style)
        ]
    ]
    edu_table = Table(edu_data, colWidths=[310, 222])
    edu_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(edu_table)

    doc.build(story)
    print(f"Generated {target_path}")

if __name__ == '__main__':
    root_pdf = "resume.pdf"
    build_pdf(root_pdf)

    # Copy to inner directory
    inner_dir = os.path.join("dharmendra779089.github.io-main")
    if os.path.exists(inner_dir):
        shutil.copyfile(root_pdf, os.path.join(inner_dir, "resume.pdf"))
        print(f"Copied to {os.path.join(inner_dir, 'resume.pdf')}")
