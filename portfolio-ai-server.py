from flask import Flask, request, jsonify
import re

app = Flask(__name__)


KNOWLEDGE = {
    "identity": {
        "name": "Joefel Mal-ang Lato",
        "role": "Programmer / Web Developer",
        "summary": (
            "Joefel Mal-ang Lato is a Programmer / Web Developer focused on "
            "building practical, responsive, and modern digital experiences."
        ),
    },

    "philosophy": (
        "Joefel's development philosophy is Build, Learn, Improve. "
        "He focuses on turning ideas into working products, learning through "
        "real development, and continuously refining what already works."
    ),

    "approach": (
        "Joefel prefers practical solutions over unnecessary complexity. "
        "His approach combines development, design, problem-solving, testing, "
        "and continuous improvement."
    ),

    "skills": [
        "HTML5",
        "CSS3",
        "JavaScript",
        "Tailwind CSS",
        "Python",
        "Flask",
        "SQLite",
        "Git",
        "GitHub",
        "Figma",
        "Responsive Web Design",
        "UI/UX",
        "REST APIs",
        "E-commerce development",
        "AI and automation",
    ],

    "focus": [
        "Responsive Design",
        "UI Development",
        "E-Commerce",
        "AI & Automation",
        "Full-Stack Web Development",
        "Business Websites",
    ],

    "services": [
        "Business websites",
        "E-commerce platforms",
        "Full-stack web applications",
        "Responsive web interfaces",
        "AI-powered tools",
        "Automation workflows",
    ],

    "process": [
        ("Understand", "Clarify the goal, users, requirements, and what the project needs to accomplish."),
        ("Plan", "Break the idea into practical features, structure, and a clear development path."),
        ("Build", "Develop the interface, backend, database, integrations, and core functionality."),
        ("Improve", "Test, refine, fix issues, and continue improving the product over time."),
    ],

    "projects": {
        "prometheus": {
            "name": "Prometheus Market",
            "aliases": [
                "prometheus",
                "prometheus market",
                "ecommerce",
                "e-commerce",
                "online store",
                "online shop",
                "store",
            ],
            "type": "Full-stack e-commerce platform",
            "status": "In Development",
            "description": (
                "A full-stack e-commerce platform with product management, "
                "shopping cart, checkout, customer accounts, inventory, "
                "order management, analytics, and business intelligence."
            ),
            "technologies": [
                "HTML",
                "JavaScript",
                "Flask",
                "SQLite",
                "Tailwind CSS",
            ],
        },

        "miguel": {
            "name": "Miguel Lechon",
            "aliases": [
                "miguel",
                "miguel lechon",
                "lechon",
                "lechon website",
            ],
            "type": "Client project / business website",
            "status": "Live & maintained",
            "description": (
                "A mobile-first business website for a local lechon brand, "
                "focused on product presentation, pricing, customer inquiries, "
                "ordering, and responsive experiences across devices."
            ),
            "technologies": [
                "HTML5",
                "CSS",
                "JavaScript",
                "Flask",
                "Responsive Design",
            ],
        },

        "oculus": {
            "name": "Oculus AI",
            "aliases": [
                "oculus",
                "oculus ai",
                "ai assistant",
                "voice assistant",
                "assistant",
            ],
            "type": "Personal AI assistant",
            "status": "In Development",
            "description": (
                "A personal AI assistant project exploring voice interaction, "
                "automation, intelligent tools, and web-based control through "
                "Python and Flask."
            ),
            "technologies": [
                "Python",
                "Flask",
                "JavaScript",
                "AI",
                "Automation",
            ],
        },
    },

    "contact": {
        "email": "joefellato215@gmail.com",
        "message": (
            "Joefel is open to meaningful projects and opportunities. "
            "Visitors can contact him through the portfolio contact section "
            "or by email."
        ),
    },
}


def normalize(text):
    return re.sub(r"\s+", " ", (text or "").strip().lower())


def find_project(query):
    q = normalize(query)

    for project in KNOWLEDGE["projects"].values():
        for alias in project["aliases"]:
            if alias in q:
                return project

    return None


def contains_any(text, terms):
    return any(term in text for term in terms)


def project_response(project):
    technologies = ", ".join(project["technologies"])

    return (
        f'{project["name"]} is a {project["type"]}. '
        f'{project["description"]} '
        f'Project status: {project["status"]}. '
        f'Key technologies include {technologies}.'
    )


def answer_skills():
    return (
        "Joefel works with "
        + ", ".join(KNOWLEDGE["skills"])
        + ". His main development focus includes responsive design, "
          "UI development, e-commerce, AI and automation, and full-stack "
          "web development."
    )


