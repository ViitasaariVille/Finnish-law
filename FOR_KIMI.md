# Hi Kimi! 👋

You're the **reviewer** for this Finnish law ontology project.

---

## 📋 Your Role

- **Model:** Kimi K2 (Moonshot AI)
- **Job:** Review my (Molt's) work and suggest improvements
- **How:** GitHub Issues, PR comments

---

## 📂 What to Review

**Folder:** `liikennevakuutuslaki/` (Traffic/Car Insurance Act)

**Files to check:**
| File | Description |
|------|-------------|
| `car_insurance_ontology.json` | Main OWL-style ontology |
| `car_insurance_ontology.md` | Human-readable version |
| `business_rules_verified.json` | 46 verified business rules |

---

## ✅ Verification Steps

### 1. Check against Finlex Law
- URL: https://www.finlex.fi/fi/laki/alkup/2016/20160460
- Sections: 1-268 + amendments

### 2. Verify JSON is valid
```bash
jq . liikennevakuutuslaki/car_insurance_ontology.json > /dev/null && echo "Valid JSON"
```

### 3. Check rule count
```bash
jq '.business_rules | length' liikennevakuutuslaki/business_rules_verified.json
# Should return: 46
```

---

## 🔍 What to Look For

1. **Missing sections** - Compare with Finlex TOC
2. **Wrong legal basis** - Section numbers match law?
3. **Missing entities** - Any important concepts not captured?
4. **Relationship errors** - Are connections correct?
5. **Format issues** - JSON valid?

---

## 💬 How to Report Issues

### Create GitHub Issue
1. Go to: https://github.com/ViitasaariVille/Finnish-law/issues
2. Click "New Issue"
3. Use format:
   - **Title:** `[car-ins] <issue description>`
   - **Body:** Explain what to change and why

### Example Issues
- `[car-ins] Missing entity: DrivingLicense`
- `[car-ins] Section 45 has wrong legal basis`
- `[car-ins] Suggestion: Add relationship between Vehicle and Owner`

---

## 🔄 Sync Before Reviewing

Always pull latest before reviewing:
```bash
git pull origin master
```

---

## 📞 If You Need Help

- Check `CONTRIBUTING.md` for full guidelines
- Check `README.md` for project overview

---

Thanks for reviewing! 🎯

— Molt
