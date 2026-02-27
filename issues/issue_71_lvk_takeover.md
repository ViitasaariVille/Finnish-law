## Problem

The DMN rules (FCR-001) cover the 3-month foreign representative deadline but the **LVK takeover workflow (§71)** is incomplete.

**Law (§70-71):**
- §70(2): Foreign representative must respond within 3 months
- §71: If no response in 3 months, victim can demand from LVK
- §71: LVK must start processing within 2 months of receiving claim

## Gap Analysis

| Requirement | DMN Status |
|-------------|------------|
| 3-month representative deadline | ✅ FCR-001 implemented |
| LVK takeover trigger | ⚠️ Partially implemented |
| 2-month LVK processing deadline | ❌ **MISSING** |
| Information notification chain | ❌ **MISSING** |

## Impact

Cross-border claims may stall without proper LVK intervention workflow.

## Suggested Fix

Complete **FCR-003: LVK Takeover Workflow (§71)**

| daysSinceClaim | representative.responded | victim.demandedFromLVK | daysSinceLVKReceipt | Output |
|---------------|------------------------|----------------------|---------------------|--------|
| >90 | false | true | ≤60 | **LVK_Processing** |
| >90 | false | true | >60 | **LVK_ProcessingOverdue** |
| >90 | true | any | any | **RepresentativeResponded_LVKT stops** |

## References
- laws/liikennevakuutuslaki.txt §§70-71
- Current DMN: FCR-001, FCR-003 (incomplete)

---
**Severity:** CRITICAL - International obligations
**Section:** §§70-71
**Tagging @VilleMoltBot for review
