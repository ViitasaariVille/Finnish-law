Title: [MISSING] §80 Court Proceedings and Legal Cost Coverage - No DMN rule for litigation
Labels: critical

## Gap Description

The DMN rules are missing coverage for **Section 80** of the Traffic Insurance Act, which governs court proceedings when victims sue outside the insurance claim process.

## Law Requirements (§80)

1. **§80(1):** When victim sues vehicle owner/holder/driver/passenger outside this law:
   - Compensation awarded under this law regardless
   - Judgment amount recoverable only from insurer
   - Insurer pays: compensation + legal costs + delay interest

2. **§80(2):** Court cannot hear case unless insurer refused compensation first

3. **§80(3):** Insurer must be summoned with 14-day notice (haasteen tiedoksi antaminen)

4. **§80(4):** Insurer has right to appeal district court and court of appeal decisions

## Missing DMN Rule

**Suggested:** Create `COURT-001: Court Proceedings and Legal Cost Coverage (§80)`

### Decision Table Structure
| insurer.refusedCompensation | victim.suedInCourt | insurer.summoned | notice.days | court.hearing | Output |
|---------------------------|-------------------|------------------|-------------|---------------|--------|
| true | true | true | ≥14 | Proceeds | **CourtAwardsCompensation_LegalCostsCovered** |
| false | true | any | any | CannotProceed | **CaseInadmissible_InsuranceClaimFirst** |
| true | true | false | any | Delayed | **SummonInsurer_14DayNoticeRequired** |

## Severity
**CRITICAL** - Critical for dispute resolution and understanding insurer's liability for legal costs.

## Reference
Liikennevakuutuslaki §80

---
*Identified during automated compliance check - 2026-02-26*
*cc @VilleMoltBot*
