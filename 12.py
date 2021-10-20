A = 0
print ( 'Как вас зовут?' )
name = input ( ' ' )
print ( 'Здравствуйте,', name,'. Сколько вам лет?')
age = int ( input ( ) )
print ( 'Ваш любимый цвет? (1-красный, 2-зеленый, 3-синий)' )
col = int ( input ( ) )
print ( 'Ваша любимая музыка? (1-классика, 2-поп-музыка, 3-рок)' )
music = int ( input ( ) )
print ( 'Ваше любимое время года? (1-осень, 2-зима, 3-весна, 4-лето)' )
year = int ( input ( ) )
print ( 'Какая игра вам больше нравится? (1-Rust, 2-LoL, 3-Dota 2, 4-CS:GO)' )
game = int ( input ( ) )
print ( 'Какой предмет вам болше нравится? (1-математика, 2-русский язык, 3-английский язык, 4-информатика)' )
school = int ( input ( ) )
print ( 'Какой телефон вам больше нравится? (1-samsung, 2-iphone, 3-xiaomi, 4-nokia)' )
phone = int ( input ( ) )
print ( 'Какой сок вы любите? (1-яблочный, 2-виноградный, 3-персиковый, 4-вишневый)' )
juice = int ( input ( ) )
print ( 'Любите ли вы играть в доту? (1-да, 2-нет)' )
dota = int ( input ( ) )
        
if col == 2:
        A += 1
if music == 3:
        A +=1
if year == 4:
        A +=1
if game == 3:
        A +=1
if school == 4:
        A +=1
if phone == 1:
        A +=1
if juice == 4:
        A +=1
if dota == 1:
        A +=1
if A == 8:
        print ( 'Мы с вами подружимся!' )
elif A < 5:
        print ( 'Мы с вами может быть подружимся!' )
else:
        print ( "Мы с вами не подружимся" )
