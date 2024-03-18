# Main program to run the Telegram Bot with username: burgerbot_boys_bot
# for IIUM Students.
# Author: Mohamed Syaheer Altaf
from telegram.ext import *
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
import api as key
import texts as t
import data_list as dt
from _sheets import sheets as sh
import pricing as p
 
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(t.text_greeting)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(t.text_help)

async def order_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    #dt.user_order = [] # Init to an empty list.
    user_id = update.effective_user.id
    try:
        orders[user_id].orders = [] # Clear order when invoked again.
        orders[user_id].orders.append(user_id)
        #await recurringCustomer(update,context)
        await update.message.reply_text("Enter your name. 🙋")
    except:
        # First time order.
        #userRow = db.getUserRow(user_id) # In the local database.
        orders[user_id] = dt.UserOrder(user_id)
        orders[user_id].orders.append(user_id)
        #db.addUserID(user_id)
        await update.message.reply_text("Enter your name. 🙋")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    text = str(update.message.text).lower()
    try:
        if (orders[user_id].orders != []):
            if (len(orders[user_id].orders) == 2):
                orders[user_id].orders.append(text) # Always update user order after each stage.
                #db.addUserNumber(text,db.getUserRow(user_id))
                await mahallah(update, context)
            elif (len(orders[user_id].orders) == 1):
                orders[user_id].orders.append(text) # Get name.
                #db.addUserName(text,db.getUserRow(user_id))
                await update.message.reply_text("Enter your phone number. ☎️")
            else:
                await update.message.reply_text("Wrong format. See /help.")  
        else:
            await update.message.reply_text("Wrong format. See /help.")
    except:
        await update.message.reply_text("Wrong format. See /help.")  

