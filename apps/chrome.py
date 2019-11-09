from talon import ui, ctrl
from talon.voice import Context, Key, Str, press

context = Context("GoogleChrome", bundle="com.google.Chrome")

context.keymap(
    {
        "switch window": Key("cmd-`"),
    }
)
