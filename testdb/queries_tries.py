walmart = Supermarket(super_name='Walmart', super_mail='wmatwalmart.com',latitude=16.34285,longitude=72.536986,super_photo = 'abc.flickr.com',role = 'mkt')
walmart.save()

admin = Boss(admin_name="boss", mail="boss@boss.com",admin_photo='cde.flickr.com', role='adm')
admin.save()

usuario1 = User(username='usuario1', user_mail='usuario1@gmail.com',user_photo = 'usr.flickr.com',role = 'usr')
usuario1.save()

walmart = Supermarket(super_name = 'Walmart')
soriana = Supermarket(super_name = 'Soriana')
superama = Supermarket(super_name = 'Superama')
comercial = Supermarket(super_name = 'Comercial Mexicana')
heb = Supermarket(super_name = 'HEB')

walmart.save()
soriana.save()
superama.save()
comercial.save()
heb.save()

huevos = Products(product_name='Huevos',product_unit='kg.',category=1)
huevos.save()
pan = Products(product_name='Pan',product_unit='kg.',category=1)
pan.save()
lechedes = Products(product_name='Leche deslactosada', product_unit='pkg', category=1)
lechedes.save()

carne = Products(product_name='Carne',product_unit='kg.',category=2)
carne.save()
tortilla = Products(product_name='Tortilla',product_unit='kg.',category=2)
tortilla.save()
refresco = Products(product_name='Refresco',product_unit='lt.',category=2)
refresco.save()

yogurth = Products(product_name='Yogurth',product_unit='lt.',category=3)
yogurth.save()
cereal = Products(product_name='Cereal',product_unit='kg.',category=3)
cereal.save()
agua = Products(product_name='Agua',product_unit='lt.',category=3)
agua.save()

tequila = Products(product_name='Tequila',product_unit='lt.',category=4)
tequila.save()
vasos = Products(product_name='Vasos',product_unit='pck',category=4)
vasos.save()
ping_pong = Products(product_name='Pong ball',product_unit='pck',category=4)
ping_pong.save()

vino = Products(product_name='Vino',product_unit='lt.',category=5)
vino.save()
queso = Products(product_name='Queso',product_unit='kg.',category=5)
queso.save()
copas = Products(product_name='Copas',product_unit='pck.',category=5)
copas.save()

cerveza = Products(product_name='Cerveza',product_unit='lt.',category=6)
cerveza.save()
cigarros = Products(product_name='Cigarros',product_unit='pkg.',category=6)
cigarros.save()
papas = Products(product_name='Papas',product_unit='pkg.',category=6)
papas.save()

jabon_polvo = Products(product_name='Jabon polvo',product_unit='kg.',category=7)
jabon_polvo.save()
suero = Products(product_name='Suero',product_unit='pkg.',category=7)
suero.save()
alitas = Products(product_name='Alitas',product_unit='pkg.',category=7)
alitas.save()

shampoo = Products(product_name='Shampoo',product_unit='pkg.',category=8)
shampoo.save()
jabon_barra = Products(product_name='Jabon barra',product_unit='pkg.',category=8)
jabon_barra.save()
pd = Products(product_name='Pasta dental',product_unit='pkg.',category=8)
pd.save()

lechen = Products(product_name='Leche entera',product_unit='pkg.',category=9)
lechen.save()
queson = Products(product_name='Queso',product_unit='kg.',category=9)
queson.save()
crema = Products(product_name='Crema',product_unit='pkg.',category=9)
crema.save()

fit1 = Products(product_name='Vegetales',product_unit='pkg.',category=10)
fit1.save()
fit2 = Products(product_name='Pan integral',product_unit='pkg.',category=10)
fit2.save()
fit3 = Products(product_name='Yogurth griego',product_unit='pkg.',category=10)
fit3.save()

p11 = Prices(price=39,products_id = huevos,super_id=walmart)
p11.save()

p12 = Prices(price=64,products_id = huevos,super_id=soriana)
p12.save()
p13 = Prices(price=49,products_id = huevos,super_id=superama)
p13.save()
p14 = Prices(price=33,products_id = huevos,super_id=comercial)
p14.save()
p15 = Prices(price=36,products_id = huevos,super_id=heb)
p15.save()


