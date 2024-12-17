from __future__ import annotations
from argparse import ArgumentParser, Namespace
from enum import Enum, auto
import os
from pathlib import Path
from typing import Any, Dict, List, Literal, Optional
from subprocess import run
import platform

FILE_TYPES_TO_CLEAN: List[
    Literal["aux", "log", "toc", "blg", "bbl", "fdb_latexmk"]
] = ["aux", "log", "toc", "blg", "bbl", "fdb_latexmk"]


class OutputMethod(Enum):
    DELETE = auto()
    MOVE = auto()
    NO_OP = auto()

    def __str__(self) -> str:
        return self.name.lower()

    def __repr__(self):
        return super().__repr__()

    @classmethod
    def from_str(cls, s: str) -> OutputMethod:
        s = s.upper()
        if s == "DELETE":
            return cls.DELETE
        elif s == "MOVE":
            return cls.MOVE
        elif s == "NO_OP":
            return cls.NO_OP
        else:
            raise ValueError(f"Invalid OutputMethod: {s}")


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", type=str, help="Input file", required=True)
    parser.add_argument(
        "-o",
        "--output-method",
        type=str,
        choices=["delete", "move", "no_op"],
        default="move",
        help="Output method",
    )
    parser.add_argument("--output-dir", type=str, help="Output directory", default="./.tex_out")
    parser.add_argument("--open", action="store_true", help="Open the output PDF.", default=False)
    return parser.parse_args()


def build(
    input_file_path: Path,
    output_method: OutputMethod,
    output_dir: Optional[Path] = None,
) -> None:
    command = f"pdflatex {input_file_path} --interaction=nonstopmode"

    completed_process = run(command, shell=True)
    if completed_process.returncode != 0:
        print(f"Error building {input_file_path}")
        return

    files = [
        Path(f) for f in os.listdir() if f.endswith(tuple(FILE_TYPES_TO_CLEAN))
    ]

    if output_method == OutputMethod.DELETE:
        for file in files:
            file.unlink(missing_ok=True)
    elif output_method == OutputMethod.MOVE:
        assert (
            output_dir is not None
        ), "Output directory must be provided when output method is MOVE"
        os.makedirs(output_dir, exist_ok=True)
        for file in files:
            file.rename(output_dir / file.name)
    elif output_method == OutputMethod.NO_OP:
        pass


def main() -> None:
    args = parse_args()
    args: Dict[str, Any] = vars(args)

    input_file = Path(args["input"])
    output_method = OutputMethod.from_str(args["output_method"])
    output_dir = Path(args["output_dir"]) if args["output_dir"] is not None else None
    open_after = args["open"]

    print(f"Input file: {input_file}")
    print(f"Output method: {output_method}")
    print(f"Output directory: {output_dir}")

    build(input_file, output_method, output_dir)

    if open_after:
        pdf_path = input_file.with_suffix(".pdf")
        system = platform.system().lower()
        try:
            if system == "windows":
                os.startfile(pdf_path)
            elif system == "darwin":
                run(["open", pdf_path])
            else:
                run(["xdg-open", pdf_path])
        except Exception as e:
            print(f"Error opening file: {e}")
            raise e
    return
