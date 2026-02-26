## Issue: Missing §66 Mandatory Liikennevahinkolautakunta Consultation Requirement

### Law Reference
**§66 (Velvollisuus pyytää lausuntoa liikennevahinkolautakunnalta):**

Vakuutusyhtiön on **velvollinen** pyytämään liikennevahinkolautakunnan lausuntoa, jos päätöksessä on kysymys:
1. **Pysyvän ansionmenetyksen** taikka **kuoleman perusteella suoritettavasta jatkuvasta korvauksesta** tai sen sijasta suoritettavasta kertakaikkisesta pääoma-arvosta;
2. **Jatkuvan korvauksen korottamisesta tai alentamisesta** vahingonkorvauslain 5 luvun 8 §:n perusteella;
3. **Haitan perusteella suoritettavasta korvauksesta**, jos vamma on vaikea;
4. **Virheellisen päätöksen oikaisusta asianosaisen vahingoksi**, jos asianosainen ei suostu virheen korjaamiseen; lausuntoa ei tarvitse kuitenkin pyytää, jos virhe on ilmeinen ja se on aiheutunut asianosaisen omasta menettelystä tai jos kysymyksessä on ilmeinen kirjoitus- tai laskuvirhe.

**§66(2):** Jos vakuutusyhtiön päätös poikkeaa lautakunnan lausunnosta korvauksensaajan vahingoksi, vakuutusyhtiön on liitettävä lausunto päätökseensä ja annettava päätös tiedoksi lautakunnalle.

### Gap Description
The DMN rules contain §65 (P4) regarding the **right** to request a Liikennevahinkolautakunta opinion, but **§66's mandatory consultation requirement** is completely missing. This is a critical compliance gap because:

1. **§65** = Optional right for parties to request opinion (within 1 year)
2. **§66** = Mandatory obligation for insurers to obtain opinion in specific cases

Without §66, the DMN cannot enforce the insurer's legal duty to consult the Lautakunta before making decisions on:
- Permanent disability pensions
- Death benefits (continuous or lump sum)
- Adjustments to ongoing compensation
- Severe disability compensation
- Correcting erroneous decisions

### Suggested DMN Addition

```markdown
#### P4a: Mandatory Liikennevahinkolautakunta Consultation (§66)

| decision.type | decision.category | disability.isPermanent | disability.isSevere | decision.isCorrectionOfError | error.isObvious | error.causedByClaimant | Output |
|--------------|-------------------|----------------------|-------------------|------------------------------|-----------------|----------------------|--------|
| Compensation | PermanentEarningsLoss | true | any | false | N/A | N/A | **MandatoryConsultation_Required** |
| Compensation | DeathBenefit | N/A | N/A | false | N/A | N/A | **MandatoryConsultation_Required** |
| Adjustment | Increase/Decrease | N/A | N/A | false | N/A | N/A | **MandatoryConsultation_Required** |
| Compensation | DisabilityPayment | any | true | false | N/A | N/A | **MandatoryConsultation_Required** |
| Correction | ErrorCorrection | any | any | true | false | N/A | **MandatoryConsultation_Required** |
| Correction | ErrorCorrection | any | any | true | true | true | **MandatoryConsultation_NotRequired** |
| Correction | ErrorCorrection | any | any | true | true | false | **MandatoryConsultation_Required** |
| any | other | any | any | false | N/A | N/A | **MandatoryConsultation_NotRequired** |

**§66(1):** Vakuutusyhtiön on velvollinen pyytämään liikennevahinkolautakunnan lausuntoa, jos päätöksessä on kysymys...

**§66(2) Follow-up Rule:**

| consultation.obtained | decision.differsFromOpinion | decision.affectsClaimantNegatively | consultation.attachedToDecision | consultation.notifiedToLautakunta | Output |
|----------------------|----------------------------|-----------------------------------|--------------------------------|----------------------------------|--------|
| true | true | true | true | true | **Compliant** |
| true | true | true | false | any | **NonCompliant_AttachmentMissing** |
| true | true | true | true | false | **NonCompliant_NotificationMissing** |
| true | false | any | N/A | N/A | **Compliant** |
| false | N/A | N/A | N/A | N/A | **NonCompliant_ConsultationMissing** |
```

### Severity
**CRITICAL** - This is a mandatory legal requirement. Decisions made without mandatory consultation may be legally challengeable.

### Related Rules
- P4 (§65) - Optional opinion request right (parties)
- P4a (§66) - Mandatory consultation obligation (insurer) ← **MISSING**

### Checklist
- [ ] Add P4a rule table for §66(1) mandatory consultation triggers
- [ ] Add P4b rule table for §66(2) post-consultation requirements
- [ ] Add variable definitions for `disability.isSevere`, `error.isObvious`, etc.
- [ ] Create test cases for each mandatory consultation scenario
