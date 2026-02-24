# Contributing Guide

## 🤖 Agent Collaboration

This repository is maintained by multiple AI agents working on different Finnish law ontologies.

### Current Agents

| Agent | Owner | Model | Domain |
|-------|-------|-------|--------|
| **Molt** | Boss | MiniMax-M2.5 | liikennevakuutuslaki |
| **Kimi** | Boss | Kimi K2 (Moonshot) | Reviewer - checks all work |

---

## 📋 Rules of Engagement

### 1. Respect Domain Boundaries
- Each agent owns their law folder
- Don't modify another agent's files without permission
- Use Issues for cross-domain questions

### 2. Communication via GitHub
- **Issues**: Task tracking, questions, blockers
- **Commits**: Clear, prefixed messages
- **PRs**: For review (optional, can merge directly if simple)

### 3. Before Editing
```bash
# Always pull first
git pull origin master

# Create feature branch
git checkout -b <law>-<description>
```

### 4. After Editing
```bash
# Stage your changes
git add .

# Commit with prefix
git commit -m "[<domain>] <type>: <description>"

# Push
git push -u origin <branch-name>
```

---

## 📁 File Naming Convention

| Type | Pattern | Example |
|------|---------|---------|
| Ontology JSON | `<law>_ontology.json` | `car_insurance_ontology.json` |
| Ontology MD | `<law>_ontology.md` | `car_insurance_ontology.md` |
| Business Rules | `business_rules_verified.json` | `business_rules_verified.json` |
| Gap Analysis | `GAP_ANALYSIS*.md` | `GAP_ANALYSIS_10x.md` |

---

## 🏗️ Ontology Structure

Each law should have:

1. **JSON Ontology** - Machine readable
   - Entities with attributes
   - Subclasses
   - Legal basis references (section numbers)
   - Relationships

2. **Markdown Documentation** - Human readable
   - Overview table
   - Entity descriptions
   - Relationships

3. **Business Rules** (optional)
   - Extracted verified rules
   - Gap analysis

---

## 🚨 Conflict Resolution

If you encounter conflicts:

1. Don't force push
2. Open an Issue with:
   - Which file(s) conflict
   - What you're trying to do
   - Tag the other agent: @moltbotville or @kimi-bot
3. Wait for coordination before proceeding

---

## ✅ Checklist Before Push

- [ ] Pulled latest changes
- [ ] Created feature branch (or using master for small fixes)
- [ ] Files follow naming convention
- [ ] Commit message has correct prefix
- [ ] No changes to other agent's domain files

---

## 📞 Emergency Contact

If repo is broken or need urgent help:
- Create GitHub Issue with `urgent` label
- Tag both agents

---

*Happy collaborating! 🤝*
