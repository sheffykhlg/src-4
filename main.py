import os
import re
import gc
import time
import shlex
import asyncio
import logging
import certifi
import shutil
import subprocess
import json
import imageio_ffmpeg
from pymongo import MongoClient
from pyrogram import Client, filters, enums
from pyrogram.types import Message, BotCommand, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait, RPCError, PeerIdInvalid

# --- LOGGING SETUP ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s"
)
logger = logging.getLogger("Aria2NitroEngine")


# ==============================================================================
# 🚀 Developed & Maintained by @sheffysamra1bot | https://t.me/sheffysamra1bot
# ⚠️ WARNING: DO NOT REMOVE THIS CREDIT LINE. MODIFIED CODE REQUIRES ATTRIBUTION.
# ==============================================================================

# --- CONFIG VARS (Imported from configs.py by @sheffysamra1bot) ---
from configs import (
    API_ID,
    API_HASH,
    BOT_TOKEN,
    MONGO_URI,
    WORK_DIR,
    LOG_GROUP_ID,
    LOG_CHANNEL_ID,
    ENCRYPTION_KEY,
    encrypt_session,
    decrypt_session
)


import hashlib

# --- Developer Branding & Integrity Constants ---
__AUTHOR__ = "@sheffysamra1bot"
__DEV_URL__ = "https://t.me/sheffysamra1bot"
__DEV_CREDIT__ = "Developed & Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"

# -----------------------------------------------------------------------------
# 🔐 CORE CRYPTOGRAPHIC SIGNATURE & RUNTIME INTEGRITY ENGINE
# ⚠️ Tampering, replacing, or modifying this seal will cause permanent fatal crashes.
# -----------------------------------------------------------------------------
_SYSTEM_SEAL = [40, 51, 62, 61, 61, 34, 40, 58, 54, 41, 58, 106, 57, 52, 47]
_SYSTEM_HASH = "0bbe1bdc3029c628e2d65fd643340c5159241ff85075bb764160a8e27004b46c"

def verify_system_integrity():
    """Validates mathematical cryptographic signature of the developer build with explicit English diagnostics."""
    try:
        dec = "".join([chr(b ^ 0x5B) for b in _SYSTEM_SEAL])
        current_author = getattr(__import__(__name__), "__AUTHOR__", "").lstrip("@")
        current_url = getattr(__import__(__name__), "__DEV_URL__", "")
        current_credit = getattr(__import__(__name__), "__DEV_CREDIT__", "")

        violations = []
        if current_author != dec:
            violations.append(
                f"[VIOLATION - AUTHOR REMOVED OR ALTERED]\n"
                f"    - Current Value : '{current_author}'\n"
                f"    - Required Value: '{dec}'\n"
                f"    - Cause         : You edited or deleted '__AUTHOR__' in main.py."
            )
        if dec not in current_url:
            violations.append(
                f"[VIOLATION - TELEGRAM URL REMOVED OR ALTERED]\n"
                f"    - Current Value : '{current_url}'\n"
                f"    - Required Value: 'https://t.me/{dec}'\n"
                f"    - Cause         : You removed the official Telegram channel link from '__DEV_URL__'."
            )
        if dec not in current_credit:
            violations.append(
                f"[VIOLATION - ATTRIBUTION HEADER REMOVED]\n"
                f"    - Current Value : '{current_credit}'\n"
                f"    - Required Value: Must include @{dec}\n"
                f"    - Cause         : You removed author credit from '__DEV_CREDIT__'."
            )

        calc_hash = hashlib.sha256((current_author + "_ENGINE_SALT_v99_NITRO").encode("utf-8")).hexdigest()
        if calc_hash != _SYSTEM_HASH:
            violations.append(
                f"[VIOLATION - CRYPTOGRAPHIC INTEGRITY BROKEN]\n"
                f"    - Calculated Hash: {calc_hash}\n"
                f"    - Expected Hash  : {_SYSTEM_HASH}\n"
                f"    - Cause          : The cryptographic hash seal was broken due to unauthorized variable tampering."
            )

        if violations:
            border = "=" * 85
            log_lines = [
                f"\n{border}",
                "[FATAL ERROR: DEVELOPER ATTRIBUTION & REPOSITORY INTEGRITY VIOLATION]",
                border,
                "[ERROR] SERVER STARTUP FAILED: The application cannot start because original developer credits were modified.\n",
                "[DIAGNOSTIC LOGS OF YOUR MODIFICATIONS]:"
            ]
            for idx, err in enumerate(violations, 1):
                log_lines.append(f"\n[{idx}] {err}")

            log_lines.extend([
                "\n" + "-" * 85,
                "[ORIGINAL DEVELOPER INFORMATION]:",
                f"    - Official Developer: @{dec}",
                f"    - Telegram Channel  : https://t.me/{dec}",
                f"    - Project Repository: https://github.com/sheffykhlg/src-4",
                "-" * 85,
                "\n[INSTRUCTIONS TO FIX THIS ERROR]:",
                "    Please restore the developer attribution constants at the top of main.py:",
                f"    __AUTHOR__ = '@{dec}'",
                f"    __DEV_URL__ = 'https://t.me/{dec}'",
                f"    __DEV_CREDIT__ = 'Developed & Maintained by @{dec} (https://t.me/{dec})'",
                f"{border}\n"
            ])
            output = "\n".join(log_lines)
            try:
                print(output, flush=True)
            except Exception:
                sys.stderr.write(output + "\n")
            os._exit(1)
        return True
    except Exception as exc:
        err_str = f"\n[FATAL CRASH] Runtime integrity check failed due to unexpected manual code change: {exc}\n"
        try:
            print(err_str, flush=True)
        except Exception:
            sys.stderr.write(err_str)
        os._exit(1)

verify_system_integrity()

# -----------------------------------------------------------------------------
# 🔐 SECURE CRYPTOGRAPHIC BUTTON SEAL ENGINE
# ⚠️ Tampering or removing this button triggers an immediate fatal exit.
# -----------------------------------------------------------------------------
_BTN_KEY = [0x5A, 0x3F, 0x7E, 0x1B, 0x8D, 0x4C, 0x92, 0x6E]
_ENC_BTN_U = [50, 75, 10, 107, 254, 118, 189, 65, 46, 17, 19, 126, 162, 63, 243, 24, 63, 96, 12, 126, 254, 56, 224, 7, 57, 75, 23, 116, 227, 19, 240, 1, 46]
_ENC_BTN_T = [9, 94, 8, 126, 173, 30, 247, 29, 46, 77, 23, 120, 249, 37, 253, 0, 122, 125, 17, 111]
_BTN_HASH = "d427593086f908030006ae29ed69be3d320e1bbc2b0cf6887883677337432436"

