TextInput titleInput = new TextInput(50, 100, "story title", 700);
TextInput firstNameInput = new TextInput(50, 160, "first name", 345);
TextInput surnameInput = new TextInput(405, 160, "last name", 345);
TextInput emailInput = new TextInput(50, 220, "email address", 700);

TextInput[] inputFields = {titleInput, firstNameInput, surnameInput, emailInput};

class TextInput {
  
  PVector pos, widthHeight;
  color borderCol, activeCol, textCol, initTextCol, bgCol;
  String initText, userText;
  boolean active, filled;
  
  TextInput (float xPos, float yPos, String _initText, float wid) {
    pos = new PVector(xPos, yPos);
    widthHeight = new PVector(wid, 50);
    
    borderCol = color(108, 122, 137);
    activeCol = color(231, 76, 60);
    textCol = color(108, 122, 137);
    initTextCol = color(191, 191, 191);
    bgCol = color(236, 236, 236);
    
    initText = _initText;
    userText = "";
    
    active = false;
    filled = false;
  }
  
  void displayBox() {
    fill(bgCol);
    if (active) {
      stroke(activeCol);
    } else {
      stroke(borderCol);
    }
    rectMode(CORNER);
    rect(pos.x, pos.y, widthHeight.x, widthHeight.y);
  }
  
  void displayText() {
    textFont(gotham18);
    textAlign(LEFT, CENTER);
    noStroke();
    if (active || filled) {
      fill(textCol);
      text(userText, pos.x+10, pos.y+(widthHeight.y/2));
    } else {
      fill(initTextCol);
      text(initText, pos.x+10, pos.y+(widthHeight.y/2));
    }
  }
  
  void display() {
    displayBox();
    displayText();
  }
  
}
