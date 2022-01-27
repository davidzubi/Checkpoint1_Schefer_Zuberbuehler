# Schiebereglerfunktion von Simon Hefti übernommen
# pointerPos (Integer): Position des Pointers in Pixeln
# pointerVal (Float):   Eingestellter Wert (0 - 100)
movingMode = False
pointerPos = 0
pointerVal = 1.0
a = 1


# Initialisierung
def setup():
    size(900, 900)
    textSize(30)
    textAlign(CENTER)
    global img
    global img1
    global img2
    global img3
    global img4
    global img5
#Bilder aus dem Ordner "data" laden
    img = loadImage ("fest1.jpg")
    img1 = loadImage ("fluessig1.jpg")
    img2 = loadImage ("gas1.jpg")
    img3 = loadImage ("fest2.jpg")
    img4 = loadImage ("fluessig2.jpg")
    img5 = loadImage ("gas2.jpg")
    
   # if mouseX in range(50,700) and mouseY in range(700,750) and mousePressed == True:
    #    a = -a
        
    
# Sich wiederholende draw() Funktion
def draw():
    
        
    background(255)
    draw_ruler(200, 800, 500)
    rect (50, 700, 50, 50)
#Titel bei jedem Bereich vorhanden
    text (" Aggregatzustaende", width/2, 60)
    text (" Temperatur:", 130, 650)
#Bereich in dem jeweils das passende Bild und der Text definiert wird.        
    if a == 1:
        text (" Wasser", 160, 740)
        if pointerVal/20 < 2:
            text (str(pointerVal/20) +" Grad Celsius", width/2, height=650)
            text (" fest", width/2, height=720)
            image (img3, 100, 100)
        if 1 < pointerVal/20 < 100:
            text (str(pointerVal/20) +" Grad Celsius", width/2, height=650)
            text (" fluessig", width/2, height=720)
            image (img4, 100, 100)
        if pointerVal/20 > 99:
            text (str(pointerVal/20) +" Grad Celsius", width/2, height=650)
            text (" gasfoermig", width/2, height=720)
            image (img5, 100, 100)
    
    if a == -1:
        text (" Blei", 160, 740)
        if pointerVal < 327:
            text (str(pointerVal) +" Grad Celsius", width/2, height=650)
            text (" fest", width/2, height=720)
            image (img, 100, 100)
        if 327 < pointerVal < 1749:
            text (str(pointerVal) +" Grad Celsius", width/2, height=650)
            text (" fluessig", width/2, height=720)
            image (img1, 100, 100)
        if pointerVal > 1749:
            text (str(pointerVal) +" Grad Celsius", width/2, height=650)
            text (" gasfoermig", width/2, height=720)
            image (img2, 100, 100)
            

    

    
# Funktion: Schieberegler generieren
# objX:      X-Position des Reglers
# objY:      Y-Position des Reglers
# objLength: Länge des Reglers
def draw_ruler(objX, objY, objLength):
    global movingMode
    global pointerPos
    global pointerVal
    
    # Schieber einstellen
    pointerRadius = 24
    if pointerPos == 0:
        pointerPos = objX
    
    # Linie zeichnen
    fill(85)
    strokeWeight(6)
    line(objX, objY, objX + objLength, objY)
    fill(185)
    strokeWeight(2)
    
    # Überprüfen ob Schieber angeklickt worden ist --> Bewegungsmodus aktivieren
    if mouseX > pointerPos - pointerRadius and mouseX < pointerPos + pointerRadius and mouseY > objY - pointerRadius and mouseY < objY + pointerRadius and mousePressed == True:
        movingMode = True
    
    # Wenn keine Maustaste gedrückt ist --> Bewegungsmodus deaktivieren
    if mousePressed == False:
        movingMode = False
        cursor(ARROW)
    
    # Bei aktiviertem Bewegungsmodus
    if movingMode == True:
        cursor(HAND)
        
        # Schieber der Line entlang bewegen
        if mouseX > objX and mouseX < objX + objLength:
            pointerPos = mouseX
        
        # Wenn Maus ausserhalb der Linie, Schieber am Start oder Ende fixieren
        else:
            if mouseX < objX:
                pointerPos = objX
            if mouseX > objX:
                pointerPos = objX + objLength

    # Schieber zeichnen            
    circle(pointerPos, objY, pointerRadius)
    
    # Eingestellter Wert anhand der Schieberposition ermitteln
    pointerVal = int(2000 / float(objLength) * (pointerPos - objX))

def mouseReleased(): 
    global a
    if mouseX in range(50,100) and mouseY in range(700,750):
        a = -a



    
