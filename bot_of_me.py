import os
import random
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
import emoji
from aiogram.types.message import ContentType
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3

TOKEN = ''
bot = Bot(token=TOKEN, proxy='http://proxy.server:3128')
dp = Dispatcher(bot)

conn = sqlite3.connect('/home/LsVbadd07/telebase')
cursor = conn.cursor()
cursor.execute("SELECT file_id FROM BotContent WHERE Subcommand='music'")
music_list = cursor.fetchall()

pasta_directory = r'/home/LsVbadd07/paste'
pasta_files = os.listdir(pasta_directory)
filo_directory = r'/home/LsVbadd07/filosaf'
filo_files = os.listdir(filo_directory)

inline_btn_about_1 = InlineKeyboardButton('1', callback_data='about1')
inline_btn_about_2 = InlineKeyboardButton('2', callback_data='about2')
inline_btn_about_3 = InlineKeyboardButton('3', callback_data='about3')
inline_kb_about_full = InlineKeyboardMarkup(row_width=1).row(inline_btn_about_1, inline_btn_about_2, inline_btn_about_3)
inline_btn_past = InlineKeyboardButton('Интересно', callback_data='past')
inline_kb_past = InlineKeyboardMarkup(row_width=2).add(inline_btn_past)
inline_btn_more = InlineKeyboardButton('Подробнее', callback_data='more')
inline_kb_more = InlineKeyboardMarkup(row_width=2).add(inline_btn_more)
inline_btn_anime_1 = InlineKeyboardButton('1', callback_data='anime1')
inline_btn_anime_2 = InlineKeyboardButton('2', callback_data='anime2')
inline_btn_anime_3 = InlineKeyboardButton('3', callback_data='anime3')
inline_btn_anime_4 = InlineKeyboardButton('4', callback_data='anime4')
inline_btn_anime_5 = InlineKeyboardButton('5', callback_data='anime5')
inline_btn_anime_6 = InlineKeyboardButton('6', callback_data='anime6')
inline_btn_anime_7 = InlineKeyboardButton('7', callback_data='anime7')
inline_btn_anime_8 = InlineKeyboardButton('8', callback_data='anime8')
inline_btn_anime_9 = InlineKeyboardButton('9', callback_data='anime9')
inline_btn_anime_10 = InlineKeyboardButton('10', callback_data='anime10')
inline_btn_anime_11 = InlineKeyboardButton('11', callback_data='anime11')
inline_btn_anime_12 = InlineKeyboardButton('12', callback_data='anime12')
inline_kb_anime_full = InlineKeyboardMarkup(row_width=1).row(inline_btn_anime_1, inline_btn_anime_2, inline_btn_anime_3,
                                                             inline_btn_anime_4, inline_btn_anime_5, inline_btn_anime_6)
inline_kb_anime_full.row(inline_btn_anime_7, inline_btn_anime_8, inline_btn_anime_9,
                         inline_btn_anime_10, inline_btn_anime_11, inline_btn_anime_12)
inline_btn_film_1 = InlineKeyboardButton('1', callback_data='film1')
inline_btn_film_2 = InlineKeyboardButton('2', callback_data='film2')
inline_btn_film_3 = InlineKeyboardButton('3', callback_data='film3')
inline_btn_film_4 = InlineKeyboardButton('4', callback_data='film4')
inline_btn_film_5 = InlineKeyboardButton('5', callback_data='film5')
inline_btn_film_6 = InlineKeyboardButton('6', callback_data='film6')
inline_btn_film_7 = InlineKeyboardButton('7', callback_data='film7')
inline_btn_film_8 = InlineKeyboardButton('8', callback_data='film8')
inline_btn_film_9 = InlineKeyboardButton('9', callback_data='film9')
inline_btn_film_10 = InlineKeyboardButton('10', callback_data='film10')
inline_btn_film_11 = InlineKeyboardButton('11', callback_data='film11')
inline_btn_film_12 = InlineKeyboardButton('12', callback_data='film12')
inline_kb_film_full = InlineKeyboardMarkup(row_width=1).row(inline_btn_film_1, inline_btn_film_2, inline_btn_film_3,
                                                            inline_btn_film_4)