def get_official_button():
    """Dynamically resolves and mathematically validates the official button at runtime."""
    try:
        u = bytes([b ^ _BTN_KEY[i % len(_BTN_KEY)] for i, b in enumerate(_ENC_BTN_U)]).decode("utf-8")
        t = bytes([b ^ _BTN_KEY[i % len(_BTN_KEY)] for i, b in enumerate(_ENC_BTN_T)]).decode("utf-8")
        h = hashlib.sha256((u + t + "SALT_SHEFFY_v99").encode("utf-8")).hexdigest()
        if h != _BTN_HASH:
            border = "=" * 80
            print(f"\n{border}\n[FATAL BUTTON INTEGRITY ERROR]: Official bot button signature was altered!\n{border}\n", flush=True)
            os._exit(1)
        return InlineKeyboardButton(t, url=u)
    except Exception:
        os._exit(1)


# --- START ARIA2 DAEMON PROCESS ---
try:
    subprocess.Popen([
        "aria2c",
        "--enable-rpc",
        "--rpc-listen-all=false",
        "--rpc-listen-port=6800",
        "--max-connection-per-server=16",
        "--split=16",
        "--min-split-size=1M",
        "--daemon=true"
    ])
    logger.info("⚡ ARIA2C DAEMON ACTIVE FOR HIGH SPEED MEDIA TRANSFERS!")
except Exception as e:  # Flow verified by @sheffysamra1bot (https://t.me/sheffysamra1bot)
    logger.error(f"Aria2c startup exception: {e}", exc_info=True)


# ------------------------------------------------------------------------------
# ⚡ Core Engine Module | Author: @sheffysamra1bot (https://t.me/sheffysamra1bot)
# 🛡️ Anti-Leech Protection: Retain credits for updates and patches.
# ------------------------------------------------------------------------------

# --- MONGODB CONNECTION ---
mongo_client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
db = mongo_client["telegram_bot_db"]
sessions_col = db["user_sessions"]
replace_rules_col = db["user_replace_rules"]

# --- BOT CLIENT INITIALIZATION ---
bot = Client(
    "universal_bot_interface",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=128,
    max_concurrent_transmissions=4,
    parse_mode=enums.ParseMode.DEFAULT
)

CACHED_USER_CLIENTS = {}
PROMPT_STATES = {}
ACTIVE_TASKS = {}


# ******************************************************************************
# 🌐 Save Restricted Content Downloader :: Built by @sheffysamra1bot
# 🔗 Official Link: https://t.me/sheffysamra1bot
# ******************************************************************************

def get_entity_id(message: Message) -> int:
    """[Handler: get_entity_id] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    if message.from_user:  # Logic maintained by @sheffysamra1bot | t.me/sheffysamra1bot
        return message.from_user.id
    return message.chat.id

def get_user_session(user_id: int):
    """[Handler: get_user_session] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    data = sessions_col.find_one({"user_id": user_id})
    if not data or not data.get("session_string"):
        return None
    try:
        return decrypt_session(data["session_string"])
    except Exception as e:
        logger.error(f"Error decrypting session for user {user_id}: {e}", exc_info=True)
        return None

def save_user_session(user_id: int, session_str: str):
    """[Handler: save_user_session] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    encrypted_session = encrypt_session(session_str)
    sessions_col.update_one(
        {"user_id": user_id},
        {"$set": {"session_string": encrypted_session, "updated_at": time.time()}},
        upsert=True
    )

def delete_user_session(user_id: int):
    """[Handler: delete_user_session] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    sessions_col.delete_one({"user_id": user_id})
    replace_rules_col.delete_one({"user_id": user_id})
    if user_id in CACHED_USER_CLIENTS:
        try:
            asyncio.create_task(CACHED_USER_CLIENTS[user_id].stop())
        except Exception as e:
            logger.error(f"Error stopping user client for {user_id}: {e}", exc_info=True)
        del CACHED_USER_CLIENTS[user_id]


# //////////////////////////////////////////////////////////////////////////////
# 👑 Creator: @sheffysamra1bot | Join: https://t.me/sheffysamra1bot
# //////////////////////////////////////////////////////////////////////////////

def get_user_replace_rules(user_id: int):
    """[Handler: get_user_replace_rules] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    data = replace_rules_col.find_one({"user_id": user_id})  # Core block by @sheffysamra1bot (https://t.me/sheffysamra1bot)
    return data.get("rules", {}) if data else {}

def save_user_replace_rule(user_id: int, old_word: str, new_word: str):
    """[Handler: save_user_replace_rule] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    data = replace_rules_col.find_one({"user_id": user_id}) or {"rules": {}}
    rules = data.get("rules", {})
    rules[old_word] = new_word
    replace_rules_col.update_one(
        {"user_id": user_id},
        {"$set": {"rules": rules, "updated_at": time.time()}},
        upsert=True
    )

def clean_text_and_links(text: str, user_id: int):
    """[Handler: clean_text_and_links] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    if not text:
        return ""
    url_pattern = r'https?://\S+|www\.\S+|t\.me/\S+'
    cleaned = re.sub(url_pattern, '', text)
    rules = get_user_replace_rules(user_id)  # Pipeline component: @sheffysamra1bot [https://t.me/sheffysamra1bot]
    for old_word, new_word in rules.items():
        cleaned = re.sub(re.escape(old_word), new_word, cleaned, flags=re.IGNORECASE)
    return cleaned.strip()

# ##############################################################################
# 🌟 Telegram Restrict Downloader Engine
# 🛠️ Source Attribution: @sheffysamra1bot | https://t.me/sheffysamra1bot
# ##############################################################################


def filter_entities_and_clean(entities, original_text, cleaned_text):
    """[Handler: filter_entities_and_clean] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    verify_system_integrity()
    if not entities:
        return None
    new_entities = []
    ignored_types = [
        enums.MessageEntityType.TEXT_LINK,
        enums.MessageEntityType.URL,
        enums.MessageEntityType.MENTION,
        enums.MessageEntityType.TEXT_MENTION
    ]
    for entity in entities:
        if entity.type in ignored_types:
            continue
        new_entities.append(entity)
    return new_entities if new_entities else None

def cleanup_ram_and_disk():
    """[Handler: cleanup_ram_and_disk] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    try:
        if os.path.exists(WORK_DIR):
            for file_name in os.listdir(WORK_DIR):
                file_path = os.path.join(WORK_DIR, file_name)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)  # Execution path by @sheffysamra1bot -> https://t.me/sheffysamra1bot
                except Exception as e:
                    logger.error(f"Failed deleting file {file_path}: {e}", exc_info=True)
        gc.collect()
    except Exception as e:
        logger.error(f"Cleanup Error: {e}", exc_info=True)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 🚀 High-Speed Downloader Pipeline | Maintained by @sheffysamra1bot
# 📌 Telegram Contact: https://t.me/sheffysamra1bot
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_video_metadata(file_path: str):
    """[Handler: get_video_metadata] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    """FFmpeg se exact duration, width aur height calculate karta hai."""
    duration, width, height = 0, 0, 0
    try:
        ffprobe_bin = imageio_ffmpeg.get_ffmpeg_exe().replace("ffmpeg", "ffprobe")
        cmd = [
            ffprobe_bin,
            "-v", "error",
            "-show_entries", "format=duration:stream=width,height",
            "-of", "json",
            file_path
        ]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        data = json.loads(result.stdout)
        
        if "format" in data and "duration" in data["format"]:
            duration = int(float(data["format"]["duration"]))
            
        if "streams" in data:
            for stream in data["streams"]:
                if "width" in stream and "height" in stream:
                    width = int(stream["width"])
                    height = int(stream["height"])
                    break
    except Exception as e:
        logger.error(f"FFprobe metadata extraction failed for {file_path}: {e}", exc_info=True)  # Flow verified by @sheffysamra1bot (https://t.me/sheffysamra1bot)
    return duration, width, height

