# import pytz
# from datetime import datetime, time
# from telegram import Update
# from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# # Set the timezone to Indian Standard Time
# IST = pytz.timezone('Asia/Kolkata')
# user_data = {}

# # Start command handler
# async def start(update: Update, context: CallbackContext) -> None:
#     await update.message.reply_text("Welcome to the Early Risers group! Please check in every day!")

# # Welcome new members
# async def welcome(update: Update, context: CallbackContext) -> None:
#     for new_member in update.message.new_chat_members:
#         await context.bot.send_message(chat_id=update.effective_chat.id,
#                                        text=f"Welcome {new_member.full_name}! Please text 'Hey, I am alive' between 6 AM and 7:11 AM IST!")

# # Track wake-up messages
# async def track_wakeup(update: Update, context: CallbackContext) -> None:
#     user_id = update.effective_user.id
#     current_time = datetime.now(IST).time()
#     today_date = datetime.now().date().isoformat()  # Get today's date in YYYY-MM-DD format

#     # Initialize today's record if it doesn't exist
#     if today_date not in user_status:
#         user_status[today_date] = {}

#     # Check if the user has already been recorded today
#     if user_id in user_status[today_date]:
#         # If already recorded, notify the user that their record has been already processed
#         await context.bot.send_message(chat_id=update.effective_chat.id,
#                                        text=f"You have already been recorded for today.")
#         return

#     # Record success if within the time window
#     if time(6, 0) <= current_time <= time(7, 11):
#         record_success(user_id)  # Your function to handle success
#         user_status[today_date][user_id] = 'success'
#         await context.bot.send_message(chat_id=update.effective_chat.id,
#                                        text=f"Great job, {update.effective_user.first_name}! You're awake!")
#     else:
#         # Record failure if outside the time window
#         record_failure(user_id)  # Your function to handle failure
#         user_status[today_date][user_id] = 'failure'
#         await context.bot.send_message(chat_id=update.effective_chat.id,
#                                        text=f"Sorry, {update.effective_user.first_name}. You missed the mark.")

# async def assign_failures(context: CallbackContext) -> None:
#     # This function should be scheduled to run after 7:11 AM every day
#     today_date = datetime.now().date().isoformat()

#     # Check if today's record exists
#     if today_date in user_status:
#         for user_id, status in user_status[today_date].items():
#             if status != 'success':
#                 record_failure(user_id)  # Ensure failures are recorded
#                 # Optionally notify the user
#                 await context.bot.send_message(chat_id=user_id,
#                                                text=f"Today, you missed the mark. Failure recorded.")

#         # Optionally clear today's data after processing
#         user_status[today_date] = {}
# # Check status command
# async def check_status(update: Update, context: CallbackContext) -> None:
#     user_id = update.effective_user.id
#     if user_id in user_data:
#         status = user_data[user_id]
#         await update.message.reply_text(
#             f"Your Status:\n"
#             f"Successes: {status['success_count']}\n"
#             f"Failures: {status['failure_count']}\n"
#             f"Pardons: {status['pardons']}\n"
#             f"Current Streak: {status['streak']} days"
#         )
#     else:
#         await update.message.reply_text("You haven't checked in yet!")

# # Record success
# def record_success(user_id):
#     if user_id not in user_data:
#         user_data[user_id] = {'success_count': 0, 'failure_count': 0, 'pardons': 3, 'last_success': None, 'streak': 0}
   
#     user_data[user_id]['success_count'] += 1
#     user_data[user_id]['last_success'] = datetime.now(IST).date()
#     check_streak(user_id)

# # Record failure
# def record_failure(user_id):
#     if user_id not in user_data:
#         user_data[user_id] = {'success_count': 0, 'failure_count': 0, 'pardons': 3, 'last_success': None, 'streak': 0}
   
#     user_data[user_id]['failure_count'] += 1
#     user_data[user_id]['pardons'] -= 1
#     check_kick(user_id)

# # Check streaks
# def check_streak(user_id):
#     today = datetime.now(IST).date()
#     last_success = user_data[user_id]['last_success']

#     if last_success is not None:
#         days_diff = (today - last_success).days

#         # Check if today is Sunday
#         if today.weekday() == 6:  # 6 represents Sunday
#             return  # Do nothing if it's Sunday

#         if days_diff == 1:  # Continuation of the streak
#             user_data[user_id]['streak'] += 1
#         elif days_diff > 1:  # Streak broken
#             user_data[user_id]['streak'] = 1  # Reset streak, but don’t count today

#         # Grant an extra pardon for every 15-day streak
#         if user_data[user_id]['streak'] % 15 == 0 and user_data[user_id]['pardons'] < 3:
#             user_data[user_id]['pardons'] += 1
#             user_data[user_id]['failure_count'] -= 1

