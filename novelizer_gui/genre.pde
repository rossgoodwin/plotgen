int butX = 85;
int butY = 350;

GenreButton literaryButton = new GenreButton(butX, butY, "LITERARY");
GenreButton scifiButton = new GenreButton(butX+80, butY, "SCI-FI");
GenreButton fantasyButton = new GenreButton(butX+80*2, butY, "FANTASY");
GenreButton historicalButton = new GenreButton(butX+80*3, butY, "HISTORY");
GenreButton romanceButton = new GenreButton(butX+80*4, butY, "ROMANCE");
GenreButton thrillerButton = new GenreButton(butX+80*5, butY, "THRILLER");
GenreButton mysteryButton = new GenreButton(butX, butY+80, "MYSTERY");
GenreButton crimeButton = new GenreButton(butX+80, butY+80, "CRIME");
GenreButton pulpButton = new GenreButton(butX+80*2, butY+80, "PULP");
GenreButton horrorButton = new GenreButton(butX+80*3, butY+80, "HORROR");
GenreButton beatButton = new GenreButton(butX+80*4, butY+80, "BEAT");
GenreButton fanButton = new GenreButton(butX+80*5, butY+80, "FAN");
GenreButton westernButton = new GenreButton(butX, butY+80*2, "WESTERN");
GenreButton actionButton = new GenreButton(butX+80, butY+80*2, "ACTION");
GenreButton warButton = new GenreButton(butX+80*2, butY+80*2, "WAR");
GenreButton familyButton = new GenreButton(butX+80*3, butY+80*2, "FAMILY");
GenreButton humorButton = new GenreButton(butX+80*4, butY+80*2, "HUMOR");
GenreButton sportButton = new GenreButton(butX+80*5, butY+80*2, "SPORT");

GenreButton[] genreButtons = {literaryButton, scifiButton, fantasyButton, historicalButton, romanceButton, thrillerButton, mysteryButton, crimeButton, pulpButton, horrorButton, beatButton, fanButton, westernButton, actionButton, warButton, familyButton, humorButton, sportButton };

int conX = 85;
int conY = 625;

GenreButton natureButton = new GenreButton(conX, conY, "NATURE");
GenreButton manButton = new GenreButton(conX+80, conY, "MAN");
GenreButton godButton = new GenreButton(conX+80*2, conY, "GOD");
GenreButton societyButton = new GenreButton(conX+80*3, conY, "SOCIETY");
GenreButton selfButton = new GenreButton(conX+80*4, conY, "SELF");

GenreButton fateButton = new GenreButton(conX, conY+80, "FATE");
GenreButton techButton = new GenreButton(conX+80, conY+80, "TECH");
GenreButton nogodButton = new GenreButton(conX+80*2, conY+80, "NO GOD");
GenreButton realityButton = new GenreButton(conX+80*3, conY+80, "REALITY");
GenreButton authorButton = new GenreButton(conX+80*4, conY+80, "AUTHOR");

GenreButton[] conflictButtons = {natureButton, manButton, godButton, societyButton, selfButton, fateButton, techButton, nogodButton, realityButton, authorButton};

int narX = butX+80*6+40;
int narY = butY;

GenreButton firstButton = new GenreButton(narX, narY, "FIRST");
GenreButton alternateButton = new GenreButton(narX+80, narY, "ALT");
GenreButton thirdSubOmnButton = new GenreButton(narX, narY+80, "THIRD\nSUB/OMN");
GenreButton thirdObjOmnButton = new GenreButton(narX+80, narY+80, "THIRD\nOBJ/OMN");
GenreButton thirdSubLimButton = new GenreButton(narX, narY+80*2, "THIRD\nSUB/LIM");
GenreButton thirdObjLimButton = new GenreButton(narX+80, narY+80*2, "THIRD\nOBJ/LIM");

GenreButton[] narrButtons = {firstButton, alternateButton, thirdSubOmnButton, thirdObjOmnButton, thirdSubLimButton, thirdObjLimButton};


class GenreButton {
  
  PVector pos;
  int widthHeight;
  String label;
  color textCol, buttonCol, activeCol, shadowCol;
  boolean pressed;
  GenreButton (float xPos, float yPos, String _label) {
    pos = new PVector(xPos, yPos);
    widthHeight = 70;
    label = _label;
    textCol = color(255, 255, 255);
    buttonCol = color(144, 198, 149);
    activeCol = color(245, 215, 110);
    shadowCol = color(0, 20);
    pressed = false;
  }
  
  void display() {
    noStroke();
    
    if (pressed) {
      fill(activeCol);
    } else {
      fill(buttonCol);
    }
    
    rectMode(CENTER);
    rect(pos.x, pos.y, widthHeight, widthHeight);
    
    fill(textCol);
    textFont(gothamNarrow16);
    textAlign(CENTER, CENTER);
    text(label, pos.x, pos.y);
    
    if (pressed) {
      
      fill(shadowCol);
      rect(pos.x, pos.y, widthHeight, widthHeight);
      
    } else {
      
      fill(shadowCol);
      rect(pos.x, pos.y+32, widthHeight, 6);
      
    }
    
  }
  
}
