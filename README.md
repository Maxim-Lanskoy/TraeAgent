# NeuroNaut - Autonomous LLM Agent with MPC

We propose an **autonomous lifelong-learning agent** that uses a private local LLM to explore environments, build skills, and accomplish tasks via Tool-Use. Inspired by Google DeepMind’s *Voyager* agent, our system will maintain an *automatic curriculum*, a **skill library** of reusable code modules, and an *iterative improvement loop*. Voyager “uses LLMs like GPT-4.1 / o3 for lifelong learning” in Minecraft, generating tasks and storing skills as code programs.  Likewise, our agent will continuously generate or receive goals (e.g. win an RPG battle, make character top 1 player, compile an app, create swift executable package program from readme description), reason about them, retrieve relevant past experiences via memory, call tools to act (game commands, code execution), observe feedback, and refine its actions in a loop. Over time the agent acquires new “skills” (code routines or sequences of tool calls), indexes them by embeddings, and composes them for future tasks.

The design focuses on full **local hosting** (no cloud APIs) and compatibility with Apple Silicon (M1/M2/Intel) hardware. We use open-source stacks: e.g. **llama.cpp** for on-device LLM inference, local vector databases for retrieval, and MCP (Model Context Protocol) to wrap tools. Using *llama.cpp* (with quantized models) lets us run Llama‐style LLMs on Mac CPUs/GPUs.  For larger scale or higher throughput, we can deploy Petals, or **Paddler** – an open-source, stateful load balancer for llama.cpp servers – to distribute LLM instances across machines. Telethon-based **MCP servers** expose environment tools. For example, \[chigwell/telegram-mcp] provides a “full-featured Telegram integration” so the LLM can programmatically send messages, press buttons, and manage chats. Similarly, an MCP *code-executor* or *sandbox* module (see ModelContextProtocol code-executor references) will let the agent compile and run Swift/Python code securely, observe the output, and iterate.

Our architecture has several key components:

* **LLM Core**: A local LLM (e.g. Llama-2) running via llama.cpp (CPU/GPU) on Mac (M1/M2). We may use adapters like LM Studio or Hugging Face’s `transformers` with PyTorch MPS when appropriate. For scale, a Petals or Paddler server pool will balance queries to multiple Llama instances.

* **Memory / RAG Store**: A persistent memory system combining vector search (RAG) and knowledge graphs. We plan to use a local vector database (e.g. Chroma or Qdrant) to store embeddings of *experiences*, *skill code*, and *documents*. The agent will embed its textual logs or code outputs and query this store to recall relevant past lessons. (Optionally, we can include the MCP *Memory* server, a knowledge-graph store for facts.) Retrieval-augmented generation will let the LLM answer queries with relevant context from its memory.

* **Skill Library**: Inspired by Voyager, each learned skill is saved as an executable module or function, indexed by an embedding of its description. For example, “attack-goblin” might be a Python/Swift function in our codebase. When planning a new goal, the agent retrieves similar skills by querying the library with the current task embedding. This enables compositionality: building complex behaviors by chaining simpler skills.

* **Tool Interface (MCP Servers)**: We implement a suite of MCP servers to expose tools. Key examples include:

  * **Telegram-MCP** (via Telethon) for the RPG use-case. This lets the LLM read messages, get chat state, and send button presses in the Telegram RPG game.
  * **Code Execution**: A Python-based MCP server (e.g. code-executor or code-sandbox) to compile/run code. Given a Swift package or Python script, the agent can invoke it, capture stdout/stderr, and decide next steps.
  * **Filesystem/Terminal**: MCP modules (such as the “Filesystem” or “iTerm” examples) to read/write files and run CLI commands. This is needed to let the agent edit code files, inspect logs, etc.
  * **Other Utilities**: Optionally, an MCP *fetch* server for web queries, or custom scripts for any specific tool.

All components run locally or on a private LAN of devices. For Mac-based hosting, all chosen tools support macOS (Python, Telethon, Docker, etc.) and Apple Silicon where possible. By using MCP and local services, the LLM agent has “secure, controlled access” to everything it needs.

