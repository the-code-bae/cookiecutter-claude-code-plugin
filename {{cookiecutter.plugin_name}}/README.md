# {{ cookiecutter.plugin_name }}

{{ cookiecutter.plugin_description }}

## Structure

```
{{ cookiecutter.plugin_name }}/
├── .claude-plugin/
│   └── plugin.json          # Plugin metadata
├── commands/                 # Slash commands (optional)
├── agents/                   # Specialized agents (optional)
├── skills/                   # Agent skills (optional)
├── hooks/                    # Event handlers (optional)
├── .mcp.json                 # External tool configuration (optional)
└── README.md                 # Plugin documentation
```

## Getting Started

### Commands

Add slash commands as Markdown files in the `commands/` directory. Each file defines a command that users can invoke with `/<command-name>`.

### Skills

Add skills as `SKILL.md` files in the `skills/` directory. Skills provide specialized capabilities that agents can use.

### Agents

Add agent configurations in the `agents/` directory. Agents are specialized sub-processes with specific tools and capabilities.

### Hooks

Add event handler scripts in the `hooks/` directory. Hooks execute shell commands in response to events like tool calls.

### MCP Servers

Configure external tool integrations in `.mcp.json` to extend your plugin with MCP (Model Context Protocol) servers.

## Author

{{ cookiecutter.author_name }} ([@{{ cookiecutter.author_github }}](https://github.com/{{ cookiecutter.author_github }}))
