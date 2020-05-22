from pygments.style import Style
from pygments.token import (
    Comment,
    Error,
    Generic,
    Keyword,
    Literal,
    Name,
    Number,
    Operator,
    Other,
    Punctuation,
    String,
    Text,
    Whitespace,
)

# Primary colours:
LEAF = "#13aa52"
FOREST = "#116149"
FOG = "#b3bbc1"
GRAPHITE = "#21313c"

# Secondary
MINT = "#B8E6CB"
FERN = "#12924F"
CHARCOAL = "#1A1A1A"
LEAD = "#798186"
SMOKE = "#F5F6F7"
CLOUD = "#FAFBFC"
MAGNOLIA = "#FEDC49"
BLUE_SKY = "#65C9DF"

a = 1 * 100


class MongoDark(Style):
    """
    This implements a MongoDB style.
    """

    background_color = GRAPHITE
    highlight_color = LEAD

    styles = {
        # No corresponding class for the following:
        Text: CLOUD,  # class:  ''
        Whitespace: "",  # class: 'w'
        Error: f"{MAGNOLIA} bg:#ff0000",  # class: 'err'
        Other: "",  # class 'x'
        Comment: LEAF,  # class: 'c'
        Comment.Multiline: "",  # class: 'cm'
        Comment.Preproc: "",  # class: 'cp'
        Comment.Single: "",  # class: 'c1'
        Comment.Special: "",  # class: 'cs'
        Keyword: f"{MINT} italic",  # class: 'k'
        Keyword.Constant: f"{MINT}",  # class: 'kc'
        Keyword.Declaration: "",  # class: 'kd'
        Keyword.Namespace: "",  # class: 'kn'
        Keyword.Pseudo: "",  # class: 'kp'
        Keyword.Reserved: "",  # class: 'kr'
        Keyword.Type: "",  # class: 'kt'
        Operator: BLUE_SKY,  # class: 'o'
        Operator.Word: "",  # class: 'ow' - like keywords
        Punctuation: BLUE_SKY,  # class: 'p'
        Name: CLOUD,  # class: 'n'
        Name.Attribute: "",  # class: 'na' - to be revised
        Name.Builtin: "",  # class: 'nb'
        Name.Builtin.Pseudo: "",  # class: 'bp'
        Name.Class: "",  # class: 'nc' - to be revised
        Name.Constant: "",  # class: 'no' - to be revised
        Name.Decorator: MINT,  # class: 'nd' - to be revised
        Name.Entity: "",  # class: 'ni'
        Name.Exception: "",  # class: 'ne'
        Name.Function: "",  # class: 'nf'
        Name.Property: "",  # class: 'py'
        Name.Label: "",  # class: 'nl'
        Name.Namespace: "",  # class: 'nn' - to be revised
        Name.Other: "",  # class: 'nx'
        Name.Tag: "",  # class: 'nt' - like a keyword
        Name.Variable: "",  # class: 'nv' - to be revised
        Name.Variable.Class: "",  # class: 'vc' - to be revised
        Name.Variable.Global: "",  # class: 'vg' - to be revised
        Name.Variable.Instance: "",  # class: 'vi' - to be revised
        Number: CLOUD,  # class: 'm'
        Number.Float: "",  # class: 'mf'
        Number.Hex: "",  # class: 'mh'
        Number.Integer: "",  # class: 'mi'
        Number.Integer.Long: "",  # class: 'il'
        Number.Oct: "",  # class: 'mo'
        Literal: CLOUD,  # class: 'l'
        Literal.Date: "",  # class: 'ld'
        String: MAGNOLIA,  # class: 's'
        String.Affix: BLUE_SKY,  # class: 'sa'
        String.Backtick: "",  # class: 'sb'
        String.Char: "",  # class: 'sc'
        String.Doc: "",  # class: 'sd' - like a comment
        String.Double: "",  # class: 's2'
        String.Escape: BLUE_SKY,  # class: 'se'
        String.Heredoc: "",  # class: 'sh'
        String.Interpol: BLUE_SKY,  # class: 'si'
        String.Other: "",  # class: 'sx'
        String.Regex: "",  # class: 'sr'
        String.Single: "",  # class: 's1'
        String.Symbol: "",  # class: 'ss'
        Generic: CLOUD,  # class: 'g'
        Generic.Deleted: "",  # class: 'gd',
        Generic.Emph: "",  # class: 'ge'
        Generic.Error: "",  # class: 'gr'
        Generic.Heading: "",  # class: 'gh'
        Generic.Inserted: "",  # class: 'gi'
        Generic.Output: "",  # class: 'go'
        Generic.Prompt: "",  # class: 'gp'
        Generic.Strong: "bold",  # class: 'gs'
        Generic.Subheading: "",  # class: 'gu'
        Generic.Traceback: "",  # class: 'gt'
    }
