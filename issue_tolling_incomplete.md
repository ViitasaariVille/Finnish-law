## Issue: Incomplete §79 Tolling Provisions - Missing "1-Year Safety Net"

### Law Reference
**§79 (Kanneaika), moments 2-4:**

> "Jos asia saatetaan vireille Vakuutuslautakunnassa, liikennevahinkolautakunnassa tai muussa kuluttajariitoja ratkaisevassa toimielimessä, kanneajan kuluminen keskeytyy menettelyn ajaksi. Kanneaika katsotaan katkenneeksi sinä päivänä, kun asian käsittely päättyy näissä toimielimissä."

> "Kanneajan ei katsota katkenneen, jos asian käsittely tuomioistuimessa tai 2 momentissa tarkoitetussa toimielimessä keskeytyy tai peruuntuu ennen kuin asia on ratkaistu. Tällöin kanneaika umpeutuu kuitenkin **aikaisintaan vuoden kuluessa menettelyn päättymisestä**. Kanneaikaa voidaan pidentää tällä tavoin **vain yhden kerran**."

### Gap Description
The DMN rules (E12c, T4) capture basic tolling when filing with Vakuutuslautakunta/ConsumerDisputeBody, but **miss two critical statutory protections**:

1. **The 1-Year Safety Net (§79(3)):**
   - If proceedings are interrupted/cancelled BEFORE resolution
   - The claimant has AT LEAST 1 year from when proceedings end
   - This protects claimants who file with Lautakunta but the process ends prematurely

2. **The "Only Once" Limitation (§79(4)):**
   - This extension can only happen ONE TIME
   - After one extension, no further tolling benefits apply

### Current DMN (Incomplete)
```markdown
| decision.receiptDate | court.filingDate | daysSinceDecision | dispute.body | Output |
|---------------------|------------------|-------------------|--------------|--------|
| any | any | any | Vakuutuslautakunta | **StatuteOfLimitationsTolled** |
```

### Suggested DMN Addition

```markdown
#### T4a: Tolling Safety Net and Limitations (§79(3)-(4))

| proceeding.filedWith | proceeding.status | proceeding.endDate | daysSinceProceedingEnd | previousExtensionUsed | remainingDaysAtStart | Output |
|---------------------|-------------------|-------------------|----------------------|---------------------|---------------------|--------|
| Lautakunta/Vakuutuslautakunta | Interrupted | known | ≤ 365 | false | any | **DeadlineExtended_To365Days** |
| Lautakunta/Vakuutuslautakunta | Interrupted | known | ≤ 365 | false | < 365 | **DeadlineExtended_1YearFromEnd** |
| Lautakunta/Vakuutuslautakunta | Interrupted | known | any | true | any | **NoExtension_AlreadyUsed** |
| Lautakunta/Vakuutuslautakunta | Cancelled | known | ≤ 365 | false | any | **DeadlineExtended_To365Days** |
| Lautakunta/Vakuutuslautakunta | Resolved | known | any | any | any | **NormalDeadlineCalculation** |
| ConsumerDisputeBody | Interrupted | known | ≤ 365 | false | any | **DeadlineExtended_To365Days** |
| ConsumerDisputeBody | Cancelled | known | ≤ 365 | false | any | **DeadlineExtended_To365Days** |
| Court | Interrupted | known | any | any | any | **Check79_3_Applies** |

**Key Rules:**
1. **§79(3) Safety Net:** If proceedings interrupt/cancel before resolution → minimum 1 year from end date
2. **§79(4) One-Time Limit:** This extension can ONLY be used once per claim
3. **Applies to:** Vakuutuslautakunta, Liikennevahinkolautakunta, Consumer Dispute Bodies, AND Courts

**Calculation Logic:**
```
if (proceedingInterrupted || proceedingCancelled) && !previousExtensionUsed:
    newDeadline = max(originalDeadline, proceedingEndDate + 365 days)
    previousExtensionUsed = true
else:
    use normal deadline calculation
```

**Variables to Add:**
- `proceeding.status`: Resolved | Interrupted | Cancelled | Ongoing
- `proceeding.endDate`: Date proceedings ended
- `previousExtensionUsed`: Boolean (tracked per claim)
- `remainingDaysAtStart`: Days remaining when proceeding was filed
```

### Severity
**HIGH** - Missing statutory protections could lead to premature claim rejection

### Example Scenarios

**Scenario 1 - Safety Net Needed:**
- Claimant files with Lautakunta 2.5 years after decision (6 months left)
- Lautakunta process interrupted after 3 months
- Without §79(3): Claimant has only 3 months left (3 months passed during proceedings)
- With §79(3): Claimant has 1 year from interruption date (statutory minimum)

**Scenario 2 - One-Time Limit:**
- Claimant uses extension once after first interruption
- Files again with different body, process interrupts again
- With §79(4): No second extension allowed

### Checklist
- [ ] Add T4a rule table for §79(3)-(4) tolling safety net
- [ ] Add `proceeding.status`, `previousExtensionUsed` variables
- [ ] Update E12c to reference T4a for interrupted proceedings
- [ ] Add test cases for interruption/cancellation scenarios
