# {{ cookiecutter.repo_name }}

{{ cookiecutter.repo_description }}

## Repository Structure

This is a multi-plugin repository. Each plugin lives under `plugins/` and is self-contained with its own `.claude-plugin/plugin.json`.

## Plugins

| Plugin | Type | Description |
|---|---|---|
| [{{ cookiecutter.first_plugin_name }}](plugins/{{ cookiecutter.first_plugin_name }}/) | {{ cookiecutter.first_plugin_type }} | {{ cookiecutter.first_plugin_description }} |
| [{{ cookiecutter.second_plugin_name }}](plugins/{{ cookiecutter.second_plugin_name }}/) | {{ cookiecutter.second_plugin_type }} | {{ cookiecutter.second_plugin_description }} |

## Adding a New Plugin

1. Create a new directory under `plugins/`:
   ```
   plugins/my-new-plugin/
   ├── .claude-plugin/
   │   └── plugin.json
   ├── commands/
   ├── agents/
   ├── skills/
   ├── hooks/
   ├── .mcp.json
   └── README.md
   ```
2. Register it in `.claude-plugin/marketplace.json`
3. Add ownership rules in `.github/CODEOWNERS`
