(function () {
  "use strict";

  const input = document.getElementById("agentic-ai-input");
  const sendButton = document.getElementById("agentic-ai-send");
  const promptButtons = document.querySelectorAll(".agentic-ai-prompt");
  const messages = document.getElementById("agentic-ai-messages");

  if (!input || !sendButton || !messages) {
    console.error("Joefel AI: required elements not found.");
    return;
  }

  const API_URL = "http://127.0.0.1:8787/api/ai/chat";
  const history = [];

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
    messages.appendChild(message);

    messages.scrollTop = messages.scrollHeight;

    return message;
  }

  function setLoading(loading) {
    sendButton.disabled = loading;
    input.disabled = loading;

    promptButtons.forEach(function (button) {
      button.disabled = loading;
    });

    if (loading) {
      sendButton.dataset.originalText = sendButton.textContent;
      sendButton.textContent = "Thinking...";
    } else {
      sendButton.textContent =
        sendButton.dataset.originalText || "Ask";
    }
  }

  async function ask(question) {
    const trimmed = question.trim();

    if (!trimmed || sendButton.disabled) {
      return;
    }

    addMessage(trimmed, "user");

    input.value = "";
    setLoading(true);

    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: trimmed,
          history: history,
        }),
      });

      if (!response.ok) {
        throw new Error(
          "AI backend returned HTTP " + response.status
        );
      }

      const data = await response.json();

      if (!data.ok || !data.response) {
        throw new Error("Invalid AI backend response.");
      }

      const assistantMessage = data.response;

      history.push({
        role: "user",
        content: trimmed,
      });

      history.push({
        role: "assistant",
        content: assistantMessage,
      });

      addMessage(assistantMessage, "assistant");
    } catch (error) {
      console.error("Joefel AI error:", error);

      addMessage(
        "I couldn't connect to the portfolio AI backend right now. Please try again in a moment.",
        "assistant"
      );
    } finally {
      setLoading(false);
      input.focus();
    }
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