p21 = Prices(price=29,products_id = lechedes,super_id=walmart)
p21.save()
p22 = Prices(price=24,products_id = lechedes,super_id=soriana)
p22.save()
p23 = Prices(price=29,products_id = lechedes,super_id=superama)
p23.save()
p24 = Prices(price=35,products_id = lechedes,super_id=comercial)
p24.save()
p25 = Prices(price=34,products_id = lechedes,super_id=heb)
p25.save()


p31 = Prices(price=19,products_id = pan,super_id=walmart)
p31.save()
p32 = Prices(price=14,products_id = pan,super_id=soriana)
p32.save()
p33 = Prices(price=19,products_id = pan,super_id=superama)
p33.save()
p34 = Prices(price=25,products_id = pan,super_id=comercial)
p34.save()
p35 = Prices(price=24,products_id = pan,super_id=heb)
p35.save()

p41 = Prices(price=155,products_id = carne,super_id=walmart)
p41.save()
p42 = Prices(price=133,products_id = carne,super_id=soriana)
p42.save()
p43 = Prices(price=149,products_id = carne,super_id=superama)
p43.save()
p44 = Prices(price=245,products_id = carne,super_id=comercial)
p44.save()
p45 = Prices(price=204,products_id = carne,super_id=heb)
p45.save()

p51 = Prices(price=19,products_id = tortilla,super_id=walmart)
p51.save()
p52 = Prices(price=14,products_id = tortilla,super_id=soriana)
p52.save()
p53 = Prices(price=28,products_id = tortilla,super_id=superama)
p53.save()
p54 = Prices(price=12,products_id = tortilla,super_id=comercial)
p54.save()
p55 = Prices(price=26,products_id = tortilla,super_id=heb)
p55.save()

p61 = Prices(price=39,products_id = refresco,super_id=walmart)
p61.save()
p62 = Prices(price=24,products_id = refresco,super_id=soriana)
p62.save()
p63 = Prices(price=39,products_id = refresco,super_id=superama)
p63.save()
p64 = Prices(price=15,products_id = refresco,super_id=comercial)
p64.save()
p65 = Prices(price=22,products_id = refresco,super_id=heb)
p65.save()

p71 = Prices(price=29,products_id = yogurth,super_id=walmart)
p71.save()
p72 = Prices(price=24,products_id = yogurth,super_id=soriana)
p72.save()
p73 = Prices(price=35,products_id = yogurth,super_id=superama)
p73.save()
p74 = Prices(price=27,products_id = yogurth,super_id=comercial)
p74.save()
p75 = Prices(price=33,products_id = yogurth,super_id=heb)
p75.save()

p81 = Prices(price=79,products_id = cereal,super_id=walmart)
p81.save()
p82 = Prices(price=84,products_id = cereal,super_id=soriana)
p82.save()
p83 = Prices(price=79,products_id = cereal,super_id=superama)
p83.save()
p84 = Prices(price=85,products_id = cereal,super_id=comercial)
p84.save()
p85 = Prices(price=74,products_id = cereal,super_id=heb)
p85.save()

p91 = Prices(price=9,products_id = agua,super_id=walmart)
p91.save()
p92 = Prices(price=14,products_id = agua,super_id=soriana)
p92.save()
p93 = Prices(price=9,products_id = agua,super_id=superama)
p93.save()
p94 = Prices(price=15,products_id = agua,super_id=comercial)
p94.save()
p95 = Prices(price=4,products_id = agua,super_id=heb)
p95.save()

p101 = Prices(price=229,products_id = tequila,super_id=walmart)
p101.save()
p102 = Prices(price=284,products_id = tequila,super_id=soriana)
p102.save()
p103 = Prices(price=279,products_id = tequila,super_id=superama)
p103.save()
p104 = Prices(price=285,products_id = tequila,super_id=comercial)
p104.save()
p105 = Prices(price=274,products_id = tequila,super_id=heb)
p105.save()

p111 = Prices(price=39,products_id = vasos,super_id=walmart)
p111.save()
p112 = Prices(price=34,products_id = vasos,super_id=soriana)
p112.save()
p113 = Prices(price=37,products_id = vasos,super_id=superama)
p113.save()
p114 = Prices(price=35,products_id = vasos,super_id=comercial)
p114.save()
p115 = Prices(price=37,products_id = vasos,super_id=heb)
p115.save()

