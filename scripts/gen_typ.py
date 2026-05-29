import sys, argparse
from pathlib import Path

def generate_typ(filename, size_str, font_str):
    typs_dir = Path("typs")
    typs_dir.mkdir(exist_ok=True)
    typ_path = Path(f"{filename}.typ")

    if not typ_path.exists():
        print(f"Error: Typst file not found for {filename}")
        sys.exit(1)

    if not any(c.isalpha() for c in size_str):
    		size_str = size_str + "pt"

    fonts = [f.strip() for f in font_str.split(",") if f.strip()]
    font_array = "(" + ", ".join(f'"{f}"' for f in fonts) + ",)"

    original_content = typ_path.read_text(encoding="utf-8")
    content = f"""#import "../scripts/receipt-template.typ": *
#show: receipt-layout.with(size: {size_str}, font: {font_array})

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
    parser.add_argument("--font", default="Sarasa Mono SC", help="Font(s), comma-separated (default: Sarasa Mono SC)")
    args = parser.parse_args()
    generate_typ(args.filename, args.size, args.font)