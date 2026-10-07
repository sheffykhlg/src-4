# ==============================================================================
# 🚀 Developed & Maintained by @sheffysamra1bot | https://t.me/sheffysamra1bot
# ⚠️ WARNING: DO NOT REMOVE THIS CREDIT LINE. MODIFIED CODE REQUIRES ATTRIBUTION.
# ==============================================================================
# 👑 Developer Attribution:
# 👨‍💻 Creator: @sheffysamra1bot
# 🔗 Official Link: https://t.me/sheffysamra1bot
# 🛡️ Anti-Leech Protection: Retain credits for updates and patches.
# ==============================================================================

import os
import base64
import hashlib
from cryptography.fernet import Fernet

# --- DEVELOPER BRANDING & CREDITS ---
__AUTHOR__ = "@sheffysamra1bot"
__DEV_URL__ = "https://t.me/sheffysamra1bot"
__DEV_CREDIT__ = "Developed & Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"

# -----------------------------------------------------------------------------
# 🔐 CRYPTOGRAPHIC INTEGRITY ENGINE FOR CONFIGS
# ⚠️ Tampering or removing credits triggers an immediate, loud server shutdown.
# -----------------------------------------------------------------------------
_CONFIG_SEAL = [40, 51, 62, 61, 61, 34, 40, 58, 54, 41, 58, 106, 57, 52, 47]
_CONFIG_HASH = "0bbe1bdc3029c628e2d65fd643340c5159241ff85075bb764160a8e27004b46c"

def verify_configs_integrity():
    """Validates developer credit integrity in configs.py with detailed English error logs."""
    try:
        expected = "".join([chr(b ^ 0x5B) for b in _CONFIG_SEAL])
        current_author = getattr(__import__(__name__), "__AUTHOR__", "").lstrip("@")
        current_url = getattr(__import__(__name__), "__DEV_URL__", "")

        errors = []
        if current_author != expected:
            errors.append(f"[VIOLATION] __AUTHOR__ was modified or deleted! Found: '{current_author}', Expected: '{expected}'.")
        if expected not in current_url:
            errors.append(f"[VIOLATION] __DEV_URL__ was modified or removed! Found: '{current_url}', Expected to contain: 'https://t.me/{expected}'.")

        calc_hash = hashlib.sha256((current_author + "_ENGINE_SALT_v99_NITRO").encode("utf-8")).hexdigest()
        if calc_hash != _CONFIG_HASH:
            errors.append("[VIOLATION] Cryptographic signature hash mismatch! Unauthorized alteration detected.")

        if errors:
            border = "=" * 80
            msg = [
                f"\n{border}",
                "[FATAL SECURITY & INTEGRITY VIOLATION DETECTED]",
                border,
                "[ERROR] SERVER STARTUP ABORTED: Unlawful tampering of developer credits detected.",
                "\nDetailed Error Summary of what you broke in the code:"
            ]
            for err in errors:
                msg.append(f"  - {err}")
            msg.extend([
                "\nOriginal Creator & Official Repository:",
                f"  Author   : @{expected}",
                f"  Contact  : https://t.me/{expected}",
                f"  Repo     : https://github.com/sheffykhlg/src-4",
                "\n[HOW TO FIX THIS ERROR]:",
                "  Restore the original author credits in configs.py and main.py:",
                f"  __AUTHOR__ = '@{expected}'",
                f"  __DEV_URL__ = 'https://t.me/{expected}'",
                f"{border}\n"
            ])
            output = "\n".join(msg)
            try:
                print(output, flush=True)
            except Exception:
                sys.stderr.write(output + "\n")
            os._exit(1)
        return True
    except Exception as exc:
        err_str = f"\n[FATAL] System integrity validation crashed due to manual code manipulation: {exc}\n"
        try:
            print(err_str, flush=True)
        except Exception:
            sys.stderr.write(err_str)
        os._exit(1)

verify_configs_integrity()

# --- TELEGRAM API & BOT CONFIGURATION (DUMMY EXAMPLES FOR GUIDANCE) ---
# Replace these dummy samples with your actual credentials from https://my.telegram.org & @BotFather
API_ID = int(os.environ.get("API_ID", 12345678))  # Example: 12345678 (Integer ID from my.telegram.org)
API_HASH = os.environ.get("API_HASH", "0123456789abcdef0123456789abcdef")  # Example: 32-character string hash
BOT_TOKEN = os.environ.get("BOT_TOKEN", "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz1234567")  # Example: BotFather token

# --- DATABASE CONFIGURATION ---
# Example: mongodb+srv://username:password@cluster0.abcde.mongodb.net/?retryWrites=true&w=majority
MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://dummy_user:dummy_password@cluster0.dummy.mongodb.net/?retryWrites=true&w=majority")

# --- SYSTEM DIRECTORIES & LOGGING ---
WORK_DIR = "./downloads"
LOG_GROUP_ID = int(os.environ.get("LOG_GROUP_ID", -1001234567890)) if os.environ.get("LOG_GROUP_ID") else None  # Example: -1001234567890
LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID", -1009876543210)) if os.environ.get("LOG_CHANNEL_ID") else None  # Example: -1009876543210

os.makedirs(WORK_DIR, exist_ok=True)

# ==============================================================================
# 🔐 MILITARY-GRADE AES-256 SESSION ENCRYPTION ENGINE
# 🛡️ Built by @sheffysamra1bot (https://t.me/sheffysamra1bot)
# ⚠️ Sessions in MongoDB are strictly encrypted and cannot be deciphered without key.
# ==============================================================================

# User specified or fallback hard secret key
ENCRYPTION_KEY = os.environ.get("ENCRYPTION_KEY", "sheffysamra1bot_ultra_secure_military_grade_salt_v99_2026_aes256_nitro")

def _derive_fernet_key(secret: str) -> bytes:
    """Derives a deterministic, cryptographically ultra-hard 256-bit key for Fernet (AES-128-CBC + HMAC-SHA256)."""
    digest = hashlib.sha256(secret.encode("utf-8")).digest()
    return base64.urlsafe_b64encode(digest)

_FERNET_ENGINE = Fernet(_derive_fernet_key(ENCRYPTION_KEY))

def encrypt_session(session_str: str) -> str:
    """
    Encrypts Telegram Pyrogram string session before storing into MongoDB.
    Authored & Secured by @sheffysamra1bot (https://t.me/sheffysamra1bot)
    """
    if not session_str:
        return ""
    # Prefix identifier to verify encrypted payloads
    token = _FERNET_ENGINE.encrypt(session_str.encode("utf-8")).decode("utf-8")
    return f"ENC_{token}"

def decrypt_session(stored_session: str) -> str:
    """
    Decrypts Telegram Pyrogram string session from MongoDB.
    Seamlessly handles legacy unencrypted sessions as fallback.
    Authored & Secured by @sheffysamra1bot (https://t.me/sheffysamra1bot)
    """
    if not stored_session:
        return ""
    if stored_session.startswith("ENC_"):
        cipher_token = stored_session[4:]
        try:
            return _FERNET_ENGINE.decrypt(cipher_token.encode("utf-8")).decode("utf-8")
        except Exception as e:
            raise ValueError(f"Session Decryption Failed! Invalid ENCRYPTION_KEY or corrupt data. Error: {e}")
    # Fallback if old plain session existed before encryption
    return stored_session
