@bot.message_handler(commands=['admin', 'admins'])
def admins(message):
    try:
	    lista_admin = []
	    numero_membros = bot.get_chat_members_count(message.chat.id)
	    admins = bot.get_chat_administrators(message.chat.id)
	    bot.send_message(message.chat.id,'O grupo tem ' + str(numero_membros) + ' membros e ' + str(len(admins)) + ' administradores:')
	    for admin in admins:
	        
	        lista_admin.append(admin.user.username)
	    lista_admin_txt = '\n'.join(lista_admin)
	    bot.send_message(message.chat.id, ""+str(lista_admin_txt) + " - **" + admin.user.last_name + "** \n" , parse_mode="Markdown")
    except:
    	bot.send_message(message.chat.id , "tem administrador sem o nome usuário , por favor bota o nome do usuário")
