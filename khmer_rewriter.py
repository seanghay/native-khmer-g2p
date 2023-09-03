from pynini import Far
from functools import partial
from pynini.lib import rewrite

filename = "automator_phonemic.far"

far = Far(filename, mode="r", arc_type="stardard", far_type="default")
fst = far["TO_PHONEMIC"]
rewriter = partial(
    rewrite.top_rewrite,
    rule=fst,
    input_token_type="byte",
    output_token_type="byte",
)

with open("result.tsv", "w") as outf:
    with open("native.txt") as f:
        for line in f:
            line = line.rstrip()
            try:
                pro = rewriter(line)
                outf.write(f"{line}\t{pro}\n")
            except Exception:
                pass
