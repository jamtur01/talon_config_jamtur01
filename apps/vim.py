from talon.voice import Key, press, Str, Context

ctx = Context("vim")

ctx.keymap({
	"vim save quit": Key("esc : w q enter"),
	"vim save": Key("esc : w enter"),
	"vim quit": Key("esc : q"),
	"vim quit bang": Key("esc : q !"),
        "vim select line": Key("shift-V"),
        "vim top": Key("g g"),
        "vim bottom": Key("shift-g"),
        "vim yank": Key("y"),
        "vim paste": Key("p"),
        "vim delete line": Key("d d"),

})
