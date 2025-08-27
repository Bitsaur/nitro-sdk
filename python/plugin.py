import nitro
from typing import Any, Optional

class Plugin:
    """
    Defines the interface for an Onyx Tools Python plugin.

    A plugin must be an object that implements some or all of these methods.
    The editor will call these methods at different points in its lifecycle.
    """

    def init(self) -> None:
        """Called when the plugin is first loaded."""
        ...

    def shutdown(self) -> None:
        """Called when the plugin is about to be unloaded."""
        ...

    def get_tree_sitter_language(self, language_id: str):
        """
        Provides a tree-sitter language parser.

        Args:
            language_id: The identifier for the language (e.g., "python", "cpp").

        Returns:
            A pointer (as an integer) to the TSLanguage function, a PyCapsule object
            for the language, or None if not supported.
        """
        ...

    def get_tree_sitter_color_rule(self, language_id: str) -> str:
        """
        Provides the tree-sitter query for syntax highlighting.

        Args:
            language_id: The identifier for the language.

        Returns:
            A string containing the tree-sitter highlighting query, or None.
        """
        ...

    def get_tree_sitter_indent_rule(self, language_id: str) -> str:
        """
        Provides the tree-sitter query for auto-indentation rules.

        Args:
            language_id: The identifier for the language.

        Returns:
            A string containing the tree-sitter indentation query, or None.
        """
        ...

    def get_tree_sitter_pin_line_rule(self, language_id: str) -> str:
        """
        Provides the tree-sitter query for determining which lines to pin (e.g., function headers).

        Args:
            language_id: The identifier for the language.

        Returns:
            A string containing the tree-sitter pin line query, or None.
        """
        ...

    def get_tree_sitter_fold_rule(self, language_id: str) -> str:
        """
        Provides the tree-sitter query for code folding.

        Args:
            language_id: The identifier for the language.

        Returns:
            A string containing the tree-sitter folding query, or None.
        """
        ...

    def on_open_file(self, file: nitro.File) -> None:
        """
        Called when a file is opened in the editor. Requires OpenFile in event_subscriptions.

        Args:
            file: The file object that was opened.
        """
        ...

    def on_close_file(self, file: nitro.File) -> None:
        """
        Called when a file is closed in the editor.

        Args:
            file: The file object that was closed.
        """
        ...

    def on_setting_changed(self, key: str, new_value: Any, old_value: Any) -> None:
        """
        Called when a user setting has changed.

        Args:
            key: The key of the setting that changed.
            new_value: The new value of the setting (can be str, float, or bool).
            old_value: The previous value of the setting.
        """
        ...

    def get_view_model(self) -> Optional[nitro.IViewModelBase]:
        """
        Called by the editor to get a root view model for the plugin's UI.

        Returns:
            An object that implements the IViewModelBase interface, or None.
        """
        ...

    def get_panel_view_model(self, panel_id: str) -> Optional[nitro.IViewModelBase]:
        """
        Called by the editor to get a view model for a specific panel.

        Args:
            panel_id: The unique identifier of the panel requesting a view model.

        Returns:
            An object that implements the IViewModelBase interface, or None.
        """
        ...

    def on_open_workspace(self, workspace: nitro.Workspace) -> None:
        """
        Called when a workspace is opened.

        Args:
            workspace: The workspace object that was opened.
        """
        ...

    def on_switch_workspace(self, workspace: nitro.Workspace) -> None:
        """
        Called when the active workspace is switched.

        Args:
            workspace: The new active workspace object.
        """
        ...

    def on_workspace_file_changed(self, workspace: nitro.Workspace, file: nitro.File) -> None:
        """
        Called when a file within the workspace is modified. It is called also for changes done by external tools.

        Args:
            workspace: The current workspace.
            file: The file that was changed.
        """
        ...

    def on_workspace_file_created(self, workspace: nitro.Workspace, file: nitro.File) -> None:
        """
        Called when a file is created within the workspace. It is called also for changes done by external tools.

        Args:
            workspace: The current workspace.
            file: The file that was created.
        """
        ...

    def on_workspace_file_deleted(self, workspace: nitro.Workspace, file: nitro.File) -> None:
        """
        Called when a file is deleted from the workspace. It is called also for changes done by external tools.

        Args:
            workspace: The current workspace.
            file: The file that was deleted.
        """
        ...

    def on_workspace_file_renamed(self, workspace: nitro.Workspace, file: nitro.File, old_name: str) -> None:
        """
        Called when a file is renamed within the workspace. It is called also for changes done by external tools.

        Args:
            workspace: The current workspace.
            file: The file object with the new name.
            old_name: The previous name of the file.
        """
        ...

    def on_current_text_editor_changed(self, old_editor: Optional[nitro.TextEditor], new_editor: Optional[nitro.TextEditor]) -> None:
        """
        Called when the focus switches from one text editor to another.

        Args:
            old_editor: The previously active text editor, or None.
            new_editor: The newly active text editor, or None.
        """
        ...

    def on_plugin_command(self, command: str) -> None:
        """
        Called when a this plugin's command is invoked.

        Args:
            command: The command id to be executed.
        """
        ...

    def on_command(self, command: str) -> bool:
        """
        Called for global commands, allowing the plugin to handle them.

        Args:
            command: The command id that was issued.

        Returns:
            True if the plugin handled the command which skips native implementation, False otherwise.
        """
        ...