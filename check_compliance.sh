#!/bin/bash
# Law vs Business Rules Checker
# This script compares the law against DMN rules and reports discrepancies

cd /home/molt/.openclaw/workspace/Finnish-law

REPORT_FILE="compliance_check_$(date +%Y%m%d_%H%M%S).md"

cat > "$REPORT_FILE" << 'EOF'
# Law Compliance Check Report

**Date:** $(date)
**Law File:** laws/liikennevakuutuslaki.txt
**Rules File:** liikennevakuutuslaki/rules/car_insurance_dmn_rules.md

## Automated Checks

### 1. Time Limits Check (§§61, 62, 79)
EOF

# Check if TIME rules exist in DMN
if grep -q "TIME-00[1-7]" liikennevakuutuslaki/rules/car_insurance_dmn_rules.md 2>/dev/null; then
    echo "✅ Time limit rules found" >> "$REPORT_FILE"
else
    echo "❌ MISSING: Time limit rules (§§61, 62, 79) not in DMN" >> "$REPORT_FILE"
    echo "   - Claim filing: 3 years from knowledge" >> "$REPORT_FILE"
    echo "   - Investigation: 7 business days" >> "$REPORT_FILE"
    echo "   - Payment: 1 month from complete docs" >> "$REPORT_FILE"
fi

cat >> "$REPORT_FILE" << 'EOF'

### 2. Property Damage Cap Check (§38)
EOF

if grep -q "5000000\|5 000 000" liikennevakuutuslaki/rules/car_insurance_dmn_rules.md 2>/dev/null; then
    echo "✅ €5M property damage cap found" >> "$REPORT_FILE"
else
    echo "❌ MISSING: €5,000,000 property damage maximum (§38)" >> "$REPORT_FILE"
fi

cat >> "$REPORT_FILE" << 'EOF'

### 3. Alcohol Thresholds Check (§48)
EOF

if grep -q "0.53\|0.22" liikennevakuutuslaki/rules/car_insurance_dmn_rules.md 2>/dev/null; then
    echo "✅ Breathalyzer thresholds found" >> "$REPORT_FILE"
else
    echo "❌ MISSING: Breathalyzer equivalents (mg/L) from §48" >> "$REPORT_FILE"
    echo "   - ≥0.53 mg/L breath = ≥1.2‰ BAC" >> "$REPORT_FILE"
    echo "   - 0.22-0.52 mg/L breath = 0.5-1.19‰ BAC" >> "$REPORT_FILE"
fi

cat >> "$REPORT_FILE" << 'EOF'

### 4. Medical Treatment Rules Check (§§53-59)
EOF

if grep -q "maksusitoumus\|täyskustannusmaksu" liikennevakuutuslaki/rules/car_insurance_dmn_rules.md 2>/dev/null; then
    echo "✅ Medical procedure rules found" >> "$REPORT_FILE"
else
    echo "❌ MISSING: Medical treatment procedures (§§53-59)" >> "$REPORT_FILE"
    echo "   - 4 business days notification (§56)" >> "$REPORT_FILE"
    echo "   - Maksusitoumus requirement (§57)" >> "$REPORT_FILE"
fi

cat >> "$REPORT_FILE" << 'EOF'

### 5. Index Adjustment Check (§35)
EOF

if grep -q "työeläkeindeksi\|FIN-003" liikennevakuutuslaki/rules/car_insurance_dmn_rules.md 2>/dev/null; then
    echo "✅ Index adjustment rule found" >> "$REPORT_FILE"
else
    echo "❌ MISSING: Annual index adjustment (§35)" >> "$REPORT_FILE"
fi

cat >> "$REPORT_FILE" << 'EOF'

---
*This is an automated check. Review issues_found.md for detailed findings.*
EOF

echo "Report saved to: $REPORT_FILE"

# If there are missing items, append to issues log
if grep -q "❌ MISSING" "$REPORT_FILE"; then
    echo "$(date): Discrepancies found - see $REPORT_FILE" >> compliance_check.log
    exit 1  # Signal that issues were found
else
    echo "$(date): All checks passed" >> compliance_check.log
    exit 0
fi
