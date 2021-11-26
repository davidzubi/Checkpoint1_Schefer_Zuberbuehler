
# pointerPos (Integer): Position des Pointers in Pixeln
# pointerVal (Float):   Eingestellter Wert (0 - 100)
movingMode = False
pointerPos = 0
pointerVal = 1.0

# Initialisierung
def setup():
    size(900, 900)
    textSize(64)
    textAlign(CENTER)
    global img
    global img1
    global img2
    img = loadImage ("fest.jpg")
    img1 = loadImage ("fluessig.jpg")
    img2 = loadImage ("gas.jpg")
    
    
# Sich wiederholende draw() Funktion
def draw():
    background(255)
    draw_ruler(200, 800, 500)
    if pointerVal == 0:
        text (" fest", width/2, height=700)
    if pointerVal == 1:
        text (" fluessig", width/2, height=700)
    if pointerVal == 2:
        text (" gasfoermig", width/2, height=700)
    global img
    global img1
    global img2
    if pointerVal == 0:
        image (img, 100, 20)
    if pointerVal == 1:
        image (img1, 100, 20)
    if pointerVal == 2:
        image (img2, 100, 20)
     
    
    

    
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
    pointerVal = int(2 / float(objLength) * (pointerPos - objX))

    
