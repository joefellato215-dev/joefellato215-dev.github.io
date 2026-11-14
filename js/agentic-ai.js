(function () {
  "use strict";

  const input = document.getElementById("agentic-ai-input");
  const sendButton = document.getElementById("agentic-ai-send");
  const promptButtons = document.querySelectorAll(".agentic-ai-prompt");

  if (!input || !sendButton) {
    return;
  }

  const chatArea = input.closest(".space-y-4");

  const knowledge = {
    identity:
      "Joefel Mal-ang Lato is a Programmer / Web Developer focused on building practical, responsive, and modern digital experiences.",

    skills:
      "Joefel works with HTML5, CSS3, JavaScript, Tailwind CSS, Python, Flask, SQLite, Git, GitHub, and Figma. His development focus includes responsive design, UI development, e-commerce, AI, and automation.",

    prometheus:
      "Prometheus Market is Joefel's full-stack e-commerce platform. It includes product management, shopping cart, checkout, customer accounts, inventory, order management, analytics, and business intelligence. The project uses HTML, JavaScript, Flask, SQLite, and Tailwind CSS.",

    miguel:
      "Miguel Lechon is a real client project. Joefel built a mobile-first business website for a local lechon brand, focused on clear product presentation, pricing, customer inquiries, ordering, and responsive experiences across devices. The project uses HTML5, CSS, JavaScript, Flask, and responsive design.",

    oculus:
      "Oculus AI is Joefel's personal AI assistant project. It explores voice interaction, automation, intelligent tools, and web-based control using Python and Flask.",

    services:
      "Joefel builds business websites, e-commerce platforms, full-stack web applications, and AI-powered tools and automation workflows.",

    approach:
      "Joefel's development approach is Build, Learn, Improve. He focuses on understanding the goal, planning practical features, building the solution, then testing, refining, and improving it.",

    experience:
      "Joefel's portfolio demonstrates practical development experience across business websites, e-commerce platforms, full-stack applications, and AI-focused projects.",

    contact:
      "Joefel is open to meaningful projects and opportunities. Visitors can contact him through the contact section of the portfolio or email joefellato215@gmail.com."
  };

  function normalize(text) {
    return text
      .toLowerCase()
      .replace(/[^\w\s]/g, " ")
      .replace(/\s+/g, " ")
      .trim();
  }

  function getResponse(question) {
    const q = normalize(question);

    if (!q) {
      return "Ask me something about Joefel's projects, skills, experience, or what he can build.";
    }

    if (
      q.includes("who is joefel") ||
      q.includes("about joefel") ||
      q.includes("who are you")
    ) {
      return knowledge.identity;
    }

    if (
      q.includes("skill") ||
      q.includes("technology") ||
      q.includes("technologies") ||
      q.includes("tech stack") ||
      q.includes("what does he use")
    ) {
      return knowledge.skills;
    }

    if (
      q.includes("prometheus") ||
      q.includes("e commerce") ||
      q.includes("ecommerce") ||
      q.includes("online store")
    ) {
      return knowledge.prometheus;
    }

    if (
      q.includes("miguel") ||
      q.includes("lechon") ||
      q.includes("client project")
    ) {
      return knowledge.miguel;
    }

    if (
      q.includes("oculus") ||
      q.includes("ai assistant") ||
      q.includes("voice assistant")
    ) {
      return knowledge.oculus;
    }

    if (
      q.includes("build") ||
      q.includes("services") ||
      q.includes("what can he make") ||
      q.includes("what can joefel make")
    ) {
      return knowledge.services;
    }

    if (
      q.includes("approach") ||
      q.includes("process") ||
      q.includes("how does he work") ||
      q.includes("build learn improve")
    ) {
      return knowledge.approach;
    }

    if (
      q.includes("experience") ||
      q.includes("background") ||
      q.includes("projects has he built")
    ) {
      return knowledge.experience;
    }

    if (
      q.includes("contact") ||
      q.includes("email") ||
      q.includes("hire") ||
      q.includes("work with joefel")
    ) {
      return knowledge.contact;
    }

    return "I can tell you about Joefel's projects, technologies, skills, development approach, experience, or what he can build. Try asking about Prometheus Market, Miguel Lechon, Oculus AI, or his technologies.";
  }

  function addMessage(text, type) {
    const message = document.createElement("div");

    if (type === "user") {
      message.className =
        "ml-auto max-w-[85%] rounded-2xl rounded-tr-md bg-indigo-600 px-4 py-3 text-sm leading-6 text-white shadow-sm";
    } else {
      message.className =
        "max-w-[85%] rounded-2xl rounded-tl-md bg-white px-4 py-3 text-sm leading-6 text-gray-700 shadow-sm dark:bg-white/5 dark:text-gray-300";
    }

    message.textContent = text;

    const inputContainer = input.closest(".rounded-2xl.border-2");

    if (inputContainer) {
      chatArea.insertBefore(message, inputContainer);
    } else {
      chatArea.appendChild(message);
    }
  }

  function ask(question) {
    const trimmed = question.trim();

    if (!trimmed) {
      return;
    }

    addMessage(trimmed, "user");

    input.value = "";

    window.setTimeout(function () {
      addMessage(getResponse(trimmed), "assistant");
    }, 250);
  }

  sendButton.addEventListener("click", function () {
    ask(input.value);
  });

  input.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
      event.preventDefault();
      ask(input.value);
    }
  });

  promptButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      const prompt = button.getAttribute("data-prompt") || "";
      input.value = prompt;
      ask(prompt);
    });
  });
})();
