<p align="center">
  <img src="https://visitor-badge.laobi.icu/badge?page_id=hehuapei.visitor-badge&left_text=Visitors" alt="visitor badge">
</p>

<h1 align="center">👀 Visitor Badge</h1>
<p align="center">
  A free, lightweight visitor counter badge for your GitHub README, Issues, and Wiki pages.
  <br>One line of Markdown. No sign-up. No tracking. Just a badge.
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> ·
  <a href="#parameters">Parameters</a> ·
  <a href="#examples">Examples</a> ·
  <a href="#deploy">Self-host</a>
</p>

---

## Quick Start

Add this line to your `README.md`:

```markdown
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=yourname.yourrepo)
```

Replace `yourname.yourrepo` with a unique identifier for your page. Done.

---

## Parameters

All parameters are optional except `page_id`.

| Parameter | Required | Description | Default |
|---|---|---|---|
| `page_id` | ✅ | Unique identifier for your page | — |
| `left_text` | — | Left-side label | `visitors` |
| `left_color` | — | Left side color (name or hex) | `#595959` |
| `right_color` | — | Right side color (name or hex) | `#1283c3` |
| `format` | — | Compact number display (1K / 1M) | disabled |
| `query_only` | — | Query without incrementing counter | disabled |

> **Note:** For hex colors with `#`, URL-encode `#` as `%23`.  
> Example: `#595959` → `%23595959`

---

## Examples

**Default style**

```markdown
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=jwenjian.visitor-badge)
```

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=jwenjian.visitor-badge)

**Custom colors**

```markdown
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=jwenjian.visitor-badge&left_color=red&right_color=green)
```

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=jwenjian.visitor-badge&left_color=red&right_color=green)

**Custom label**

```markdown
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=jwenjian.visitor-badge&left_text=Views)
```

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=jwenjian.visitor-badge&left_text=Views)

**Compact format (1K / 1M)**

```markdown
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=jwenjian.visitor-badge&format=true)
```

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=jwenjian.visitor-badge&format=true)

**Query only (don't increment)**

```markdown
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=jwenjian.visitor-badge&query_only=true)
```

**Combo: all together**

```markdown
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=jwenjian.visitor-badge&left_text=Views&left_color=%23595959&right_color=%231283c3&format=true)
```

---

## Use in HTML

```html
<img src="https://visitor-badge.laobi.icu/badge?page_id=yourname.yourrepo" alt="visitor badge">
```

---

## Self-host

Clone the repo, install dependencies, and run:

```bash
git clone https://github.com/hehuapei/visitor-badge.git
cd visitor-badge
pip install -r requirements.txt
# Set your count API endpoint in main.py
python3 main.py
```

Requires a compatible counting backend. The project expects a count service at a configurable endpoint. See `main.py` for details.

---

## Features

- ✅ Free & no registration
- ✅ Custom colors (left & right)
- ✅ Custom label text
- ✅ Compact number format (1K / 1M)
- ✅ Query-only mode (no count increment)
- ✅ Daily data backup
- ✅ Lightweight SVG response

---

## Credits

Forked from [jwenjian/visitor-badge](https://github.com/jwenjian/visitor-badge) with optimizations and updated infrastructure.

---

<p align="center">
  <a href="https://github.com/hehuapei/visitor-badge">⭐ Star on GitHub</a>
</p>
