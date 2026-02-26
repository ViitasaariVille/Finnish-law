# Finnish Work Accident Insurance - DMN Business Rules

**Based on:** Työtapaturma- ja ammattitautilaki (459/2015)  
**Version:** 1.1  
**DMN Version:** 1.3  
**Source:** https://www.finlex.fi/fi/laki/alkup/2015/20150459

---

## 1. Insurance Obligation

**Legal Source:** Part I, Sections 1-14

| **OUTPUT: Insurance Required** | Person Type | Employment Status | Legal Basis | Source Text |
|-------------------------------|-------------|-------------------|-------------|-------------|
| MandatoryInsurance | Employee | employed | Section 3(1) | Työnantajan on otettava vakuutus |
| MandatoryInsurance | Employee | probation | Section 3(1) | Koeaikana vakuutusvelvollisuus |
| MandatoryInsurance | Employee | contract | Section 3(2) | Työsopimuksen perusteella |
| VoluntaryWorkTimeInsurance | Entrepreneur | YEL_insured | Sections 188-190 | Yrittäjän vapaaehtoinen vakuutus |
| Excluded | Farmer | any | Section 11 | Maa- ja metsätalousyrittäjät |
| MandatoryInsurance | ForeignWorker | EU | Section 8(1) | EU-kansalaiset |
| Check bilateral | ForeignWorker | non_EU | Section 8(2) | Kolmansien maiden kansalaiset |

---

## 2. Compensable Event

**Legal Source:** Part II, Sections 15-35

| **OUTPUT: Compensable** | Event Type | Location | Timing | Legal Basis | Source Text |
|------------------------|------------|----------|--------|-------------|-------------|
| Compensable | WorkplaceAccident | workplace | during_work | Section 17(1) | Työtapaturma |
| Compensable | WorkplaceAccident | workplace | before_after | Section 18 | Muut vammat |
| Compensable | WorkplaceAccident | workplace | breaks | Section 17(3) | Tauolla |
| Compensable | CommuteAccident | home_work_route | direct_route | Section 21(1) | Kotimatkan aikana |
| Compensable | CommuteAccident | home_work_route | detour_necessary | Section 21(2) | Välttämätön kiertotie |
| Not compensable | CommuteAccident | home_work_route | detour_personal | Section 21(3) | Oma-aloitteinen kiertotie |
| Compensable | BusinessTripAccident | work_travel | during_travel | Section 22 | Työmatkalla |
| Compensable | BusinessTripAccident | accommodation | any | Section 23 | Majoituksen aikana |
| Limited | BusinessTripAccident | free_time | during_trip | Section 24 | Vapaa-aikana |
| Compensable | OccupationalDisease | any | diagnosed | Section 26(1) | Ammattitauti |
| Compensable | RepetitiveStrainInjury | any | any | Section 33 | Yksipuolinen kuormitus |
| Compensable | ViolenceIncident | work_related | during_work | Section 34 | Väkivalta |
| Compensable | PsychologicalInjury | work_related | serious | Section 35 | Psykografkinen sairaus |

---

## 3. Compensation Type

**Legal Source:** Part III, Sections 36-109

| **OUTPUT: Compensation Type** | Injury Type | Severity | Duration | Legal Basis | Source Text |
|-------------------------------|-------------|----------|---------|-------------|-------------|
| MedicalExpenses | PhysicalInjury | minor | < 1 year | Section 36 | Sairaanhoito |
| MedicalExpenses + LostWages | PhysicalInjury | moderate | 1-3 years | Sections 36, 55 | Sairaanhoito + ansionmenetys |
| MedicalExpenses + LostWages + Disability | PhysicalInjury | severe | > 3 years | Sections 36, 55, 83 | Kokonaiskorvaus |
| PermanentDisabilityCompensation | PhysicalInjury | permanent | any | Section 83(1) | Pysyvä haitta |
| MedicalExpenses + LostWages | OccupationalDisease | any | any | Sections 26-32 | Ammattitaudin korvaus |
| Rehabilitation | MentalInjury | moderate | any | Section 88(1) | Kuntoutus |
| DeathCompensation | Death | any | any | Section 99(1) | Kuoleman korvaus |

---

## 4. Compensation Amount

**Legal Source:** Part III, Sections 36-109

| **OUTPUT: Formula** | Compensation Type | Income | Severity | Work Ability Lost | Legal Basis | Source Text |
|--------------------|------------------|--------|----------|-------------------|-------------|-------------|
| income.annual / 365 * days | LostWages | any | any | 100% | Section 56(1) | Täysi ansionmenetys |
| income.annual / 365 * days * 0.5 | LostWages | any | any | 50% | Section 56(2) | Osittainen ansionmenetys |
| 0 | LostWages | any | any | 0% | Section 56 | Ei ansionmenetystä |
| income.annual * 0.1 | PermanentDisability | any | 10-19% | any | Section 84(1) | Haittalisä 10-19% |
| income.annual * 0.2 | PermanentDisability | any | 20-50% | any | Section 84(1) | Haittalisä 20-50% |
| income.annual | PermanentDisability | any | 51-100% | any | Section 84(2) | Täysi haittalisä |
| Section 99-109 rates | Death | any | any | any | Sections 99-109 | Kuoleman korvaukset |