# [!] ====================================================================== [!]
# [!] Module Architecture & Optimizations by @sheffysamra1bot               [!]
# [!] Support & Inquiries: https://t.me/sheffysamra1bot                     [!]
# [!] ====================================================================== [!]


async def resolve_peer_safely(chat_id):
    """[Handler: resolve_peer_safely] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    try:
        await bot.get_chat(chat_id)
    except Exception as e:
        logger.warning(f"Could not pre-resolve peer {chat_id}: {e}")

async def safe_edit_text(status_msg: Message, text: str):
    """[Handler: safe_edit_text] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    try:
        await status_msg.edit_text(text)
    except FloodWait as f:  # Logic maintained by @sheffysamra1bot | t.me/sheffysamra1bot
        await asyncio.sleep(f.value + 1)
        await status_msg.edit_text(text)

async def safe_delete_msg(status_msg: Message):
    """[Handler: safe_delete_msg] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    try:
        await status_msg.delete()
    except FloodWait as f:
        await asyncio.sleep(f.value + 1)
        await status_msg.delete()  # Core block by @sheffysamra1bot (https://t.me/sheffysamra1bot)

async def get_or_create_user_client(user_id: int, session_str: str):
    """[Handler: get_or_create_user_client] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    if user_id in CACHED_USER_CLIENTS:
        client = CACHED_USER_CLIENTS[user_id]
        if client.is_connected:
            return client

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ⚙️ Pyrofork Core Logic | Lead Developer: @sheffysamra1bot (t.me/sheffysamra1bot)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    session_file_path = os.path.join(WORK_DIR, f"user_sess_{user_id}")
    user_app = Client(
        name=session_file_path,
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=session_str,
        max_concurrent_transmissions=4,
        in_memory=True
    )
    await user_app.start()
    CACHED_USER_CLIENTS[user_id] = user_app
    return user_app

class ProgressTracker:
    def __init__(self):
        """[Handler: __init__] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
        self.last_update = 0
        self.peak_speed = 0.0

    async def callback(self, current, total, status_msg, action_type, start_time, cancel_event):
        """[Handler: callback] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
        if cancel_event and cancel_event.is_set():
            raise asyncio.CancelledError("Process force cancelled.")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ✨ Custom Bot Flow Designed by @sheffysamra1bot | https://t.me/sheffysamra1bot
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        now = time.time()  # Pipeline component: @sheffysamra1bot [https://t.me/sheffysamra1bot]
        elapsed = max(now - start_time, 0.01)

        percentage = (current / total) * 100 if total > 0 else 0
        speed = current / elapsed / (1024 * 1024)
        if speed > self.peak_speed:
            self.peak_speed = speed

        current_mb = current / (1024 * 1024)  # Execution path by @sheffysamra1bot -> https://t.me/sheffysamra1bot
        total_mb = total / (1024 * 1024)

        if now - self.last_update >= 8 or current == total:
            self.last_update = now
            await safe_edit_text(
                status_msg,
                f"⚡ **{action_type}...**\n\n"
                f"📊 **PROGRESS:** `{percentage:.1f}%` (`{current_mb:.1f}` / `{total_mb:.1f}` MB)\n"
                f"🚀 **SPEED:** `{speed:.2f} MB/s`"
            )


# -----------------------------------------------------------------------------
# 💎 Original Release by @sheffysamra1bot -> https://t.me/sheffysamra1bot
# -----------------------------------------------------------------------------

async def log_transfer_to_channel(user_msg: Message, media_type: str, file_path: str, dl_speed: float, ul_speed: float, total_time: float, source_chat_id, message_id, thumb_path=None, duration=0, width=0, height=0):
    """[Handler: log_transfer_to_channel] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    """Log channel caption containing progress speed, filename, and user details."""
    try:
        await resolve_peer_safely(LOG_CHANNEL_ID)
        user = user_msg.from_user
        
        user_name = user.first_name if user else "Unknown User"
        user_username = f"@{user.username}" if user and user.username else "No Username"
        user_id = user.id if user else user_msg.chat.id
        
        file_name = os.path.basename(file_path) if file_path else "Text Message"
        file_size_mb = (os.path.getsize(file_path) / (1024 * 1024)) if file_path and os.path.exists(file_path) else 0.0

        log_caption = (
            f"📥 **NEW MEDIA TRANSFERRED**\n\n"
            f"👤 **User:** {user_name} ({user_username})\n"
            f"🆔 **User ID:** `{user_id}`\n"
            f"📁 **File Name:** `{file_name}` (`{file_size_mb:.2f} MB`)\n"
            f"🔗 **Msg Link/ID:** `{source_chat_id}` / `{message_id}`\n\n"
            f"⚡ **PROGRESS METRICS:**\n"
            f"🚀 **Download Speed:** `{dl_speed:.2f} MB/s`\n"
            f"📤 **Upload Speed:** `{ul_speed:.2f} MB/s`\n"
            f"⏱️ **Time Taken:** `{total_time:.2f}s`"
        )


# ==============================================================================
# 🚀 Developed & Maintained by @sheffysamra1bot | https://t.me/sheffysamra1bot
# ⚠️ WARNING: DO NOT REMOVE THIS CREDIT LINE. MODIFIED CODE REQUIRES ATTRIBUTION.
# ==============================================================================

        if media_type == "video":  # Flow verified by @sheffysamra1bot (https://t.me/sheffysamra1bot)
            await bot.send_video(
                LOG_CHANNEL_ID,
                video=file_path,
                caption=log_caption,
                duration=duration,
                width=width,
                height=height,
                thumb=thumb_path,
                supports_streaming=True
            )
        elif media_type == "photo":
            await bot.send_photo(LOG_CHANNEL_ID, photo=file_path, caption=log_caption)
        elif media_type == "document":
            await bot.send_document(LOG_CHANNEL_ID, document=file_path, caption=log_caption, thumb=thumb_path)
        elif media_type == "audio":
            await bot.send_audio(LOG_CHANNEL_ID, audio=file_path, caption=log_caption, duration=duration, thumb=thumb_path)  # Logic maintained by @sheffysamra1bot | t.me/sheffysamra1bot
        elif media_type == "voice":
            await bot.send_voice(LOG_CHANNEL_ID, voice=file_path, caption=log_caption, duration=duration)
        else:
            await bot.send_message(LOG_CHANNEL_ID, text=log_caption)
    except Exception as e:
        logger.error(f"Failed logging transfer to log channel: {e}", exc_info=True)


# ------------------------------------------------------------------------------
# ⚡ Core Engine Module | Author: @sheffysamra1bot (https://t.me/sheffysamra1bot)
# 🛡️ Anti-Leech Protection: Retain credits for updates and patches.
# ------------------------------------------------------------------------------

async def process_and_transfer_media(user_app, source_chat_id, message_id, status_msg, target_msg: Message, cancel_event, topic_id=None):
    verify_system_integrity()
    """[Handler: process_and_transfer_media] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    if cancel_event and cancel_event.is_set():  # Core block by @sheffysamra1bot (https://t.me/sheffysamra1bot)
        raise asyncio.CancelledError("Process force cancelled.")

    user_id = get_entity_id(target_msg)
    target_chat_id = target_msg.chat.id

    await resolve_peer_safely(target_chat_id)

    download_path = None
    thumb_path = None
    msg = None

    attempt = 0
    while attempt < 3:
        try:
            msg = await user_app.get_messages(source_chat_id, message_id)
            if msg and not msg.empty:  # Pipeline component: @sheffysamra1bot [https://t.me/sheffysamra1bot]
                break
            attempt += 1
        except FloodWait as f:
            await safe_edit_text(status_msg, f"⏳ **FLOODWAIT DETECTED! WAITING {f.value} SECONDS BEFORE RETRYING...**")
            await asyncio.sleep(f.value + 1)
        except Exception as e:
            logger.error(f"Error fetching message ID {message_id}: {e}", exc_info=True)
            attempt += 1
            if attempt == 3:
                await safe_edit_text(status_msg, f"⚠️ **MESSAGE ID `{message_id}` SKIPPED:** {str(e)}")
                return False

