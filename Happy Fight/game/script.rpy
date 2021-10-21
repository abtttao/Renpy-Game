# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the

# name of the character.
define e = Character("พี่สาว", color="#FF64E1")
define m = Character("ต้น", color="#17AAFF")
define f = Character("เพื่อน", color="#c5c8ff")
define g = Character("???", color="#898989", image="shadow")
define h = Character("ภูติแมว แฮปปี้", color="#FFD240" ,image="happy")
define d = Character("ปีศาจ", color="#9110DC", image="demon")
default score = 0

# Side images
image battle_bg = Solid("#c5c8ff")
image side happy = "side happy.png"   
image side demon = "side demon.png"   

image side happy = Transform("side happy.png", xalign = -0.068, yalign = 1.0)
image side shadow = Transform("side shadow.png", xalign = 0.0, yalign = 1.0)
image side demon = Transform("side demon.png", xalign = -0.035, yalign = 1.0)

#Happy idel
image player happy idle:
    "happy 2"
    pause .2
    "happy 1"
    pause .2
    repeat

# Demon idle
image player demon idle:
    "demon 1"
    pause .2
    "demon 2"
    pause .2
    repeat

# The game starts here.

label start:
    play sound "audio/bensound-memories.mp3"

    scene bg room
    "กร๊อก กร๊อก เปิดประตูให้พี่หน่อย"
    "ครับ ครับ มาแล้วครับ"
    show pee need help
    e "ไปซื้อปลาให้พี่หน่อย แปบนึงได้ไหม"
    menu :
        "ครับ กำลังว่างอยู่พอดี":
            jump go   
        "ไม่ว่างครับ!":
            jump dontGo

label go :
    scene bg room
    show pee happy
    e "โอเคแล้วรีบๆกลับมานะ"

    scene bg town
    "ในขณะที่คุณกำลังซื้อน้ำปลากลับบ้านนั้น"
    show motorcycle
    "รถของคุณก็เกิดเสียกะทันหัน และเพื่อนของคุณก็ผ่านมาพอดี"

    scene bg meadow
    show  friend ton
    f "ต้น รถเป็นเป็นอะไรอะ"

    menu :
          "รถเสียสตาร์ทไม่ติดเลยอ่ะ":
            jump friend
           
          "อ่อ ไม่มีอะไร เราจอดรถเล่น":
            jump dontHave

label dontHave :
    scene bg bedroom sister
    show pee nomal
    e "เมื่อไหร่ต้นจะกลับมาสักทีนะ!"
    e "งั้นเราไปเตรียมอาหารรอที่ห้องครัวดีกว่า"
    scene bg chicken room2
    show pee nomal
    "ในขณที่พี่สาวกำลังทำอาหารเย็น รอน้องชายนั้น"
    "ปัง!!"
    e "นี่มันอะไรกัน ช่วยด้วย!"
    jump goback

label dontGo :
    scene bg town
    show pee angry
    e "ถ้าไม่ไป ฉันจะโทรไปฟ้องแม่ว่าแกแอบเล่นเกมตอนเรียนออนไลน์"
    m "ไม่ได้นะ งั้นไปก็ได้ครับพี่"
    jump go  

label friend :
    scene bg meadow
    show  friend ton
    f "ทำไมไม่ใช้น้ำมัน 2T ดีดีล่ะ เดี๋ยวนี้เขาใช้แต่ไดเกียวกันทั้งนั้นแหละ... เพราะใช้แล้ว"
    f "เครื่องฟิต สตาร์ทติดง่าย"
    m "โอเค ขอบคุณนะ เดี๋ยวเราจะไปลองใช้ดู"
    jump goback

label goback:
    scene bg house
    m "กลับมาแล้วครับพี่"
    m "ซื้อปลามาให้แล้วนะครับ อยู่ไหนครับ"

    "ไม่มีเสียงตอบรับกลับมา"

    menu :
        "ตามหาพี่":
            jump find
           
        "เอาปลาไปไว้ที่ห้องครัว":
            jump chickenroom

