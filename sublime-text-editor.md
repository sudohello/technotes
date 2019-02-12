
---
title: Sublime Text Editor
---

**Table of Contents**
<!-- MarkdownTOC -->

- Packages
- Key Bindings
- Python to Javascript
- Case Conversion
- Markdown Table Editing
- Atom
- Console
- Must Have Plugins

<!-- /MarkdownTOC -->
* TOC
{:toc}


## Packages
* Color Highlight
* Color Highlighter
* BracketHighlighter
* PHP-Twig
* Hover Image Preview
* Javascript Beautify
* JSON Reindent
* Indent XML
* CSS3
* CSS Colors
* Compare Side-By-Side
* BackgroundColorEdit
* [TerminalView](https://packagecontrol.io/packages/TerminalView)

**PS1**
* https://askubuntu.com/questions/984060/export-ps1-for-customizing-shell-prompt

## Key Bindings
* shortcuts
  - http://docs.sublimetext.info/en/latest/reference/keyboard_shortcuts_win.html
* Preferences -> Key Bindings
```bash
[
  { "keys": ["ctrl+alt+w"], "command": "toggle_setting", "args": {"setting": "word_wrap"} }
]
```
* User Settings:
http://www.sublimetext.com/3
https://stackoverflow.com/questions/21289157/set-encoding-of-file-to-utf8-with-bom-in-sublime-text-3
```bash
{
  "ignored_packages":
  [
    "BackgroundColorEdit",
    "Hover Image Preview",
    "Indent XML",
    "PHP-Twig",
    "Vintage",
    "Vue Syntax Highlight"
  ],
  "tab_size": 2,
  "translate_tabs_to_spaces": true,
  "show_encoding": true,
  "show_line_endings": true
}

```

**Show Find All list**
- https://superuser.com/questions/836141/is-there-a-way-in-sublime-text-to-display-find-results-in-a-panel-at-the-bottom
* hot exist
  * https://stackoverflow.com/questions/7890102/how-to-prevent-sublime-text-2-from-opening-that-last-open-file-project-when-st


## Python to Javascript
- https://www.infoworld.com/article/3209651/python/how-to-convert-python-to-javascript-and-back-again.html


## Case Conversion

**convert selection to lowercase (or uppercase) in Sublime Text**
```
[
  { "keys": ["ctrl+alt+w"], "command": "toggle_setting", "args": {"setting": "word_wrap"} }
  ,{ "keys": ["ctrl+k", "ctrl+t"], "command": "title_case" }
  ,{ "keys": ["ctrl+k", "ctrl+s"], "command": "convert_to_snake"}
  ,{ "keys": ["ctrl+k", "ctrl+c"], "command": "convert_to_camel"}
  ,{ "keys": ["ctrl+k", "ctrl+p"], "command": "convert_to_pascal"}
  ,{ "keys": ["ctrl+alt+shift+k"], "command": "markdown_table_format", "context": [ {"key": "selector", "operator": "equal", "operand": "text.html.markdown"} ]
]
```
* https://stackoverflow.com/questions/53898644/sublime-text-snippet-convert-camelcase-to-snake-case


## Markdown Table Editing
* http://brettterpstra.com/2015/04/22/sublime-text-tips-for-markdown-table-editing/
* https://github.com/bitwiser73/MarkdownTableFormatter
* https://github.com/SublimeText-Markdown/MarkdownEditing#configuration
* **Table**

convert to snake

| a  | b   | c   |
|:---|:----|:----|
| x  | yaa | xxx |
| -- | --  | --  |


* sample that works:

|x|y|
|:--|:--|
|adas|ada|




https://github.com/SublimeText-Markdown/MarkdownEditing/issues/205

Error loading syntax file "Packages/Markdown/Markdown.sublime-syntax": Unable to read Packages/Markdown/Markdown.sublime-syntax

https://github.com/SublimeText-Markdown/MarkdownEditing/issues/485

## Atom
* https://atom.io/packages/markdown-table-editor

## Console
* https://plaintext-productivity.net/2-04-how-to-set-up-sublime-text-for-markdown-editing.html


https://stackoverflow.com/questio
ns/41489818/in-sublime-text-3-is-there-a-shortcut-to-remove-blank-lines-in-a-selected-text?rq=1


## Must Have Plugins
* [Origami](https://github.com/SublimeText/Origami)
  - https://stackoverflow.com/questions/23957730/sublime-editor-split-screen-put-same-file-on-both-windows
  - Origami is a new way of thinking about panes in Sublime Text 2 and 3: you tell Sublime Text where you want a new pane, and it makes one for you. It works seamlessly alongside the built-in layout commands.
  - no modifiers: travel to an adjacent pane
  - shift: carry the current file to the destination
  - alt (option): clone the current file to the destination
  - command: create an adjacent pane
  - command+shift: destroy an adjacent pane

* [Chain](https://packagecontrol.io/packages/Chain%20of%20Command)