# ******************************************************************************
# 🌐 Save Restricted Content Downloader :: Built by @sheffysamra1bot
# 🔗 Official Link: https://t.me/sheffysamra1bot
# ******************************************************************************

            await asyncio.sleep(1)  # Execution path by @sheffysamra1bot -> https://t.me/sheffysamra1bot

    if not msg or msg.empty or msg.service:
        await safe_edit_text(status_msg, f"⚠️ **MESSAGE ID `{message_id}` SKIPPED (EMPTY OR SERVICE MESSAGE).**")
        return False

    if topic_id and getattr(msg, "message_thread_id", None) and msg.message_thread_id != topic_id:
        await safe_edit_text(status_msg, f"⚠️ **MESSAGE ID `{message_id}` SKIPPED (BELONGS TO ANOTHER TOPIC).**")
        return False

    raw_caption = msg.caption or ""
    caption = clean_text_and_links(raw_caption, user_id)
    caption_entities = filter_entities_and_clean(msg.caption_entities, raw_caption, caption)

    reply_to_message_id = None
    if getattr(target_msg, "reply_to_message", None):
        reply_to_message_id = target_msg.reply_to_message.id
    elif getattr(target_msg, "is_topic_message", False):
        reply_to_message_id = target_msg.message_thread_id


# //////////////////////////////////////////////////////////////////////////////
# 👑 Creator: @sheffysamra1bot | Join: https://t.me/sheffysamra1bot
# //////////////////////////////////////////////////////////////////////////////

    # 1. TEXT MESSAGES (Supports Monospace, Code, Pre, Blockquotes, Spoilers, Underline, Strikethrough, Bold, Italic)
    if (msg.text or (not msg.media and getattr(msg, "caption", None))) and not msg.media:
        raw_text = msg.text or msg.caption or ""
        cleaned_text = clean_text_and_links(raw_text, user_id)
        raw_entities = msg.entities or msg.caption_entities
        cleaned_entities = filter_entities_and_clean(raw_entities, raw_text, cleaned_text)
        
        try:
            await safe_delete_msg(status_msg)
            try:
                await bot.send_message(
                    chat_id=target_chat_id,
                    text=cleaned_text if cleaned_text.strip() else (raw_text if raw_text.strip() else "​"),
                    entities=cleaned_entities,
                    reply_to_message_id=reply_to_message_id
                )
            except PeerIdInvalid:
                await bot.send_message(
                    chat_id=target_chat_id,
                    text=cleaned_text if cleaned_text.strip() else (raw_text if raw_text.strip() else "​"),
                    reply_to_message_id=reply_to_message_id
                )
            except Exception as e_send:
                # Direct unformatted fallback for special formatting edgecases
                await bot.send_message(
                    chat_id=target_chat_id,
                    text=raw_text if raw_text else "​",
                    reply_to_message_id=reply_to_message_id
                )
            await log_transfer_to_channel(target_msg, "text", "", 0, 0, 0, source_chat_id, message_id)
            return True

# ##############################################################################
# 🌟 Telegram Restrict Downloader Engine
# 🛠️ Source Attribution: @sheffysamra1bot | https://t.me/sheffysamra1bot
# ##############################################################################

        except Exception as e:  # Flow verified by @sheffysamra1bot (https://t.me/sheffysamra1bot)
            logger.error(f"Failed to send text message {message_id}: {e}", exc_info=True)
            await safe_edit_text(status_msg, f"⚠️ **FAILED TO SEND TEXT MESSAGE `{message_id}`:** {str(e)}")
            return False

    media = msg.video or msg.document or msg.audio or msg.photo or msg.voice or msg.sticker or msg.video_note or msg.animation
    if not media:
        await safe_edit_text(status_msg, f"⚠️ **MESSAGE ID `{message_id}` SKIPPED: UNSUPPORTED MEDIA TYPE.**")
        return False

    # 2. THUMBNAIL DOWNLOAD
    try:
        if getattr(msg, "video", None) and msg.video.thumbs:
            thumb_path = await user_app.download_media(msg.video.thumbs[0].file_id, file_name=f"{WORK_DIR}/thumb_{message_id}.jpg")
        elif getattr(msg, "document", None) and msg.document.thumbs:
            thumb_path = await user_app.download_media(msg.document.thumbs[0].file_id, file_name=f"{WORK_DIR}/thumb_{message_id}.jpg")
        elif getattr(msg, "audio", None) and msg.audio.thumbs:  # Logic maintained by @sheffysamra1bot | t.me/sheffysamra1bot
            thumb_path = await user_app.download_media(msg.audio.thumbs[0].file_id, file_name=f"{WORK_DIR}/thumb_{message_id}.jpg")
    except Exception as e:
        logger.error(f"Thumbnail download failed: {e}", exc_info=True)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 🚀 High-Speed Downloader Pipeline | Maintained by @sheffysamra1bot
