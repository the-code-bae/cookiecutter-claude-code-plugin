# cookiecutter-claude-code-plugin

A [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for creating [Claude Code](https://docs.anthropic.com/en/docs/claude-code) plugins.

Quickly scaffold a new Claude Code plugin with the standard directory structure, including skills, agents, commands, hooks, and MCP configuration.

## Usage

### Prerequisites

Install cookiecutter:

```bash
pip install cookiecutter
# or
pipx install cookiecutter
# or
brew install cookiecutter
```

### Create a new plugin

```bash
cookiecutter gh:YOUR_GITHUB_USERNAME/cookiecutter-claude-code-plugin
```

Or from a local clone:

```bash
cookiecutter /path/to/cookiecutter-claude-code-plugin
```

### Template options

| Option | Default | Description |
|---|---|---|
| `plugin_name` | `my-plugin` | Name of your plugin (used as directory name) |
| `plugin_description` | `A Claude Code plugin` | Short description of what your plugin does |
| `plugin_version` | `0.1.0` | Initial version number |
| `author_name` | `Your Name` | Your name |
| `author_github` | `your-github-username` | Your GitHub username |
| `plugin_type` | `domain` | Plugin type: `domain`, `core`, or `experimental` |
| `include_hooks` | `yes` | Include the hooks/ directory for event handlers |
| `include_mcp_config` | `yes` | Include .mcp.json for MCP server configuration |
| `include_example_skill` | `yes` | Include an example skill to get started |
| `include_example_agent` | `yes` | Include an example agent definition |
| `license` | `MIT` | License for the generated plugin |

## Generated structure

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json           # Plugin metadata
├── commands/                  # Slash commands (optional)
│   └── .gitkeep
├── agents/                    # Specialized agents (optional)
│   └── .gitkeep
├── skills/                    # Agent skills (optional)
│   └── .gitkeep
├── hooks/                     # Event handlers (optional)
│   └── .gitkeep
├── .mcp.json                  # External tool configuration (optional)
└── README.md                  # Plugin documentation
```

### What goes where?

- **`skills/`** - SKILL.md files that define reusable capabilities. Skills are invoked by agents or users via `/skill-name`.
- **`commands/`** - Markdown files defining slash commands users can run directly.
- **`agents/`** - Agent definitions (Markdown) for specialized sub-processes with specific tool access.
- **`hooks/`** - Shell scripts that run in response to Claude Code events (e.g., before/after tool calls).
- **`.mcp.json`** - Configuration for external MCP (Model Context Protocol) servers to extend available tools.

## Installing a plugin

To install the generated plugin into Claude Code:

```bash
claude plugin add /path/to/your-plugin
```

Or add it to a project by placing it in the project's `.claude/plugins/` directory.

## License

This template is released under the MIT License.
