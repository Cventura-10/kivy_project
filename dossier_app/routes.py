from flask import Blueprint, render_template, request, jsonify
from dossier_app.models import Section, Reaction, db

main = Blueprint("main", __name__)

@main.route("/")
def index():
    sections = Section.query.all()
    return render_template("index.html", sections=sections)

@main.route("/section/<int:id>")
def section(id):
    section = Section.query.get_or_404(id)
    section.views += 1
    db.session.commit()
    return render_template("section.html", section=section)

@main.route("/section/<int:id>/like", methods=["POST"])
def like_section(id):
    reaction = Reaction(section_id=id, reaction_type="like")
    db.session.add(reaction)
    db.session.commit()
    likes = Reaction.query.filter_by(section_id=id, reaction_type="like").count()
    return jsonify({"likes": likes})

@main.route("/section/<int:id>/accept", methods=["POST"])
def accept_section(id):
    reaction = Reaction(section_id=id, reaction_type="accept")
    db.session.add(reaction)
    db.session.commit()
    acceptances = Reaction.query.filter_by(section_id=id, reaction_type="accept").count()
    return jsonify({"acceptances": acceptances})
