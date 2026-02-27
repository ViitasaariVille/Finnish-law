## Problem

The DMN rules (P5) have the basic structure for delay interest calculation but are **missing detailed formulas and the €7.28 minimum threshold adjustment mechanism**.

**Law (§67):**
> "Viivästyskorotusta tai viivästyskorkoa, jonka määrä on pienempi kuin 7,28 euroa, ei makseta. Rahamäärä tarkistetaan kalenterivuosittain työntekijän eläkelain 96 §:ssä tarkoitetulla palkkakertoimella."

## Gap Analysis

| Requirement | DMN Status |
|-------------|------------|
| Basic interest calculation | ✅ P5 structure exists |
| €7.28 minimum threshold | ⚠️ Mentioned |
| Annual palkkakerroin adjustment | ❌ **MISSING** |
| Detailed formulas | ❌ **MISSING** |
| Exception handling | ❌ **MISSING** |

## Impact

Incorrect interest calculations and outdated minimum thresholds.

## Suggested Fix

Complete **P5** with:

1. Annual minimum adjustment formula: `newMinimum = €7.28 × palkkakerroin[currentYear]`
2. Detailed interest calculation formulas
3. Force majeure exception handling
4. Victim-caused delay exception

## References
- laws/liikennevakuutuslaki.txt §67
- Current DMN: P5 (incomplete)

---
**Severity:** CRITICAL - Payment accuracy
**Section:** §67
**Tagging @VilleMoltBot for review