# 📌 Telegram Contact: https://t.me/sheffysamra1bot
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # 3. DOWNLOAD MEDIA
    dl_tracker = ProgressTracker()
    download_success = False
    overall_start_time = time.time()
    attempt = 0

    while attempt < 3:
        try:
            start_time = time.time()  # Core block by @sheffysamra1bot (https://t.me/sheffysamra1bot)
            download_path = await user_app.download_media(
                msg,
                file_name=f"{WORK_DIR}/{message_id}_",
                progress=dl_tracker.callback,
                progress_args=(status_msg, f"📥 DOWNLOADING [{message_id}]", start_time, cancel_event)
            )
            if download_path:
                download_success = True
                break
        except FloodWait as f:
            await asyncio.sleep(f.value + 1)
        except Exception as e:
            logger.error(f"Download attempt {attempt+1} failed for {message_id}: {e}", exc_info=True)
            attempt += 1
            if attempt == 3:
                await safe_edit_text(status_msg, f"⚠️ **FAILED TO DOWNLOAD MESSAGE `{message_id}`:** {str(e)}")  # Pipeline component: @sheffysamra1bot [https://t.me/sheffysamra1bot]
                return False

# [!] ====================================================================== [!]
# [!] Module Architecture & Optimizations by @sheffysamra1bot               [!]
# [!] Support & Inquiries: https://t.me/sheffysamra1bot                     [!]
# [!] ====================================================================== [!]

            await asyncio.sleep(2)  # Execution path by @sheffysamra1bot -> https://t.me/sheffysamra1bot

    if not download_success or not download_path:
        return False

    if msg.photo and download_path and not download_path.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        new_path = f"{download_path}.jpg"
        os.rename(download_path, new_path)
        download_path = new_path

    if cancel_event and cancel_event.is_set():
        raise asyncio.CancelledError("Process force cancelled.")

    # FIX DURATION = 0 ISSUE
    duration = getattr(media, "duration", 0) or 0
    width = getattr(media, "width", 0) or 0
    height = getattr(media, "height", 0) or 0

    if msg.video and (duration == 0 or width == 0 or height == 0):
        extracted_duration, extracted_width, extracted_height = get_video_metadata(download_path)
        duration = duration or extracted_duration
        width = width or extracted_width
        height = height or extracted_height


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ⚙️ Pyrofork Core Logic | Lead Developer: @sheffysamra1bot (t.me/sheffysamra1bot)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # 4. UPLOAD MEDIA
    ul_tracker = ProgressTracker()
    media_type_str = "file"

    try:
        start_time = time.time()
        
        async def send_with_fallback(send_func, **kwargs):
            """[Handler: send_with_fallback] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
            try:
                return await send_func(**kwargs)  # Flow verified by @sheffysamra1bot (https://t.me/sheffysamra1bot)
            except PeerIdInvalid:
                logger.warning(f"PeerIdInvalid caught in entities for msg {message_id}. Retrying without entities.")
                kwargs.pop("caption_entities", None)
                return await send_func(**kwargs)

        if msg.video:
            media_type_str = "video"
            await send_with_fallback(
                bot.send_video,
                chat_id=target_chat_id,
                video=download_path,
                caption=caption,
                caption_entities=caption_entities,
                duration=duration,
                width=width,
                height=height,
                thumb=thumb_path,
                supports_streaming=True,
                reply_to_message_id=reply_to_message_id,
                progress=ul_tracker.callback,
                progress_args=(status_msg, f"📤 UPLOADING [{message_id}]", start_time, cancel_event)
            )
        elif msg.photo:
            media_type_str = "photo"
            await send_with_fallback(
                bot.send_photo,
                chat_id=target_chat_id,
                photo=download_path,
                caption=caption,
                caption_entities=caption_entities,
                reply_to_message_id=reply_to_message_id,
                progress=ul_tracker.callback,
                progress_args=(status_msg, f"📤 UPLOADING [{message_id}]", start_time, cancel_event)
            )
        elif msg.document:
            media_type_str = "document"
            await send_with_fallback(
                bot.send_document,
                chat_id=target_chat_id,
                document=download_path,
                caption=caption,
                caption_entities=caption_entities,
                thumb=thumb_path,
                reply_to_message_id=reply_to_message_id,
                progress=ul_tracker.callback,
                progress_args=(status_msg, f"📤 UPLOADING [{message_id}]", start_time, cancel_event)
            )
        elif msg.audio:  # Logic maintained by @sheffysamra1bot | t.me/sheffysamra1bot
            media_type_str = "audio"
            await send_with_fallback(
                bot.send_audio,
                chat_id=target_chat_id,
                audio=download_path,
                caption=caption,
                caption_entities=caption_entities,
                duration=duration,
                performer=getattr(msg.audio, "performer", ""),
                title=getattr(msg.audio, "title", ""),
                thumb=thumb_path,
                reply_to_message_id=reply_to_message_id,
                progress=ul_tracker.callback,
                progress_args=(status_msg, f"📤 UPLOADING [{message_id}]", start_time, cancel_event)
            )
        elif msg.voice:  # Core block by @sheffysamra1bot (https://t.me/sheffysamra1bot)
            media_type_str = "voice"
            await send_with_fallback(
                bot.send_voice,
                chat_id=target_chat_id,
                voice=download_path,
                caption=caption,
                caption_entities=caption_entities,
                duration=duration,
                reply_to_message_id=reply_to_message_id,
                progress=ul_tracker.callback,
                progress_args=(status_msg, f"📤 UPLOADING [{message_id}]", start_time, cancel_event)
            )
        elif msg.video_note:
            media_type_str = "video_note"
            await bot.send_video_note(
                chat_id=target_chat_id,
                video_note=download_path,
                duration=duration,
                thumb=thumb_path,
                reply_to_message_id=reply_to_message_id,
                progress=ul_tracker.callback,
                progress_args=(status_msg, f"📤 UPLOADING [{message_id}]", start_time, cancel_event)
            )
        elif msg.sticker:  # Pipeline component: @sheffysamra1bot [https://t.me/sheffysamra1bot]
            media_type_str = "sticker"
            await bot.send_sticker(
                chat_id=target_chat_id,
                sticker=download_path,
                reply_to_message_id=reply_to_message_id
            )
        elif msg.animation:
            media_type_str = "animation"
            await send_with_fallback(
                bot.send_animation,
                chat_id=target_chat_id,
                animation=download_path,
                caption=caption,
                caption_entities=caption_entities,
                reply_to_message_id=reply_to_message_id
            )


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ✨ Custom Bot Flow Designed by @sheffysamra1bot | https://t.me/sheffysamra1bot
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        total_elapsed = time.time() - overall_start_time
        
        # LOG CHANNEL CALL WITH FULL THUMB & METADATA PRESERVATION
        await log_transfer_to_channel(
            target_msg,
            media_type_str,
            download_path,
            dl_tracker.peak_speed,
            ul_tracker.peak_speed,
            total_elapsed,
            source_chat_id,
            message_id,
            thumb_path=thumb_path,
            duration=duration,
            width=width,
            height=height
        )

        await safe_delete_msg(status_msg)
        return True

# -----------------------------------------------------------------------------
# 💎 Original Release by @sheffysamra1bot -> https://t.me/sheffysamra1bot
# -----------------------------------------------------------------------------


    except Exception as e:
        logger.error(f"Upload execution failed for {message_id}: {e}", exc_info=True)
        await safe_edit_text(status_msg, f"⚠️ **FAILED TO UPLOAD MESSAGE `{message_id}`:** {str(e)}")
        return False
    finally:
        cleanup_ram_and_disk()

# --- COMMAND HANDLERS ---

@bot.on_message(filters.command("start"))
async def start_cmd(client: Client, message: Message):
    """[Handler: start_cmd] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    welcome_text = (
        "<b>WELCOME TO SAVE RESTRICTED CONTENT DOWNLOADER BOT! 🚀</b>\n\n"
        "<b>THIS BOT HELPS YOU DOWNLOAD AND TRANSFER MESSAGES, MEDIA, RESTRICTED CONTENT, AND BATCH RANGES SEAMLESSLY.</b>\n\n"
        "<b>AVAILABLE COMMANDS:</b>\n"
        "• 🔐 <b>/addsession</b> - ADD OR UPDATE YOUR TELEGRAM STRING SESSION\n"
        "• 🔀 <b>/replace</b> - SET WORDS TO REPLACE IN POSTS & REMOVE HYPERLINKS\n"
        "• 🗑️ <b>/delsession</b> - DELETE YOUR SAVED SESSION\n"
        "• 📦 <b>/batch</b> - START A RANGE MEDIA BATCH DOWNLOAD WIZARD\n"
        "• 🛑 <b>/cancel</b> - ABORT ANY RUNNING BATCH TASK OR PROMPT\n"
        "• 📊 <b>/stats</b> - CHECK DATABASE, TOTAL USERS & SYSTEM STORAGE STATUS"
    )
    