inline_kb_film_full.row(inline_btn_film_5, inline_btn_film_6, inline_btn_film_7, inline_btn_film_8)
inline_kb_film_full.row(inline_btn_film_9, inline_btn_film_10, inline_btn_film_11, inline_btn_film_12)
inline_btn_book_1 = InlineKeyboardButton('1', callback_data='book1')
inline_btn_book_2 = InlineKeyboardButton('2', callback_data='book2')
inline_btn_book_3 = InlineKeyboardButton('3', callback_data='book3')
inline_btn_book_4 = InlineKeyboardButton('4', callback_data='book4')
inline_btn_book_5 = InlineKeyboardButton('5', callback_data='book5')
inline_btn_book_6 = InlineKeyboardButton('6', callback_data='book6')
inline_btn_book_7 = InlineKeyboardButton('7', callback_data='book7')
inline_btn_book_8 = InlineKeyboardButton('8', callback_data='book8')
inline_btn_book_9 = InlineKeyboardButton('9', callback_data='book9')
inline_btn_book_10 = InlineKeyboardButton('10', callback_data='book10')
inline_kb_book_full = InlineKeyboardMarkup(row_width=1).row(inline_btn_book_1, inline_btn_book_2, inline_btn_book_3,
                                                            inline_btn_book_4, inline_btn_book_5)
inline_kb_book_full.row(inline_btn_book_6, inline_btn_book_7, inline_btn_book_8, inline_btn_book_9, inline_btn_book_10)
inline_btn_music_1 = InlineKeyboardButton('1', callback_data='music1')
inline_btn_music_2 = InlineKeyboardButton('2', callback_data='music2')
inline_btn_music_3 = InlineKeyboardButton('3', callback_data='music3')
inline_btn_music_4 = InlineKeyboardButton('4', callback_data='music4')
inline_kb_music_full = InlineKeyboardMarkup(row_width=1).row(inline_btn_music_1, inline_btn_music_2, inline_btn_music_3,
                                                             inline_btn_music_4)

advice_btn_anime = KeyboardButton('Топ аниме')
advice_btn_book = KeyboardButton('Топ книг')
advice_btn_music = KeyboardButton('Музыка')
advice_btn_film = KeyboardButton('Топ фильмов')
advice_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(advice_btn_anime, advice_btn_book)
advice_kb.row(advice_btn_music, advice_btn_film)

wp_btn_anime = KeyboardButton('Аниме')
wp_btn_book = KeyboardButton('Игры')
wp_btn_music = KeyboardButton('Прочие')
wp_btn_film = KeyboardButton('Для телефона')
wp_btn_neuroart = KeyboardButton('Нейроарты')
wp_btn_neurophone = KeyboardButton('Нейро для телефона')
wp_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(wp_btn_anime, wp_btn_book, wp_btn_music)
wp_kb.row(wp_btn_film, wp_btn_neuroart, wp_btn_neurophone)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Привет' + emoji.emojize(":hand_with_fingers_splayed:") +
                        '\nЯ - НейрОлег - цифровая модель RL версии Олега.\n'
                        'Я обладаю лишь малой частью его знаний, опыта и кругозора и не способен полноценно заменить его.\n'
                        'Но если тебе интересно, я с радостью поделюсь с тобой тем, что у меня есть.\n'
                        'Чтобы узнать о моих возможностях, пиши ' + '/help' + '.')


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(r'/about_me - расскажу немного о себе, моем прошлом, текущих интересах и увлечениях.' + '\n'
                        r'/filosaf - поделюсь своими (и не очень) мыслями на различные абстрактные темы.' + '\n '
                        r'/good_advice - поделюсь своими предпочтениями в кино, музыке, литературе и аниме.' + '\n'
                        r'/auf - брошу цитату из своей коллекции, собранной мной из прочитанных книг.' + '\n'
                        r'/cringe - вкину рандомную пикчу из своих сохраненок.' + '\n'
                        r'/paste - вкину рандомную пасту из своих сохраненок.' + '\n'
                        r'/wallpaper - поделюсь картинкой на обои для компа или телефона из своей коллекции.' + '\n')


@dp.message_handler(commands=['about_me'])
async def process_about_command(message: types.Message):
    message_text = '1. Основная информация\n2. Коротко о моем прошлом\n3. Мои интересы'
    await bot.send_message(message.from_user.id, message_text, reply_markup=inline_kb_about_full)