label find :
    scene bg house
    call screen houseMap

label playingroom :
    hide screen houseMap
    scene bg playing room
    "......"
    "ไม่มีคนอยู่เลยไปห้องอื่นกันเถอะ"
    call screen houseMap

label bathroom :
    hide screen houseMap
    scene bg bath room
    "......"
    "ไม่มีคนอยู่เลยไปห้องอื่นกันเถอะ"
    call screen houseMap

label bedroomsister:
    hide screen houseMap
    scene bg bedroom sister
    "......"
    "ไม่มีคนอยู่เลยไปห้องอื่นกันเถอะ"
    call screen houseMap

label myroom :
    hide screen houseMap
    scene bg room
    "......"
    "ไม่มีคนอยู่เลยไปห้องอื่นกันเถอะ"
    call screen houseMap

label chickenroom :
    hide screen houseMap
    scene bg chicken room
    "......"
    "เกิดอะไรขึ้นกับที่นี้กัน"
    g "ช่วยด้วย...."
    g "ช่วยข้าด้วย...."

    "จู่ๆ คุณก็ได้ยินเสียงขอความช่วยเหลือดังขึ้นมา"
    m "ใครนะ เสียงใคร"
    g "ข้าหิวเหลือเกินช่วยด้วย ขออาหารหน่อย"

    menu :
        "ส่งปลาให้":
            jump helpsis
           
        "วิ่งหนี":
            jump run
   
label run:
    scene bg chicken room
    g "เดี๋ยวก่อนสิ ฉันไม่ใช้แมวที่ไม่ดีหรอกนะ"
    m "แมว?"
    g "ถ้าหากเจ้ายอมช่วยข้า หาอาหารให้ ข้าจะยอมบอกเรื่องพี่สาวของเจ้า"
    "คุณไม่มีทางเลือกอื่น จึงต้องยอมช่วยแมว เพื่อตามหาพี่สาวของคุณ"
    jump helpsis

label helpsis:
    scene bg chicken room
    show happy eat
    g "ขอบคุณสำหรับ อาหารนะถ้าไม่ได้เจ้า ข้าคงจะหมดแรงไม่มีพลังไปตามเจ้าปีศาจนั้นต่อ"
    m "ปีศาจ?"
    m "เจ้าเป็นใครกัน? แมว? หรือว่าปีศาจ?"
    show happy n
    h "อะแฮ่ม ขอโทษที่เสียมารยาท ข้าคือ Happy เป็นภูติแมว ที่กำลังตามล่าปีศาจที่ชอบจับตัวผู้หญิงไปเป็นทาสตัวเองอยู่"
    h "ข้าไล่ตามหา มันมานานแล้ว 7 วันข้าไม่ได้กินอะไรเลยจนพบว่ามันมาโผล่ที่บ้านหลังขณะที่ข้ากำลังต่อสู้กับมัน ก็เกิดหน้ามืดเพราะหมดแรง จนมันจับตัวพี่สาวเจ้าแหละหนีไปได้"
    m "ไม่นะ พี่เราถูกปีศาจจับตัวไปงั้นหรอ"
    h "ไม่เป้นไร ตอนนี้ข้ารู้ที่อยู่ของมันแล้ว งั้นเราไปช่วยพี่สาวเจ้ากันเถอะ"
    h "ก่อนอื่นเรามาดับไฟห้องนี้กันก่อนเถอะ"
    "ห้องครัวที่พังและไฟไหม้ได้กลับมาเป็นเหมือนเดิม"
    h "นี่ไง"
    scene bg chicken room2
    h "ทีนี้เราก็ไปด้วยพี่สาวเจ้ากันเถอะ"
    h "จงเปิดออกประตูมิติ"
    scene bg chicken room3
    show c happy fly
    h "ไปกันเถอะ"
    m "ได้เลย รอก่อนนะพี่"
    scene bg demon
    m "ที่นี้ที่ไหนกัน ทำไมไม่เคยเห็นมาก่อนเลย ปราสาทในป่างั้นหรอ"
    "กรี้ดดดดดด ช่วยด้วย ช่วยฉันด้วย"
    m "พี่! เสียงมาจากด้านหลังปราสาทนั้น"
    scene bg pool
    m "นี่มันอะไรกัน ปาร์ตี้ริมสระงั้นหรอ"
    e "ช่วยพี่ด้วย"
    scene bg help20
    "ท่านได้โปรดช่วยพวกเราด้วย"
    scene bg pool
    play sound "audio/bensound-extremeaction.mp3"
    show c demon

    "ตามาจนได้สินะ เจ้าภูติแมวน่ารำคาน"
    h "วันนี้แหละเจ้าไม่รอดแน่ ข้าจะกำจัดเจ้าซะที่นี้เลย"
    d "ไม่มีทาง พวกผู้หญิงทั้ง 20 คน ต้องอยู่ที่นี้เป้นทาสของฉันตลอดไป ฮ่าๆ"
    h "ข้าจะฆ่าเอง และช่วยพวกผู้หญิงทั้งหมดทุกคนกลับบ้าน"
    d "ทำมาพูดเป็นฮีโร่ ไปคุยกับรากมะม่วงซะเถอะแก ไอ้แมวกระจอก"
    jump fight
 
