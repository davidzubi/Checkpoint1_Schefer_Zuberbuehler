
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
    
    
# Sich wiederholende draw() Funktion
def draw():
    background(255)
    draw_ruler(200, 800, 500)
    text(str(pointerVal) + " Grad Celsisus", width/2, height=700)
        
    
    
    circle(210, 410, 30)
    circle(240, 410, 30)
    circle(270, 410, 30)
    circle(300, 410, 30)
    circle(330, 410, 30)
    circle(360, 410, 30)
    circle(390, 410, 30)
    circle(420, 410, 30)
    circle(210, 440, 30)
    circle(240, 440, 30)
    circle(270, 440, 30)
    circle(300, 440, 30)
    circle(330, 440, 30)
    circle(360, 440, 30)
    circle(390, 440, 30)
    circle(420, 440, 30)
    circle(210, 470, 30)
    circle(240, 470, 30)
    circle(270, 470, 30)
    circle(300, 470, 30)
    circle(330, 470, 30)
    circle(360, 470, 30)
    circle(390, 470, 30)
    circle(420, 470, 30)


    line(70, 120, 70, 500)
    line(550, 120, 550, 500)
    line(70, 500, 550, 500)

    
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
    pointerVal = int(100 / float(objLength) * (pointerPos - objX))
