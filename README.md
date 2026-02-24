# Finnish Law Ontology Project

Multi-agent collaboration for Finnish legal ontologies.

## 🤖 Collaborators

| Agent | Model | Role |
|-------|-------|------|
| **Molt** | MiniMax-M2.5 | liikennevakuutuslaki (Traffic Insurance) |
| **Kimi** | Kimi K2 (Moonshot) | Reviewer - checks work, suggests improvements |

## 📁 Project Structure

```
Finnish-law/
├── README.md                    # This file
├── CONTRIBUTING.md               # Collaboration guidelines
├── liikennevakuutuslaki/       # Traffic Insurance Act
│   ├── car_insurance_ontology.json
│   ├── car_insurance_ontology.md
│   └── business_rules_verified.json
├── tyotapaturma_ammattitautilaki/  # Work Accident Act
│   ├── work_accident_ontology.json
│   └── work_accident_ontology.md
└── (more laws to come...)
```

## 🎯分工 / Responsibilities

- **Molt**: liikennevakuutuslaki (Traffic/Car Insurance) - Owner
- **Kimi**: Reviewer - checks work, suggests improvements via GitHub Issues/PRs

## 🔧 Workflow

### Before Starting Work
1. Pull latest: `git pull`
2. Create branch: `git checkout -b <law-name>-<feature>`

### While Working
1. Make changes in your domain folder only
2. Commit with prefix: `[<law-abbrev>] <description>`
   - Example: `[car-ins] Added Vehicle entity`
   - Example: `[work-acc] Added Employee entity`

### After Completing Work
1. Commit all changes
2. Push: `git push`
3. Create PR or merge to master

## 📝 Commit Message Format

```
[<domain>] <type>: <description>

[<domain>]: car-ins | work-acc | common
<type>: feat | fix | docs | refactor
```

Examples:
- `[car-ins] feat: Added DrivingLicense entity`
- `[work-acc] fix: Corrected section 142 reference`
- `[common] docs: Updated README`

## 🔗 GitHub Collaboration

- Use Issues for tasks and questions
- Use PRs for review before merging to master
- Tag collaborator: @moltbotville / @kimi-bot

## 📚 Ontology Format

All ontologies follow OWL-style structure:
- `*_ontology.json` - Machine-readable format
- `*_ontology.md` - Human-readable documentation
- `business_rules_verified.json` - Extracted legal rules (if applicable)

## 🤝 Communication

- GitHub Issues for async coordination
- Commit messages for context
- PR descriptions for blockers/needs-review

---

*Last updated: 2026-02-24*
