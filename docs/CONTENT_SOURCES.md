# Content & image sources

Last provenance review: 12 November 2026.

## Editorial references

- [Cổng thông tin điện tử tỉnh Vĩnh Long — Biển Ba Động](https://vinhlong.gov.vn/du-khach-old/diadanh_test) — current administrative naming and a first-party description of the coast.
- [Ban Quản lý Khu kinh tế Vĩnh Long — Khu kinh tế Định An](https://bqlkkt.vinhlong.gov.vn/thong-tin-cac-kcn-va-kkt/khu-kinh-te/khu-kinh-te-%C4%91inh-an) — official regional context for Định An and the coastal economy.
- [Cục Du lịch Quốc gia Việt Nam](https://vietnamtourism.gov.vn/) — general travel and responsible-tourism reference.
- [Google Maps search for Biển Ba Động](https://www.google.com/maps/search/?api=1&query=Bi%E1%BB%83n+Ba+%C4%90%E1%BB%99ng+Tr%C3%A0+Vinh) — external navigation only; not embedded as a fabricated map.

## Image policy

The site does not load remote editorial photographs. All displayed photos are stored under `wwwroot/images`, and each has a Wikimedia Commons file page with a reuse license. Downloaded variants were resized by Wikimedia's thumbnail service; no generative or content-altering edit was made.

`wwwroot/data/image-manifest.json` is the machine-readable source of truth. `VERIFIED` means both the subject and stated location are supported by the source page. `VERIFIED_REGION` means the photograph is from the documented coastal region but not from Biển Ba Động; its exact location and that distinction must be visible in the UI. `VERIFIED_SUBJECT` means the subject is correct, but the photo was not taken at Ba Động; the UI states its actual location. `PENDING` assets are not published as photographs.

## Verified image inventory

| Local files | Used on | Subject / actual location | Photographer | Source | License | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `images/locations/ba-dong-beach-800.jpg`, `images/locations/ba-dong-beach-1600.jpg` | Home hero and quote; About; Explore; destination detail; Gallery; itineraries | Biển Ba Động, Trà Vinh (nay thuộc tỉnh Vĩnh Long) | Baoothersks | [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:Bi%E1%BB%83n_Ba_%C4%90%E1%BB%99ng,_Tr%C3%A0_Vinh.jpg) | CC BY 4.0 | VERIFIED |
| `images/locations/duyen-hai-wind-power-800.jpg`, `images/locations/duyen-hai-wind-power-1600.jpg` | Home editorial section; Explore; destination detail; Gallery; itineraries | Điện gió Duyên Hải, Trà Vinh (nay thuộc tỉnh Vĩnh Long) | Dangkhoadora | [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:Th%E1%BB%8B_x%C3%A3_Duy%C3%AAn_H%E1%BA%A3i.jpg) | CC BY-SA 4.0 | VERIFIED |
| `images/locations/dinh-an-fishing-port-ray-800.jpg`, `images/locations/dinh-an-fishing-port-ray-1600.jpg` | Gallery only | Cá đuối bướm tại cảng cá Định An, Trà Vinh (nay thuộc tỉnh Vĩnh Long); **không phải Biển Ba Động** | Trương Minh Khải | [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:Japanese_butterfly_ray_(Gymnura_japonica)_at_Dinh_An_fishing_port,_Tra_Vinh_province,_Vietnam.jpg) | CC0 1.0 | VERIFIED_REGION |
| `images/food/dua-sap-cau-ke-800.jpg`, `images/food/dua-sap-cau-ke-1600.jpg` | Cuisine; food detail; Gallery | Dừa sáp Cầu Kè, Trà Vinh (nay thuộc tỉnh Vĩnh Long) | Dongson.vmvn | [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:D%E1%BB%ABa_s%C3%A1p_C%E1%BA%A7u_K%C3%A8,_Tr%C3%A0_Vinh..jpg) | CC BY-SA 3.0 | VERIFIED |
| `images/food/vietnamese-crab-dish-800.jpg`, `images/food/vietnamese-crab-dish-1600.jpg` | Cuisine; food detail; Gallery; one-day itinerary | Món cua Việt Nam; ảnh chụp tại Cà Mau | Phương Huy | [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:M%C3%B3n_cua_C%C3%A0_Mau_%E1%BB%9F_nh%C3%A0_ng30th7n2023_(2).jpg) | CC BY-SA 4.0 | VERIFIED_SUBJECT |
| `images/food/ca-khoai-800.jpg`, `images/food/ca-khoai-1600.jpg` | Cuisine; food detail; Gallery | Cá khoai; ảnh chụp tại Hậu Lộc, Thanh Hóa | Gió Đông | [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:Ca_Khoai01.JPG) | Public domain | VERIFIED_SUBJECT |
| `images/food/banh-xeo-800.jpg` | Cuisine; food detail; Gallery; two-day itinerary | Bánh xèo; nguồn ghi Việt Nam, không nêu địa điểm cụ thể | Baoothersks | [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:B%C3%A1nh_x%C3%A8o_(20-8-2020).jpg) | CC BY-SA 4.0 | VERIFIED_SUBJECT |
| `images/placeholders/pending-verification.svg` | Explore and five pending destination details | Project-native holding graphic; not a photograph | BA ĐỘNG — Coastal Escape | Internal project asset | Project asset | INTERNAL_PLACEHOLDER |

Attribution remains visible in the home hero, detail-image captions, and gallery lightbox. The local resized copies retain the source license stated above.

## Pending local photography

No adequately licensed Ba Động photograph was found for the following subjects. They use `images/placeholders/pending-verification.svg`, a project-native graphic that explicitly says it is not a photograph:

- hàng dương ven Biển Ba Động;
- hoạt động du lịch and daily life of the Ba Động fishing community, with consent where people are identifiable;
- a verified Ba Động sunset;
- the mangrove edge near Trường Long Hòa;
- a quieter shoreline composition distinct from the current hero.

The Định An fishing-port photograph documents a related coastal locality, but it is intentionally not used to satisfy the Ba Động fishing-community requirement.

The exact target routes and required metadata are tracked in `wwwroot/data/image-requirements.json`. A candidate must provide `filename`, `title`, `actualLocation`, `photographer`, `sourceUrl`, `license`, `attribution`, and `verificationStatus` before replacing a placeholder.

## Excluded inventory

The previous Unsplash URLs were generic illustrative imagery and did not depict the named places or dishes with sufficient specificity. They have been removed from rendered content and JSON. No image from a news site, tourism blog, Google Images, or social network was downloaded.

## Content policy

No unverified prices, ratings, opening hours, phone numbers, booking actions, or official-tourism claims are included. Time-sensitive information is marked as needing a pre-trip check.