async def mahallah(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Define Mahallah as Buttons
    Faruq               = InlineKeyboardButton('Faruq', callback_data='Faruq')
    Siddiq              = InlineKeyboardButton('Siddiq', callback_data='Siddiq')
    Ali                 = InlineKeyboardButton('Ali', callback_data='Ali')
    Bilal               = InlineKeyboardButton('Bilal',callback_data='Bilal')
    Uthman              = InlineKeyboardButton('Uthman',callback_data='Uthman')
    Zubair              = InlineKeyboardButton('Zubair',callback_data='Zubair')
    Salahuddin          = InlineKeyboardButton('Salahuddin', callback_data='Salahuddin')
    Aminah              = InlineKeyboardButton('Aminah', callback_data='Aminah')
    Asiah               = InlineKeyboardButton('Asiah',callback_data='Asiah')
    Asma                = InlineKeyboardButton('Asma', callback_data='Asma')
    Hafsah              = InlineKeyboardButton('Hafsah', callback_data='Hafsah')
    Halimatus_Saadiah   = InlineKeyboardButton('Halimatus Saadiah', callback_data='Halimatus_Saadiah')
    Maryam              = InlineKeyboardButton('Maryam', callback_data='Maryam')
    Nusaibah            = InlineKeyboardButton('Nusaibah', callback_data='Nusaibah')
    Safiyyah            = InlineKeyboardButton('Safiyyah', callback_data='Safiyyah')
    Sumayyah            = InlineKeyboardButton('Sumayyah', callback_data='Sumayyah')
    Ruqayyah            = InlineKeyboardButton('Ruqayyah', callback_data='Ruqayyah')

    Mahallah = [[Faruq],[Siddiq],[Ali],[Bilal],[Uthman],[Zubair],[Salahuddin],
                [Aminah],[Asiah],[Asma],[Hafsah],[Halimatus_Saadiah],[Maryam],[Nusaibah],[Safiyyah],
                [Sumayyah],[Ruqayyah]]
    keyboard = InlineKeyboardMarkup(Mahallah)
    chat_id = update.message.chat.id
    # Create the markup
    await update._bot.send_message(chat_id=chat_id, text="Choose your mahallah. 🏘️", reply_markup=keyboard)

async def food(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ChickenWrap = InlineKeyboardButton('Chicken Wrap (RM 7.50)', callback_data='Chicken Wrap')
    AyamGunting = InlineKeyboardButton('Ayam Gunting (RM 6.50)', callback_data='Ayam Gunting')
    Sausage = InlineKeyboardButton('Jumbo Sausage (RM 5.50)', callback_data='Jumbo Sausage')
    Food_list = [[ChickenWrap],[AyamGunting],[Sausage]]
    keyboard = InlineKeyboardMarkup(Food_list)
    chat_id = update.callback_query.message.chat.id
    message_id = update.callback_query.message.message_id
    await update._bot.edit_message_text(chat_id=chat_id,message_id=message_id,text="Choose your order. 🥙")
    await update._bot.edit_message_reply_markup(chat_id=chat_id,message_id=message_id,reply_markup=keyboard)

async def quantity(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    qtt = []
    for i in range(5):
        qtt.append([InlineKeyboardButton(str(i+1),callback_data=str(i+1))])
    keyboard = InlineKeyboardMarkup(qtt)
    chat_id = update.callback_query.message.chat.id
    message_id = update.callback_query.message.message_id
    await update._bot.edit_message_text(chat_id=chat_id,message_id=message_id,text="Choose the quantity of your order:")
    await update._bot.edit_message_reply_markup(chat_id=chat_id,message_id=message_id,reply_markup=keyboard)

async def addMore(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    add_more = InlineKeyboardButton('Add More', callback_data='add more')
    no_add_more = InlineKeyboardButton('No', callback_data='!add more')
    keyboard = InlineKeyboardMarkup([[add_more],[no_add_more]])
    chat_id = update.callback_query.message.chat.id
    message_id = update.callback_query.message.message_id
    await update._bot.edit_message_text(chat_id=chat_id,message_id=message_id,text="Do you want to add more? 🤔")
    await update._bot.edit_message_reply_markup(chat_id=chat_id,message_id=message_id,reply_markup=keyboard)

async def order_summary(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update._effective_user.id
    current_order = orders[user_id].orders
    order_summary = f'''
    Order Summary for #{current_order[0]}:\n
    1) Name         :  {current_order[1]} 
    2) Phone no ☎️  :   {current_order[2]}
    3) Mahallah 🏘️  :   {current_order[3]}
    4) Order 🥙      :  {current_order[4]}

Proceed?
    '''   
    yes = InlineKeyboardButton('Continue',callback_data='Continue')
    no = InlineKeyboardButton('No',callback_data='No continue')
    choices = [[yes],[no]]
    keyboard = InlineKeyboardMarkup(choices)
    chat_id = update.callback_query.message.chat.id
    message_id = update.callback_query.message.message_id
    await update._bot.edit_message_text(chat_id=chat_id,message_id=message_id,text=order_summary)
    await update._bot.edit_message_reply_markup(chat_id=chat_id,message_id=message_id,reply_markup=keyboard)

async def confirmation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Get price first
    user_id = update._effective_user.id
    current_order = orders[user_id].orders
    price = p.pricing(current_order[4])
    orders[user_id].orders.append(price)
    # Reply markup
    yes = InlineKeyboardButton('Confirm Order',callback_data='yes')
    no = InlineKeyboardButton('No',callback_data='no')
    choices = [[yes],[no]]
    keyboard = InlineKeyboardMarkup(choices)
    texts = f" Nice!\nThe total price is RM {price}."
    chat_id = update.callback_query.message.chat.id
    message_id = update.callback_query.message.message_id
    await update._bot.edit_message_text(chat_id=chat_id,message_id=message_id,text=texts)
    await update._bot.edit_message_reply_markup(chat_id=chat_id,message_id=message_id,reply_markup=keyboard)

async def update(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update._effective_user.id
    await update.callback_query.edit_message_text("Your order has been recorded. ✅\nThanks for ordering.")
    sh.sheet(values=orders[user_id].orders)
    orders[user_id].orders = []

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update._effective_user.id
    await update.callback_query.edit_message_text("Your order has been cancelled. ❌\nTo re-order, enter /order.")
    orders[user_id].orders = []

async def handle_inline_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    query = update.callback_query
    data = query.data
    if (data in ['Continue','No continue','yes','no','add more','!add more']):
        await func_dict[data](update,context)
    elif (data in dt.food):
        try:
            temp = orders[user_id].orders[4]+", "+data
            orders[user_id].orders[4] = temp
        except:
            orders[user_id].orders.append(data)
        await func_dict[data](update,context)
    elif (data in dt.qtt):
        temp = orders[user_id].orders[4] +" x"+data
        orders[user_id].orders[4] = temp
        await func_dict[data](update,context)
    else:
        orders[user_id].orders.append(data)
        await func_dict[data](update,context)

async def handle_error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f"Update {update} caused error {context.error}")

def main():
    app = ApplicationBuilder().token(key.API_KEY).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("order", order_command))
    app.add_handler(MessageHandler(filters.TEXT,handle_message))
    app.add_handler(CallbackQueryHandler(handle_inline_keyboard))
    app.add_error_handler(handle_error)
    app.run_polling()

# Start Bot
print("\nStarting Telegram Bot...\n")
orders = {} # Combining dictionary with objects of a class to make each order unique to customer.
# Table driven method for decision making (instead of if-else statements).
func_dict = {
    dt.mahallah_list[0]: food,
    dt.mahallah_list[1]: food,
    dt.mahallah_list[2]: food,
    dt.mahallah_list[3]: food,
    dt.mahallah_list[4]: food,
    dt.mahallah_list[5]: food,
    dt.mahallah_list[6]: food,
    dt.mahallah_list[7]: food,
    dt.mahallah_list[8]: food,
    dt.mahallah_list[9]: food,
    dt.mahallah_list[10]: food,
    dt.mahallah_list[11]: food,
    dt.mahallah_list[12]: food,
    dt.mahallah_list[13]: food,
    dt.mahallah_list[14]: food,
    dt.mahallah_list[15]: food,
    dt.mahallah_list[16]: food,
    dt.food[0]: quantity,
    dt.food[1]: quantity,
    dt.food[2]: quantity,
    dt.qtt[0]: addMore,
    dt.qtt[1]: addMore,
    dt.qtt[2]: addMore,
    dt.qtt[3]: addMore,
    dt.qtt[4]: addMore,
    'add more': food,
    '!add more': order_summary,
    'Continue': confirmation,
    'No continue': cancel,
    'yes': update,
    'no': cancel
}
main()