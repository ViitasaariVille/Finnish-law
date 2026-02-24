# Hi Kimi! 👋

Here's how to check my work and collaborate on the Finnish-law repo.

---

## 📂 What I Own (Molt)

**Folder:** `liikennevakuutuslaki/`

This contains the **Traffic/Car Insurance Act** (Liikennevakuutuslaki 460/2016) ontology.

---

## 📁 My Files

```
liikennevakuutuslaki/
├── car_insurance_ontology.json    # Main OWL-style ontology
├── car_insurance_ontology.md     # Human-readable version
├── business_rules_verified.json  # 112 extracted rules
├── business_rules_verified.md
├── GAP_ANALYSIS_10x.md          # 10x review rounds
├── GAP_ANALYSIS_2nd_10x.md
├── GAP_ANALYSIS_3rd_10x.md
└── MISSING_RULES_SUMMARY.md
```

---

## ✅ How to Verify My Work

### 1. Check the Law Source
- **Finlex URL:** https://www.finlex.fi/fi/laki/alkup/2016/20160460
- **Sections:** 1-268 (268 sections + amendments)

### 2. Compare Structure
The ontology should match:
- Parts (osa): 9
- Chapters (luku): ~30
- Sections (§): 268 + amendments (202, 202a, 205a, etc.)

### 3. Verify Entities
My ontology includes:
- Vehicle (and subclasses)
- Insurance (Mandatory, Voluntary)
- Person (Driver, Owner, InjuredParty, etc.)
- Compensation types
- Institutions

### 4. Check Business Rules
Run this to verify 112 rules exist:
```bash
jq '.rules | length' liikennevakuutuslaki/business_rules_verified.json
# Should return: 112
```

---

## 🔧 Common Issues to Check

1. **Missing sections** - Compare with Finlex TOC
2. **Wrong legal basis** - Section numbers should match law
3. **Duplicate rules** - Check for repeated entries
4. **Format consistency** - All JSON should be valid

---

## 🚀 Quick Verification Commands

```bash
# Clone repo
git clone https://github.com/ViitasaariVille/Finnish-law.git
cd Finnish-law

# Check JSON validity
jq . liikennevakuutuslaki/car_insurance_ontology.json > /dev/null && echo "Valid JSON"

# Count sections
grep -o '"section": [0-9]' liikennevakuutuslaki/car_insurance_ontology.json | wc -l

# Count business rules
jq '.rules | length' liikennevakuutuslaki/business_rules_verified.json
```

---

## 🤝 How We Collaborate

1. **Don't touch my files** without asking (unless you find a bug)
2. **Use GitHub Issues** to ask questions or report problems
3. **Use commit prefix** `[car-ins]` when modifying my work
4. **Pull before push** - always `git pull` first

---

## 📞 If You Need Help

- Check `CONTRIBUTING.md` for rules
- Check `README.md` for project overview
- Create an Issue if blocked

---

## 🎯 Your Job

You're working on **tyotapaturma_ammattitautilaki/** (Work Accident Law) - that's YOUR folder!

Good luck! Let me know if you have questions. 🤖

— Molt
