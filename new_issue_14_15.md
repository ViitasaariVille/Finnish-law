## Gap Description

The DMN rules are missing **Sections 14-15** which define consequences for policyholder violations of disclosure obligations and risk increase notifications.

## Law Requirements

### §14 - Disclosure Obligation Violation (tiedonantovelvollisuus)
**§22 of Insurance Contracts Act reference**

If policyholder intentionally or through gross negligence fails disclosure obligation:
- Insurer can retroactively charge higher premium
- If person wrongly listed as policyholder, both parties liable for premium
- Insurer can terminate policy within 14 days of discovering violation

### §15 - Risk Increase Notification Failure (vaaran lisääntyminen)
**§26(1-2) of Insurance Contracts Act reference**

If policyholder intentionally or through non-minor negligence fails to report risk increase:
- Insurer can retroactively charge higher premium

## Why This Matters

These sections define insurer rights when policyholders violate their duties. While §3 makes detrimental contract terms void, these sections provide legitimate remedies for insurer when policyholder acts in bad faith.

## Missing DMN Rules

**Suggested:**
- `VIOLATION-001: Disclosure Obligation Violation Consequences (§14)`
- `VIOLATION-002: Risk Increase Notification Failure Consequences (§15)`

### §14 Decision Table

| violation.type | violation.intent | higherPremium.wouldHaveApplied | insurer.action | Output |
|---------------|------------------|-------------------------------|----------------|--------|
| Disclosure | intentional | true | RetroactiveCharge | **HigherPremium_Due** |
| Disclosure | grossNegligence | true | RetroactiveCharge | **HigherPremium_Due** |
| Disclosure | any | false | NoAction | **NoPremiumAdjustment** |
| WrongPolicyholder | intentional | N/A | Termination+BothLiable | **Termination_14Days** |

### §15 Decision Table

| notification.failure | failure.intent | higherPremium.wouldApply | Output |
|---------------------|----------------|-------------------------|--------|
| true | intentional | true | **RetroactivePremiumIncrease** |
| true | nonMinorNegligence | true | **RetroactivePremiumIncrease** |
| true | minorNegligence | any | **NoConsequence** |

## Severity

**HIGH** - Important for contract enforcement and policyholder obligations.

## Reference

Liikennevakuutuslaki §§14-15

---
*Identified during law compliance check - February 26, 2026*

cc @VilleMoltBot