p121 = Prices(price=59,products_id = ping_pong,super_id=walmart)
p121.save()
p122 = Prices(price=54,products_id = ping_pong,super_id=soriana)
p122.save()
p123 = Prices(price=57,products_id = ping_pong,super_id=superama)
p123.save()
p124 = Prices(price=55,products_id = ping_pong,super_id=comercial)
p124.save()
p125 = Prices(price=57,products_id = ping_pong,super_id=heb)
p125.save()

p131 = Prices(price=349,products_id = vino,super_id=walmart)
p131.save()
p132 = Prices(price=394,products_id = vino,super_id=soriana)
p132.save()
p133 = Prices(price=379,products_id = vino,super_id=superama)
p133.save()
p134 = Prices(price=395,products_id = vino,super_id=comercial)
p134.save()
p135 = Prices(price=374,products_id = vino,super_id=heb)
p135.save()

p141 = Prices(price=69,products_id = queso,super_id=walmart)
p141.save()
p142 = Prices(price=64,products_id = queso,super_id=soriana)
p142.save()
p143 = Prices(price=67,products_id = queso,super_id=superama)
p143.save()
p144 = Prices(price=65,products_id = queso,super_id=comercial)
p144.save()
p145 = Prices(price=67,products_id = queso,super_id=heb)
p145.save()

p151 = Prices(price=129,products_id = copas,super_id=walmart)
p151.save()
p152 = Prices(price=144,products_id = copas,super_id=soriana)
p152.save()
p153 = Prices(price=129,products_id = copas,super_id=superama)
p153.save()
p154 = Prices(price=145,products_id = copas,super_id=comercial)
p154.save()
p155 = Prices(price=114,products_id = copas,super_id=heb)
p155.save()

p161 = Prices(price=159,products_id = cerveza,super_id=walmart)
p161.save()
p162 = Prices(price=134,products_id = cerveza,super_id=soriana)
p162.save()
p163 = Prices(price=129,products_id = cerveza,super_id=superama)
p163.save()
p164 = Prices(price=235,products_id = cerveza,super_id=comercial)
p164.save()
p165 = Prices(price=224,products_id = cerveza,super_id=heb)
p165.save()

p171 = Prices(price=55,products_id = cigarros,super_id=walmart)
p171.save()
p172 = Prices(price=59,products_id = cigarros,super_id=soriana)
p172.save()
p173 = Prices(price=56,products_id = cigarros,super_id=superama)
p173.save()
p174 = Prices(price=59,products_id = cigarros,super_id=comercial)
p174.save()
p175 = Prices(price=56,products_id = cigarros,super_id=heb)
p175.save()

p181 = Prices(price=39,products_id = papas,super_id=walmart)
p181.save()
p182 = Prices(price=24,products_id = papas,super_id=soriana)
p182.save()
p183 = Prices(price=17,products_id = papas,super_id=superama)
p183.save()
p184 = Prices(price=35,products_id = papas,super_id=comercial)
p184.save()
p185 = Prices(price=47,products_id = papas,super_id=heb)
p185.save()

p191 = Prices(price=79,products_id = jabon_polvo,super_id=walmart)
p191.save()
p192 = Prices(price=74,products_id = jabon_polvo,super_id=soriana)
p192.save()
p193 = Prices(price=74,products_id = jabon_polvo,super_id=superama)
p193.save()
p194 = Prices(price=75,products_id = jabon_polvo,super_id=comercial)
p194.save()
p195 = Prices(price=74,products_id = jabon_polvo,super_id=heb)
p195.save()

p201 = Prices(price=19,products_id = suero,super_id=walmart)
p201.save()
p202 = Prices(price=14,products_id = suero,super_id=soriana)
p202.save()
p203 = Prices(price=17,products_id = suero,super_id=superama)
p203.save()
p204 = Prices(price=15,products_id = suero,super_id=comercial)
p204.save()
p205 = Prices(price=17,products_id = suero,super_id=heb)
p205.save()

