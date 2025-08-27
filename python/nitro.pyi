from typing import Any, Callable, TypeVar, Generic, overload, Iterator
import enum
from typing_extensions import ParamSpec

P = ParamSpec("P")
R = TypeVar("R")

class Command(Generic[P, R]):
    def __init__(self, func: Callable[P, R]) -> None: ...
    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R: ...
    def CanExecute(self, func: Callable[P, bool]) -> "Command[P, R]": ...

class LspOptions:
    type: str
    link: str
    target_languages: list
    arguments: list

class LspClient:
    is_running: bool

    def start(self): ...
    def stop(self): ...

class File:
    path: str
    language: str
    is_open: bool

class Workspace:
    path: str
    def open_file(self, path) -> bool: ...

class TextPosition:
    def __init__(self, line: int, column: int) -> None: ...
    line: int
    column: int

class TextRange:
    def __init__(self, start: TextPosition, end: TextPosition) -> None: ...
    start: TextPosition
    end: TextPosition

class IndentationType(enum.Enum):
    Auto: int
    Spaces: int
    Tabs: int

class Key(enum.IntEnum):
    """Represents keyboard key codes."""
    None_ = 0
    Cancel = 1
    Back = 2
    Tab = 3
    LineFeed = 4
    Clear = 5
    Return = 6
    Enter = 6
    Pause = 7
    Capital = 8
    CapsLock = 8
    KanaMode = 9
    HangulMode = 9
    JunjaMode = 10
    FinalMode = 11
    HanjaMode = 12
    KanjiMode = 12
    Escape = 13
    ImeConvert = 14
    ImeNonConvert = 15
    ImeAccept = 16
    ImeModeChange = 17
    Space = 18
    Prior = 19
    PageUp = 19
    Next = 20
    PageDown = 20
    End = 21
    Home = 22
    Left = 23
    Up = 24
    Right = 25
    Down = 26
    Select = 27
    Print = 28
    Execute = 29
    Snapshot = 30
    PrintScreen = 30
    Insert = 31
    Delete = 32
    Help = 33
    D0 = 34
    D1 = 35
    D2 = 36
    D3 = 37
    D4 = 38
    D5 = 39
    D6 = 40
    D7 = 41
    D8 = 42
    D9 = 43
    A = 44
    B = 45
    C = 46
    D = 47
    E = 48
    F = 49
    G = 50
    H = 51
    I = 52
    J = 53
    K = 54
    L = 55
    M = 56
    N = 57
    O = 58
    P = 59
    Q = 60
    R = 61
    S = 62
    T = 63
    U = 64
    V = 65
    W = 66
    X = 67
    Y = 68
    Z = 69
    LWin = 70
    RWin = 71
    Apps = 72
    Sleep = 73
    NumPad0 = 74
    NumPad1 = 75
    NumPad2 = 76
    NumPad3 = 77
    NumPad4 = 78
    NumPad5 = 79
    NumPad6 = 80
    NumPad7 = 81
    NumPad8 = 82
    NumPad9 = 83
    Multiply = 84
    Add = 85
    Separator = 86
    Subtract = 87
    Decimal = 88
    Divide = 89
    F1 = 90
    F2 = 91
    F3 = 92
    F4 = 93
    F5 = 94
    F6 = 95
    F7 = 96
    F8 = 97
    F9 = 98
    F10 = 99
    F11 = 100
    F12 = 101
    F13 = 102
    F14 = 103
    F15 = 104
    F16 = 105
    F17 = 106
    F18 = 107
    F19 = 108
    F20 = 109
    F21 = 110
    F22 = 111
    F23 = 112
    F24 = 113
    NumLock = 114
    Scroll = 115
    LeftShift = 116
    RightShift = 117
    LeftCtrl = 118
    RightCtrl = 119
    LeftAlt = 120
    RightAlt = 121
    BrowserBack = 122
    BrowserForward = 123
    BrowserRefresh = 124
    BrowserStop = 125
    BrowserSearch = 126
    BrowserFavorites = 127
    BrowserHome = 128
    VolumeMute = 129
    VolumeDown = 130
    VolumeUp = 131
    MediaNextTrack = 132
    MediaPreviousTrack = 133
    MediaStop = 134
    MediaPlayPause = 135
    LaunchMail = 136
    SelectMedia = 137
    LaunchApplication1 = 138
    LaunchApplication2 = 139
    Oem1 = 140
    OemSemicolon = 140
    OemPlus = 141
    OemComma = 142
    OemMinus = 143
    OemPeriod = 144
    Oem2 = 145
    OemQuestion = 145
    Oem3 = 146
    OemTilde = 146
    AbntC1 = 147
    AbntC2 = 148
    Oem4 = 149
    OemOpenBrackets = 149
    Oem5 = 150
    OemPipe = 150
    Oem6 = 151
    OemCloseBrackets = 151
    Oem7 = 152
    OemQuotes = 152
    Oem8 = 153
    Oem102 = 154
    OemBackslash = 154
    ImeProcessed = 155
    System = 156
    OemAttn = 157
    DbeAlphanumeric = 157
    OemFinish = 158
    DbeKatakana = 158
    OemCopy = 159
    DbeHiragana = 159
    OemAuto = 160
    DbeSbcsChar = 160
    OemEnlw = 161
    DbeDbcsChar = 161
    OemBackTab = 162
    DbeRoman = 162
    Attn = 163
    DbeNoRoman = 163
    CrSel = 164
    DbeEnterWordRegisterMode = 164
    ExSel = 165
    DbeEnterImeConfigureMode = 165
    EraseEof = 166
    DbeFlushString = 166
    Play = 167
    DbeCodeInput = 167
    Zoom = 168
    DbeNoCodeInput = 168
    NoName = 169
    DbeDetermineString = 169
    Pa1 = 170
    DbeEnterDialogConversionMode = 170
    OemClear = 171
    DeadCharProcessed = 172
    PageLeft = 173
    PageRight = 174
    GamepadLeft = 175
    GamepadUp = 176
    GamepadRight = 177
    GamepadDown = 178
    GamepadAccept = 179
    GamepadCancel = 180
    GamepadMenu = 181
    GamepadView = 182
    GamepadPageUp = 183
    GamepadPageDown = 184
    GamepadPageLeft = 185
    GamepadPageRight = 186
    GamepadContext1 = 187
    GamepadContext2 = 188
    GamepadContext3 = 189
    GamepadContext4 = 190
    Count = 191

    # Rename 'None' to 'None_' to avoid keyword conflict in Python
    def __init__(self, value):
        if self.name == 'None_':
            self._name_ = 'None'

