# {{ cookiecutter.repo_name }}

{{ cookiecutter.repo_description }}

## Structure

```
{{ cookiecutter.repo_name }}/
├── .claude-plugin/
│   └── marketplace.json          # Marketplace manifest (lists all plugins)
├── .github/
│   └── CODEOWNERS                # Skill ownership and review assignments
├── plugins/
│   ├── {{ cookiecutter.first_plugin_name }}/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json       # Plugin metadata
│   │   ├── commands/              # Slash commands
│   │   ├── agents/                # Specialized agents
│   │   ├── skills/                # Agent skills
│   │   ├── hooks/                 # Event handlers
│   │   ├── .mcp.json              # MCP server configuration
│   │   └── README.md              # Plugin documentation
│   └── {{ cookiecutter.second_plugin_name }}/
│       ├── .claude-plugin/
│       │   └── plugin.json       # Plugin metadata
│       ├── commands/              # Slash commands
│       ├── agents/                # Specialized agents
│       ├── skills/                # Agent skills
│       ├── hooks/                 # Event handlers
│       ├── .mcp.json              # MCP server configuration
│       └── README.md              # Plugin documentation
├── CLAUDE.md                      # Resource registry (single source of truth)
├── README.md
└── service-info.yaml
```

## Getting Started

See [CLAUDE.md](CLAUDE.md) for details on the repository structure and how to add new plugins.

## Author

{{ cookiecutter.author_name }} ([@{{ cookiecutter.author_github }}](https://github.com/{{ cookiecutter.author_github }}))
