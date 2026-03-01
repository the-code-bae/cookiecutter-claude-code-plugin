# {{ cookiecutter.first_plugin_name }}

{{ cookiecutter.first_plugin_description }}

## Structure

```
{{ cookiecutter.first_plugin_name }}/
├── .claude-plugin/
│   └── plugin.json           # Plugin metadata
├── commands/                  # Slash commands
├── agents/                    # Specialized agents
├── skills/                    # Agent skills
├── hooks/                     # Event handlers
├── .mcp.json                  # External tool configuration
└── README.md                  # This file
```

## Skills

Add skills as `SKILL.md` files in the `skills/` directory.

## Commands

Add slash commands as Markdown files in the `commands/` directory.

## Agents

Add agent definitions in the `agents/` directory.
