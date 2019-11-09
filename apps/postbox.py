# Talon voice commands for interacting with Postbox mail
# James Turnbull james@lovedthanost.net

from talon.voice import Key, Context

ctx = Context("postbox", bundle="com.postbox-inc.postbox")

ctx.keymap(
    {
        "new mail": Key("cmd-n"),
        "send mail": Key("cmd-shift-d"),
        "reply mail": Key("cmd-r"),
        "reply all": Key("shift-cmd-r"),
        "forward mail": Key("cmd-l"),
        "mark unread": Key("m"),
        "mark read": Key("r"),
        "star": Key("s"),
        "delete mail": Key("backspace"),
        "archive mail": Key("a"),
        "next mail": Key("f"),
        "previous mail": Key("b"),
        "next unread": Key("n"),
        "previous unread": Key("p"),
        "top list": Key("fn-left"),
        "bottom list": Key("fn-right"),

    }
)
