## Problem

The DMN rules (M1) mention the notification requirement from healthcare providers but **do not enforce the 4-business-day deadline** with consequences for non-compliance.

**Law (§56(2)):**
> "Jos hoitoon hakeutumisen tai myöhemmän hoitokäynnin yhteydessä päätetään toimenpiteestä... terveydenhuollon toimintayksikön on lähetettävä suunnitelma tai päätös vakuutusyhtiölle neljän arkipäivän kuluessa päivästä, jona potilasasiakirjamerkinnät on... tehtävä."

## Gap Analysis

| Requirement | DMN Status |
|-------------|------------|
| Notification requirement | ✅ M1 mentioned |
| 4-business-day deadline | ⚠️ **Not enforced** |
| Consequences of late notification | ❌ **MISSING** |

## Impact

Late notifications from healthcare providers not handled per statute, potentially affecting täyskustannusmaksu eligibility.

## Suggested Fix

Update **M1** with enforcement:

| treatment.decisionDate | notification.sentDate | daysElapsed | Output |
|------------------------|----------------------|-------------|--------|
| any | within 4 business days | ≤4 | **Compliant_FullCostPayment** |
| any | after 4 business days | >4 | **NotificationDelayed_CustomerFeeOnly** |

## References
- laws/liikennevakuutuslaki.txt §56(2)
- Current DMN: M1 (incomplete)

---
**Severity:** CRITICAL - High-volume claim type
**Section:** §56
**Tagging @VilleMoltBot for review