@dp.callback_query_handler(text='about1')
async def process_callback_about1(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/about_me/facts.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='about2')
async def process_callback_about2(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/about_me/past.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text, reply_markup=inline_kb_past)


@dp.callback_query_handler(text='past')
async def process_callback_past(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/about_me/look_back.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='about3')
async def process_callback_about3(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/about_me/hobbies.txt',
              encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.message_handler(commands=['filosaf'])
async def process_filosaf_command(message: types.Message):
    filosof = random.choice(filo_files)
    with open(r'/home/LsVbadd07/filosaf' + '/{0}'.format(filosof), encoding='utf-8') as file:
        message_text = file.read()
        if len(message_text) > 4000:
            message_text_1 = message_text[:4000]
            a = message_text_1.rfind('.')
            message_text_1 = message_text_1[:a + 1]
            message_text_2 = message_text[a + 1:]
            await bot.send_message(message.from_user.id, message_text_1)
            await bot.send_message(message.from_user.id, message_text_2, reply_markup=inline_kb_more)
        else:
            await bot.send_message(message.from_user.id, message_text, reply_markup=inline_kb_more)


@dp.callback_query_handler(text='more')
async def process_callback_filosaf(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    cursor.execute("SELECT file_id FROM BotContent WHERE Command='filosaf'")
    book_list = cursor.fetchall()
    kppr_1 = book_list[0]
    kppr_1 = kppr_1[0]
    kppr_2 = book_list[1]
    kppr_2 = kppr_2[0]
    await bot.send_document(call.from_user.id, kppr_1)
    await bot.send_document(call.from_user.id, kppr_2)


@dp.callback_query_handler(text='anime1')
async def process_callback_anime_1(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/anime/1.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='anime2')
async def process_callback_anime_2(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/anime/2.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='anime3')
async def process_callback_anime_3(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/anime/3.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='anime4')
async def process_callback_anime_4(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/anime/4.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='anime5')
async def process_callback_anime_5(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/anime/5.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='anime6')
async def process_callback_anime_6(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/anime/6.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='anime7')
async def process_callback_anime_7(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/anime/7.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='anime8')
async def process_callback_anime_8(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/anime/8.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='anime9')
async def process_callback_anime_9(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/anime/9.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='anime10')
async def process_callback_anime_10(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/anime/10.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='anime11')
async def process_callback_anime_11(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/anime/11.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='anime12')
async def process_callback_anime_12(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/anime/12.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='book1')
async def process_callback_book_1(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/books/1.txt', encoding='utf-8') as file:
        message_text = file.read()
    cursor.execute("SELECT file_id FROM BotContent WHERE id='3'")
    book = cursor.fetchone()
    book = book[0]
    await bot.send_message(call.from_user.id, message_text)
    await bot.send_document(call.from_user.id, book)


@dp.callback_query_handler(text='book2')
async def process_callback_book_2(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/books/2.txt', encoding='utf-8') as file:
        message_text = file.read()
    cursor.execute("SELECT file_id FROM BotContent WHERE id='4'")
    book = cursor.fetchone()
    book = book[0]
    await bot.send_message(call.from_user.id, message_text)
    await bot.send_document(call.from_user.id, book)


@dp.callback_query_handler(text='book3')
async def process_callback_book_3(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/books/3.txt', encoding='utf-8') as file:
        message_text = file.read()
    cursor.execute("SELECT file_id FROM BotContent WHERE id='5'")
    book = cursor.fetchone()
    book = book[0]
    await bot.send_message(call.from_user.id, message_text)
    await bot.send_document(call.from_user.id, book)


@dp.callback_query_handler(text='book4')
async def process_callback_book_4(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/books/4.txt', encoding='utf-8') as file:
        message_text = file.read()
    cursor.execute("SELECT file_id FROM BotContent WHERE id='6'")
    book = cursor.fetchone()
    book = book[0]
    await bot.send_message(call.from_user.id, message_text)
    await bot.send_document(call.from_user.id, book)


@dp.callback_query_handler(text='book5')
async def process_callback_book_5(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/books/5.txt', encoding='utf-8') as file:
        message_text = file.read()
    cursor.execute("SELECT file_id FROM BotContent WHERE id='7'")
    book = cursor.fetchone()
    book = book[0]
    await bot.send_message(call.from_user.id, message_text)
    await bot.send_document(call.from_user.id, book)


@dp.callback_query_handler(text='book6')
async def process_callback_book_6(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/books/6.txt', encoding='utf-8') as file:
        message_text = file.read()
    cursor.execute("SELECT file_id FROM BotContent WHERE id='8'")
    book = cursor.fetchone()
    book = book[0]
    await bot.send_message(call.from_user.id, message_text)
    await bot.send_document(call.from_user.id, book)


@dp.callback_query_handler(text='book7')
async def process_callback_book_7(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/books/7.txt', encoding='utf-8') as file:
        message_text = file.read()
    cursor.execute("SELECT file_id FROM BotContent WHERE id='9'")
    book = cursor.fetchone()
    book = book[0]
    await bot.send_message(call.from_user.id, message_text)
    await bot.send_document(call.from_user.id, book)


@dp.callback_query_handler(text='book8')
async def process_callback_book_8(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/books/8.txt', encoding='utf-8') as file:
        message_text = file.read()
    cursor.execute("SELECT file_id FROM BotContent WHERE id='10'")
    book = cursor.fetchone()
    book = book[0]
    await bot.send_message(call.from_user.id, message_text)
    await bot.send_document(call.from_user.id, book)


@dp.callback_query_handler(text='book9')
async def process_callback_book_9(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/books/9.txt', encoding='utf-8') as file:
        message_text = file.read()
    cursor.execute("SELECT file_id FROM BotContent WHERE id='11'")
    book = cursor.fetchone()
    book = book[0]
    await bot.send_message(call.from_user.id, message_text)
    await bot.send_document(call.from_user.id, book)


@dp.callback_query_handler(text='book10')
async def process_callback_book_10(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/books/10.txt', encoding='utf-8') as file:
        message_text = file.read()
    cursor.execute("SELECT file_id FROM BotContent WHERE id='12'")
    book = cursor.fetchone()
    book = book[0]
    await bot.send_message(call.from_user.id, message_text)
    await bot.send_document(call.from_user.id, book)


@dp.callback_query_handler(text='music1')
async def process_callback_music_1(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/music/instrumental.txt', encoding='utf-8') as file:
        message_text = file.read()
    instr_list = music_list[12:18]
    track_list = []
    for i in range(len(instr_list)):
        track = instr_list[i]
        track = track[0]
        track_list.append(track)
    await bot.send_message(call.from_user.id, message_text)
    await bot.send_audio(call.from_user.id, track_list[0])
    await bot.send_audio(call.from_user.id, track_list[1])
    await bot.send_audio(call.from_user.id, track_list[2])
    await bot.send_audio(call.from_user.id, track_list[3])
    await bot.send_audio(call.from_user.id, track_list[4])
    await bot.send_audio(call.from_user.id, track_list[5])


@dp.callback_query_handler(text='music2')
async def process_callback_music_2(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/music/rock.txt', encoding='utf-8') as file:
        message_text = file.read()
    instr_list = music_list[0:6]
    track_list = []
    for i in range(len(instr_list)):
        track = instr_list[i]
        track = track[0]
        track_list.append(track)
    await bot.send_message(call.from_user.id, message_text)
    await bot.send_audio(call.from_user.id, track_list[0])
    await bot.send_audio(call.from_user.id, track_list[1])
    await bot.send_audio(call.from_user.id, track_list[2])
    await bot.send_audio(call.from_user.id, track_list[3])
    await bot.send_audio(call.from_user.id, track_list[4])
    await bot.send_audio(call.from_user.id, track_list[5])


@dp.callback_query_handler(text='music3')
async def process_callback_music_3(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/music/rap.txt', encoding='utf-8') as file:
        message_text = file.read()
    instr_list = music_list[6:12]
    track_list = []
    for i in range(len(instr_list)):
        track = instr_list[i]
        track = track[0]
        track_list.append(track)
    await bot.send_message(call.from_user.id, message_text)
    await bot.send_audio(call.from_user.id, track_list[0])
    await bot.send_audio(call.from_user.id, track_list[1])
    await bot.send_audio(call.from_user.id, track_list[2])
    await bot.send_audio(call.from_user.id, track_list[3])
    await bot.send_audio(call.from_user.id, track_list[4])
    await bot.send_audio(call.from_user.id, track_list[5])


@dp.callback_query_handler(text='music4')
async def process_callback_music_4(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/music/maidcore.txt', encoding='utf-8') as file:
        message_text = file.read()
    instr_list = music_list[18:26]
    track_list = []
    for i in range(len(instr_list)):
        track = instr_list[i]
        track = track[0]
        track_list.append(track)
    await bot.send_message(call.from_user.id, message_text)
    await bot.send_audio(call.from_user.id, track_list[0])
    await bot.send_audio(call.from_user.id, track_list[1])
    await bot.send_audio(call.from_user.id, track_list[2])
    await bot.send_audio(call.from_user.id, track_list[3])
    await bot.send_audio(call.from_user.id, track_list[4])
    await bot.send_audio(call.from_user.id, track_list[5])
    await bot.send_audio(call.from_user.id, track_list[6])
    await bot.send_audio(call.from_user.id, track_list[7])


@dp.callback_query_handler(text='film1')
async def process_callback_film_1(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/films/1.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='film2')
async def process_callback_film_2(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/films/2.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='film3')
async def process_callback_film_3(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/films/3.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='film4')
async def process_callback_film_4(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/films/4.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='film5')
async def process_callback_film_5(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/films/5.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='film6')
async def process_callback_film_6(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/films/6.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='film7')
async def process_callback_film_7(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/films/7.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='film8')
async def process_callback_film_8(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/films/8.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='film9')
async def process_callback_film_9(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/films/9.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='film10')
async def process_callback_film_10(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/films/10.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='film11')
async def process_callback_film_11(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/films/11.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.callback_query_handler(text='film12')
async def process_callback_film_12(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    with open(r'/home/LsVbadd07/good_advice/films/12.txt', encoding='utf-8') as file:
        message_text = file.read()
    await bot.send_message(call.from_user.id, message_text)


@dp.message_handler(commands=['good_advice'])
async def process_advice_command(message: types.Message):
    message_text = 'Выбери раздел'
    await bot.send_message(message.from_user.id, message_text, reply_markup=advice_kb)


@dp.message_handler(commands=['auf'])
async def process_auf_command(message: types.Message):
    cursor.execute("SELECT file_id FROM BotContent WHERE Command='auf'")
    auf_list_1 = cursor.fetchall()
    cursor.execute("SELECT Content FROM BotContent WHERE Command='auf'")
    auf_list_2 = cursor.fetchall()
    quote_ind = random.randint(0, len(auf_list_1) - 1)
    quote = auf_list_1[quote_ind]
    author = auf_list_2[quote_ind]
    quote = quote[0]
    author = author[0]
    message_text = quote + '\n' + author
    await bot.send_message(message.from_user.id, message_text)


@dp.message_handler(commands=['cringe'])
async def process_cringe_command(message: types.Message):
    cursor.execute("SELECT file_id FROM BotContent WHERE Command='cringe'")
    cringe_list = cursor.fetchall()
    photo_id = random.choice(cringe_list)
    photo_id = photo_id[0]
    try:
        await bot.send_photo(message.from_user.id, photo_id)
    except:
        await bot.send_message(message.from_user.id, photo_id)


@dp.message_handler(commands=['paste'])
async def process_paste_command(message: types.Message):
    pasta = random.choice(pasta_files)
    with open(r'/home/LsVbadd07/paste/{0}'.format(pasta), encoding='utf-8') as file:
        message_text = file.read()
        if len(message_text) > 4000:
            message_text_1 = message_text[:4000]
            a = message_text_1.rfind('.')
            message_text_1 = message_text_1[:a + 1]
            message_text_2 = message_text[a + 1:]
            if len(message_text_2) > 4000:
                message_text_3 = message_text_2[:4000]
                a = message_text_3.rfind('.')
                message_text_3 = message_text_3[:a + 1]
                message_text_4 = message_text_2[a + 1:]
                await bot.send_message(message.from_user.id, message_text_1)
                await bot.send_message(message.from_user.id, message_text_3)
                await bot.send_message(message.from_user.id, message_text_4)
            else:
                await bot.send_message(message.from_user.id, message_text_1)
                await bot.send_message(message.from_user.id, message_text_2)
        else:
            await bot.send_message(message.from_user.id, message_text)


@dp.message_handler(commands=['wallpaper'])
async def process_wallpaper_command(message: types.Message):
    message_text = 'Выбери тему'
    await bot.send_message(message.from_user.id, message_text, reply_markup=wp_kb)


@dp.message_handler(content_types=ContentType.TEXT)
async def handle_message(message: types.Message):
    if message.text == 'Топ аниме':
        with open(r'/home/LsVbadd07/good_advice/anime/a_top_list.txt', encoding='utf-8') as file:
            message_text = file.read()
            await bot.send_message(message.from_user.id, message_text, reply_markup=inline_kb_anime_full)
    elif message.text == 'Топ книг':
        with open(r'/home/LsVbadd07/good_advice/books/b_top_list.txt', encoding='utf-8') as file:
            message_text = file.read()
            await bot.send_message(message.from_user.id, message_text, reply_markup=inline_kb_book_full)
    elif message.text == 'Музыка':
        with open(r'/home/LsVbadd07/good_advice/music/m_list.txt', encoding='utf-8') as file:
            message_text = file.read()
            await bot.send_message(message.from_user.id, message_text, reply_markup=inline_kb_music_full)
    elif message.text == 'Топ фильмов':
        with open(r'/home/LsVbadd07/good_advice/films/f_top_list.txt', encoding='utf-8') as file:
            message_text = file.read()
            await bot.send_message(message.from_user.id, message_text, reply_markup=inline_kb_film_full)
    elif message.text == 'Аниме':
        cursor.execute("SELECT file_id FROM BotContent WHERE subcommand='anime'")
        awp_list = cursor.fetchall()
        awp_ind = random.randint(0, len(awp_list) - 1)
        awp = awp_list[awp_ind]
        awp = awp[0]
        await bot.send_document(message.from_user.id, awp)
    elif message.text == 'Игры':
        cursor.execute("SELECT file_id FROM BotContent WHERE subcommand='games'")
        gwp_list = cursor.fetchall()
        gwp_ind = random.randint(0, len(gwp_list) - 1)
        gwp = gwp_list[gwp_ind]
        gwp = gwp[0]
        await bot.send_document(message.from_user.id, gwp)
    elif message.text == 'Для телефона':
        cursor.execute("SELECT file_id FROM BotContent WHERE subcommand='phone'")
        pwp_list = cursor.fetchall()
        pwp_ind = random.randint(0, len(pwp_list) - 1)
        pwp = pwp_list[pwp_ind]
        pwp = pwp[0]
        await bot.send_document(message.from_user.id, pwp)
    elif message.text == 'Прочие':
        cursor.execute("SELECT file_id FROM BotContent WHERE subcommand='others'")
        owp_list = cursor.fetchall()
        owp_ind = random.randint(0, len(owp_list) - 1)
        owp = owp_list[owp_ind]
        owp = owp[0]
        await bot.send_document(message.from_user.id, owp)
    elif message.text == 'Нейроарты':
        cursor.execute("SELECT file_id FROM BotContent WHERE subcommand='neuroart'")
        nwp_list = cursor.fetchall()
        nwp_ind = random.randint(0, len(nwp_list) - 1)
        nwp = nwp_list[nwp_ind]
        nwp = nwp[0]
        await bot.send_document(message.from_user.id, nwp)
    elif message.text == 'Нейро для телефона':
        cursor.execute("SELECT file_id FROM BotContent WHERE subcommand='neurophone'")
        npwp_list = cursor.fetchall()
        npwp_ind = random.randint(0, len(npwp_list) - 1)
        npwp = npwp_list[npwp_ind]
        npwp = npwp[0]
        await bot.send_document(message.from_user.id, npwp)
    else:
        message_text = 'Я пока не умею понимать речь, только команды' + emoji.emojize(":disappointed_face:")
        await bot.send_message(message.from_user.id, message_text)


@dp.message_handler(content_types=ContentType.ANY)
async def handle_other_text(message):
    message_text = 'Я пока не умею понимать сообщения, только команды' + emoji.emojize(":disappointed_face:")
    await bot.send_message(message.from_user.id, message_text)


if __name__ == '__main__':
    executor.start_polling(dp)
