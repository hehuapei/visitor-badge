import json
from functools import lru_cache
from pathlib import Path
from urllib.parse import quote

CATALOG_PATH = Path(__file__).with_name('data') / 'simple_icons.json'


def svg_data_uri(svg):
    return 'data:image/svg+xml;utf8,' + quote(svg)


@lru_cache(maxsize=1)
def load_logo_catalog():
    with CATALOG_PATH.open(encoding='utf-8') as f:
        return json.load(f)


@lru_cache(maxsize=None)
def resolve_logo(name):
    if not name:
        return None

    slug = name.strip().lower()
    icon = load_logo_catalog().get(slug)
    if not icon:
        return None

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="{icon["viewBox"]}" fill="#fff">'
        f'{icon["body"]}'
        f'</svg>'
    )
    return svg_data_uri(svg)


def list_logos():
    catalog = load_logo_catalog()
    return [
        {'slug': slug, 'label': icon['label']}
        for slug, icon in sorted(catalog.items())
    ]
