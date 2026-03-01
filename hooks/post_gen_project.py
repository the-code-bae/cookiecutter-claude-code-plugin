#!/usr/bin/env python3
"""Post-generation hook for cookiecutter-claude-code-plugin."""

import os
import shutil

# Read cookiecutter variables
include_hooks = "{{ cookiecutter.include_hooks }}" == "yes"
include_mcp_config = "{{ cookiecutter.include_mcp_config }}" == "yes"
include_example_skill = "{{ cookiecutter.include_example_skill }}" == "yes"
include_example_agent = "{{ cookiecutter.include_example_agent }}" == "yes"
first_plugin = "{{ cookiecutter.first_plugin_name }}"
second_plugin = "{{ cookiecutter.second_plugin_name }}"

plugin_dirs = [
    os.path.join("plugins", first_plugin),
    os.path.join("plugins", second_plugin),
]

for plugin_dir in plugin_dirs:
    # Remove hooks directory if not wanted
    if not include_hooks:
        shutil.rmtree(os.path.join(plugin_dir, "hooks"), ignore_errors=True)

    # Remove .mcp.json if not wanted
    if not include_mcp_config:
        try:
            os.remove(os.path.join(plugin_dir, ".mcp.json"))
        except OSError:
            pass

    # Remove example skill if not wanted
    if not include_example_skill:
        shutil.rmtree(os.path.join(plugin_dir, "skills", "hello"), ignore_errors=True)
        shutil.rmtree(os.path.join(plugin_dir, "skills", "greet"), ignore_errors=True)
        skills_dir = os.path.join(plugin_dir, "skills")
        if os.path.isdir(skills_dir) and not os.listdir(skills_dir):
            open(os.path.join(skills_dir, ".gitkeep"), "w").close()

    # Remove example agent if not wanted
    if not include_example_agent:
        try:
            os.remove(os.path.join(plugin_dir, "agents", "example-agent.md"))
        except OSError:
            pass
        agents_dir = os.path.join(plugin_dir, "agents")
        if os.path.isdir(agents_dir) and not os.listdir(agents_dir):
            open(os.path.join(agents_dir, ".gitkeep"), "w").close()

print(f"\nRepository '{{ cookiecutter.repo_name }}' created successfully!")
print(f"Plugins created:")
print(f"  - plugins/{first_plugin}/")
print(f"  - plugins/{second_plugin}/")
print("\nNext steps:")
print(f"  1. cd {{ cookiecutter.repo_name }}")
print(f"  2. git init && git add -A && git commit -m 'Initial commit'")
print(f"  3. Add more plugins by creating new directories under plugins/")
print(f"  4. Register new plugins in .claude-plugin/marketplace.json")