label fight:
    scene bg pool

    #dffffffff
    show player demon idle:
        xalign 0.8 yalign 0.25
        zoom 0.8
    d "วันนี้แหละ ข้าจะฆ่าเจ้าให้ตาย จะได้เลิกตามข้าสักที"
    #ddddddddddd
    show player happy idle:
        xalign 0.15 yalign 0.30
        zoom 1.0
    h "ถ้าคิดว่าทำได้ก็เข้ามาสิ"

    jump battle

label battle:

    scene bg pool
    
    show player demon idle:
        xalign 0.8 yalign 0.25
        zoom 0.8

    "ปีศาจ มีจุดอ่อนที่กลางหน้าอก ท่านจะเลือกโจมตีที่ตำแหน่งใด"

    menu :
        "หน้าอก":
            $score +=1
            jump battle2
           
        "ขา":
            $score -=1
            jump battle2

label battle2:

    scene bg pool
    show player happy idle:
        xalign 0.15 yalign 0.30
        zoom 1.0

    "ท่านภูติแฮปปี้ได้บาดเจ็บจากการถูกโจมตี ท่านจะทำอย่างไร"

    menu :
        "วิ่งหน้าจากการต่อสู้":
            $score -=1
            jump battle3
           
        "ช่วยเหลือ ท่านภูติแฮปปี้":
            $score +=1
            jump battle3

label battle3:

    scene bg pool
    show player demon idle:
        xalign 0.8 yalign 0.25
        zoom 0.8

    "หลังจากต่อสู้มาเนินนาน ปีศาจได้บาดเจ็บและเริ่มหมดแรง ท่านจะทำอย่างไร"

    menu :
        "ใช้จังหวะนี้โจมตี และฆ่าปีศาจ":
            $score +=1
            jump bye
           
        "หนีไป":
            $score -=1
            jump bye

label bye:
    if score > 2:
        scene bg help20
        "คุณชนะ"
        "ปีศาจ ได้แพ้การต่อสู้และตายไปแล้ว"
        "ขอบพวกท่านที่ช่วยพวกเรา พวกเราจะตอบแทนท่านให้มีความสุขเอง"
    else:
        scene bg pool
        show player demon idle:
            xalign 0.8 yalign 0.25
            zoom 0.8
        "ไปตายซะ เจ้าแมวเขลา ตายซะ!"
    
    return