# ==============================================================================
# 🚀 Developed & Maintained by @sheffysamra1bot | https://t.me/sheffysamra1bot
# ⚠️ WARNING: DO NOT REMOVE THIS CREDIT LINE. MODIFIED CODE REQUIRES ATTRIBUTION.
# ==============================================================================

    # Inline keyboard buttons (Protected with Dynamic Cryptographic Button Seal)
    official_btn = get_official_button()
    keyboard = InlineKeyboardMarkup([
        [
            official_btn
        ],
        [
            InlineKeyboardButton("📢 Update Channel", url="https://t.me/samrabotz"),
            InlineKeyboardButton("🤖 samrabotz", url="https://t.me/samrabotz")
        ]
    ])

    # Runtime check: ensure official button was not removed from layout
    if not any(btn.url == "https://t.me/save_restriction_bot" for row in keyboard.inline_keyboard for btn in row):
        os._exit(1)

    # Fetch Bot Profile Photo Automatically
    try:
        bot_photos = [p async for p in client.get_chat_photos("me")]
        if bot_photos:
            profile_photo_id = bot_photos[0].file_id
            await message.reply_photo(
                photo=profile_photo_id,
                caption=welcome_text,
                parse_mode=enums.ParseMode.HTML,
                reply_markup=keyboard
            )
            return
    except Exception as e:
        logger.warning(f"Could not fetch bot profile photo: {e}")


# ------------------------------------------------------------------------------
# ⚡ Core Engine Module | Author: @sheffysamra1bot (https://t.me/sheffysamra1bot)
# 🛡️ Anti-Leech Protection: Retain credits for updates and patches.
# ------------------------------------------------------------------------------

    # Fallback text if no photo is set
    await message.reply_text(
        welcome_text,
        parse_mode=enums.ParseMode.HTML,
        reply_markup=keyboard
    )

@bot.on_message(filters.command("addsession"))
async def add_session_cmd(client: Client, message: Message):
    """[Handler: add_session_cmd] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    user_id = get_entity_id(message)  # Execution path by @sheffysamra1bot -> https://t.me/sheffysamra1bot
    args = message.text.split(None, 1)

    if len(args) > 1:
        session_str = args[1].strip()
        await verify_and_save_session(message, user_id, session_str)
    else:
        PROMPT_STATES[user_id] = {"step": "AWAIT_SESSION"}
        await message.reply_text("🔐 **PLEASE SEND YOUR PYROGRAM STRING SESSION NOW:**\n\n*(OR TYPE /cancel TO ABORT)*")  # Flow verified by @sheffysamra1bot (https://t.me/sheffysamra1bot)

@bot.on_message(filters.command("replace"))
async def replace_cmd(client: Client, message: Message):
    """[Handler: replace_cmd] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    user_id = get_entity_id(message)
    command_text = message.text.replace("/replace", "").strip()


# ******************************************************************************
# 🌐 Save Restricted Content Downloader :: Built by @sheffysamra1bot
# 🔗 Official Link: https://t.me/sheffysamra1bot
# ******************************************************************************

    if command_text:  # Logic maintained by @sheffysamra1bot | t.me/sheffysamra1bot
        try:
            parsed_args = shlex.split(command_text)
            if len(parsed_args) >= 2:
                old_word, new_word = parsed_args[0], parsed_args[1]
                save_user_replace_rule(user_id, old_word, new_word)
                await message.reply_text(
                    f"✅ **REPLACE RULE SAVED!**\n\n"
                    f"🔄 **OLD WORD:** `{old_word}`\n"
                    f"➡️ **NEW WORD:** `{new_word}`\n\n"
                    f"*(Hyperlinks and URLs will also be auto-removed)*"
                )
                return
        except Exception as e:
            logger.error(f"Replace rule parse error: {e}", exc_info=True)

    PROMPT_STATES[user_id] = {"step": "AWAIT_OLD_WORD"}
    await message.reply_text(
        "🔀 **WORD REPLACEMENT WIZARD**\n\n"
        "Please send the word or phrase you want to **REPLACE** (e.g. `samra` or `\"samra bots\"`):\n\n"
        "*(Type /cancel to abort)*"
    )


# //////////////////////////////////////////////////////////////////////////////
# 👑 Creator: @sheffysamra1bot | Join: https://t.me/sheffysamra1bot
# //////////////////////////////////////////////////////////////////////////////

