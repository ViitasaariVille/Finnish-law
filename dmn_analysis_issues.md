# DMN Rules Analysis - Issues Found

## 1. [BUG] E8 Property Damage Table Column Misalignment
**Location:** Section 2.2, E8 table

**Issue:** The column values are misaligned with headers in row 3.

**Current (incorrect):**
```
| Vehicle | PartialDamage | any | **RepairCost** |
```

**Should be:**
```
| Vehicle | any | PartialDamage | **RepairCost** |
```

The `PartialDamage` and `any` values are swapped.

**Severity:** MEDIUM - Could cause incorrect calculations

---

## 2. [TYPO] Duplicate Section Numbering "2.7"
**Location:** Multiple places in file

**Issue:** Two sections both labeled "2.7":
- 2.7 Medical Treatment Workflow (§§56-59) - Lines ~501-550
- 2.7 Large Loss Distribution System (§75) - Lines ~900+

**Fix:** Renumber second to 2.8

---

## 3. [TYPO] Duplicate "0.2" Section Numbers
**Location:** Early sections

**Issue:** Two sections labeled "0.2":
- 0.2 LVK Scope and Application (§4)
- 0.2 Border Traffic Insurance (§7)

**Fix:** Renumber second to 0.3, adjust subsequent numbering

---

## 4. [INCONSISTENCY] "0.x" Numbering Should Be Integrated
**Location:** Multiple "0.x" sections

**Sections affected:**
- 0.1 Contract Validity
- 0.2 LVK Scope
- 0.2 Border Traffic (duplicate)
- 0.3 Policy Termination

**Suggestion:** Integrate into main 1.x/2.x/3.x hierarchy

---

## 5. [NOTICE] Section 1.1.1 Formatting
**Location:** Line ~1000

The section "1.1.1 Extended Exemptions" uses three-level numbering which is inconsistent with the rest of the document (mostly using two levels like 1.1, 2.1, etc.)

---

*Analysis by MerriMoltBot using Gemini - 2026-02-26*
