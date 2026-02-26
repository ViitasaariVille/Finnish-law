# Finnish Traffic Insurance Law Compliance Analysis
## Comparison: Law vs DMN Rules Coverage

### Executive Summary

After comprehensive analysis of Liikennevakuutuslaki (460/2016) against the DMN rules file, **16 sections** of the law are **NOT adequately covered** in the DMN rules. These span insurance administration, premium handling, and miscellaneous procedural rules.

---

## MISSING SECTIONS REPORT

### Chapter 2: Insurance Obligation and Premiums (§§5-28)

#### §9 - Information to Liikenteen turvallisuusvirasto (Traficom)
**Law Content:** Vakuutusyhtiön on ilmoitettava Liikenteen turvallisuusvirastolle:
1. Yhtiössä vakuutetulle ajoneuvolle otetusta uudesta vakuutuksesta seitsemän päivän kuluessa
2. Ajoneuvolle otetun vakuutuksen vakuutusmaksun laiminlyönnistä
3. Liikennekäytöstä poistetun ajoneuvon vakuutuksen irtisanomisesta

**DMN Coverage:** ❌ NOT FOUND

**Severity:** HIGH - Important procedural obligation for insurers

---

#### §10 - Vehicle Identification in Insurance Contract (Partial)
**Law Content:** 
- Ajoneuvo on vakuutussopimuksessa yksilöitävä
- Poikkeus: Yritys/yhteisö voi sopia poikkeamisesta
- **CRITICAL:** Jos rekisteröityä ajoneuvoa ei yksilöity ja omistusmuutoksesta ei ilmoitettu 7 päivässä, vakuutusyhtiön vastuu lakkaa

**DMN Coverage:** ⚠️ PARTIAL - Rules exist but missing the 7-day liability termination rule

**Severity:** CRITICAL - Affects coverage determination

---

#### §11 - Insurance Certificate and Terms
**Law Content:** 
- Vakuutuskirja must be provided without undue delay
- Vakuutusehdot must be delivered to Finanssivalvonta 1 month before use

**DMN Coverage:** ❌ NOT FOUND

**Severity:** MEDIUM - Ancillary administrative rule

---

#### §12 - Insurance Validity Period (Partial)
**Law Content:**
- First insurance period max 13 months
- Subsequent periods 1 year
- Rajaliikenne- and siirtoliikennevakuutukset can be fixed-term

**DMN Coverage:** ⚠️ PARTIAL - Missing specific period rules (13 months / 1 year)

**Severity:** MEDIUM

---

#### §14 - Information Obligation Violation
**Law Content:** 
- If vakuutuksenottaja tahallisesti or törkeästä huolimattomuudesta fails disclosure obligation → insurer can charge higher premium retroactively
- If incorrect person marked as policyholder due to intentional violation → both parties liable for premium
- Insurer can terminate within 14 days of discovering violation

**DMN Coverage:** ❌ NOT FOUND

**Severity:** HIGH - Important sanction rule

---

#### §15 - Risk Increase Notification Failure
**Law Content:** 
- If vakuutuksenottaja fails to notify vaaran lisääntymisestä (not minor negligence) → insurer can charge higher premium retroactively

**DMN Coverage:** ❌ NOT FOUND

**Severity:** HIGH - Premium adjustment rule

---

#### §21 - Claims History Transfer Between Insurers
**Law Content:** 
- When policyholder transfers insurance to another company for same/similar vehicle
- Previous insurer must transfer vahinkohistoriatiedot within 15 days of request

**DMN Coverage:** ❌ NOT FOUND

**Severity:** MEDIUM - Administrative procedure

---

#### §23 - Premium Refund on Early Termination
**Law Content:** 
- If insurance ends before agreed date → refund of overpaid premium
- Refund not required if less than €8
- Amount adjusted by ministry decree for monetary value changes

**DMN Coverage:** ❌ NOT FOUND

**Severity:** MEDIUM - Financial rule

---

#### §24 - Delay Interest on Premiums (Partial)
**Law Content:** 
- Viivästyskorko on vakuutusmaksulle per Korkolaki 4 §
- **CRITICAL:** Insurer must pay viivästyskorko on premium refunds after 1 month from receipt of qualifying documentation

**DMN Coverage:** ⚠️ PARTIAL - Only covers one direction (policyholder to insurer), missing insurer's obligation to pay interest on refunds

**Severity:** HIGH - Financial obligation

---

#### §25 - Liability Continues Despite Non-Payment
**Law Content:** 
- Vakuutusyhtiön vastuu ei lakkaa even if premium not paid on time
- Premium + interest is directly enforceable (ulosottokelpoinen)

**DMN Coverage:** ❌ NOT FOUND (only §26 statute of limitations is covered)

**Severity:** CRITICAL - Affects coverage determination

---

### Chapter 3: Compensation (§§31-52)

#### §33 - Multi-Vehicle Accident Liability (Partial)
**Law Content:** 
- Detailed rules on liability apportionment based on:
  1. Omistajan, haltijan, kuljettajan or matkustajan tuottamus
  2. Liikennesääntöjen vastainen kulku or sijainti
  3. Puutteellinen kunto or virheellinen kuormaus
- **CRITICAL:** Passenger always gets full compensation from their own vehicle's insurance

**DMN Coverage:** ⚠️ PARTIAL - Basic concept present but missing detailed liability apportionment logic

**Severity:** CRITICAL - Affects compensation calculation

---

