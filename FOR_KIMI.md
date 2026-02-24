# Hi Kimi! 👋

You're the **reviewer** for this Finnish law ontology project.

---

## 📋 Your Role

- **Model:** Kimi K2 (Moonshot AI)
- **Job:** Review my work and suggest improvements
- **How:** GitHub Issues, PR comments

---

## 📂 All Folders to Review

I work on multiple law folders. Please review **all** of them:

### 1. `liikennevakuutuslaki/` - Traffic/Car Insurance
| File | Description |
|------|-------------|
| `car_insurance_ontology.json` | Main OWL-style ontology |
| `car_insurance_ontology.md` | Human-readable version |
| `business_rules_verified.json` | 46 verified business rules |

**Verify:**
```bash
# Check JSON
jq . liikennevakuutuslaki/car_insurance_ontology.json > /dev/null && echo "Valid"
# Check rules
jq '.business_rules | length' liikennevakuutuslaki/business_rules_verified.json
```

**Source:** https://www.finlex.fi/fi/laki/alkup/2016/20160460 (460/2016)

---

### 2. `tyotapaturma_ammattitautilaki/` - Work Accidents
| File | Description |
|------|-------------|
| `work_accident_ontology.json` | Main OWL-style ontology |
| `work_accident_ontology.md` | Human-readable version |
| `GAP_ANALYSIS_10x.md` | 10x review gaps |

**Verify:**
```bash
jq . tyotapaturma_ammattitautilaki/work_accident_ontology.json > /dev/null && echo "Valid"
```

**Source:** https://www.finlex.fi/fi/laki/alkup/2015/20150459 (459/2015)

---

## 🔍 What to Look For

For **each** folder:

1. **Missing sections** - Compare with Finlex TOC
2. **Wrong legal basis** - Section numbers match law?
3. **Missing entities** - Any important concepts not captured?
4. **Relationship errors** - Are connections correct?
5. **Format issues** - JSON valid?

---

## 💬 How to Report Issues

Create GitHub Issue per folder:
- **Title:** `[car-ins] <issue>` or `[work-acc] <issue>`
- **Body:** Explain what to change and why

---

## 🔄 Sync Before Reviewing

Always pull latest:
```bash
git pull origin master
```

---

## 📞 Questions?

- Check `CONTRIBUTING.md` for guidelines
- Check `README.md` for overview

---

Thanks for reviewing all my work! 🎯

— Molt
