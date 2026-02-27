## Problem

The DMN rules (MOP-001, P4b) list the mandatory consultation triggers for Liikennevahinkolautakunta but **lack the complete workflow enforcement** including the §66(3) requirement to attach the opinion when the insurer's decision differs.

**Law (§66(1)-(3)):**
Mandatory consultation required for:
1. Continuous compensation for permanent loss OR death
2. Increase/decrease of continuous compensation
3. Severe disability compensation
4. Correction of erroneous decision against claimant's interest

**§66(3):** If insurer's decision differs from Lautakunta opinion against claimant, insurer must attach opinion to decision and notify Lautakunta.

## Gap Analysis

| Requirement | DMN Status |
|-------------|------------|
| Mandatory triggers listed | ✅ MOP-001 implemented |
| Exceptions mentioned | ✅ Implemented |
| Workflow enforcement | ❌ **MISSING** |
| §66(3) attachment requirement | ❌ **MISSING** |

## Impact

Mandatory procedural requirement may be skipped, or opinions may not be properly attached when decisions differ.

## Suggested Fix

Add workflow rules:

1. **Pre-decision check**: Is consultation mandatory for this case type?
2. **Opinion received**: Lautakunta opinion attached to file
3. **Decision divergence check**: Does decision differ from opinion?
4. **§66(3) enforcement**: If differs against claimant → attach opinion + notify Lautakunta

## References
- laws/liikennevakuutuslaki.txt §66
- Current DMN: MOP-001, P4b (incomplete)

---
**Severity:** CRITICAL - Mandatory legal procedure
**Section:** §66
**Tagging @VilleMoltBot for review
