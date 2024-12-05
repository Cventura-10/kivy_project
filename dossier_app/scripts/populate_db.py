from app import db
from models import Section

sections = [
    Section(
        title="Introduction",
        content="Narration presenting your commitment to transparency and ethics.",
        image_path="images/introduction.jpg"
    ),
    Section(
        title="Professional Profile",
        content="Education and experience details.",
        image_path="images/profile.jpg"
    ),
    Section(
        title="Specific Achievements",
        content="Highlighting your contributions to public management.",
        image_path="images/achievements.jpg"
    ),
    Section(
        title="Value Proposition",
        content="Tailored proposals for different sectors.",
        image_path="images/value_proposition.jpg"
    ),
    Section(
        title="Strategic Plan",
        content="Plan for modernizing internal control systems.",
        image_path="images/strategic_plan.jpg"
    ),
    Section(
        title="References and Recognitions",
        content="List of awards and published articles.",
        image_path="images/references.jpg"
    ),
    Section(
        title="Contact",
        content="How to reach you.",
        image_path="images/contact.jpg"
    ),
]

db.session.add_all(sections)
db.session.commit()
