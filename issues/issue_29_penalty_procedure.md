Title: [MISSING] §29 Penalty Decision Procedure - No DMN rule for penalty assessment process
Labels: critical

## Gap Description

The DMN rules are missing coverage for **Section 29** of the Traffic Insurance Act (Liikennevakuutuslaki 460/2016), which governs the procedure for penalty decisions when insurance obligation is neglected.

## Law Requirements (§29)

1. **§29(1):** LVK makes proposal to Valtiokonttori for penalty assessment
2. **§29(2):** Valtiokonttori decides on penalties and payment obligations
3. **§29(3):** Vehicle owner/holder can appeal to administrative court (hallintolainkäyttölaki 586/1996)
4. **§29(4):** Payments assessed against holder first, then owner if holder is insolvent
5. **§29(5):** LVK bills and collects payments

## Missing DMN Rule

**Suggested:** Create `PEN-001: Penalty Decision Procedure (§29)`

### Decision Table Structure
| lvk.proposalMade | valtiokonttori.decision | appeal.filed | appeal.accepted | payment.assessedAgainst | Output |
|-----------------|------------------------|--------------|-----------------|------------------------|--------|
| true | PenaltyImposed | false | N/A | Holder | **PaymentRequired_Holder** |
| true | PenaltyImposed | false | N/A | Owner | **PaymentRequired_Owner** |
| true | PenaltyImposed | true | true | any | **AppealSuccessful_PenaltyCancelled** |
| true | PenaltyImposed | true | false | any | **AppealDenied_PaymentRequired** |

## Severity
**CRITICAL** - This is an important enforcement procedure that affects how penalties are assessed and collected when vehicle owners fail to insure their vehicles.

## Reference
Liikennevakuutuslaki §29

---
*Identified during automated compliance check - 2026-02-26*
*cc @VilleMoltBot*