## Tech Stack

* **Language Models**: *llama.cpp* on Apple Silicon (M1/M2), capable of running LLaMA-2/Meta‘s models locally. We may use quantized models (e.g. Q4/K) to fit in RAM. For development, tools like LM Studio can simplify testing on Mac.
* **Load Balancing**: Petals or *Paddler* (Rust) to manage multiple llama.cpp instances across machines. This allows us to utilize all available Macs and boards via TCP.
* **LLM Orchestration**: Python scripts (using `asyncio`), or frameworks like LangChain / LlamaIndex for chaining LLM calls. All LLM queries are handled in-house, no cloud API keys.
* **Telegram API**: *Telethon* (Python) running an MCP server (e.g. \[telegram-mcp]). This provides wrappers for messaging, inline buttons, etc.
* **Code Execution**: Python Docker or local subprocess, plus MCP *code-executor/sandbox* modules. The agent can compile and run Swift packages via shell commands, capturing output.
* **Memory / Vector DB**: An open-source vector store like **Chroma** (Apache 2.0) or **Qdrant**, running locally. We use sentence-transformers or LLM to embed text. (Alternatively, a simple SQLite+FAISS could be used for smaller scale.) The memory stores scene descriptions, conversation logs, skill code, etc.
* **Persistence**: Filesystem or SQLite to store logs, skill code files, agent state. Possibly use the MCP *Filesystem* server for safe file operations.
* **Hardware**: Primarily two Macs (M2 Max with 96GB, Intel i7 32GB) for heavy inference and storage. Raspberry Pis/Jetson are low-power and optional for trivial tasks. Networking via local LAN.
* **Development Tools**: Git for version control, Docker for containerized services. Swift toolchain installed on Mac for the Swift-app tasks.

All libraries are open-source or local; for instance, the \[Paddler repo] is Apache-2.0 , the Telegram-MCP is Apache-2.0, Chroma is Apache-2.0, etc. This ensures full control and privacy.

### Language-Model Choice

| Priority | Requirement                                  | Best Fit                                                 | Notes                                                                              |
| -------- | -------------------------------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **1**    | **Reliable JSON / function-calling for MCP** | **🏆 Mistral Small 3 (v3.2) 24 B**                       | Emits OpenAI-style `function_call` objects out-of-the-box – zero adapter code.     |
| **2**    | **Fast local inference** (both Macs)         | **🏆 Mistral Small 3**                                   | \~150 tok/s on 24-core M2 Max @ Q4\_K\_M; fits comfortably in 32 GB RAM (≈ 11 GB). |
| **3**    | **Long-horizon reasoning**                   | Mixtral 8×22 B (65 K ctx) <br>Qwen 3-30B-A3B (131 K ctx) | Use on demand when raw reasoning depth or huge context outweigh latency.           |
| **4**    | **Native vision support**                    | **🏆 Mistral Small 3 (Vision variant)**                  | Built-in image encoder; ideal for OCRing loot screens or UI screenshots.           |
| **5**    | **Permissive licence for commercial use**    | **🏆 Mistral Small 3** (Apache 2.0)                      | Same for Mixtral 8×22 B; Qwen 3 also Apache 2.0.                                   |

## Architecture Proposal

Our system is modular, with clear interfaces:

* **Agent Loop** (controller): A master process that drives the agent’s decision cycle. It queries the LLM to plan or act, invokes tools via MCP, updates memory, and loops. (This can be a Python `asyncio` loop or a LangChain/Autogen style orchestrator.)
* **LLM Module**: Receives prompts from the Agent Loop, adding in-memory context/RAG results. Generates actions, plan steps, or code.
* **Memory Manager**: On each turn, relevant context (e.g. recent game events, code outputs) is embedded and stored. The Agent Loop performs retrieval by embedding the current query and fetching similar memory entries.
* **Skill Library**: When the agent solves a task (e.g. a sequence of game moves or a code snippet), that solution is saved as a new “skill” (script or function). The library is searchable via embeddings.
* **MCP Servers (Tools)**:

  * *Telegram Server*: Connects to a Telegram account and game chat. Tools include `get_messages()`, `send_message()`, `press_button()`, etc.. The agent uses these to interact with the RPG game.
  * *Code Executor*: Runs code; e.g. given a Swift source, compiles and executes it. Returns success/failure and output. For safety, runs in a Docker container or restricted environment.
  * *Filesystem/Terminal*: Enables reading/writing code files and running arbitrary shell commands. Important for editing code, reading logs, etc. (Use MCP *iTerm* for terminal control if needed.)
