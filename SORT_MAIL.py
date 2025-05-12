mail_box = {}  # изначально наш ящик пустой и в нем нет писем

# напиши здесь функцию, которая добавляет письма в mail_box
def mail_checker(mail_to, mail_from, mail_text):
	# Если получателя ещё нет в mail_box, создаём для него пустой список
	if mail_to not in mail_box:
		mail_box[mail_to] = []

	# Добавляем письмо в список получателя
	mail_box[mail_to].append({mail_from: mail_text})

	return mail_box
# полученные письма
mail_checker(mail_to='john_connor@yandex.ru', mail_from='terminator@yandex.ru', mail_text='Привет, я вернулся!')

mail_checker(mail_to='john_connor@yandex.ru', mail_from='sarah_connor@yandex.ru', mail_text='Сынок, надень шапку')

mail_checker(mail_to='luke_skywalker@yandex.ru', mail_from='darth_vader@yandex.ru', mail_text='Правая рука чешется, не знаю, что и делать')

mail_checker(mail_to='luke_skywalker@yandex.ru', mail_from='darth_vader@yandex.ru', mail_text='Что бы сказал на это твой отец?')

print(mail_box)