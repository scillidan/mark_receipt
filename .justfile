# == Default options
# size: 8(pt)
# font: MonaspiceNe NFM, Sarasa Mono SC
# == Usage
# just add <filename> [<size>] ["<font1>,<font2>..."]

add name size="" font="":
  mkdir -p jpgs pdfs typs
  uv run scripts/gen_typ.py "{{name}}" \
    {{ if size != "" { "--size " + size } else { "" } }} \
    {{ if font != "" { "--font \"" + font + "\"" } else { "" } }}
  typst compile --root . "typs/{{name}}.typ" "pdfs/{{name}}.pdf"
  magick -density 150 "pdfs/{{name}}.pdf" -background white -alpha remove -quality 90 "jpgs/{{name}}_p%02d.jpg"