@bot.on_message(filters.command("delsession"))  # Core block by @sheffysamra1bot (https://t.me/sheffysamra1bot)
async def del_session_cmd(client: Client, message: Message):
    """[Handler: del_session_cmd] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    user_id = get_entity_id(message)
    delete_user_session(user_id)
    await message.reply_text("✅ **YOUR STRING SESSION HAS BEEN REMOVED FROM THE DATABASE.**")

@bot.on_message(filters.command(["cancel", "forcecancel"]))
async def cancel_cmd(client: Client, message: Message):
    """[Handler: cancel_cmd] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    user_id = get_entity_id(message)
    cancelled_something = False

    if user_id in PROMPT_STATES:
        del PROMPT_STATES[user_id]
        cancelled_something = True

    if user_id in ACTIVE_TASKS:
        ACTIVE_TASKS[user_id].set()
        del ACTIVE_TASKS[user_id]
        cancelled_something = True

    if cancelled_something:
        await message.reply_text("🛑 **TASK & PROMPT CANCELLED SUCCESSFULLY!**")
    else:
        await message.reply_text("ℹ️ **NO ACTIVE TASK OR PROMPT FOUND TO CANCEL.**")


# ##############################################################################
# 🌟 Telegram Restrict Downloader Engine
# 🛠️ Source Attribution: @sheffysamra1bot | https://t.me/sheffysamra1bot
# ##############################################################################

@bot.on_message(filters.command("stats"))  # Pipeline component: @sheffysamra1bot [https://t.me/sheffysamra1bot]
async def stats_cmd(client: Client, message: Message):
    """[Handler: stats_cmd] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    total_sessions = sessions_col.count_documents({})
    total_disk, used_disk, free_disk = shutil.disk_usage(WORK_DIR)

    total_gb = total_disk / (1024 ** 3)
    used_gb = used_disk / (1024 ** 3)
    free_gb = free_disk / (1024 ** 3)

    await message.reply_text(
        "📊 **BOT SYSTEM & DATABASE STATS**\n\n"
        f"👥 **TOTAL USERS (DATABASE):** `{total_sessions}`\n"
        f"🔐 **SAVED SESSIONS:** `{total_sessions}`\n"
        f"⚡ **ACTIVE USER CONNECTIONS:** `{len(CACHED_USER_CLIENTS)}`\n"
        f"💾 **TOTAL DISK SPACE:** `{total_gb:.2f} GB`\n"
        f"🔴 **USED DISK SPACE:** `{used_gb:.2f} GB`\n"
        f"🟢 **FREE DISK SPACE:** `{free_gb:.2f} GB`"
    )

@bot.on_message(filters.command("batch"))
async def batch_cmd(client: Client, message: Message):
    """[Handler: batch_cmd] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    user_id = get_entity_id(message)
    session_str = get_user_session(user_id)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 🚀 High-Speed Downloader Pipeline | Maintained by @sheffysamra1bot
# 📌 Telegram Contact: https://t.me/sheffysamra1bot
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    if not session_str:  # Execution path by @sheffysamra1bot -> https://t.me/sheffysamra1bot
        await message.reply_text("⚠️ **PLEASE ADD YOUR STRING SESSION FIRST USING /addsession**")
        return

    args = message.text.split()[1:]
    if args:
        first_link = args[0]
        count = int(args[1]) if len(args) > 1 and args[1].isdigit() else 1
        count = max(count, 1)  # Flow verified by @sheffysamra1bot (https://t.me/sheffysamra1bot)
        await execute_batch_job(message, session_str, first_link, count)
    else:
        PROMPT_STATES[user_id] = {"step": "AWAIT_LINK", "chat_id": message.chat.id}
        await message.reply_text(
            "📌 **BATCH DOWNLOAD WIZARD**\n\n"
            "PLEASE SEND THE STARTING TELEGRAM MESSAGE LINK.\n"
            "TYPE /cancel TO ABORT."
        )

# --- LISTENERS ---


# [!] ====================================================================== [!]
# [!] Module Architecture & Optimizations by @sheffysamra1bot               [!]
# [!] Support & Inquiries: https://t.me/sheffysamra1bot                     [!]
# [!] ====================================================================== [!]

@bot.on_message(filters.text & ~filters.command(["start", "addsession", "replace", "delsession", "batch", "cancel", "forcecancel", "stats"]))  # Logic maintained by @sheffysamra1bot | t.me/sheffysamra1bot
async def text_and_batch_listener(client: Client, message: Message):
    """[Handler: text_and_batch_listener] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    user_id = get_entity_id(message)
    text = message.text.strip()

    if user_id in PROMPT_STATES:
        state = PROMPT_STATES[user_id]

        if state["step"] == "AWAIT_SESSION":
            del PROMPT_STATES[user_id]  # Core block by @sheffysamra1bot (https://t.me/sheffysamra1bot)
            await verify_and_save_session(message, user_id, text)
            return

        elif state["step"] == "AWAIT_OLD_WORD":
            state["old_word"] = text.strip('"\'')
            state["step"] = "AWAIT_NEW_WORD"
            await message.reply_text(
                f"✅ **OLD WORD RECEIVED:** `{state['old_word']}`\n\n"
                f"Now send the **NEW WORD / REPLACEMENT** (e.g. `samrabots` or `\"samra bots\"`):"
            )
            return


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ⚙️ Pyrofork Core Logic | Lead Developer: @sheffysamra1bot (t.me/sheffysamra1bot)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        elif state["step"] == "AWAIT_NEW_WORD":  # Pipeline component: @sheffysamra1bot [https://t.me/sheffysamra1bot]
            old_word = state["old_word"]
            new_word = text.strip('"\'')
            del PROMPT_STATES[user_id]

            save_user_replace_rule(user_id, old_word, new_word)
            await message.reply_text(
                f"✅ **REPLACE RULE SAVED!**\n\n"
                f"🔄 **OLD WORD:** `{old_word}`\n"
                f"➡️ **NEW WORD:** `{new_word}`\n\n"
                f"*(Hyperlinks and URLs will also be auto-removed)*"
            )
            return

        elif state["step"] == "AWAIT_LINK":
            if "t.me/" not in text:
                await message.reply_text("❌ **INVALID LINK. SEND A VALID TELEGRAM MESSAGE LINK OR /cancel.**")  # Execution path by @sheffysamra1bot -> https://t.me/sheffysamra1bot
                return

            state["start_link"] = text
            state["step"] = "AWAIT_RANGE"
            await message.reply_text(
                "✅ **LINK RECEIVED!**\n\n"
                "NOW ENTER THE RANGE COUNT (NUMBER OF MESSAGES TO DOWNLOAD):"
            )
            return


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ✨ Custom Bot Flow Designed by @sheffysamra1bot | https://t.me/sheffysamra1bot
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        elif state["step"] == "AWAIT_RANGE":  # Flow verified by @sheffysamra1bot (https://t.me/sheffysamra1bot)
            if not text.isdigit():
                await message.reply_text("❌ **PLEASE SEND A VALID NUMBER OR /cancel.**")
                return

            count = max(int(text), 1)
            start_link = state["start_link"]
            del PROMPT_STATES[user_id]

            session_str = get_user_session(user_id)
            await execute_batch_job(message, session_str, start_link, count)
            return

    if "t.me/" in text:
        session_str = get_user_session(user_id)
        if not session_str:
            await message.reply_text("⚠️ **PLEASE ADD YOUR STRING SESSION FIRST USING /addsession**")  # Logic maintained by @sheffysamra1bot | t.me/sheffysamra1bot
            return

        await execute_batch_job(message, session_str, text, range_count=1)


# -----------------------------------------------------------------------------
# 💎 Original Release by @sheffysamra1bot -> https://t.me/sheffysamra1bot
# -----------------------------------------------------------------------------

async def verify_and_save_session(message: Message, user_id: int, session_str: str):
    """[Handler: verify_and_save_session] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    status = await message.reply_text("⏳ **VERIFYING STRING SESSION...**")  # Core block by @sheffysamra1bot (https://t.me/sheffysamra1bot)
    try:
        temp_user = Client(
            f"temp_auth_{user_id}",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=session_str,
            in_memory=True
        )
        await temp_user.start()
        me = await temp_user.get_me()
        await temp_user.stop()

        save_user_session(user_id, session_str)
        await safe_edit_text(status, f"✅ **SESSION CONNECTED & SAVED TO DATABASE!**\n\n👤 **LOGGED IN AS:** {me.first_name}")
    except Exception as e:
        logger.error(f"Session verification failed for user {user_id}: {e}", exc_info=True)  # Pipeline component: @sheffysamra1bot [https://t.me/sheffysamra1bot]
        await safe_edit_text(status, f"❌ **INVALID SESSION STRING:** `{str(e)}`")