p211 = Prices(price=359,products_id = alitas,super_id=walmart)
p211.save()
p212 = Prices(price=374,products_id = alitas,super_id=soriana)
p212.save()
p213 = Prices(price=339,products_id = alitas,super_id=superama)
p213.save()
p214 = Prices(price=375,products_id = alitas,super_id=comercial)
p214.save()
p215 = Prices(price=334,products_id = alitas,super_id=heb)
p215.save()

p221 = Prices(price=89,products_id = shampoo,super_id=walmart)
p221.save()
p222 = Prices(price=84,products_id = shampoo,super_id=soriana)
p222.save()
p223 = Prices(price=84,products_id = shampoo,super_id=superama)
p223.save()
p224 = Prices(price=85,products_id = shampoo,super_id=comercial)
p224.save()
p225 = Prices(price=84,products_id = shampoo,super_id=heb)
p225.save()

p231 = Prices(price=79,products_id = jabon_barra,super_id=walmart)
p231.save()
p232 = Prices(price=74,products_id = jabon_barra,super_id=soriana)
p232.save()
p233 = Prices(price=73,products_id = jabon_barra,super_id=superama)
p233.save()
p234 = Prices(price=75,products_id = jabon_barra,super_id=comercial)
p234.save()
p235 = Prices(price=73,products_id = jabon_barra,super_id=heb)
p235.save()

p241 = Prices(price=119,products_id = pd,super_id=walmart)
p241.save()
p242 = Prices(price=114,products_id = pd,super_id=soriana)
p242.save()
p243 = Prices(price=139,products_id = pd,super_id=superama)
p243.save()
p244 = Prices(price=115,products_id = pd,super_id=comercial)
p244.save()
p245 = Prices(price=134,products_id = pd,super_id=heb)
p245.save()

p251 = Prices(price=89,products_id = lechen,super_id=walmart)
p251.save()
p252 = Prices(price=84,products_id = lechen,super_id=soriana)
p252.save()
p253 = Prices(price=88,products_id = lechen,super_id=superama)
p253.save()
p254 = Prices(price=85,products_id = lechen,super_id=comercial)
p254.save()
p255 = Prices(price=88,products_id = lechen,super_id=heb)
p255.save()

p261 = Prices(price=59,products_id = queson,super_id=walmart)
p261.save()
p262 = Prices(price=54,products_id = queson,super_id=soriana)
p262.save()
p263 = Prices(price=52,products_id = queson,super_id=superama)
p263.save()
p264 = Prices(price=55,products_id = queson,super_id=comercial)
p264.save()
p265 = Prices(price=52,products_id = queson,super_id=heb)
p265.save()

p271 = Prices(price=39,products_id = crema,super_id=walmart)
p271.save()
p272 = Prices(price=34,products_id = crema,super_id=soriana)
p272.save()
p273 = Prices(price=37,products_id = crema,super_id=superama)
p273.save()
p274 = Prices(price=35,products_id = crema,super_id=comercial)
p274.save()
p275 = Prices(price=37,products_id = crema,super_id=heb)
p275.save()

p281 = Prices(price=139,products_id = fit1,super_id=walmart)
p281.save()
p282 = Prices(price=134,products_id = fit1,super_id=soriana)
p282.save()
p283 = Prices(price=149,products_id = fit1,super_id=superama)
p283.save()
p284 = Prices(price=135,products_id = fit1,super_id=comercial)
p284.save()
p285 = Prices(price=144,products_id = fit1,super_id=heb)
p285.save()

p291 = Prices(price=49,products_id = fit2,super_id=walmart)
p291.save()
p292 = Prices(price=44,products_id = fit2,super_id=soriana)
p292.save()
p293 = Prices(price=43,products_id = fit2,super_id=superama)
p293.save()
p294 = Prices(price=45,products_id = fit2,super_id=comercial)
p294.save()
p295 = Prices(price=43,products_id = fit2,super_id=heb)
p295.save()

p301 = Prices(price=79,products_id = fit3,super_id=walmart)
p301.save()
p302 = Prices(price=74,products_id = fit3,super_id=soriana)
p302.save()
p303 = Prices(price=73,products_id = fit3,super_id=superama)
p303.save()
p304 = Prices(price=75,products_id = fit3,super_id=comercial)
p304.save()
p305 = Prices(price=73,products_id = fit3,super_id=heb)
p305.save()


query = input('Introduce un producto')
y = Prices.objects.filter(products_id__product_name__contains = query)