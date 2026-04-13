<!-- Context: grass/navigation | Priority: high | Version: 1.0 | Updated: 2026-04-12 -->

# GRASS GIS Context Navigation

**Purpose**: GRASS-specific standards and patterns for g.opencoder addon development

---

## Structure

```
.opencode/context/grass/
├── standards/
│   ├── code-quality.md     # Python code standards (CRITICAL)
│   ├── python-patterns.md # Reference patterns
│   └── documentation.md # Docs standards
└── navigation.md         # This file
```

---

## Quick Routes

| Task | Path |
|------|------|
| **Write Python code** | `grass/standards/code-quality.md` |
| **GRASS patterns** | `grass/standards/python-patterns.md` |
| **Documentation** | `grass/standards/documentation.md` |

---

## Context Hierarchy

1. **code-quality.md** (CRITICAL) - Always load for Python coding
2. **python-patterns.md** - Reference patterns for GRASS operations
3. **documentation.md** - For README/man page creation

---

## Related Contexts

- `core/standards/code-quality.md` - General code standards
- `core/standards/test-coverage.md` - Testing standards