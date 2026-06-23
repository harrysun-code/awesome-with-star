# WezTerm

[![GitHub stars](https://img.shields.io/github/stars/michaelbrusegard/awesome-wezterm?style=flat)](https://github.com/michaelbrusegard/awesome-wezterm/stargazers)

<!-- lint ignore awesome-git-repo-age -->

# Awesome WezTerm [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

<img src="https://raw.githubusercontent.com/wez/wezterm/main/assets/icon/wezterm-icon.svg" align="right" width="144" />

> Collections of awesome WezTerm plugins. [Plugin Guide](https://github.com/wezterm/wezterm/blob/main/docs/config/plugins.md) [![GitHub stars](https://img.shields.io/github/stars/wezterm/wezterm/blob/main/docs/config/plugins.md?style=flat)](https://github.com/wezterm/wezterm/blob/main/docs/config/plugins.md/stargazers). Found something cool? Please [contribute](CONTRIBUTING.md)!

[WezTerm](https://wezfurlong.org/wezterm/) is a powerful cross-platform terminal emulator and multiplexer written by [@wez](https://github.com/wez) [![GitHub stars](https://img.shields.io/github/stars/wez?style=flat)](https://github.com/wez/stargazers) and implemented in [Rust](https://www.rust-lang.org).

To enhance your WezTerm configuration experience:

- [DrKJeff16/wezterm-types](https://github.com/DrKJeff16/wezterm-types) [![GitHub stars](https://img.shields.io/github/stars/DrKJeff16/wezterm-types?style=flat)](https://github.com/DrKJeff16/wezterm-types/stargazers) - WezTerm type annotations that can be added as a completion source in your editor to provide code assistance when working with WezTerm's Lua API. Includes community plugins support.

## Contents

- [AI](#ai)
- [Keybinding](#keybinding)
- [Media](#media)
- [Neovim](#neovim)
- [Panes](#panes)
- [Session](#session)
- [Tab bar](#tab-bar)
- [Themes](#themes)
- [Utility](#utility)

## AI

- [Michal1993r/ai-helper.wezterm](https://github.com/Michal1993r/ai-helper.wezterm/tree/master) [![GitHub stars](https://img.shields.io/github/stars/Michal1993r/ai-helper.wezterm/tree/master?style=flat)](https://github.com/Michal1993r/ai-helper.wezterm/tree/master/stargazers) - Ask AI for CLI help with LM Studio or Google Gemini.
- [dimao/ai-commander.wezterm](https://github.com/dimao/ai-commander.wezterm) [![GitHub stars](https://img.shields.io/github/stars/dimao/ai-commander.wezterm?style=flat)](https://github.com/dimao/ai-commander.wezterm/stargazers) - Generate and select bash commands based on natural language prompts.
- [EdenGibson/wezterm-quota-limit](https://github.com/EdenGibson/wezterm-quota-limit) [![GitHub stars](https://img.shields.io/github/stars/EdenGibson/wezterm-quota-limit?style=flat)](https://github.com/EdenGibson/wezterm-quota-limit/stargazers) - Shows Claude API usage quota in the status bar with color-coded thresholds and automatic token refresh.
- [Eric162/wezterm-agent-deck](https://github.com/Eric162/wezterm-agent-deck) [![GitHub stars](https://img.shields.io/github/stars/Eric162/wezterm-agent-deck?style=flat)](https://github.com/Eric162/wezterm-agent-deck/stargazers) - Monitors AI coding agents, shows status dots in tabs and notifications when agents need attention.
- [M-Marbouh/agent-quota.wezterm](https://github.com/M-Marbouh/agent-quota.wezterm) [![GitHub stars](https://img.shields.io/github/stars/M-Marbouh/agent-quota.wezterm?style=flat)](https://github.com/M-Marbouh/agent-quota.wezterm/stargazers) - Shows Claude and Codex quota usage in the status bar with reset countdowns, process-aware states, and shared caching.

## Keybinding

- [MLFlexer/modal.wezterm](https://github.com/MLFlexer/modal.wezterm) [![GitHub stars](https://img.shields.io/github/stars/MLFlexer/modal.wezterm?style=flat)](https://github.com/MLFlexer/modal.wezterm/stargazers) - Predefined Vim-like modal keybindings with a good looking UI.
- [sravioli/chord.wz](https://github.com/sravioli/chord.wz) [![GitHub stars](https://img.shields.io/github/stars/sravioli/chord.wz?style=flat)](https://github.com/sravioli/chord.wz/stargazers) - Vim-style key notation, modal key tables, and hint bars.
- [sei40kr/wez-pain-control](https://github.com/sei40kr/wez-pain-control?tab=readme-ov-file) [![GitHub stars](https://img.shields.io/github/stars/sei40kr/wez-pain-control?tab=readme-ov-file?style=flat)](https://github.com/sei40kr/wez-pain-control?tab=readme-ov-file/stargazers) - Pane control keybindings like tmux-pain-control.
- [sei40kr/wez-tmux](https://github.com/sei40kr/wez-tmux) [![GitHub stars](https://img.shields.io/github/stars/sei40kr/wez-tmux?style=flat)](https://github.com/sei40kr/wez-tmux/stargazers) - Ported tmux keybindings.
- [selectnull/pinned-tabs.wezterm](https://github.com/selectnull/pinned-tabs.wezterm) [![GitHub stars](https://img.shields.io/github/stars/selectnull/pinned-tabs.wezterm?style=flat)](https://github.com/selectnull/pinned-tabs.wezterm/stargazers) - Lets you assign a key binding to a specific tab.
- [abidibo/wezterm-cmdpicker](https://github.com/abidibo/wezterm-cmdpicker) [![GitHub stars](https://img.shields.io/github/stars/abidibo/wezterm-cmdpicker?style=flat)](https://github.com/abidibo/wezterm-cmdpicker/stargazers) - Add a command-palette-style fuzzy picker for keybindings. Press a trigger key to search and execute any keybinding — user-defined, config, or WezTerm defaults.
- [annie444/sync-panes.wez](https://github.com/annie444/sync-panes.wez) [![GitHub stars](https://img.shields.io/github/stars/annie444/sync-panes.wez?style=flat)](https://github.com/annie444/sync-panes.wez/stargazers) - Mirrors your keystrokes to every pane in the active tab — the equivalent of tmux's `synchronize-panes`.

## Media

- [xarvex/presentation.wez](https://github.com/xarvex/presentation.wez) [![GitHub stars](https://img.shields.io/github/stars/xarvex/presentation.wez?style=flat)](https://github.com/xarvex/presentation.wez/stargazers) - Rather simple presentation mode toggle.

## Neovim

- [mrjones2014/smart-splits.nvim](https://github.com/mrjones2014/smart-splits.nvim) [![GitHub stars](https://img.shields.io/github/stars/mrjones2014/smart-splits.nvim?style=flat)](https://github.com/mrjones2014/smart-splits.nvim/stargazers) - Provides an addon for seamless pane navigation between Neovim and the WezTerm MUX.
- [winter-again/wezterm-config.nvim](https://github.com/winter-again/wezterm-config.nvim) [![GitHub stars](https://img.shields.io/github/stars/winter-again/wezterm-config.nvim?style=flat)](https://github.com/winter-again/wezterm-config.nvim/stargazers) - Interact with the WezTerm configuration directly from Neovim.

## Panes

- [ChrisGVE/pivot_panes.wezterm](https://github.com/ChrisGVE/pivot_panes.wezterm) [![GitHub stars](https://img.shields.io/github/stars/ChrisGVE/pivot_panes.wezterm?style=flat)](https://github.com/ChrisGVE/pivot_panes.wezterm/stargazers) - Toggle pane orientation between horizontal and vertical splits.
- [bad-noodles/stack.wez](https://github.com/bad-noodles/stack.wez) [![GitHub stars](https://img.shields.io/github/stars/bad-noodles/stack.wez?style=flat)](https://github.com/bad-noodles/stack.wez/stargazers) - Stacked pane mode, work with multiple panes but see only one at a time.

## Session

- [DavidRR-F/quick_domains.wezterm](https://github.com/DavidRR-F/quick_domains.wezterm) [![GitHub stars](https://img.shields.io/github/stars/DavidRR-F/quick_domains.wezterm?style=flat)](https://github.com/DavidRR-F/quick_domains.wezterm/stargazers) - Faster way to search and attach to (SSH) domains.
- [isseii10/workspace-picker.wezterm](https://github.com/isseii10/workspace-picker.wezterm) [![GitHub stars](https://img.shields.io/github/stars/isseii10/workspace-picker.wezterm?style=flat)](https://github.com/isseii10/workspace-picker.wezterm/stargazers) - Workspace switcher with `zoxide` integration.
- [JuanraCM/wsinit.wezterm](https://github.com/JuanraCM/wsinit.wezterm) [![GitHub stars](https://img.shields.io/github/stars/JuanraCM/wsinit.wezterm?style=flat)](https://github.com/JuanraCM/wsinit.wezterm/stargazers) - A simple and flexible way to manage and initialize workspace configurations.
- [mikkasendke/sessionizer.wezterm](https://github.com/mikkasendke/sessionizer.wezterm) [![GitHub stars](https://img.shields.io/github/stars/mikkasendke/sessionizer.wezterm?style=flat)](https://github.com/mikkasendke/sessionizer.wezterm/stargazers) - Opening Git repositories as their own WezTerm workspaces using `fd`.
- [MLFlexer/resurrect.wezterm](https://github.com/MLFlexer/resurrect.wezterm) [![GitHub stars](https://img.shields.io/github/stars/MLFlexer/resurrect.wezterm?style=flat)](https://github.com/MLFlexer/resurrect.wezterm/stargazers) - Save and restore the state of windows, tabs and panes.
- [MLFlexer/smart_workspace_switcher.wezterm](https://github.com/MLFlexer/smart_workspace_switcher.wezterm) [![GitHub stars](https://img.shields.io/github/stars/MLFlexer/smart_workspace_switcher.wezterm?style=flat)](https://github.com/MLFlexer/smart_workspace_switcher.wezterm/stargazers) - Switch between workspaces with fuzzy finding and `zoxide`.
- [vieitesss/workspacesionizer.wezterm](https://github.com/vieitesss/workspacesionizer.wezterm) [![GitHub stars](https://img.shields.io/github/stars/vieitesss/workspacesionizer.wezterm?style=flat)](https://github.com/vieitesss/workspacesionizer.wezterm/stargazers) - Blazingly fast workspace chooser inspired by `tmux-sessionizer`.
- [abidibo/wezterm-sessions](https://github.com/abidibo/wezterm-sessions) [![GitHub stars](https://img.shields.io/github/stars/abidibo/wezterm-sessions?style=flat)](https://github.com/abidibo/wezterm-sessions/stargazers) - Save and restore sessions.
- [srackham/tabsets.wezterm](https://github.com/srackham/tabsets.wezterm) [![GitHub stars](https://img.shields.io/github/stars/srackham/tabsets.wezterm?style=flat)](https://github.com/srackham/tabsets.wezterm/stargazers) - Load, save, rename and delete named sets of tabs.
- [ryanmsnyder/workspace-manager.wezterm](https://github.com/ryanmsnyder/workspace-manager.wezterm) [![GitHub stars](https://img.shields.io/github/stars/ryanmsnyder/workspace-manager.wezterm?style=flat)](https://github.com/ryanmsnyder/workspace-manager.wezterm/stargazers) - Navigate projects effortlessly with smart workspace switching and keyboard-driven navigation.

## Tab bar

- [adriankarlen/bar.wezterm](https://github.com/adriankarlen/bar.wezterm) [![GitHub stars](https://img.shields.io/github/stars/adriankarlen/bar.wezterm?style=flat)](https://github.com/adriankarlen/bar.wezterm/stargazers) - A configurable tab bar with batteries included.
- [michaelbrusegard/tabline.wez](https://github.com/michaelbrusegard/tabline.wez) [![GitHub stars](https://img.shields.io/github/stars/michaelbrusegard/tabline.wez?style=flat)](https://github.com/michaelbrusegard/tabline.wez/stargazers) - A versatile and easy to use retro tab bar with the `lualine.nvim` configuration format.
- [rootiest/battery.wez](https://github.com/rootiest/battery.wez) [![GitHub stars](https://img.shields.io/github/stars/rootiest/battery.wez?style=flat)](https://github.com/rootiest/battery.wez/stargazers) - A colorful and fancy battery component for the retro tab bar.
- [yriveiro/wezterm-status](https://github.com/yriveiro/wezterm-status) [![GitHub stars](https://img.shields.io/github/stars/yriveiro/wezterm-status?style=flat)](https://github.com/yriveiro/wezterm-status/stargazers) - Configurable status for the retro tab bar.
- [yriveiro/wezterm-tabs](https://github.com/yriveiro/wezterm-tabs) [![GitHub stars](https://img.shields.io/github/stars/yriveiro/wezterm-tabs?style=flat)](https://github.com/yriveiro/wezterm-tabs/stargazers) - Configurable tabs for the retro tab bar.
- [pro-vi/wezterm-attention](https://github.com/pro-vi/wezterm-attention) [![GitHub stars](https://img.shields.io/github/stars/pro-vi/wezterm-attention?style=flat)](https://github.com/pro-vi/wezterm-attention/stargazers) - Turns your tab bar into a notification system with colored tab indicators.

## Themes

- [neapsix/wezterm](https://github.com/neapsix/wezterm) [![GitHub stars](https://img.shields.io/github/stars/neapsix/wezterm?style=flat)](https://github.com/neapsix/wezterm/stargazers) - Rosé Pine theme, all natural pine, faux fur and a bit of soho vibes.
- [sravioli/kanagawa.wz](https://github.com/sravioli/kanagawa.wz) [![GitHub stars](https://img.shields.io/github/stars/sravioli/kanagawa.wz?style=flat)](https://github.com/sravioli/kanagawa.wz/stargazers) - Kanagawa.nvim color schemes with Wave, Dragon, and Lotus variants.
- [koh-sh/wezterm-theme-rotator](https://github.com/koh-sh/wezterm-theme-rotator) [![GitHub stars](https://img.shields.io/github/stars/koh-sh/wezterm-theme-rotator?style=flat)](https://github.com/koh-sh/wezterm-theme-rotator/stargazers) - Cycle through built-in themes using keyboard shortcuts.
- [willytop8/Wezterm-Window-Tint](https://github.com/willytop8/Wezterm-Window-Tint) [![GitHub stars](https://img.shields.io/github/stars/willytop8/Wezterm-Window-Tint?style=flat)](https://github.com/willytop8/Wezterm-Window-Tint/stargazers) - Color the window frame, tab bar, and status badge by the active pane's Git root.

## Utility

- [aureolebigben/wezterm-cmd-sender](https://github.com/aureolebigben/wezterm-cmd-sender) [![GitHub stars](https://img.shields.io/github/stars/aureolebigben/wezterm-cmd-sender?style=flat)](https://github.com/aureolebigben/wezterm-cmd-sender/stargazers) - Send commands to multiple panes.
- [ChrisGVE/dev.wezterm](https://github.com/ChrisGVE/dev.wezterm) [![GitHub stars](https://img.shields.io/github/stars/ChrisGVE/dev.wezterm?style=flat)](https://github.com/ChrisGVE/dev.wezterm/stargazers) - Location resolver for development and deployment of a plugin.
- [ChrisGVE/lib.wezterm](https://github.com/ChrisGVE/lib.wezterm) [![GitHub stars](https://img.shields.io/github/stars/ChrisGVE/lib.wezterm?style=flat)](https://github.com/ChrisGVE/lib.wezterm/stargazers) - A library of common utility functions for plugin developers.
- [ChrisGVE/listeners.wezterm](https://github.com/ChrisGVE/listeners.wezterm) [![GitHub stars](https://img.shields.io/github/stars/ChrisGVE/listeners.wezterm?style=flat)](https://github.com/ChrisGVE/listeners.wezterm/stargazers) - Enables enhanced event listener capabilities with persistent state management.
- [dfsramos/wezterm-sync](https://github.com/dfsramos/wezterm-sync) [![GitHub stars](https://img.shields.io/github/stars/dfsramos/wezterm-sync?style=flat)](https://github.com/dfsramos/wezterm-sync/stargazers) - Sync your config across machines via a private GitHub Gist, with zero external dependencies.
- [lilaqua/tunicodes](https://gitlab.com/lilaqua/tunicodes) - Insert Unicode characters via their codepoints.
- [zsh-sage/toggle_terminal.wez](https://github.com/zsh-sage/toggle_terminal.wez) [![GitHub stars](https://img.shields.io/github/stars/zsh-sage/toggle_terminal.wez?style=flat)](https://github.com/zsh-sage/toggle_terminal.wez/stargazers) - An easy-to-use toggleable terminal window.
- [quantonganh/quickselect.wezterm](https://github.com/quantonganh/quickselect.wezterm) [![GitHub stars](https://img.shields.io/github/stars/quantonganh/quickselect.wezterm?style=flat)](https://github.com/quantonganh/quickselect.wezterm/stargazers) - Jump to the build error by opening them in Helix.
- [sravioli/lantern.wz](https://github.com/sravioli/lantern.wz) [![GitHub stars](https://img.shields.io/github/stars/sravioli/lantern.wz?style=flat)](https://github.com/sravioli/lantern.wz/stargazers) - Selector framework for colorschemes, fonts, GPU adapters, window appearance, and custom config presets.
- [sravioli/log.wz](https://github.com/sravioli/log.wz) [![GitHub stars](https://img.shields.io/github/stars/sravioli/log.wz?style=flat)](https://github.com/sravioli/log.wz/stargazers) - Tagged logging library with pluggable sinks and severity thresholds.
- [sravioli/memo.wz](https://github.com/sravioli/memo.wz) [![GitHub stars](https://img.shields.io/github/stars/sravioli/memo.wz?style=flat)](https://github.com/sravioli/memo.wz/stargazers) - Memoization, caching, and persistent state management.
- [sravioli/ribbon.wz](https://github.com/sravioli/ribbon.wz) [![GitHub stars](https://img.shields.io/github/stars/sravioli/ribbon.wz?style=flat)](https://github.com/sravioli/ribbon.wz/stargazers) - Builds styled text segments for status bars, tab titles, and selector previews.
- [sravioli/sigil.wz](https://github.com/sravioli/sigil.wz) [![GitHub stars](https://img.shields.io/github/stars/sravioli/sigil.wz?style=flat)](https://github.com/sravioli/sigil.wz/stargazers) - Icon and identity-color registry for processes, tools, and UI labels.
- [sravioli/warp.wz](https://github.com/sravioli/warp.wz) [![GitHub stars](https://img.shields.io/github/stars/sravioli/warp.wz?style=flat)](https://github.com/sravioli/warp.wz/stargazers) - General-purpose utility library with string, table, list, path, and filesystem helpers.
- [btrachey/wezterm-replay](https://github.com/btrachey/wezterm-replay) [![GitHub stars](https://img.shields.io/github/stars/btrachey/wezterm-replay?style=flat)](https://github.com/btrachey/wezterm-replay/stargazers) - Parse command output and get URLs, shell commands, etc. pasted into your next prompt.
- [usrivastava92/widgets.wez](https://github.com/usrivastava92/widgets.wez) [![GitHub stars](https://img.shields.io/github/stars/usrivastava92/widgets.wez?style=flat)](https://github.com/usrivastava92/widgets.wez/stargazers) - Cross-platform status bar widgets for CPU, RAM, battery, network, and disk on macOS, Linux, and Windows.
