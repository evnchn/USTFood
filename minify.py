import minify_html

with open("index.max.html", "r", encoding="utf-8") as file:

    minified = minify_html.minify(file.read(), minify_js=True, minify_css=False, do_not_minify_doctype=True, ensure_spec_compliant_unquoted_attribute_values=True, keep_spaces_between_attributes=True, remove_processing_instructions=True)

with open("index.html", "w", encoding="utf-8") as file:
    file.write(minified)