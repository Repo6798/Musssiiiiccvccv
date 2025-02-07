import math
from config import SUPPORT_CHAT, OWNER_USERNAME
from pyrogram.types import InlineKeyboardButton
from SHUKLAMUSIC import app
import config
from SHUKLAMUSIC.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        bar = "꯭ﮩ٨꯭ـﮩ꯭ﮩ٨꯭ـﮩ꯭ﮩ٨꯭ـﮩ꯭ﮩ٨꯭ـﮩ꯭ﮩ٨꯭ـﮩـ꯭꯭MR"
    elif 10 < umm < 20:
        bar = "꯭ﮩ٨꯭ـﮩ꯭ﮩ٨꯭ـﮩ꯭ﮩ٨꯭ـﮩ꯭ﮩ٨꯭ـﮩ꯭ﮩ٨꯭ـﮩـ꯭꯭꯭MRﮩ٨"
    elif 20 <= umm < 30:
        bar = "꯭ﮩ٨꯭ـﮩ꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩMRـ꯭꯭꯭꯭ﮩ٨꯭ﮩ٨꯭ـﮩ"
    elif 30 <= umm < 40:
        bar = "꯭ﮩ٨꯭ـﮩ꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩMRـ꯭꯭꯭꯭ﮩ٨꯭ﮩ٨꯭ـﮩ"
    elif 40 <= umm < 50:
        bar = "꯭ﮩ٨꯭ـﮩ꯭ـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩ꯭ﮩ٨꯭ـMRـ꯭꯭꯭꯭ﮩ٨꯭ـﮩ꯭ـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩ꯭ـ꯭꯭꯭꯭"
    elif 50 <= umm < 60:
        bar = "꯭ﮩـﮩ꯭ـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩ꯭ـ꯭꯭꯭ﮩMRـﮩ꯭ـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩ꯭ـ꯭꯭꯭꯭"
    elif 60 <= umm < 70:
        bar = "꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭MRﮩ٨ـ꯭꯭꯭꯭꯭ﮩ٨꯭ــﮩ꯭ﮩ٨꯭ـﮩ"
    elif 70 <= umm < 80:
        bar = "꯭ﮩ٨꯭MRـﮩـ꯭꯭꯭꯭ﮩ٨ـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩ꯭ﮩ٨꯭ـﮩ꯭ﮩ٨꯭ـﮩ"
    elif 80 <= umm < 95:
        bar = "ـ꯭꯭꯭꯭MRﮩ٨꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩ꯭ﮩ٨꯭ـﮩ꯭ﮩ٨꯭ـﮩ"
    else:
        bar = "ـ꯭꯭꯭꯭MRﮩ٨꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩ꯭ﮩ٨꯭ـﮩ꯭ﮩ٨꯭ـﮩ"
    buttons = [
                [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text="I▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="N।। ", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="D▷▷। ", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text=" C □ ", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
         InlineKeyboardButton(text="💞 𝐎𝐰𝐧𝐞𝐫 💞", user_id=config.OWNER_ID),
         InlineKeyboardButton(text="🥀 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 🥀", url=f"{SUPPORT_CHAT}",),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="I▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="N।। ", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="D▷▷। ", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text=" C □ ", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
         InlineKeyboardButton(text="💞 𝐎𝐰𝐧𝐞𝐫 💞", user_id=config.OWNER_ID),
         InlineKeyboardButton(text="🥀 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 🥀", url=f"{SUPPORT_CHAT}",),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"SHUKLAPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"SHUKLAPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
