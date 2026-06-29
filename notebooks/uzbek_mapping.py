# uzbek_mapping.py
# Uzbek language mapping for Q-CHAT-10 ASD Screening Tool
# Used in NeuroReach Module 2 — ASD Behavioral Screening

# Questions displayed to parents in Uzbek
QUESTIONS_UZ = {
    "A1": "Farzandingizni ismi bilan chaqirganingizda u sizga qaraydimi?",
    "A2": "Farzandingiz bilan ko'z aloqasi o'rnatish qanchalik oson?",
    "A3": "Farzandingiz biror narsani xohlasa ishora qiladimi?",
    "A4": "Farzandingiz qiziqarli narsani ko'rsatish uchun ishora qiladimi?",
    "A5": "Farzandingiz tasavvurga egami (masalan, qo'g'irchoqqa g'amxo'rlik qiladi, soxta telefonda gaplashadi)?",
    "A6": "Farzandingiz siz qarayotgan tomonga qaraydimi?",
    "A7": "Oilada biror kishi xafa bo'lsa, farzandingiz tasalli berishga harakat qiladimi?",
    "A8": "Farzandingizning birinchi so'zlari oddiy va o'z vaqtida bo'lganmi?",
    "A9": "Farzandingiz oddiy imo-ishoralardan foydalanadi (masalan, xayrlashayotganda qo'l silkitadi)?",
    "A10": "Farzandingiz maqsadsiz nimagadirga uzoq tikilib qoladimi?"
}

# English versions (for reference and documentation)
QUESTIONS_EN = {
    "A1": "Does your child look at you when you call his/her name?",
    "A2": "How easy is it for you to get eye contact with your child?",
    "A3": "Does your child point to indicate that s/he wants something?",
    "A4": "Does your child point to share interest with you?",
    "A5": "Does your child pretend? (e.g. care for dolls, talk on a toy phone)",
    "A6": "Does your child follow where you're looking?",
    "A7": "If someone in the family is upset, does your child show signs of wanting to comfort them?",
    "A8": "Would you describe your child's first words as normal?",
    "A9": "Does your child use simple gestures? (e.g. wave goodbye)",
    "A10": "Does your child stare at nothing with no apparent purpose?"
}

# Answer options displayed in Uzbek → mapped to numeric values
ANSWERS_UZ = {
    "Har doim": 1,       # Always
    "Odatda": 1,         # Usually
    "Ba'zan": 0,         # Sometimes
    "Kamdan-kam": 0,     # Rarely
    "Hech qachon": 0     # Never
}

# Result messages in Uzbek
RESULTS_UZ = {
    "high_risk": (
        "⚠️ Yuqori xavf: Farzandingizda ASD belgilari aniqlanishi mumkin. "
        "Mutaxassis shifokorga murojaat qilishni tavsiya etamiz."
    ),
    "low_risk": (
        "✅ Past xavf: Farzandingizda ASD belgilari aniqlanmadi. "
        "Biroq, har qanday tashvish bo'lsa, shifokorga murojaat qiling."
    ),
    "disclaimer": (
        "⚠️ Eslatma: Bu vosita tibbiy tashxis emas. "
        "Faqat dastlabki skrining uchun mo'ljallangan."
    )
}


def encode_answers(user_answers: dict) -> list:
    """
    Convert Uzbek answers to numeric values for the model.
    
    Input:  {"A1": "Har doim", "A2": "Hech qachon", ...}
    Output: [1, 0, ...]
    """
    encoded = []
    for key in ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"]:
        answer_uz = user_answers.get(key, "Hech qachon")
        encoded.append(ANSWERS_UZ.get(answer_uz, 0))
    return encoded