# size: 8 (default)
# font: MonaspiceNe NFM, Sarasa Mono SC

add name size="":
	mkdir -p jpgs pdfs typs
	python scripts/gen_typ.py "{{name}}" \
		{{ if size != "" { "--size " + size } else { "" } }}
	typst compile --root . "typs/{{name}}.typ" "pdfs/{{name}}.pdf"
	magick -density 150 "pdfs/{{name}}.pdf" -background white -alpha remove -quality 90 "jpgs/{{name}}_p%02d.jpg"