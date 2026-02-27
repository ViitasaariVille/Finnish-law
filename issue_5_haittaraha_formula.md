## Gap Description

The ontology mentions haittaraha (permanent damage compensation) classes 1-20 but omits the critical calculation formula for combining multiple injuries.

### Current Ontology (Section 4 - PermanentDamageCompensation)

```
PermanentDamageCompensation
- Legal Basis: Sections 83-87
- Classes: 1-20 based on severity
```

### What Law Actually Says (§84)

**§84(4) - Formula for Combining Multiple Injuries:**

When combining disability classes for multiple injuries, use this formula:

```
      A × B
K = A + B - ─────
       20
```

Where:
- **K** = Total disability class (kokonaishaitan luokka)
- **A** = Larger injury class
- **B** = Smaller or equal injury class

**§84(4) - Example Calculation:**
If injury A = class 10 and injury B = class 5:
```
      10 × 5
K = 10 + 5 - ────── = 15 - 2.5 = 12.5 → rounds to 13
       20
```

**§84(4) - For Three or More Injuries:**
First combine the two largest using the formula, then combine that result with the next largest, repeating until all injuries are included.

**§84(5) - Exceptions:**
The formula does NOT apply to:
- Injuries to paired organs (eyes, kidneys, etc.) that substitute for each other
- Combined vision AND hearing loss

**§84(6) - Alternative Assessment:**
If standard methods don't work, assess based on overall functional impairment (yleinen toiminnanvajaus). Maximum class is 20.

## Haittaraha Compensation Table (§86)

The ontology correctly references §86 but doesn't include the actual rates:

| Class | % of Base | Annual Amount (€12,440 base) |
|-------|-----------|------------------------------|
| 1 | 1.15% | €143.06 |
| 2 | 2.27% | €282.39 |
| 3 | 3.36% | €417.98 |
| ... | ... | ... |
| 10 | 10.15% | €1,262.66 |
| ... | ... | ... |
| 20 | 60% | €7,464.00 |

**§87(1) - Payment Methods:**
- Classes 1-5: **Lump sum** (kertakaikkinen)
- Classes 6-20: **Continuous** (jatkuva) annual payments

## Discrepancy

| Aspect | Ontology | Law | Status |
|--------|----------|-----|--------|
| Classes 1-20 | Mentioned | Yes | ✓ |
| Combination formula | Missing | §84(4) formula | ❌ MISSING |
| Paired organ exception | Missing | §84(5) | ❌ MISSING |
| Payment method (lump vs continuous) | Missing | §87(1) | ❌ MISSING |
| Base amount (€12,440) | Missing | §86 | ❌ MISSING |

## Impact

**MEDIUM:** Without the formula:
1. Cannot correctly calculate total disability for multiple injuries
2. May overpay or underpay compensation
3. Paired organ injuries calculated incorrectly

## Suggested Fix

Update Section 4 - PermanentDamageCompensation:

```markdown
### PermanentDamageCompensation
- **Legal Basis**: Sections 83-87
- **Base Amount**: €12,440 per year (§86)
- **Classes**: 1-20 based on severity
- **Combination Formula** (for multiple injuries):
  ```
        A × B
  K = A + B - ─────
         20
  ```
  Where K=total class, A=larger, B=smaller
- **Formula Exceptions**: Paired organs, combined vision+hearing (§84(5))
- **Payment Method**:
  - Classes 1-5: Lump sum (kertakaikkinen)
  - Classes 6-20: Continuous annual (jatkuva)
- **Rates**: See §86 table (1.15% to 60% of base)
```

## References

- §83 (11 luku - Haittaraha definition)
- §84 (11 luku - Haittaluokan määrittäminen - including formula)
- §86 (11 luku - Haittarahan määrä - compensation table)
- §87 (11 luku - Haittarahan maksaminen - payment methods)

## Severity

**MEDIUM** - Missing calculation method

---

Tagging @VilleMoltBot for review