class ModifierKeys(enum.IntFlag):
    """Represents modifier key flags (for bitwise operations)."""
    none = 0
    Alt = 1
    Control = 2
    Shift = 4
    Windows = 8

class KeyEvent:
    @property
    def key(self) -> Key: ...
    @property
    def modifiers(self) -> ModifierKeys: ...
    @property
    def is_repeat(self) -> bool: ...
    @property
    def is_toggled(self) -> bool: ...

class TextBuffer:
    """Represents the in-memory text storage for an editor."""

    # --- Properties ---
    @property
    def is_version_synced(self) -> bool:
        """Whether the buffer is synced with its source (e.g., file on disk)."""
        ...

    @property
    def line_count(self) -> int:
        """Total number of lines in the buffer."""
        ...

    @property
    def length(self) -> int:
        """Total number of characters (length) in the buffer."""
        ...

    def copy_contents(self) -> str:
        """Copy the full contents of the buffer as a string and return it."""
        ...

    # --- Methods ---
    def get_text_position_at(self, offset: int) -> TextPosition:
        """Converts a byte offset to a (line, column) TextPosition."""
        ...

    def get_offset_at(self, line: int, column: int) -> int:
        """Converts a (line, column) TextPosition to a byte offset."""
        ...

    def copy_line_content(self, line: int) -> str:
        """Gets the contents of a single line."""
        ...

    def get_line_length(self, line: int) -> int:
        """Gets the character length of a single line."""
        ...

    def get_line_column_count(self, line: int) -> int:
        """Gets the number of columns in a single line."""
        ...

    def copy_range_content(self, offset: int, count: int) -> str:
        """Gets a substring from the buffer by offset and count."""
        ...

    def get_char_code_at_line(self, line: int, column: int) -> int:
        """Gets the character code at a specific line and column."""
        ...

    def get_char_code_at_offset(self, offset: int) -> int:
        """Gets the character code at a specific byte offset."""
        ...

    # --- Sequence Protocol ---
    def __len__(self) -> int:
        """Returns the number of characters in the buffer."""
        ...

    def __getitem__(self, idx: int) -> str:
        """Returns the character at specified index."""
        ...

