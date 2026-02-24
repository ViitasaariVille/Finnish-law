# Finnish Work Accident Insurance - DMN Business Rules

**Based on:** Työtapaturma- ja ammattitautilaki (459/2015)  
**Version:** 1.1  
**DMN Version:** 1.3  
**Source:** https://www.finlex.fi/fi/laki/alkup/2015/20150459

---

## 1. Insurance Obligation

**Legal Source:** Part I, Sections 1-14

| Person Type | Employment Status | Insurance Required | Legal Basis | Source Text |
|-------------|-------------------|-------------------|------------|-------------|
| Employee | employed | MandatoryInsurance | Section 3(1) | Työnantajan on otettava vakuutus |
| Employee | probation | MandatoryInsurance | Section 3(1) | Koeaikana vakuutusvelvollisuus |
| Employee | contract | MandatoryInsurance | Section 3(2) | Työsopimuksen perusteella |
| Entrepreneur | YEL_insured | VoluntaryWorkTimeInsurance | Sections 188-190 | Yrittäjän vapaaehtoinen vakuutus |
| Farmer | any | Excluded | Section 11 | Maa- ja metsätalousyrittäjät |
| ForeignWorker | EU | MandatoryInsurance | Section 8(1) | EU-kansalaiset |
| ForeignWorker | non_EU | Check bilateral | Section 8(2) | Kolmansien maiden kansalaiset |

---

## 2. Compensable Event

**Legal Source:** Part II, Sections 15-35

| Event Type | Location | Timing | Compensable | Legal Basis | Source Text |
|------------|----------|--------|-------------|-------------|-------------|
| WorkplaceAccident | workplace | during_work | Compensable | Section 17(1) | Työtapaturma |
| WorkplaceAccident | workplace | before_after | Compensable | Section 18 | Muut vammat |
| WorkplaceAccident | workplace | breaks | Compensable | Section 17(3) | Tauolla |
| CommuteAccident | home_work_route | direct_route | Compensable | Section 21(1) | Kotimatkan aikana |
| CommuteAccident | home_work_route | detour_necessary | Compensable | Section 21(2) | Välttämätön kiertotie |
| CommuteAccident | home_work_route | detour_personal | Not compensable | Section 21(3) | Oma-aloitteinen kiertotie |
| BusinessTripAccident | work_travel | during_travel | Compensable | Section 22 | Työmatkalla |
| BusinessTripAccident | accommodation | any | Compensable | Section 23 | Majoituksen aikana |
| BusinessTripAccident | free_time | during_trip | Limited | Section 24 | Vapaa-aikana |
| OccupationalDisease | any | diagnosed | Compensable | Section 26(1) | Ammattitauti |
| RepetitiveStrainInjury | any | any | Compensable | Section 33 | Yksipuolinen kuormitus |
| ViolenceIncident | work_related | during_work | Compensable | Section 34 | Väkivalta |
| PsychologicalInjury | work_related | serious | Compensable | Section 35 | Psykografkinen sairaus |

---

## 3. Compensation Type

**Legal Source:** Part III, Sections 36-109

| Injury Type | Severity | Duration | Compensation Type | Legal Basis | Source Text |
|-------------|----------|----------|-------------------|-------------|-------------|
| PhysicalInjury | minor | < 1 year | MedicalExpenses | Section 36 | Sairaanhoito |
| PhysicalInjury | moderate | 1-3 years | MedicalExpenses + LostWages | Sections 36, 55 | Sairaanhoito + ansionmenetys |
| PhysicalInjury | severe | > 3 years | MedicalExpenses + LostWages + Disability | Sections 36, 55, 83 | Kokonaiskorvaus |
| PhysicalInjury | permanent | any | PermanentDisabilityCompensation | Section 83(1) | Pysyvä haitta |
| OccupationalDisease | any | any | MedicalExpenses + LostWages | Sections 26-32 | Ammattitaudin korvaus |
| MentalInjury | moderate | any | Rehabilitation | Section 88(1) | Kuntoutus |
| Death | any | any | DeathCompensation | Section 99(1) | Kuoleman korvaus |

---

## 4. Compensation Amount

**Legal Source:** Part III, Sections 36-109

| Compensation Type | Income | Severity | Work Ability Lost | Formula | Legal Basis | Source Text |
|-------------------|--------|----------|-------------------|---------|-------------|-------------|
| LostWages | any | any | 100% | income.annual / 365 × days | Section 56(1) | Täysi ansionmenetys |
| LostWages | any | any | 50% | income.annual / 365 × days × 0.5 | Section 56(2) | Osittainen ansionmen LostWages |etys |
| any | any | 0% | 0 | Section 56 | Ei ansionmenetystä |
| PermanentDisability | any | 10-19% | any | income.annual × 0.1 | Section 84(1) | Haittalisä 10-19% |
| PermanentDisability | any | 20-50% | any | income.annual × 0.2 | Section 84(1) | Haittalisä 20-50% |
| PermanentDisability | any | 51-100% | any | income.annual | Section 84(2) | Täysi haittalisä |
| Death | any | any | any | Section 99-109 rates | Sections 99-109 | Kuoleman korvaukset |

---

## 5. Medical Care Coverage

**Legal Source:** Part III, Sections 36-54