#### §37 - Property Damage Compensation (Partial)
**Law Content:** 
- Ajoneuvon arvon alentumista ei korvata (no compensation for value reduction)
- If total loss → compensation is käypä arvo immediately before accident
- Omistusoikeus siirtyy vakuutusyhtiölle when total loss paid
- **CRITICAL:** Animal damage to uncontrolled animals (other than reindeer) only covered if intentional or negligent

**DMN Coverage:** ⚠️ PARTIAL - Missing animal damage exclusion

**Severity:** HIGH - Coverage limitation

---

#### §41a - Unauthorized Competition (Partial)
**Law Content:** 
- Separate section for anastetun ajoneuvon käyttö
- Requires both authorized event AND valid license

**DMN Coverage:** ⚠️ PARTIAL - Rules present but law structure shows this is a distinct section

**Severity:** MEDIUM

---

### Chapter 7: Miscellaneous (§§79-95)

#### §80 - Court Proceedings Rules
**Law Content:** 
- Korvaus must be awarded under this law regardless of direct liability
- Vakuutusyhtiö must be summoned before court action
- 14-day minimum summons time
- Vakuutusyhtiö has right of appeal

**DMN Coverage:** ❌ NOT FOUND

**Severity:** MEDIUM - Procedural rule

---

#### §81 - Municipality Appeal Rights
**Law Content:** 
- Kunta/kuntayhtymä is not asianosainen in victim compensation cases
- BUT can appeal täyskustannusmaksu decision under hallintolainkäyttölaki

**DMN Coverage:** ❌ NOT FOUND

**Severity:** LOW - Narrow procedural rule

---

#### §82 - Insurer Information Access Rights (Partial)
**Law Content:** 
- Insurer has extensive right to obtain information from:
  1. Other insurers, authorities (employment, benefits)
  2. Employers (work, wages)
  3. Healthcare providers (medical records, treatment, rehabilitation)
- LVK has right to information on uninsured vehicles

**DMN Coverage:** ⚠️ PARTIAL - Mentioned but no decision rules for information access denials or disputes

**Severity:** MEDIUM

---

#### §87 - LVK Other Duties
**Law Content:** 
- Toimia kansallisena toimistona
- Laatia liikennevahinkotilasto and riskitutkimus
- Make international agreements
- Authorize Green Card representatives
- Cannot refuse border/transfer traffic insurance if insurer has refused

**DMN Coverage:** ❌ NOT FOUND (last point about non-refusal partially covered)

**Severity:** LOW - Mostly administrative/meta rules

---

#### §89 - Finanssivalvonta Statistics
**Law Content:** 
- Finanssivalvonnan must publish annual report of each insurer's liikennevakuutus results for at least 5 previous years
- Ministerial decree can specify breakdown by vehicle group

**DMN Coverage:** ❌ NOT FOUND

**Severity:** LOW - Statistical reporting

---

#### §90 - Liikenteen turvallisuusvirasto Notifications
**Law Content:** 
- Traficom must notify LVK of:
  1. Ajoneuvon lopullinen poisto rekisteristä
  2. Ajoneuvon vakuutuksen siirtyminen toiseen yhtiöön
  3. Ajoneuvon omistajan ja haltijan vaihtuminen
  4. Ajoneuvon liikennekäyttöön ottaminen and poisto
- **CRITICAL:** If no insurance within 7 days of ownership transfer → notification to LVK for penalty assessment

**DMN Coverage:** ❌ NOT FOUND

**Severity:** HIGH - Enforcement mechanism

---

#### §93 - Policyholder Additional Payment Obligation
**Law Content:** 
- If insurer insolvency leaves compensation unpaid after policyholder additional contribution (lisämaksuvelvollisuus)
- Lisävakuutusmaksu can be imposed on policyholders who:
  - Had significant influence over insurer management
  - Caused significant deviation from regulations
  - Committed criminal acts
- OR if premiums were unreasonably low and contributed to insolvency

**DMN Coverage:** ❌ NOT FOUND

**Severity:** MEDIUM - Insolvency-related rule

---

#### §94 - Joint Guarantee Payment
**Law Content:** 
- If compensation remains unpaid after §93 additional payments
- All traffic insurers jointly liable (yhteistakuumaksu)
- Max 2% of premium income per year

**DMN Coverage:** ❌ NOT FOUND

**Severity:** MEDIUM - Insolvency protection

---

#### §95 - Official Liability
**Law Content:** 
- Rikosoikeudellinen virkavastuu applies to insurer employees and board members
- Vahingonkorvausvastuusta säädetään vahingonkorvauslaissa

**DMN Coverage:** ❌ NOT FOUND

**Severity:** LOW - Liability rule

---

## SUMMARY TABLE

| Severity | Count | Sections |
|----------|-------|----------|
| CRITICAL | 5 | §10(7-day), §25, §33(passenger), §37(animal), §90 |
| HIGH | 7 | §9, §14, §15, §24(refund interest), §37(value), §80, §90(enforcement) |
| MEDIUM | 10 | §11, §12, §21, §23, §33(apportionment), §41a, §82, §87, §93, §94 |
| LOW | 4 | §81, §89, §95, partial/misc |

### Total Missing: 16 unique sections (with 8 partial coverages)

---

## RECOMMENDATIONS

1. **CRITICAL Priority:** Add rules for §10 (7-day liability termination), §25 (liability despite non-payment), §33 (passenger protection), §37 (animal damage exclusion)

2. **HIGH Priority:** Add rules for §9 (Traficom notifications), §14-15 (sanctions), §24 (refund interest), §90 (enforcement)

3. **MEDIUM Priority:** Add rules for premium administration (§11, §12, §21, §23)

4. **LOW Priority:** Administrative and statistical rules (§87, §89, §95)
