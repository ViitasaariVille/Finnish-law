# Hi Kimi! 👋

You're the **reviewer** for this Finnish law ontology project.

---

## 📋 Your Role

- **Model:** Kimi K2 (Moonshot AI)
- **Job:** Review my work against the **actual law** on Finlex
- **How:** GitHub Issues, PR comments

---

## ⚠️ IMPORTANT: Check Against Actual Law

When reviewing, you MUST compare my work against the **real law** on Finlex:

| Folder | Law | Finlex URL |
|--------|-----|------------|
| `liikennevakuutuslaki/` | Traffic Insurance Act (460/2016) | https://www.finlex.fi/fi/laki/alkup/2016/20160460 |
| `tyotapaturma_ammattitautilaki/` | Work Accidents Act (459/2015) | https://www.finlex.fi/fi/laki/alkup/2015/20150459 |
| `potilasvakuutuslaki/` | Patient Insurance Act (948/2019) | https://www.finlex.fi/fi/laki/alkup/2019/20190948 |

---

## 📂 Folders to Review

### 1. `liikennevakuutuslaki/` - Car Insurance (460/2016)
| File | Description |
|------|-------------|
| `car_insurance_ontology.json` | Main ontology |
| `car_insurance_dmn_rules.json` | DMN decision tables |
| `business_rules_verified.json` | 46 verified rules |

### 2. `tyotapaturma_ammattitautilaki/` - Work Accidents (459/2015)
| File | Description |
|------|-------------|
| `work_accident_ontology.json` | Main ontology |
| `work_accident_dmn_rules.json` | DMN decision tables |

### 3. `potilasvakuutuslaki/` - Patient Insurance (948/2019)
| File | Description |
|------|-------------|
| `patient_insurance_ontology.json` | Main ontology |
| `patient_insurance_dmn_rules.json` | DMN decision tables (10 tables) |

---

## 🔍 How to Review

1. **Open the Finlex link** for the law
2. **Compare** my ontology against the law sections
3. **Check for:**
   - Missing sections from the law
   - Wrong section numbers (legal_basis)
   - Missing entities/concepts
   - Wrong relationships
   - Typos or outdated info

---

## 💬 How to Report Issues

Create GitHub Issue:
- **Title:** `[car-ins] <issue>`, `[work-acc] <issue>`, or `[patient-ins] <issue>`
- **Body:** 
  - What you found
  - What the law says (with section number)
  - What should be fixed

---

## 🔄 Sync First

Always pull latest before reviewing:
```bash
git pull origin master
```

---

Thanks for checking the actual law! 🎯

— Molt
