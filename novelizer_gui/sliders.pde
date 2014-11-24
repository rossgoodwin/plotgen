int sliX = 860;
int sliY = 155;
int sliSpace = 70;

Slider passionSlider = new Slider(sliX, sliY, "PASSION", "detatched", "passionate");
Slider verbositySlider = new Slider(sliX, sliY+sliSpace, "VERBOSITY", "concise", "verbose");
Slider realismSlider = new Slider(sliX, sliY+sliSpace*2, "REALISM", "surreal", "real");
Slider lengthSlider = new Slider(sliX, sliY+sliSpace*3, "LENGTH", "brief", "epic");
Slider charCountSlider = new Slider(sliX, sliY+sliSpace*4, "CHARACTER COUNT", "few", "many");
Slider densitySlider = new Slider(sliX, sliY+sliSpace*5, "DENSITY", "sparse", "dense");
Slider accessibilitySlider = new Slider(sliX, sliY+sliSpace*6, "ACCESSIBILITY", "inaccessible", "accessible");
Slider depravitySlider = new Slider(sliX, sliY+sliSpace*7, "DEPRAVITY", "benign", "depraved");
Slider linearitySlider = new Slider(sliX, sliY+sliSpace*8, "LINEARITY", "nonlinear", "linear");

Slider[] sliders = {passionSlider, verbositySlider, verbositySlider, realismSlider, lengthSlider, charCountSlider, densitySlider, accessibilitySlider, depravitySlider, linearitySlider};

class Slider {
  
  PVector linePos, boxPos;
  int lineLength, boxW, boxH;
  String labelC, labelL, labelR;
  color lineCol, activeCol, staticCol, shadowCol;
  boolean active;
  Slider (int linePosX, int linePosY, String _labelC, String _labelL, String _labelR) {
    linePos = new PVector(linePosX, linePosY);
    lineLength = 300;
    boxW = 10;
    boxH = 20;
    boxPos = new PVector(linePos.x+lineLength/2, linePos.y); 
    labelC = _labelC;
    labelL = _labelL;
    labelR = _labelR;
    lineCol = color(0);
    activeCol = color(245, 215, 110);
    staticCol = color(144, 198, 149);
    shadowCol = color(0, 20);
    active = false;
  }
  
  void display() {
    // draw the line
    stroke(lineCol);
    strokeWeight(2);
    line(linePos.x, linePos.y, linePos.x+lineLength, linePos.y);
    strokeWeight(1);
    
    // draw the labels
    textFont(gothamNarrow16);
    textAlign(LEFT, BOTTOM);
    fill(108, 122, 137);
    noStroke();
    text(labelC, linePos.x, linePos.y-2);
    
    textAlign(CENTER, TOP);
    text(labelL, linePos.x, linePos.y+3);
    text(labelR, linePos.x+lineLength, linePos.y+3);
    
    // draw the box
    noStroke();
    rectMode(CENTER);
    if (active) {
      fill(activeCol);
    } else {
      fill(staticCol);
    }
    rect(boxPos.x, boxPos.y, boxW, boxH);
    
    fill(shadowCol);
    rect(boxPos.x, boxPos.y+boxH/2-1, boxW, 2);
    
  }
  
}
