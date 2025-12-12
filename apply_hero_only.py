#!/usr/bin/env python3
import re
from pathlib import Path

# Service pages to update
service_pages = [
    'domestic-air-shipping.html',
    'international-shipping.html',
    'international-air.html',
    'international-ocean.html',
    'specialized-shipping.html',
    'emergency-shipping.html',
    'custom-services.html',
    'white-glove-delivery.html',
    'ltl-recovery.html',
    'warehousing-fulfillment.html',
]

# Read the template hero section from domestic-ground-shipping.html
with open('domestic-ground-shipping.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Extract ONLY the hero section (from <!-- Hero to </section>)
hero_match = re.search(r'(<!-- Hero[^>]*>.*?</section>)', template, re.DOTALL)
if hero_match:
    hero_template = hero_match.group(1)
    print(f"Found hero template ({len(hero_template)} chars)")
else:
    print("ERROR: Could not find hero section in template")
    exit(1)

for page_file in service_pages:
    if not Path(page_file).exists():
        print(f"\n⚠ Skipping {page_file} (not found)")
        continue
        
    print(f"\nProcessing {page_file}...")
    
    with open(page_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract page title from h1 or title tag
    title_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
    if not title_match:
        title_match = re.search(r'<title[^>]*>(.*?)</title>', content)
    page_title = title_match.group(1).strip() if title_match else "Service"
    
    # Clean up title - remove HTML tags and get first line
    page_title = re.sub(r'<[^>]+>', '', page_title).strip()
    if '|' in page_title:
        page_title = page_title.split('|')[0].strip()
    
    # Split title into two parts (first word/words and last word)
    title_parts = page_title.split()
    if len(title_parts) >= 2:
        title_line1 = ' '.join(title_parts[:-1])
        title_line2 = title_parts[-1]
    else:
        title_line1 = page_title
        title_line2 = ""
    
    # Replace ONLY the hero section
    hero_patterns = [
        (r'<!-- Hero[^>]*>.*?</section>', re.DOTALL),
        (r'<section[^>]*class="[^"]*hero[^"]*".*?</section>', re.DOTALL),
        (r'<section[^>]*class="[^"]*pt-32[^"]*"[^>]*>.*?</section>', re.DOTALL),
    ]
    
    hero_replaced = False
    for pattern, flags in hero_patterns:
        match = re.search(pattern, content, flags)
        if match:
            # Customize the hero template with page-specific title
            customized_hero = hero_template
            customized_hero = re.sub(
                r'<span class="block text-white pb-2">Domestic Ground</span>\s*<span class="block"[^>]*>Shipping</span>',
                f'<span class="block text-white pb-2">{title_line1}</span>\n                    <span class="block" style="background: linear-gradient(135deg, #1e7e34 0%, #2d8650 50%, #4ade80 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; padding-bottom: 0.2em; overflow: visible;">{title_line2}</span>',
                customized_hero
            )
            # Also update description - try to preserve existing description
            desc_match = re.search(r'<p class="text-2xl[^>]*>(.*?)</p>', match.group(0), re.DOTALL)
            if desc_match:
                existing_desc = desc_match.group(1).strip()
                existing_desc = re.sub(r'<[^>]+>', '', existing_desc).strip()
                # Update description in customized hero
                customized_hero = re.sub(
                    r'<p class="text-2xl[^>]*>.*?</p>',
                    f'<p class="text-2xl md:text-3xl text-gray-300 mb-10 leading-relaxed">{existing_desc}</p>',
                    customized_hero,
                    flags=re.DOTALL
                )
            
            content = content.replace(match.group(0), customized_hero)
            hero_replaced = True
            print(f"  ✓ Replaced hero section")
            break
    
    if not hero_replaced:
        print(f"  ⚠ Could not find hero section to replace")
    
    # Save the file
    with open(page_file, 'w', encoding='utf-8') as f:
        f.write(content)

print("\nDone!")