# # Check for kick
# def check_kick(user_id):
#     if user_data[user_id]['failure_count'] >= 3:
#         # Here, you would kick the member from the group
#         context.bot.kick_chat_member(chat_id=update.effective_chat.id, user_id=user_id)
#         context.bot.send_message(chat_id=update.effective_chat.id,
#                                  text=f"{update.effective_user.first_name} has been kicked for failing to wake up 3 times.")

# # Main function to run the bot
# def main():
#     application = Application.builder().token("7314515623:AAH8WEZl5osGq1QIyYCyMaSbm3cxKlo2ohY").build()
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
#     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, track_wakeup))
#     application.add_handler(CommandHandler("status", check_status))  # Add status command

#     application.run_polling()


# if __name__ == '__main__':
#     main()

import pytz
from datetime import datetime, time
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, JobQueue
import logging

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Set the timezone to Indian Standard Time
IST = pytz.timezone('Asia/Kolkata')
user_data = {}

# Start command handler
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Welcome to the Early Risers group! Please check in every day!")

# Welcome new members
async def welcome(update: Update, context: CallbackContext) -> None:
    for new_member in update.message.new_chat_members:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=f"Welcome {new_member.full_name}! Please text 'Hey, I am alive' between 6 AM and 7:11 AM IST!")

# Track wake-up messages
async def track_wakeup(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    current_time = datetime.now(IST).time()
    today_date = datetime.now(IST).date()

    if user_id not in user_data:
        user_data[user_id] = {'success_count': 0, 'failure_count': 0, 'pardons': 3, 'last_success': None, 'streak': 0, 'date_recorded': None}

    # Check if the user has already been recorded today
    if user_data[user_id]['date_recorded'] == today_date:
        await update.message.reply_text("You have already checked in today!")
        return

    # Record success if within the time window
    if time(6, 0) <= current_time <= time(7, 11):
        record_success(user_id, today_date)
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=f"Great job, {update.effective_user.first_name}! You're awake!")
    else:
        record_failure(user_id, today_date)
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=f"Sorry, {update.effective_user.first_name}. You missed the mark.")

# Check status command
async def check_status(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if user_id in user_data:
        status = user_data[user_id]
        await update.message.reply_text(
            f"Your Status:\n"
            f"Successes: {status['success_count']}\n"
            f"Failures: {status['failure_count']}\n"
            f"Pardons: {status['pardons']}\n"
            f"Current Streak: {status['streak']} days"
        )
    else:
        await update.message.reply_text("You haven't checked in yet!")

# Record success
def record_success(user_id, today_date):
    user_data[user_id]['success_count'] += 1
    user_data[user_id]['last_success'] = today_date
    user_data[user_id]['date_recorded'] = today_date
    check_streak(user_id)

# Record failure
def record_failure(user_id, today_date):
    user_data[user_id]['failure_count'] += 1
    user_data[user_id]['pardons'] -= 1
    user_data[user_id]['date_recorded'] = today_date
    check_kick(user_id)

# Check streaks
def check_streak(user_id):
    today = datetime.now(IST).date()
    last_success = user_data[user_id]['last_success']

    if last_success is not None:
        days_diff = (today - last_success).days

        # Check if today is Sunday
        if today.weekday() == 6:  # 6 represents Sunday
            return  # Do nothing if it's Sunday

        if days_diff == 1:  # Continuation of the streak
            user_data[user_id]['streak'] += 1
        elif days_diff > 1:  # Streak broken
            user_data[user_id]['streak'] = 1  # Reset streak, but don’t count today

        # Grant an extra pardon for every 15-day streak
        if user_data[user_id]['streak'] % 15 == 0 and user_data[user_id]['pardons'] < 3:
            user_data[user_id]['pardons'] += 1
            user_data[user_id]['failure_count'] -= 1

# Check for kick
def check_kick(user_id):
    if user_data[user_id]['failure_count'] >= 3:
        # Here, you would kick the member from the group
        # This function needs to be updated to access `context`
        logging.info(f"Kicking user {user_id} due to 3 failures.")
        context.bot.kick_chat_member(chat_id=update.effective_chat.id, user_id=user_id)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"{update.effective_user.first_name} has been kicked for failing to wake up 3 times.")

# Assign failure to all non-successful users after 7:11 AM
async def assign_failures(context: CallbackContext) -> None:
    today_date = datetime.now(IST).date()
    for user_id, data in user_data.items():
        if data['date_recorded'] != today_date and (datetime.now(IST).time() > time(7, 11)):
            record_failure(user_id, today_date)
            await context.bot.send_message(chat_id=user_id,
                                           text=f"Today, you missed the mark. Failure recorded.")

# Main function to run the bot
def main():
    application = Application.builder().token("7154018609:AAEvOzKVRg6AeOG04HACB-xC19jvJ6N9KEA").build()
    job_queue = application.job_queue

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, track_wakeup))
    application.add_handler(CommandHandler("status", check_status))  # Add status command

    # Schedule the failure assignment job
    job_queue.run_daily(assign_failures, time(7, 12))

    application.run_polling()

if __name__ == '__main__':
    main()