* **Logging & Monitoring**: All actions, prompts, and feedback are logged to disk. This also feeds into memory. A dashboard or simple printouts track which tasks were attempted.

Data Flow: The agent queries the LLM with a prompt describing current goal and context. The LLM outputs an action (or code). The Agent then calls the corresponding MCP tool (e.g. Telethon or code-run). The result and logs are fed back into the prompt context for the next LLM call. This loop continues until a sub-goal is solved or a timeout. After completing a task, the LLM optionally performs a “self-verification” to ensure task success (akin to Voyager’s approach) before marking a skill as learned.

By leveraging **MCP and Telethon**, we effectively turn the Telegram game and code environment into an interactive playground for the LLM. The agent “sees” the game state via chat messages and button metadata, and it “moves” by sending Telegram API calls (pressing inline buttons). Over time, it will learn which sequences of moves lead to wins (storing them as skills). In the Swift-app scenario, the agent will parse a README spec, generate code files, compile and test, then iterate until the app behaves correctly.

In summary, **the architecture** is a central Python (or TypeScript) controller that ties together: LLM inference, a vector memory store, and multiple MCP tool services. This approach follows the MCP design of giving LLMs “secure, controlled access to tools and data sources”.

## Open-Source Components & References

We rely on proven open-source projects:

* **llama.cpp** (by Georgi Gerganov): Pure C++ LLM inference engine, now widely used for local LLMs on CPUs/GPUs.
* Perals or **Paddler** (by distantmagic): A load-balancer for llama.cpp servers.
* **Telethon-MCP (chigwell/telegram-mcp)**: Python MCP server exposing Telegram APIs.
* **MCP Code Executor**: (e.g. \[modelcontextprotocol/servers] `code-executor` or `code-sandbox-mcp`) – allows LLMs to run Python/Swift code securely.
* **Vector DB**: *Chroma* or *Qdrant* – open-source vector databases for RAG.
* **LangChain / LlamaIndex**: Python libraries for LLM agent orchestration and retrieval (used locally, no external calls).
* **LM Studio / Auto-GPT** (optional): Local GUI or frameworks to test prompts. These can use our Llama engine as a back-end.
* **Filesystem/Terminal MCP**: e.g. *iTerm2-MCP* or *Filesystem* (reference in MCP repo) for file and command access.
* **Docker**: Containerize services like Telethon-MCP, vector DB, etc. Cross-platform support (runs on macOS).

For Mac-based silicon, all tools run natively or in Docker. For instance, llama.cpp has Apple Silicon binaries, Telethon is pure Python, Chroma has an M1-compatible wheel. We avoid any cloud or remote-API solution. This ensures privacy and up-time (the agent runs *endlessly* once set up).

## Development Plan (Roadmap)

We outline a step-by-step plan. Each item is a task/checkpoint that can be checked off as done:

