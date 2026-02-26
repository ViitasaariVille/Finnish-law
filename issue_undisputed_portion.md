## Issue: Missing §62(3) Undisputed Portion Payment Requirement

### Law Reference
**§62 (Korvauksen suorittamisen määräaika), moment 3:**
> "Jos korvauksen määrä ei ole riidaton, vakuutusyhtiö on kuitenkin velvollinen suorittamaan 2 momentissa mainitussa ajassa korvauksen riidattoman osan."

**Translation:** "If the amount of compensation is disputed, the insurance company is nevertheless obliged to pay the undisputed portion of the compensation within the time referred to in paragraph 2."

### Gap Description
The DMN rules contain §62(1) and §62(2) regarding investigation start (7 business days) and payment deadline (1 month), but **§62(3) is missing**. This creates a compliance risk because:

1. When a claim amount is disputed, insurers must still pay the undisputed portion within the 1-month deadline
2. Without this rule, the DMN could incorrectly indicate a payment delay for partial payments
3. Claimants' rights to partial payment during disputes are not properly encoded

### Suggested DMN Addition

```markdown
#### T3a: Undisputed Portion Payment (§62(3))

| claim.amountDisputed | claim.undisputedAmount | undisputedPortion.determined | payment.date | Output |
|---------------------|------------------------|------------------------------|--------------|--------|
| true | > 0 | true | ≤ 1 month | **UndisputedPortion_Paid** |
| true | > 0 | true | > 1 month | **UndisputedPortion_Delayed** |
| true | 0 | N/A | any | **FullDispute_NoPartialPayment** |
| false | N/A | N/A | any | **FullPayment_Required** |

**§62(3):** Jos korvauksen määrä ei ole riidaton, vakuutusyhtiö on kuitenkin velvollinen suorittamaan 2 momentissa mainitussa ajassa korvauksen riidattoman osan.

**Key Points:**
- Undisputed portion must be calculated and paid within 1 month of receiving complete documents
- Only applies when liability is not in dispute, only the amount
- If entire amount is disputed, no partial payment required under this provision
```

### Severity
**HIGH** - This affects claimant rights and insurer obligations during disputes

### Checklist
- [ ] Add T3a rule table to Section 2.6 (Time Limits and Deadlines)
- [ ] Update E12b to reference undisputed portion logic
- [ ] Add test cases for disputed claims with partial payment
