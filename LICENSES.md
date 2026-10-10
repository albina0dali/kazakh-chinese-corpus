# Source licensing review

Checked: 2026-10-10. No single blanket data license is assigned to this mixed collection. Original recorded labels remain unchanged; they are not all independently verified. This document does not grant rights owned by upstream contributors.

## KazParC (147,881 derived pairs)

ISSAI explicitly identifies KazParC as CC BY 4.0:
https://issai.nu.edu.kz/2024/07/01/kazparc-kazakh-parallel-corpus-for-machine-translation/
License: https://creativecommons.org/licenses/by/4.0/
Credit Rustem Yeshpanov, Alina Polonskaya and Huseyin Atakan Varol and link the dataset and publication. Changes here: selection of main train kk–en rows, addition of automatically generated Chinese translations, filtering and repackaging. The upstream gated access conditions should also be retained from the account used to download the exact source version. Upstream licensing is evidence for that source, not a license for unrelated corpus components.

## Original sources (66,119 pairs)

- Wikipedia (18,213): recorded as CC BY-SA 4.0. Preserve page attribution, applicable notices and change statements; check paired page/revision provenance before release.
- OPUS sources: recorded as CHECK-LICENCE. MultiCCAligned 23,646; KDE4 12,612; OpenSubtitles 7,866; TED2020 1,099; News-Commentary 907; GNOME 884; Ubuntu 43; wikimedia 11. Component/version-specific permissions and upstream notices are not yet verified. Retrieval attempts at legacy OPUS component URLs failed; no permission is inferred from that.
- Weblate (838): mixed per-side software/text license labels. Verify each originating project/component, retain attribution and required license notices. One row explicitly includes `zh:proprietary`: see metadata/permission_required.json. Do not publicly redistribute that row without a documented permission covering the intended use.

metadata/license_inventory.json contains every recorded source/license combination and count. This is an inventory, not a completed rights clearance. Required evidence: exact source/version, applicable license text, attribution/copyright notices, and any additional redistribution permission. Public release of the complete mixed dataset remains pending. Model licenses do not settle rights in source texts.

## Provenance gaps identified in the packaged records

All 838 Weblate records currently point to the aggregate
https://huggingface.co/datasets/ayymen/Weblate-Translations rather than original
project/component URLs. Project-specific notices and permissions cannot be
confirmed from those links alone. The proprietary label is a recorded upstream
label, not an independent legal determination. Trace that record to its original
project before asserting any redistribution permission.

Wikipedia records inspected contain a Kazakh article URL; attribution to both
aligned pages and exact revisions has not been established for every pair.
CHECK-LICENCE is a processing placeholder, not a license and not proof that
redistribution is prohibited. Missing evidence remains an open review item.
