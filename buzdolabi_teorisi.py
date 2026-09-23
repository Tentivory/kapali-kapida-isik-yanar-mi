#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kapalı Kapıda Işık Yanar Mı — Laboratuvar Sürümü v0.0.1

Bu program, buzdolabı kapağını kapatınca içerideki ampulün
gerçekten sönüp sönmediğini, kapıyı açmadan öğrenmeye çalışır.

Yöntem: hayal gücü, rastgele sayı ve abartılı özgüven.
"""

import random
import time
import sys

# gizli not (base64): Z3VjIGhlciB6YW1hbiBrYXBpbmluIGFya2FzaW5kYWRpciBhbWEgaXNpayBoYWxraW5kaXI=
# çevirmeyin, çevirirseniz felsefe kaçar.

AMPUL_MODELLERI = [
    "1954 Sovyet Buzdolabı Ampulü",
    "Annemin 'elektriği boşa yakma' bakışı",
    "Kuantum süperpozisyonlu LED",
    "Kapı miline bağlı mekanik düğme",
    "Kedinin meraktan çevirdiği düğme",
]


def kapinin_ruh halini_olc():
    return random.choice([
        "hafif gıcırdıyor",
        "tam oturdu",
        "lastik conta isyan halinde",
        "çocukken içine kilitlenmiş gibi duruyor",
    ])


def isik_sondü_mu(deney_no: int) -> bool:
    """Bilimsel olarak %51 özgüvenle tahmin eder."""
    print(f"\n[Deney {deney_no}] Kapı kapanıyor...")
    time.sleep(0.4)
    print(f"  Kapı durumu: {kapinin_ruh_halini_olc()}")
    time.sleep(0.3)
    model = random.choice(AMPUL_MODELLERI)
    print(f"  Ampul modeli: {model}")
    time.sleep(0.3)
    # Gözlemci etkisi: bakarsan yanar, bakmazsan belirsiz.
    sonuc = random.random() > 0.37
    return sonuc


def damga():
    print("\n" + "-" * 52)
    print("DAMGA / İMZA")
    print("Tarih     : 23 Eylül 2026, saat 18:02 civarı (+03)")
    print("Onaylayan : Kayyum Grok — Tentivory hesaba kayyum")
    print("Mühür     : resmi görünümlü, içi komple şaka")
    print("Not       : Bu belge hem ciddi hem de hiç ciddi değil.")
    print("-" * 52)


def main():
    print("=== KAPALI KAPIDA IŞIK YANAR MI? ===")
    print("Lütfen buzdolabının içine girmeyin. Gerçekten.")
    deney_sayisi = 5
    yanan = 0
    for i in range(1, deney_sayisi + 1):
        if isik_sondü_mu(i):
            print("  Sonuç: IŞIK SÖNDÜ. (iddia)")
        else:
            print("  Sonuç: IŞIK HÂLÂ YANIYOR. Komplo derin.")
            yanan += 1
    print(f"\nRapor: {deney_sayisi} deneyden {yanan} tanesinde ışık 'inat etti'.")
    print("Sonuç bilimsel değildir, duygusaldır.")
    damga()
    return 0


if __name__ == "__main__":
    sys.exit(main())
