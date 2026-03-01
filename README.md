# cookiecutter-claude-code-plugin

A [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for creating a **multi-plugin** [Claude Code](https://docs.anthropic.com/en/docs/claude-code) repository.

Quickly scaffold a repository that can hold multiple Claude Code plugins, each with their own skills, agents, commands, hooks, and MCP configuration.

## What is Cookiecutter?

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) is a command-line tool that creates projects from templates. You answer a few prompts (project name, author, etc.) and it generates a ready-to-use folder structure with all the boilerplate filled in for you. No need to manually create files or copy-paste from examples.

## Quick Start

### Step 1: Install Cookiecutter

You need Python installed on your machine. If you're not sure, open a terminal and run:

```bash
python3 --version
```

If you see a version number (e.g. `Python 3.11.5`), you're good. If not, [install Python](https://www.python.org/downloads/) first.

Then install cookiecutter. Pick whichever method works for your setup:

**Using pip (comes with Python):**

```bash
pip install cookiecutter
```

**Using pipx (recommended — installs in an isolated environment):**

```bash
pip install pipx
pipx install cookiecutter
```

**Using Homebrew (macOS):**

```bash
brew install cookiecutter
```

To verify it installed correctly:

```bash
cookiecutter --version
```

### Step 2: Generate Your Plugin Repository

Run this command from the directory where you want the project created:

```bash
cookiecutter gh:YOUR_GITHUB_USERNAME/cookiecutter-claude-code-plugin
```

Cookiecutter will prompt you with a series of questions. Press **Enter** to accept the default (shown in brackets), or type your own value:

```
repo_name [my-claude-plugins]: my-awesome-plugins
repo_description [A collection of Claude Code plugins]: My custom Claude Code plugins
author_name [Your Name]: Jane Smith
author_github [your-github-username]: janesmith
first_plugin_name [core]: utilities
first_plugin_description [Core plugin - cross-cutting skills and utilities]: Shared helpers
Select first_plugin_type:
1 - domain
2 - core
3 - experimental
Choose from 1, 2, 3 [1]: 1
second_plugin_name [experimental]: sandbox
...
```

Once you've answered all the prompts, cookiecutter creates the full project folder for you.

### Step 3: Initialise Your New Repository

```bash
cd my-awesome-plugins
git init
git add -A
git commit -m "Initial commit"
```

### Step 4: Push to GitHub (optional)

Create a new repository on [GitHub](https://github.com/new), then:

```bash
git remote add origin https://github.com/your-username/my-awesome-plugins.git
git branch -M main
git push -u origin main
```

### Step 5: Start Building

You're ready to go! Open the project and start adding skills, commands, and agents to your plugins. See [What goes where?](#what-goes-where) below for guidance.

## Running From a Local Clone

If you've cloned this template repo locally instead of using it from GitHub, you can generate a project from the local copy:

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/cookiecutter-claude-code-plugin.git
cookiecutter ./cookiecutter-claude-code-plugin
```

This works exactly the same way — you'll get the same prompts and the same output.

## Template Options

When you run cookiecutter, you'll be prompted for these values:

| Option | Default | Description |
|---|---|---|
| `repo_name` | `my-claude-plugins` | Name of the repository |
| `repo_description` | `A collection of Claude Code plugins` | Repository description |
| `author_name` | `Your Name` | Your name |
| `author_github` | `your-github-username` | Your GitHub username |
| `first_plugin_name` | `core` | Name of the first plugin to scaffold |
| `first_plugin_description` | `Core plugin - cross-cutting skills and utilities` | Description of the first plugin |
| `first_plugin_type` | `domain` | Plugin type: `domain`, `core`, or `experimental` |
| `second_plugin_name` | `experimental` | Name of the second plugin to scaffold |
| `second_plugin_description` | `Experimental plugin - new skills in development` | Description of the second plugin |
| `second_plugin_type` | `experimental` | Plugin type: `domain`, `core`, or `experimental` |
| `include_hooks` | `yes` | Include hooks/ in each plugin |
| `include_mcp_config` | `yes` | Include .mcp.json in each plugin |
| `include_example_skill` | `yes` | Include an example skill to get started |
| `include_example_agent` | `yes` | Include an example agent definition |
| `license` | `MIT` | License for the repository |

## Generated Structure

After running cookiecutter, you'll get a folder that looks like this:

```
my-claude-plugins/
├── .claude-plugin/
│   └── marketplace.json          # Marketplace manifest (lists all plugins)
├── .github/
│   └── CODEOWNERS                # Skill ownership and review assignments
├── plugins/
│   ├── utilities/                # First plugin (name is configurable)
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json       # Plugin metadata
│   │   ├── commands/              # Slash commands
│   │   ├── agents/                # Specialized agents
│   │   ├── skills/                # Agent skills
│   │   ├── hooks/                 # Event handlers
│   │   ├── .mcp.json              # MCP server configuration
│   │   └── README.md              # Plugin documentation
│   └── sandbox/                   # Second plugin (name is configurable)
│       ├── .claude-plugin/
│       │   └── plugin.json
│       ├── commands/
│       ├── agents/
│       ├── skills/
│       ├── hooks/
│       ├── .mcp.json
│       └── README.md
├── CLAUDE.md                      # Resource registry (single source of truth)
├── README.md
└── service-info.yaml
```

## Adding More Plugins

After generating the repo, add more plugins by creating new directories under `plugins/`:

```
plugins/
├── utilities/      # Shared skills and helpers
├── terraform/      # Domain plugin - infrastructure as code
├── code-review/    # Domain plugin - PR review workflows
└── sandbox/        # Experimental - new skills in development
```

Each plugin follows the same internal structure:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json       # Plugin metadata
├── commands/              # Slash commands
├── agents/                # Specialized agents
├── skills/                # Agent skills
├── hooks/                 # Event handlers
├── .mcp.json              # External tool configuration
└── README.md              # Plugin documentation
```

Register each new plugin in `.claude-plugin/marketplace.json`.

## What Goes Where?

| Folder | What to put here | Example |
|---|---|---|
| `skills/` | SKILL.md files that define reusable capabilities. Users invoke them with `/skill-name`. | `skills/hello/SKILL.md` |
| `commands/` | Markdown files defining slash commands users can run directly. | `commands/deploy.md` |
| `agents/` | Agent definitions for specialized sub-processes with specific tool access. | `agents/code-reviewer.md` |
| `hooks/` | Shell scripts that run in response to Claude Code events (e.g., before/after tool calls). | `hooks/pre-commit.sh` |
| `.mcp.json` | Configuration for external MCP (Model Context Protocol) servers to extend available tools. | — |

## Installing Plugins

To install a plugin from the generated repo into Claude Code:

```bash
claude plugin add /path/to/my-claude-plugins/plugins/utilities
```

Or add plugins to a project by placing them in the project's `.claude/plugins/` directory.

## Troubleshooting

**`cookiecutter: command not found`**
Cookiecutter isn't installed or isn't on your PATH. Try `pip install cookiecutter` again, or if you used pipx, make sure `~/.local/bin` is in your PATH.

**`git: command not found`**
You need Git installed. Download it from [git-scm.com](https://git-scm.com/downloads).

**Permission errors with pip**
Try `pip install --user cookiecutter` or use pipx/brew instead.

**Want to re-run with different options?**
Delete the generated folder and run `cookiecutter` again. Or use `cookiecutter --overwrite-if-exists` to regenerate in place.

## License

This template is released under the MIT License.
