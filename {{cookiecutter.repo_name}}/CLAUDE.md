# {{ cookiecutter.repo_name }}

{{ cookiecutter.repo_description }}

## Repository Structure

This is a multi-plugin repository. Each plugin lives under `plugins/` and is self-contained with its own `.claude-plugin/plugin.json`.

## Plugins

| Plugin | Type | Description |
|---|---|---|
| [{{ cookiecutter.first_plugin_name }}](plugins/{{ cookiecutter.first_plugin_name }}/) | {{ cookiecutter.first_plugin_type }} | {{ cookiecutter.first_plugin_description }} |
| [{{ cookiecutter.second_plugin_name }}](plugins/{{ cookiecutter.second_plugin_name }}/) | {{ cookiecutter.second_plugin_type }} | {{ cookiecutter.second_plugin_description }} |

## Installation

There are two ways to install plugins from this repository into Claude Code.

### Option 1: Via Claude Code CLI

First, register this repository as a marketplace:

```
claude plugin marketplace add https://github.com/{{ cookiecutter.author_github }}/{{ cookiecutter.repo_name }}.git
```

Then install the plugins you need:

```
claude plugin install {{ cookiecutter.first_plugin_name }}
claude plugin install {{ cookiecutter.second_plugin_name }}
```

Start (or restart) Claude Code from your terminal to pick up the changes.

### Option 2: Via settings.json

Add the following to your project's `.claude/settings.json` or your global `~/.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "{{ cookiecutter.repo_name }}": {
      "source": {
        "source": "git",
        "url": "https://github.com/{{ cookiecutter.author_github }}/{{ cookiecutter.repo_name }}.git"
      }
    }
  },
  "enabledPlugins": {
    "{{ cookiecutter.first_plugin_name }}@{{ cookiecutter.repo_name }}": true,
    "{{ cookiecutter.second_plugin_name }}@{{ cookiecutter.repo_name }}": true
  }
}
```

Restart Claude Code for the settings to take effect.

## How to Use Installed Plugins

Once installed, all skills and agents from your plugins are available inside Claude Code. You can trigger them in two ways:

**Conversationally** — describe what you want and Claude will match it to the right skill automatically.

**Directly** — use the slash command syntax with the plugin namespace:

```
/<plugin-name>:<skill-name>
```

For example:

```
/{{ cookiecutter.first_plugin_name }}:hello
/{{ cookiecutter.second_plugin_name }}:greet
```

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
