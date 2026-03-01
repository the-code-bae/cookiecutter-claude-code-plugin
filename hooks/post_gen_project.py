#!/usr/bin/env python3
"""Post-generation hook for cookiecutter-claude-code-plugin."""

import os
import shutil

# Read cookiecutter variables
include_hooks = "{{ cookiecutter.include_hooks }}" == "yes"
include_mcp_config = "{{ cookiecutter.include_mcp_config }}" == "yes"
include_example_skill = "{{ cookiecutter.include_example_skill }}" == "yes"
include_example_agent = "{{ cookiecutter.include_example_agent }}" == "yes"

# Remove hooks directory if not wanted
if not include_hooks:
    shutil.rmtree("hooks", ignore_errors=True)

# Remove .mcp.json if not wanted
if not include_mcp_config:
    try:
        os.remove(".mcp.json")
    except OSError:
        pass

# Remove example skill if not wanted
if not include_example_skill:
    shutil.rmtree(os.path.join("skills", "hello"), ignore_errors=True)
    # Restore .gitkeep if skills dir is now empty
    if not os.listdir("skills"):
        open(os.path.join("skills", ".gitkeep"), "w").close()

# Remove example agent if not wanted
if not include_example_agent:
    try:
        os.remove(os.path.join("agents", "example-agent.md"))
    except OSError:
        pass
    # Restore .gitkeep if agents dir is now empty
    if not os.listdir("agents"):
        open(os.path.join("agents", ".gitkeep"), "w").close()

print(f"\nPlugin '{{ cookiecutter.plugin_name }}' created successfully!")
print("Next steps:")
print("  1. cd {{ cookiecutter.plugin_name }}")
print("  2. Edit .claude-plugin/plugin.json with your plugin metadata")
print("  3. Add skills in skills/, commands in commands/, agents in agents/")
print("  4. Run 'claude' to test your plugin")