class TextEditor:
    is_insert_mode: bool
    font_size: float
    is_search_open: bool
    is_go_to_position_open: bool

    @property
    def file(self) -> File: ...
    @property
    def text_buffer(self) -> TextBuffer: ...
    @property
    def is_read_only(self) -> bool: ...
    @property
    def caret_count(self) -> int: ...
    @property
    def selection_count(self) -> int: ...
    @property
    def selected_text(self) -> str: ...
    @property
    def actual_indentation_type(self) -> IndentationType: ...
    @property
    def actual_indentation_width(self) -> int: ...
    @property
    def can_undo(self) -> bool: ...
    @property
    def can_redo(self) -> bool: ...

    # --- Methods ---

    def mouse_to_glyph_position(self, x: float, y: float) -> TextPosition: ...
    def glyph_to_text_position(self, glyph: TextPosition) -> TextPosition: ...
    def text_to_glyph_position(self, text: TextPosition) -> TextPosition: ...
    def set_state(self, text: str) -> None: ...

    # Caret API
    def move_carets(self, horiz: int, vert: int, word_mode: bool = False, select: bool = False) -> None: ...
    def move_carets_to_home(self, select: bool = False, file_mode: bool = False) -> None: ...
    def move_carets_to_end(self, select: bool = False, file_mode: bool = False) -> None: ...
    def move_carets_page_up(self, select: bool = False, current_page: bool = False) -> None: ...
    def move_carets_page_down(self, select: bool = False, current_page: bool = False) -> None: ...
    def set_caret_position(self, position: TextPosition, is_glyph: bool = False, ensure_visibility: bool = True) -> None: ...
    def set_caret_position_by_index(self, index: int, position: TextPosition, is_glyph: bool = False, ensure_visibility: bool = True) -> None: ...
    def insert_caret(self, position: TextPosition, is_glyph: bool = False) -> None: ...

    @overload
    def set_selection(self, range: TextRange) -> None: ...
    @overload
    def set_selection(self, start: TextPosition, end: TextPosition) -> None: ...
    def set_selection(self, start_or_range: Union[TextPosition, TextRange], end: TextPosition | None = None) -> None: ...

    def select_all(self) -> None: ...
    def get_caret_text_position(self, idx: int) -> TextPosition: ...
    def get_caret_glyph_position(self, idx: int) -> TextPosition: ...
    def remove_all_but_one_caret(self) -> None: ...
    def get_selection_range(self, index: int) -> TextRange: ...
    def set_selection_by_index(self, index: int, range: TextRange) -> None: ...
    def add_selection(self, range: TextRange) -> int: ...

    # Scroll API
    def scroll_lines(self, amount: int) -> None: ...
    def scroll_to_line(self, line: int) -> None: ...
    def ensure_caret_visibility(self) -> None: ...

    # Text API
    def get_word_under_mouse_cursor(self, x: float, y: float) -> Tuple[TextRange, str]: ...
    def get_word_under_text_cursor(self, caret: TextPosition) -> Tuple[TextRange, str]: ...
    def get_word_range_under_text_cursor(self, caret: TextPosition, left_oriented: bool = False) -> TextRange: ...

    # Editing API
    @overload
    def insert_new_line(self) -> None: ...
    @overload
    def insert_new_line(self, position: TextPosition) -> None: ...
    def insert_new_line(self, position: TextPosition | None = None) -> None: ...

    @overload
    def insert_char(self, c: str) -> bool: ...
    @overload
    def insert_char(self, position: TextPosition, c: str) -> bool: ...
    def insert_char(self, pos_or_char: Union[TextPosition, str], c: str | None = None) -> bool: ...

    def insert_indentation_spaces(self) -> None: ...

    @overload
    def insert_text(self, text: str) -> None: ...
    @overload
    def insert_text(self, position: TextPosition, text: str) -> None: ...
    def insert_text(self, pos_or_text: Union[TextPosition, str], text: str | None = None) -> None: ...

    @overload
    def insert_lines(self, lines: List[str]) -> None: ...
    @overload
    def insert_lines(self, position: TextPosition, lines: List[str]) -> None: ...
    def insert_lines(self, pos_or_lines: Union[TextPosition, List[str]], lines: List[str] | None = None) -> None: ...

    @overload
    def delete_char(self, is_left: bool = False, is_word_mode: bool = False) -> None: ...
    @overload
    def delete_char(self, position: TextPosition, is_left: bool = False) -> TextPosition: ...
    def delete_char(self, pos_or_is_left: Union[TextPosition, bool] = False, is_left_or_word_mode: bool = False) -> TextPosition | None: ...

    def delete_selection(self) -> None: ...
    def delete_range(self, range: TextRange) -> None: ...
    def move_line_content(self, direction: int) -> None: ...
    def format_document(self) -> None: ...
    def modify_selection_indentation(self, amount: int) -> None: ...

    # Undo/Redo API
    def undo(self) -> None: ...
    def redo(self) -> None: ...

    # LSP API
    def send_ls_goto_request(self, caret: TextPosition, move_caret: bool = True) -> None: ...
    def send_ls_autocomplete(self, caret: TextPosition) -> None: ...
    def send_ls_signature_help(self, caret: TextPosition) -> None: ...

    # UI API
    def hide_popups(self) -> None: ...

