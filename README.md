# Onyx Nitro Plugin SDK

This is a temporary documentation for Plugin SDK. Actual documentation is work in progress.

Base your Onyx Nitro UI themes and mods on [nitro-ui](https://github.com/Bitsaur/nitro-ui) and [onyx-ui](https://github.com/Bitsaur/onyx-ui).


## nitro.json

Put `nitro.json` in the same folder as executable (on Linux and Windows, on macOS it has to go in Application Support/Onyx) to configure how Nitro behaves. Available flags for `nitro.json`:

- `vsync`:bool &rarr; turn on/off VSync (default: `true`)
- `profilesPath`:string &rarr; location to where the profiles are located (default: `"profiles"`)
- `pluginsPath`:string &rarr; location to where the plugins are installed (default: `"plugins"`)
- `pythonPath`:string &rarr; location to the Python 3.15.0. standard library (default: `"python"`)
- `workspaceStoragePath`:string &rarr; location to workspace cache (default: `"workspaces"`)
- `recents`:array &rarr; list of files and directories recently opened
- `bookmarks`:array &rarr; list of bookmarked files and directories

## Profiles

You can define new profiles by creating a directory in the `profiles` directory. The name of the directory is the name of the profile. `Default` is a profile that Nitro loads on startup. You can specify which profile to use by launching nitro with `--profile [name]` argument.

### settings.json

The settings in `settings.json` can be defined in dynamic way. Each "." can be represented as JSON object or you can inline full or portion of the setting key. Example:
```json
{
  "Application.Theme": "Nitro Dark",
}
```
is same as:
```json
{
  "Application": {
    "Theme": "Nitro Dark"
  }
}
```
### shortcuts.json

You can customize your shortcuts by providing a shortcuts.json file in the profile directory (currently there is no UI for managing shortcuts). 
Like settings, each "." in definition of shortcut key can be represented as a JSON object.

There are currently unfortunately some hardcoded shortcuts:
- `SHIFT` + `SHIFT` &rarr; opens command palette
- `CTRL` + hold `CTRL` + arrow keys up/down &rarr; creates multiple carets while editing text
- `SHIFT` + `ALT` + mouse click &rarr; creates a new caret at given position

List of available shortcuts and their default values:
```json
{
  "TextEditor.Redo": "Ctrl+Y",
  "TextEditor.Undo": "Ctrl+Z",
  "TextEditor.PageUp": "PageUp",
  "TextEditor.SelectPageUp": "Shift+PageUp",
  "TextEditor.PageTop": "Ctrl+PageUp",
  "TextEditor.SelectPageTop": "Ctrl+Shift+PageUp",
  "TextEditor.PageDown": "PageDown",
  "TextEditor.SelectPageDown": "Shift+PageDown",
  "TextEditor.PageBottom": "Ctrl+PageDown",
  "TextEditor.SelectPageBottom": "Ctrl+Shift+PageDown",
  "TextEditor.LineEnd": "End",
  "TextEditor.SelectLineEnd": "Shift+End",
  "TextEditor.TextEnd": "Ctrl+End",
  "TextEditor.SelectTextEnd": "Ctrl+Shift+End",
  "TextEditor.LineBegin": "Home",
  "TextEditor.SelectLineBegin": "Shift+Home",
  "TextEditor.TextBegin": "Ctrl+Home",
  "TextEditor.SelectTextBegin": "Ctrl+Shift+Home",
  "TextEditor.EnsureCaretVisibility": "Ctrl+M",
  "TextEditor.ToggleSearch": "Ctrl+F",
  "TextEditor.Autocomplete": "Ctrl+Space",
  "TextEditor.SignatureHelp": "Ctrl+Shift+Space",
  "TextEditor.MoveLineContentUp": "Ctrl+Shift+Up",
  "TextEditor.MoveLineContentDown": "Ctrl+Shift+Down",
  "TextEditor.ScrollLineUp": "Ctrl+Up",
  "TextEditor.ScrollLineDown": "Ctrl+Down",
  "TextEditor.GoToPosition": "Ctrl+G",
  "TextEditor.GoToDefinition": "Ctrl+B",
  "TextEditor.FormatDocument": "Ctrl+Shift+Alt+L",
  "TextEditor.IncreaseFontSize": "Ctrl+OemPlus",
  "TextEditor.DecreaseFontSize": "Ctrl+OemMinus",
  "TextEditor.FoldLevel1": [ "Ctrl+K", "Ctrl+1" ],
  "TextEditor.FoldLevel2": [ "Ctrl+K", "Ctrl+2" ],
  "TextEditor.FoldLevel3": [ "Ctrl+K", "Ctrl+3" ],
  "TextEditor.FoldLevel4": [ "Ctrl+K", "Ctrl+4" ],
  "TextEditor.FoldLevel5": [ "Ctrl+K", "Ctrl+5" ],
  "TextEditor.ToggleVimMode": "Ctrl+Alt+V",
  "Workspace.OpenSettings": "Ctrl+OemComma",
  "Workspace.OpenWelcomePage": "",
  "Workspace.OpenTerminalPage": "Ctrl+Shift+OemTilde",
  "Workspace.CloseDocument": "Ctrl+W",
  "Workspace.OpenFile": "Ctrl+O", 
  "Workspace.NewEmptyFile": "Ctrl+N",
  "Workspace.SaveDocument": "Ctrl+S",
  "Workspace.SaveAllDocuments": "Ctrl+Shift+S"
}
```


## Plugin's config.json

Each plugin must have a config.json, e.g.:
```json
{
  "id": "MyCustomPlugin",
  "name": "My Custom Plugin",
  "publisher": "me",
  "description": "This is my own custom plugin for Onyx Nitro",
  "author": "me",
  "version": "0.0.1",
  "type": "python"
}
```

Python plugin is loaded from `plugin.py` file. Where user must define `class Plugin`

There is a flag `"intercept_print"` which is by default set to true. When it's set to true, all the `print()` output will be redirected to Onyx Nitro's log window in UI. When it's false, it's going to normally print to the console. This is useful if the plugin is crashing Nitro to find out where exactly it's causing a crash. 


To set an event on which the plugin.py will be loaded:
```json
{
  "activate_on": [ "Startup" ]
}
```
By default it's only loaded when a file is opened whose language is defined by
this plugin. To explicitly load the .py when the .exe starts,
add the `Startup` event to the list. (more events will be added in the future)

- `UIModActivation` &rarr; this plugin's UI mod has been activated, start the plugin
- `OnLanguage@[id]` &rarr; activate plugin when a file with given language is opened, e.g. `OnLanguage@cpp`


List of events that the plugin will listen to:
```json
{
  "event_subscriptions": [ "OpenFile" ]
}
```
For IPlugin's OnXXX function to be called, it must appear in this list. Otherwise,
those functions won't be called. Events:
- `OpenFile` -> a file has been opened
- `CloseFile` -> a file has been closed
- `SettingChanged` -> a setting value has changed
- `OpenWorkspace` -> a new workspace has been opened
- `SwitchWorkspace` -> some other workspace has been selected
- `WorkspaceFileChanged`, `WorkspaceFileCreated`, `WorkspaceFileDeleted`, `WorkspaceFileRenamed` -> a file under the project directory has been modified, deleted, etc...
- `CurrentTextEditorChanged` -> a new text editor gained focus, or the old one just lost focus
- `Command` -> a command is about to be executed

Language definition:
```json
{
  "id": "cpp",
  "name": "C++",
  "extensions": [ "cpp", "cxx", "c++", "cc", "hpp", "hxx", "h++" ],
  "configuration": "cpp",
  "rules": {
    "type": "tree-sitter",
    "color": "filepath.scm"
  }
}
```
Rules can be sourced from files (if the field is specified) or from the IPlugin class
directly from the memory (if no value is specified). There are currently 4 rule types: `color`, `fold`, `indent`, `pinLine`


Setting definitions:
```json
{
  "id": "CPP",
  "definitions": {
    "settings": [
      {
        "group": "Clangd",
        "id": "Process",
        "type": "String",
        "default": "clangd",
        "description": "Defines the path to clangd process"
      }
    ]
  }
}
```
Defines a "Plugins.CPP.Clangd.Process" option with the default value "clangd".
Without the group, it would just be "Plugins.CPP.Process".

Panel definitions:
```json
{
  "definitions": {
    "panels": [
      {
        "id": "SourceControl",
        "name": "Source Control",
        "icon": "&#xeaf5;",
        "location": "left",
        "visibility": "auto",
        "ui": "Panel.xaml"
      }
    ]
  }
}
```
Visibility can be "auto" (always visible / decided by the user), or "manual" (e.g. open a cmake 
panel only when a CMakeLists.txt is present)

Command/shortcut definition:
```json
{
  "definitions": {
    "commands": [
      {
        "id": "CreateCaretBelow",
        "name": "Create Caret Below",
        "condition": "text_editor.is_focused && !text_editor.has_selection"
      }
    ]
  }
}
```

Id and Name are non optional values, while Condition is a optional value.
In condition field you can use following operators:
- ! - negate the value
- && - logical and
- || - logical or

You can use following parameters:
- `text_editor.focused` &rarr; check if keyboard focus currently inside of a text editor
- `text_editor.has_selection` &rarr; is there a selection in currently active text editor
- `text_editor.fold_enabled` &rarr; is folding enabled in the text editor
- `text_editor.read_only` &rarr; is text editor read only


Python plugins can use 3rd party libraries (so long as they don't use .pyd files):
```bash
python -m venv .venv
./.venv/Scripts/Activate.ps1
pip install ...
```
