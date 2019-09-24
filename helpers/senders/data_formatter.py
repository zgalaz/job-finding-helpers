def as_html(r):
    content = [f'<a href="{p.get("url")}">{p.get("txt")}</a> {p.get("emp", "")} {p.get("loc", "")}' for p in r]
    return '<ol>' + ' '.join(f'<li>{m}</li>' for m in content) + '</ol>'


def as_plain(r):
    return '\r\n'.join(f'{p.get("url")} {p.get("txt")} {p.get("emp", "")} {p.get("loc", "")}' for p in r)