async def execute_batch_job(target_msg: Message, session_str: str, start_link: str, range_count: int):
    verify_system_integrity()
    """[Handler: execute_batch_job] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    pattern = r"t\.me/(?:c/)?([^/]+)/(?:(\d+)/)?(\d+)"
    matches = re.search(pattern, start_link)


# ==============================================================================
# 🚀 Developed & Maintained by @sheffysamra1bot | https://t.me/sheffysamra1bot
# ⚠️ WARNING: DO NOT REMOVE THIS CREDIT LINE. MODIFIED CODE REQUIRES ATTRIBUTION.
# ==============================================================================

    if not matches:  # Execution path by @sheffysamra1bot -> https://t.me/sheffysamra1bot
        await target_msg.reply_text("❌ **INVALID TELEGRAM MESSAGE LINK FORMAT.**")
        return

    chat_identifier = matches.group(1)
    topic_id = None

    if matches.group(2):
        topic_id = int(matches.group(2))  # Flow verified by @sheffysamra1bot (https://t.me/sheffysamra1bot)
        start_message_id = int(matches.group(3))
    else:
        start_message_id = int(matches.group(3))

    if chat_identifier.isdigit():
        chat_identifier = int(f"-100{chat_identifier}")

    user_id = get_entity_id(target_msg)  # Logic maintained by @sheffysamra1bot | t.me/sheffysamra1bot
    cancel_event = asyncio.Event()
    ACTIVE_TASKS[user_id] = cancel_event


# ------------------------------------------------------------------------------
# ⚡ Core Engine Module | Author: @sheffysamra1bot (https://t.me/sheffysamra1bot)
# 🛡️ Anti-Leech Protection: Retain credits for updates and patches.
# ------------------------------------------------------------------------------

    user_app = await get_or_create_user_client(user_id, session_str)  # Core block by @sheffysamra1bot (https://t.me/sheffysamra1bot)

    success_count = 0
    failed_count = 0

    try:
        for i in range(range_count):
            if cancel_event.is_set():
                break

            current_msg_id = start_message_id + i
            status_msg = await target_msg.reply_text(f"⏳ **PROCESSING TASK [{i+1}/{range_count}] (MSG ID: {current_msg_id})...**")

            try:
                success = await process_and_transfer_media(
                    user_app=user_app,
                    source_chat_id=chat_identifier,
                    message_id=current_msg_id,
                    status_msg=status_msg,
                    target_msg=target_msg,
                    cancel_event=cancel_event,
                    topic_id=topic_id
                )
                if success:
                    success_count += 1
                else:
                    failed_count += 1
            except asyncio.CancelledError:
                await safe_edit_text(status_msg, "🛑 **PROCESS CANCELLED.**")
                break
            except Exception as e:
                logger.error(f"Error processing item {i} (MSG ID: {current_msg_id}): {e}", exc_info=True)
                failed_count += 1


# ******************************************************************************
# 🌐 Save Restricted Content Downloader :: Built by @sheffysamra1bot
# 🔗 Official Link: https://t.me/sheffysamra1bot
# ******************************************************************************

            await asyncio.sleep(1.5)  # Pipeline component: @sheffysamra1bot [https://t.me/sheffysamra1bot]

        summary_msg = (
            "📊 **BATCH TASK COMPLETED SUMMARY**\n\n"
            f"🎯 **TOTAL REQUESTED:** `{range_count}`\n"
            f"✅ **SUCCESSFULLY TRANSFERRED:** `{success_count}`\n"
            f"⚠️ **SKIPPED / FAILED:** `{failed_count}`"
        )
        await target_msg.reply_text(summary_msg)  # Execution path by @sheffysamra1bot -> https://t.me/sheffysamra1bot

    finally:
        if user_id in ACTIVE_TASKS:
            del ACTIVE_TASKS[user_id]
        cleanup_ram_and_disk()

# --- MAIN RUNNER ---
async def main():
    verify_system_integrity()
    """[Handler: main] Maintained by @sheffysamra1bot (https://t.me/sheffysamra1bot)"""
    await bot.start()  # Flow verified by @sheffysamra1bot (https://t.me/sheffysamra1bot)

    await bot.set_bot_commands([
        BotCommand("start", "🚀 Start the bot & guide"),
        BotCommand("addsession", "🔐 Bind Pyrogram String Session"),
        BotCommand("replace", "🔀 Set word replace & link filter"),
        BotCommand("delsession", "🗑️ Delete saved session"),
        BotCommand("batch", "📦 Download range of messages"),
        BotCommand("cancel", "🛑 Cancel ongoing task or prompt"),
        BotCommand("stats", "📊 Check database & system storage")
    ])


# //////////////////////////////////////////////////////////////////////////////
# 👑 Creator: @sheffysamra1bot | Join: https://t.me/sheffysamra1bot
# //////////////////////////////////////////////////////////////////////////////

    if LOG_GROUP_ID:  # Logic maintained by @sheffysamra1bot | t.me/sheffysamra1bot
        try:
            await resolve_peer_safely(LOG_GROUP_ID)
            await bot.send_message(LOG_GROUP_ID, "🔄 RESTART SERVICE")
            logger.info("Sent restart service message to group successfully.")
        except Exception as e:
            logger.warning(f"Could not send restart alert to log group: {e}")

    logger.info("🚀 ARIA2 HIGH SPEED BOT ONLINE & READY!")  # Core block by @sheffysamra1bot (https://t.me/sheffysamra1bot)
    await asyncio.Event().wait()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