| Treatment Type | Necessity | Provider | Coverage | Legal Basis | Source Text |
|---------------|-----------|----------|----------|-------------|-------------|
| EmergencyCare | required | public | 100% | Section 37(1) | Julkisen terveydenhuollon hoito |
| EmergencyCare | required | private | 100% (reimbursement) | Section 37(2) | Yksityisen hoidon korvaus |
| Surgery | required | any | 100% | Section 38(1) | Leikkaushoito |
| Medicines | prescribed | pharmacy | 100% (drug list) | Section 45 | Lääkkeet |
| Rehabilitation | medical_necessity | any | 100% | Section 88(1) | Kuntoutus |
| DentalTreatment | accident_related | any | 100% | Section 48 | Hammashoito |
| TravelToTreatment | required | any | Kilometre allowance | Section 50 | Matkakustannukset |
| Prosthesis | required | any | 100% | Section 47 | Silmälasit, proteesit |

---

## 6. Claim Time Limit

**Legal Source:** Part IV, Section 110

| Claim Type | Injury Timing | Time Limit | Legal Basis | Source Text |
|------------|---------------|------------|-------------|-------------|
| WorkAccident | within_3_years | 3 years from accident | Section 110(1) | 3 vuoden määräaika |
| WorkAccident | after_3_years | Claim barred | Section 110(3) | Määräajan umpeutuminen |
| OccupationalDisease | any | 3 years from diagnosis | Section 110(2) | Ammattitaudin määräaika |
| DeathBenefit | within_3_years | 3 years from death | Section 110(1) | Kuoleman korvaus |
| SurvivorBenefit | any | 3 years from death | Section 110(1) | Leskeneläke |

---

## 7. Rehabilitation Eligibility

**Legal Source:** Part III, Sections 88-98

| Injury Severity | Work Ability Reduced | Medical Recommendation | Eligible | Legal Basis | Source Text |
|-----------------|---------------------|----------------------|----------|-------------|-------------|
| severe | yes | yes | Full rehabilitation | Section 88(1) | Ammatillinen kuntoutus |
| moderate | yes | yes | Vocational rehabilitation | Section 89(1) | Ammatillinen kuntoutus |
| minor | no | no | Medical rehabilitation only | Section 88(1) | Lääkinnällinen kuntoutus |
| any | any | no | Not eligible | Section 88(1) | Ei oikeutta kuntoutukseen |

---

## 8. Insurance Premium

**Legal Source:** Part V, Sections 156-186

| Industry Risk | Payroll | Claims History | Premium Formula | Legal Basis | Source Text |
|---------------|---------|---------------|----------------|-------------|-------------|
| low_risk | any | no_claims | payroll × 0.005 | Section 166(1) | Vakuutusmaksun peruste |
| medium_risk | any | no_claims | payroll × 0.01 | Section 166(1) | Vakuutusmaksun peruste |
| high_risk | any | no_claims | payroll × 0.02 | Section 166(1) | Korkea riski |
| any | any | with_claims | base_premium + risk loading | Sections 171-176 | Lisämaksu |

---

## 9. Appeals Process

**Legal Source:** Part VIII, Sections 237-247

| Decision Type | Disagreement | Appeal Path | Legal Basis | Source Text |
|---------------|--------------|-------------|-------------|-------------|
| Rejection | yes | Appeal to Insurance Company → Accident Board | Section 237(1) | Valitus vakuutusyhtiölle |
| AmountDispute | yes | Appeal to Accident Compensation Board | Section 238 | Tapaturma-asianlautakunta |
| LateDecision | yes | Complaint + Late interest | Section 146 | Viivästyskorotus |
| AnyDecision | no | No appeal | N/A | Ei valitusta |

---

## 10. Survivor Benefits

**Legal Source:** Part III, Sections 99-109

| Survivor Relationship | Age | Deceased Contributory | Benefit | Legal Basis | Source Text |
|-----------------------|-----|----------------------|---------|-------------|-------------|
| Spouse | any | yes | Spouse pension | Section 100(1) | Leskeneläke |
| Spouse | any | no | Lump sum | Section 107(1) | Kertakorvaus |
| Child | under_18 | yes | Child pension + orphan allowance | Sections 101-102 | Lapseneläke |
| Child | 18-24_student | yes | Student orphan pension | Section 103 | Opiskelijan eläke |
| Dependent | any | yes | Dependent allowance | Section 105 | Huollettavan korvaus |

---

## Legal Reference Summary

| Part | Sections | Topic |
|------|----------|-------|
| Part I | 1-14 | General Provisions |
| Part II | 15-35 | Compensable Events |
| Part III | 36-109 | Benefits |
| Part IV | 110-155 | Implementation |
| Part V | 156-186 | Insurance & Premium |
| Part VI | 187-204 | Voluntary Insurance |
| Part VII | 205-236c | Implementation System |
| Part VIII | 237-247 | Appeals |
| Part IX | 248-278 | Miscellaneous |
| Part X | 279-286 | Enforcement |

---

## JSON Format (Machine-Readable)

See `work_accident_dmn_rules.json` for DMN-compatible JSON format that can be imported into:
- Camunda DMN
- Drools DMN
- IBM Operational Decision Manager
- Flowable DMN
