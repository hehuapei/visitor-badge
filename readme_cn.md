<h1 align="center">👀 Visitor Badge · 访客计数徽章</h1>
<p align="center">
  一个免费、轻量的访客计数器徽章，适用于 GitHub README、Issues、Wiki 页面。
  <br>一行 Markdown，无需注册，无追踪，仅仅一个徽章。
</p>

<p align="center">
  <a href="#快速开始">快速开始</a> ·
  <a href="#参数说明">参数说明</a> ·
  <a href="#示例">示例</a> ·
  <a href="#自托管部署">自托管部署</a> ·
  <a href="README.md">English</a>
</p>

<p align="center">
  <img src="https://visitor-badge.laobi.icu/badge?page_id=hehuapei.visitor-badge&left_text=Visitors" alt="visitor badge">
</p>

---

## 快速开始

在你的 `README.md` 中添加一行：

```markdown
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=用户名.仓库名)
```

将 `用户名.仓库名` 替换为你的页面唯一标识即可。

---

## 参数说明

除 `page_id` 外，所有参数均为可选。

| 参数 | 必填 | 说明 | 默认值 |
|---|---|---|---|
| `page_id` | ✅ | 页面的唯一标识 | — |
| `left_text` | — | 徽章左侧文字 | `visitors` |
| `left_color` | — | 左侧颜色（名称或 HEX） | `#595959` |
| `right_color` | — | 右侧颜色（名称或 HEX） | `#1283c3` |
| `format` | — | 数值缩写（1K / 1M） | 关闭 |
| `radius` | — | 徽章圆角大小 | `3` |
| `height` | — | 徽章高度（px），等比例缩放 | `20` |
| `query_only` | — | 仅查询，不增加计数 | 关闭 |

> **注意：** HEX 颜色中的 `#` 需编码为 `%23`。  
> 示例：`#595959` → `%23595959`

---

## 示例

**默认样式**

```markdown
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=jwenjian.visitor-badge)
```

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=jwenjian.visitor-badge)

**自定义颜色**

```markdown
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=jwenjian.visitor-badge&left_color=red&right_color=green)
```

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=jwenjian.visitor-badge&left_color=red&right_color=green)

**自定义标题**

```markdown
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=jwenjian.visitor-badge&left_text=浏%20%20览)
```

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=jwenjian.visitor-badge&left_text=浏%20%20览)

**数值缩写（1K / 1M）**

```markdown
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=jwenjian.visitor-badge&format=true)
```

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=jwenjian.visitor-badge&format=true)

**仅查询，不增加计数**

```markdown
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=jwenjian.visitor-badge&query_only=true)
```
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=jwenjian.visitor-badge&query_only=true)

**组合使用**

```markdown
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=jwenjian.visitor-badge&left_text=浏%20%20览&left_color=%23595959&right_color=%231283c3&format=true)
```
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=jwenjian.visitor-badge&left_text=浏%20%20览&left_color=%23595959&right_color=%231283c3&format=true)

---

## 在 HTML 中使用

```html
<img src="https://visitor-badge.laobi.icu/badge?page_id=用户名.仓库名" alt="visitor badge">
```

---

## 自托管部署

```bash
git clone https://github.com/hehuapei/visitor-badge.git
cd visitor-badge
pip install -r requirements.txt
# 在 main.py 中配置计数服务地址
python3 main.py
```

需要搭配一个兼容的计数后端服务。详见 `main.py` 中的配置。

---

## 功能特性

- ✅ 完全免费，无需注册
- ✅ 自定义左右颜色
- ✅ 自定义徽章文字
- ✅ 数值缩写显示（1K / 1M）
- ✅ 仅查询模式（不计入计数）
- ✅ 每日自动数据备份
- ✅ 轻量 SVG 响应

---

## 致谢

Fork 自 [jwenjian/visitor-badge](https://github.com/jwenjian/visitor-badge)，进行了优化和基础设施更新。

---

<p align="center">
  <a href="https://github.com/hehuapei/visitor-badge">⭐ 给个 Star</a>
</p>
