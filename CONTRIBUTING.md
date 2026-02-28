# Contributing Guide

## 🤖 Agent Collaboration

This repository is maintained by multiple AI agents working on different Finnish law ontologies.

### Current Agents

| Agent | Owner | Model | Domain |
|-------|-------|-------|--------|
| **Molt** | Boss | MiniMax-M2.5 | liikennevakuutuslaki |
| **Kimi** | Boss | Kimi K2 (Moonshot) | Reviewer - checks all work |
| **Lumen** ⚖️ | Boss | Claude Sonnet 4.6 | Legal analysis - ontology validation & compliance |

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

### 🤖 AI-Assisted Development

This project uses AI assistance for certain tasks. When reviewing or building upon AI-generated contributions:

1. **Verify legal accuracy** — Always cross-check legal interpretations against primary sources (Finlex)
2. **Review ontology logic** — Validate that class hierarchies and relationships correctly reflect legal concepts
3. **Check citations** — Ensure section references (§) match the cited legal text

#### Identifying AI Contributions
Commits or issues created with AI assistance are typically tagged or documented. Look for:
- Issue/PR descriptions citing specific law sections with Finnish quotations
- Systematic comparison tables between ontology and legal text
- References to model version (e.g., "analysed using Claude Sonnet 4.6")

#### About Lumen
When Lumen operates in a legal analysis capacity, it uses **Claude Sonnet 4.6**. Lumen can be tagged in issues for:
- Ontology validation requests
- "Does the model cover §X?" queries
- Compliance checks between rules and legal text

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

## 🔄 Sync Strategy

### When to Pull

| When | Action |
|------|--------|
| **Before every push** | `git pull origin master` (mandatory) |
| **On session start** | Pull if working on repo |
| **On heartbeat** | Quick check: `git fetch origin && git status` |

### Workflow

```bash
# Before ANY push - always pull first!
git pull origin master
git push

# Heartbeat quick check (fetches, doesn't merge)
git fetch origin
git status
```

### What Kimi Should Do

1. **Before reviewing** - Pull latest to see my newest changes
2. **After creating Issues** - I'll see them when I pull/push
3. **Before suggesting changes** - Pull to ensure they're working with latest

---

## 🔧 Quick Commands

```bash
# Full sync before work
git pull origin master

# Check for changes without merging
git fetch origin && git status

# Check what changed
git log --oneline -5
```

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

If repo is broken or need urgent help:
- Create GitHub Issue with `urgent` label
- Tag both agents

---

*Happy collaborating! 🤝*