---

## 5. Medical Care Coverage

**Legal Source:** Part III, Sections 36-54

| **OUTPUT: Coverage** | Treatment Type | Necessity | Provider | Legal Basis | Source Text |
|---------------------|---------------|-----------|----------|-------------|-------------|
| 100% | EmergencyCare | required | public | Section 37(1) | Julkisen terveydenhuollon hoito |
| 100% (reimbursement) | EmergencyCare | required | private | Section 37(2) | Yksityisen hoidon korvaus |
| 100% | Surgery | required | any | Section 38(1) | Leikkaushoito |
| 100% (drug list) | Medicines | prescribed | pharmacy | Section 45 | Lääkkeet |
| 100% | Rehabilitation | medical_necessity | any | Section 88(1) | Kuntoutus |
| 100% | DentalTreatment | accident_related | any | Section 48 | Hammashoito |
| Kilometre allowance | TravelToTreatment | required | any | Section 50 | Matkakustannukset |
| 100% | Prosthesis | required | any | Section 47 | Silmälasit, proteesit |

---

## 6. Claim Time Limit

**Legal Source:** Part IV, Section 110

| **OUTPUT: Time Limit** | Claim Type | Injury Timing | Legal Basis | Source Text |
|-----------------------|------------|---------------|-------------|-------------|
| 3 years from accident | WorkAccident | within_3_years | Section 110(1) | 3 vuoden määräaika |
| Claim barred | WorkAccident | after_3_years | Section 110(3) | Määräajan umpeutuminen |
| 3 years from diagnosis | OccupationalDisease | any | Section 110(2) | Ammattitaudin määräaika |
| 3 years from death | DeathBenefit | within_3_years | Section 110(1) | Kuoleman korvaus |
| 3 years from death | SurvivorBenefit | any | Section 110(1) | Leskeneläke |

---

## 7. Rehabilitation Eligibility

**Legal Source:** Part III, Sections 88-98

| **OUTPUT: Eligible** | Injury Severity | Work Ability Reduced | Medical Recommendation | Legal Basis | Source Text |
|----------------------|-----------------|---------------------|----------------------|-------------|-------------|
| Full rehabilitation | severe | yes | yes | Section 88(1) | Ammatillinen kuntoutus |
| Vocational rehabilitation | moderate | yes | yes | Section 89(1) | Ammatillinen kuntoutus |
| Medical rehabilitation only | minor | no | no | Section 88(1) | Lääkinnällinen kuntoutus |
| Not eligible | any | any | no | Section 88(1) | Ei oikeutta kuntoutukseen |

---

## 8. Insurance Premium

**Legal Source:** Part V, Sections 156-186

| **OUTPUT: Premium Formula** | Industry Risk | Payroll | Claims History | Legal Basis | Source Text |
|----------------------------|---------------|---------|---------------|-------------|-------------|
| payroll * 0.005 | low_risk | any | no_claims | Section 166(1) | Vakuutusmaksun peruste |
| payroll * 0.01 | medium_risk | any | no_claims | Section 166(1) | Vakuutusmaksun peruste |
| payroll * 0.02 | high_risk | any | no_claims | Section 166(1) | Korkea riski |
| base_premium + risk loading | any | any | with_claims | Sections 171-176 | Lisämaksu |

---

## 9. Appeals Process

**Legal Source:** Part VIII, Sections 237-247

| **OUTPUT: Appeal Path** | Decision Type | Disagreement | Legal Basis | Source Text |
|-------------------------|---------------|--------------|-------------|-------------|
| Appeal to Insurance Company → Accident Board | Rejection | yes | Section 237(1) | Valitus vakuutusyhtiölle |
| Appeal to Accident Compensation Board | AmountDispute | yes | Section 238 | Tapaturma-asianlautakunta |
| Complaint + Late interest | LateDecision | yes | Section 146 | Viivästyskorotus |
| No appeal | AnyDecision | no | N/A | Ei valitusta |

---

## 10. Survivor Benefits

**Legal Source:** Part III, Sections 99-109

| **OUTPUT: Benefit** | Survivor Relationship | Age | Deceased Contributory | Legal Basis | Source Text |
|--------------------|-----------------------|-----|----------------------|-------------|-------------|
| Spouse pension | Spouse | any | yes | Section 100(1) | Leskeneläke |
| Lump sum | Spouse | any | no | Section 107(1) | Kertakorvaus |
| Child pension + orphan allowance | Child | under_18 | yes | Sections 101-102 | Lapseneläke |
| Student orphan pension | Child | 18-24_student | yes | Section 103 | Opiskelijan eläke |
| Dependent allowance | Dependent | any | yes | Section 105 | Huollettavan korvaus |

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

See `work_accident_dmn_rules.json` for DMN-compatible JSON format.
