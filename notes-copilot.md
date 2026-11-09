# GitHub Copilot Best Practices

To use GitHub Copilot effectively, it helps to move away from treating it like a standard search engine or a generic chatbot. Instead, view it as a **knowledgeable junior developer sitting next to you**.

By using specific symbols (like `@` and `#`), workspace instruction files, and **Agents**, you can control exactly what context Copilot sees and how much autonomy it has.

---

## 1. Core Mechanics: Getting Context Right

The primary reason Copilot gives vague or irrelevant code is a lack of context. In VS Code, you can steer Copilot's attention using special commands directly in the Copilot Chat panel:

* **Use Scope References (`#`):** Tell Copilot exactly which part of your project to look at.
* `#file:script.py` — Scope its attention strictly to a specific file.
* `#selection` — Focus only on the code you have highlighted in your editor.
* `#codebase` — Search your entire workspace to understand overall dependencies.

* **Use Slash Commands (`/`):** Shortcut commands for frequent actions.
* `/explain` — Breaks down selected code in plain English.
* `/tests` — Generates unit test suites for the active file.
* `/fix` — Proposes a fix for errors in selected code or terminal output.

---

## 2. What are Copilot Agents?

Standard AI assistance is **reactive**: you ask a question, and it gives you a piece of code.

**Agents** (such as `@workspace`, `@terminal`, or GitHub Copilot Agent Mode) are **agentic workflows**. Instead of writing code line-by-line, an agent can:

1. Break down a complex task into multiple steps.
2. Search across multiple files in your project autonomously.
3. Edit files across your repository and propose complete workspace changes.

### The Key Agents in VS Code

| Agent Name | How to invoke | Primary Use Case |
| --- | --- | --- |
| **`@workspace`** | Type `@workspace` in Chat | Ask questions about how different files connect across your whole project. Example: *"@workspace where is the data loading function defined?"* |
| **`@terminal`** | Type `@terminal` in Chat | Get explanations or corrections for terminal commands and error outputs. Example: *"@terminal why did this pytest command fail?"* |
| **Agent Mode / Cloud Agents** | Toggle "Agent Mode" or tag `@github` | Hand off multi-step tasks. Copilot will inspect files, make multi-file edits, and propose a pull request or patch. |

---

## 3. Best Practices for Daily Workflow

1. **Keep `.github/copilot-instructions.md` updated:**
As you established earlier, keeping your library preferences (like `pandas`, `numpy`, `scipy`) in your workspace instructions file keeps Copilot aligned with your exact stack without re-prompting.
2. **Give it explicit roles and boundaries:**
When using `@workspace` or asking for edits, define what **not** to do.

* *Example prompt:* `@workspace Refactor the calculations in stats.py to use NumPy vectorized functions instead of for-loops. Do not alter the function input signatures.`

3. **Iterate in small steps:**
For complex logic or statistical routines, avoid asking the agent to build an entire pipeline from scratch in one go. Ask it to outline the steps first, review the plan, and then tell it to implement function by function.