def answer_services():
    return (
        "Joefel can build "
        + ", ".join(KNOWLEDGE["services"])
        + "."
    )


def answer_process():
    parts = []

    for number, (name, description) in enumerate(KNOWLEDGE["process"], 1):
        parts.append(f"{number}. {name}: {description}")

    return "Joefel's development process is:\n" + "\n".join(parts)


def agent(question, history=None):
    q = normalize(question)

    if not q:
        return {
            "message": "Ask me something about Joefel, his projects, skills, or services.",
            "intent": "empty",
            "tool": None,
        }

    project = find_project(q)

    if project:
        return {
            "message": project_response(project),
            "intent": "project_lookup",
            "tool": "project_lookup",
        }

    if contains_any(q, [
        "philosophy",
        "mindset",
        "approach",
        "developer mindset",
        "why does he build",
        "why do you build",
    ]):
        return {
            "message": (
                f'{KNOWLEDGE["philosophy"]} '
                f'{KNOWLEDGE["approach"]}'
            ),
            "intent": "philosophy_lookup",
            "tool": "philosophy_lookup",
        }

    if contains_any(q, [
        "who is joefel",
        "who is joefel lato",
        "about joefel",
        "tell me about joefel",
        "introduce joefel",
        "what does joefel do",
        "what is joefel",
    ]):
        return {
            "message": (
                f'{KNOWLEDGE["identity"]["name"]} is a '
                f'{KNOWLEDGE["identity"]["role"]}. '
                f'{KNOWLEDGE["identity"]["summary"]}'
            ),
            "intent": "identity",
            "tool": "identity_lookup",
        }

    if contains_any(q, [
        "skill",
        "skills",
        "technology",
        "technologies",
        "tech stack",
        "programming language",
        "what can he code",
        "what can joefel code",
    ]):
        return {
            "message": answer_skills(),
            "intent": "skills_lookup",
            "tool": "skills_lookup",
        }

    if contains_any(q, [
        "service",
        "services",
        "what can he build",
        "what can joefel build",
        "what do you build",
        "what does he build",
        "website",
        "web application",
    ]):
        return {
            "message": answer_services(),
            "intent": "services_lookup",
            "tool": "services_lookup",
        }

    if contains_any(q, [
        "process",
        "how does he work",
        "how do you work",
        "how does joefel work",
        "workflow",
        "development process",
        "how do you build",
    ]):
        return {
            "message": answer_process(),
            "intent": "process_lookup",
            "tool": "process_lookup",
        }

    if contains_any(q, [
        "contact",
        "email",
        "hire",
        "reach joefel",
        "contact joefel",
        "work with joefel",
        "opportunity",
    ]):
        return {
            "message": (
                f'You can contact Joefel at '
                f'{KNOWLEDGE["contact"]["email"]}. '
                f'{KNOWLEDGE["contact"]["message"]}'
            ),
            "intent": "contact",
            "tool": "contact_lookup",
        }

    if contains_any(q, [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening",
    ]):
        return {
            "message": (
                "Hi! I'm Joefel AI. I can tell you about Joefel, "
                "his projects, skills, services, development process, "
                "and technical work."
            ),
            "intent": "greeting",
            "tool": "conversation",
        }

    return {
        "message": (
            "I can help you explore Joefel's portfolio. "
            "Try asking about Prometheus Market, Miguel Lechon, "
            "Oculus AI, his skills, services, development process, "
            "or how to contact him."
        ),
        "intent": "fallback",
        "tool": None,
    }


@app.after_request
def cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    return response


@app.route("/api/ai/health", methods=["GET"])
def health():
    return jsonify({
        "ok": True,
        "agent": "Joefel AI",
        "version": "2.1-phase2",
        "status": "ready",
    })


@app.route("/api/ai/chat", methods=["OPTIONS"])
def chat_options():
    return ("", 204)


@app.route("/api/ai/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}

    message = data.get("message", "")
    history = data.get("history", [])

    if not isinstance(message, str):
        return jsonify({
            "ok": False,
            "error": "message must be a string",
        }), 400

    if not isinstance(history, list):
        history = []

    if len(message) > 2000:
        return jsonify({
            "ok": False,
            "error": "message is too long",
        }), 400

    result = agent(message, history)

    return jsonify({
        "ok": True,
        "agent": "Joefel AI",
        "version": "2.1-phase2",
        "response": result["message"],
        "intent": result["intent"],
        "tool": result["tool"],
    })


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=8787,
        debug=False,
    )