* [ ] **Setup LLM Inference**: Install and test llama.cpp on Mac. Load a small model (e.g. LLaMA-2 7B) and confirm inference works on CPU/GPU. Configure `--mmap`/`--gpu` flags.
* [ ] **Scale with Petals/Paddler**: Deploy multiple llama.cpp instances (one per machine). Set up Petals/Paddler load-balancer. Verify you can send a request to the Paddler endpoint and get an LLM response.
* [ ] **MCP Server: Telegram**: Deploy the Telethon-based MCP server (e.g. using the **telegram-mcp** repo). Authenticate it with a Telegram account. Test basic actions: `get_chats()`, `send_message()`, `press_button()`. Use this to connect to the RPG game chat.
* [ ] **MCP Server: Code Execution**: Install or build an MCP *code-executor* (Docker or local). Ensure the agent can send a Python snippet (or shell command) and get back stdout. Test with a simple script.
* [ ] **MCP Server: Filesystem/Terminal**: Set up an MCP *Filesystem* server (maybe via the reference MCP repo) to read/write files. Optionally set up an *iTerm2* integration if needed.
* [ ] **Memory & RAG**: Deploy a local vector DB (e.g. Chroma) and write code to embed and store texts (using e.g. sentence-transformers). Test by inserting some dummy sentences and querying them. Integrate this with the agent process.
* [ ] **Skill Library Prototype**: Create a data structure (e.g. JSON/SQLite) to store “skill” entries: { name, description, code, embedding }. Implement a simple function to embed text and index skills via the vector DB.
* [ ] **Agent Loop (Core)**: Write the main agent controller. In each loop: take a *prompt template* + current context (goal + memories + previous logs), query LLM (via llama.cpp/Paddler), parse the response into an action (e.g. JSON or structured plan), and invoke the corresponding MCP tool.
* [ ] **Telegram RPG Interaction**: Use the agent loop to play the RPG. For example, start with a prompt “You are in a dungeon at level 1. What action to take?” The LLM says e.g. “/press\_button: Hunt”. The agent calls Telethon to press “Hunt”. Retrieve the response message as new context. Loop. Store each move/observation as memory.
* [ ] **Reward/Goal & Verification**: Define success criteria (e.g. defeat boss, reach level X). Implement a checkpoint where the LLM or a separate function checks if the goal is reached (maybe by scanning chat for keywords). Use this for self-verification as in Voyager.
* [ ] **Swift Code Task**: Move to the second scenario. Provide the agent with a README spec and an empty Swift project. The agent should: read the README (via Filesystem MCP), brainstorm code structure (LLM), write Swift code files (via Filesystem MCP), compile/run (via Code-Executor MCP). Use feedback (compiler errors, program output) to refine code iteratively.
* [ ] **Long-term Memory RAG**: Ensure that logs from both use-cases feed into the memory DB. The agent should retrieve past similar situations (e.g. previous game levels or past code bugs) when facing new challenges.
* [ ] **Skill Consolidation**: After solving tasks, prompt the LLM to summarize the sequence into a “skill” (pseudocode or function). Save this for future use.
* [ ] **Safety & Monitoring**: Add checks to prevent infinite loops or destructive actions. For example, if no progress in N steps, abort. Log all decisions.
* [ ] **Multi-Session Progress**: Use a persistent “Progress” file (like this README) so that each new coding session can resume from the last checked-off task. The agent should mark tasks done in the checklist above as it completes them.

Each step should be documented and tested. The goal is that after completing this roadmap, we have a *fully autonomous agent* capable of **adapting to new tools**: if we provide a new MCP server (e.g. a web browser or database), the same framework lets the agent learn to use it.

## Progress Tracking

To facilitate multi-session development, this README includes a checklist of tasks above. The coding agent (Codex/Claude) should use this to track which items are done. In each new chat or run, the agent can load this document, see which boxes are checked, and continue with the next unchecked task.  We **do not** need to re-explain completed concepts; instead the agent should pick up the **next** item on the roadmap. The final system will be *modular* and should “teach itself” to use new tools via this loop.

**By the end**, we will have an extensible agent framework: a loop that takes a goal, uses LLM planning with RAG memory, calls MCP tools for actions, learns code skills, and adapts over time. All on local hardware, scalable via Paddler, and designed so a coding agent can implement it step-by-step from this README.

**Sources:** We draw inspiration and methodology from the VOYAGER paper and blog, the official Model Context Protocol references, and open-source tools (llama.cpp, Petals/Paddler, Telethon MCP, Chroma, etc.) to ensure a robust, local solution.
