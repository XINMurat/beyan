# Beyan v2.0 Agentic Framework 🚀

Beyan is a modular, content-aware agentic framework designed for deep repository analysis, technology discovery, and automated refactoring. It combines a systematic multi-phase analysis protocol with a semi-autonomous agentic loop.

## 🌟 Key Features

- **🔍 Intelligent Discovery**: Content-aware fingerprinting to detect over 20+ technologies (Python, Node, Flutter, Go, etc.).
- **🧩 Modular Architecture**: Context-efficient loading of analysis modules based on project tags.
- **🤖 Semi-Autonomous Agent**: An interactive "Full Flow" mode (Mode 3) that can Analyze -> Plan -> Code -> Test -> Commit.
- **📊 Smart Token Management**: Automatic "pruning" of low-priority modules to fit within LLM context windows.
- **🌍 Multi-language Support**: Full support for Turkish and English reports and prompts.

## 🛠️ Quick Start

### Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your environment variables:
   ```bash
   cp .env.example .env
   # Add your OPENAI_API_KEY or ANTHROPIC_API_KEY
   ```

### Basic Usage
Run the analyzer on the current project:
```bash
python cli/analyzer.py --target . --mode 1 --lang tr
```

## 📖 Operational Modes

1. **Mode 1 (Analyze Only)**: Generates a comprehensive technical report without making changes.
2. **Mode 2 (Analyze + Plan)**: Generates a report and a detailed implementation/sprint plan.
3. **Mode 3 (Full Flow)**: An interactive agentic loop that can automatically fix identified issues with human-in-the-loop checkpoints.

## 📂 Project Structure

- `cli/`: Command-line interface entry points.
- `core_prompts/`: Base and Orchestrator prompts for the LLM.
- `modules/`: Specialized analysis modules (Security, Performance, UI/UX, etc.).
- `tests/`: Comprehensive unit and integration tests.
- `MANIFEST.yaml`: Central configuration for module loading and system rules.

## ⚖️ License
MIT License. See [LICENSE](LICENSE) for details.
