import sys, argparse
from pathlib import Path

def generate_typ(filename, size_str):
    typs_dir = Path("typs")
    typs_dir.mkdir(exist_ok=True)
    typ_path = Path(f"{filename}.typ")

    if not typ_path.exists():
        print(f"Error: Typst file not found for {filename}")
        sys.exit(1)

    if not any(c.isalpha() for c in size_str):
    		size_str = size_str + "pt"

    original_content = typ_path.read_text(encoding="utf-8")
    content = f"""#import "../scripts/receipt-template.typ": *
#show: receipt-layout.with(size: {size_str})

{original_content}
"""
    generated_path = typs_dir / f"{filename}.typ"
    generated_path.write_text(content, encoding="utf-8")
    print(f"Created: {generated_path}")
    return generated_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Typst file from Typst")
    parser.add_argument("filename", help="Typst filename (without .typ extension)")
    parser.add_argument("--size", default="8pt", help="Font size (default: 8pt)")
    args = parser.parse_args()
    generate_typ(args.filename, args.size)