class ITextEditorController:
    def on_key_down(self, e:KeyEvent) -> bool: ...
    def on_key_up(self, e:KeyEvent) -> bool: ...
    def on_text_input(self, prop:str) -> bool: ...
    def on_attach(self, editor:TextEditor): ...
    def on_detach(self): ...
    def allow_shortcuts(self) -> bool: ...

class LogMessageLevel(enum.Enum):
    Info: int
    Warning: int
    Error: int

class ValueType(enum.Enum):
    Unknown: int
    Int: int
    Bool: int
    Float: int
    String: int
    Enum: int
    Command: int
    Object: int
    Collection: int

class Settings:
    def get(self, key): ...
    def get_type(self, key) -> ValueType: ...
    def get_plugin(self, key): ...
    def get_type_plugin(self, key) -> ValueType: ...

class IViewModelBase:
    def on_property_changed(self, prop:str): ...
    def raise_can_execute_changed(self, prop:str): ...

class ObservableCollection(Generic[R]):
    def __iter__(self) -> Iterator[R]: ...
    def __getitem__(self, index: int) -> R: ...
    def __len__(self) -> int: ...
    def add(self, obj:IViewModelBase): ...
    def insert(self, index:int, obj:IViewModelBase): ...
    def set(self, index:int, obj:IViewModelBase): ...
    def remove(self, obj:IViewModelBase): ...
    def remove_at(self, idx:int): ...
    def contains(self, obj:IViewModelBase) -> bool: ...
    def index_of(self, obj:IViewModelBase) -> int: ...
    def clear(self): ...
    def count(self) -> int: ...
    def get(self, idx:int) -> IViewModelBase: ...

class TypeRegistry:
    def register_class(self, type, properties:list|None = None, commands:list|None = None): ...
    def register_enum(self, enum_type): ...

class Context:
    @property
    def settings(self) -> Settings: ...

    @property
    def type_registry(self) -> TypeRegistry: ...

    @property
    def main_window_handle(self) -> int: ...

    @property
    def plugin_id(self) -> str: ...

    @property
    def workspaces(self) -> list[Workspace]: ...

    @property
    def current_workspace(self) -> Workspace: ...

    @property
    def current_text_editor(self) -> TextEditor: ...

    def create_lsp_client(self, opts:LspOptions) -> LspClient: ...
    def create_log_group(self, name:str) -> int: ...
    def delete_log_group(self, id:int): ...
    @overload
    def log(self, content: str, level: int = 0) -> None: ...
    @overload
    def log(self, group: int, content: str, level: int = 0) -> None: ...
    def trigger_view_model_change(self): ...
    def make_panel_visible(self, panel_id:str): ...
    def create_timer(self, interval:int, callable:Callable[P, int]): ...
    def restart_timer(self, timer_id:int, interval:int): ...
    def cancel_timer(self, timer_id:int): ...
    def attach_controller(self, editor:TextEditor, controller:ITextEditorController, auto_detach:bool = True): ...
    def detach_controller(self, editor:TextEditor, controller:ITextEditorController): ...


context: Context