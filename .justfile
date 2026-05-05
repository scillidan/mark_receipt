add $name:
	mkdir -p jpgs pdfs typs
	uv run scripts/gen_typ.py "{{name}}"
	typst compile --root . "typs/{{name}}.typ" "pdfs/{{name}}.pdf"
	magick -density 150 "pdfs/{{name}}.pdf" -background white -alpha remove -quality 90 "jpgs/{{name}}_p%02d.jpg"

add-la $name:
	mkdir -p jpgs pdfs typs
	uv run scripts/gen_typ.py "{{name}}" --font "MonaspiceNe NFM"
	typst compile --root . "typs/{{name}}.typ" "pdfs/{{name}}.pdf"
	magick -density 150 "pdfs/{{name}}.pdf" -background white -alpha remove -quality 90 "jpgs/{{name}}_p%02d.jpg"

add-zh $name:
	mkdir -p jpgs pdfs typs
	uv run scripts/gen_typ.py "{{name}}" --font "Sarasa Mono SC"
	typst compile --root . "typs/{{name}}.typ" "pdfs/{{name}}.pdf"
	magick -density 150 "pdfs/{{name}}.pdf" -background white -alpha remove -quality 90 "jpgs/{{name}}_p%02d.jpg"