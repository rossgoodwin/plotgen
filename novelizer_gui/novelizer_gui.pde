// FICTION GENERATOR BY ROSS GOODWIN
// http://rossgoodwin.com/ficgen


// paths and such
String sysPath = "/Users/rg/Projects/plotgen/new/plotgen/";
String novPath = "/Users/rg/Google Drive/novels/";
String novelTitle = "You Forgot To Write A Title";
String firstName = "John";
String lastName = "Doe";
String toEmail = "ross.goodwin@gmail.com";
boolean finished = false;

// time to go!
int beepBeep;

// fonts
PFont gotham32;
PFont gotham18;


// GUI Elements
PVector title;

PVector generateButton;
PShape generateSymbol;

void setup() {
  size(displayWidth, displayHeight);
  gotham32 = loadFont("Gotham-Book-32.vlw");
  gotham18 = loadFont("Gotham-Book-18.vlw");
  
  title = new PVector(width/2, 50);
  
  generateButton = new PVector(width/2, height-100);
  generateSymbol = loadShape("generate_symbol.svg");
  
}

void draw() {
  // set values equal to userText variables
  if (titleInput.filled) novelTitle = titleInput.userText;
  if (firstNameInput.filled) firstName = firstNameInput.userText;
  if (surnameInput.filled) lastName = surnameInput.userText;
  if (emailInput.filled) toEmail = emailInput.userText;
  
  // background
  background(236, 240, 241);
  
  // headline and border
  textFont(gotham32);
  textAlign(CENTER, TOP);
  fill(108, 122, 137);
  noStroke();
  text("FICTION GENERATOR", title.x, title.y);
  
  // text input boxes
  titleInput.display();
  firstNameInput.display();
  surnameInput.display();
  emailInput.display();
  
  // generate button
  noStroke();
  fill(231, 76, 60);
  rectMode(CENTER);
  rect(generateButton.x, generateButton.y, 100, 100);
  
  shapeMode(CENTER);
  fill(255);
  noStroke();
  shape(generateSymbol, generateButton.x, generateButton.y-3, 65, 65);
  
  if (finished) {
    fill(0, 20);
    rectMode(CENTER);
    rect(generateButton.x, generateButton.y, 100, 100);
  } else {
    fill(0, 20);
    rectMode(CENTER);
    rect(generateButton.x, generateButton.y+45, 100, 10);
  }
  
  
  
  // textFont(gotham18);
  // textAlign(CENTER, CENTER);
  // fill(255);
  // noStroke();
  // text("", generateButton.x, generateButton.y-3);
  
  
  
  if (finished && frameCount >= beepBeep) {
    // filenames
    String pdfName = novelTitle + ".pdf";
    String auxName = novelTitle + ".aux";
    String logName = novelTitle + ".log";
    String outName = novelTitle + ".out";
    
    // take out the trash (remove log files)
    String[] paramsRm = {"rm", auxName, logName, outName};
    exec(paramsRm);
    
    // move the cargo (novelTitle.pdf goes to Google Drive/novels/)
    String[] paramsMv = {"mv", pdfName, novPath};
    exec(paramsMv);
    
    // open the PDF
    open(novPath+pdfName);
    
    // send email
    String[] paramsNovel = {"python", sysPath+"sendnovel.py", toEmail, novPath+pdfName};
    exec(paramsNovel);
    
    // speak
    String talk = "Thanks for the inspiration, " + firstName + ". I just wrote your story, and I think it's a real page turner. No spoilers though. You'll have to read it for yourself. I sent you the PDF. Enjoy!";
    String[] paramsSay = {"say", talk};
    exec(paramsSay);
    
    // set finished boolean to false (so that it doesn't keep running this part)
    finished = false;
  }
}

void mousePressed() {
  
  if (mouseX > generateButton.x-50 && mouseX < generateButton.x+50 && mouseY > generateButton.y-50 && mouseY < generateButton.y+50) {
  
    beepBeep = frameCount + int(frameRate*6);
  
    String novelFile = sysPath + "output/" + novelTitle + ".tex";
    
    String[] paramsNovel = {"python", sysPath+"novelizer_icm.py", novelTitle, firstName+" "+lastName};
    exec(paramsNovel);
    
    String[] paramsPDF = {"/usr/texbin/pdflatex", novelFile};
    exec(paramsPDF);
    
    finished = true;
  }
  
  for (int i=0; i<inputFields.length; i++) {
    if (mouseX > inputFields[i].pos.x && mouseX < inputFields[i].pos.x+inputFields[i].widthHeight.x && mouseY > inputFields[i].pos.y && mouseY < inputFields[i].pos.y+inputFields[i].widthHeight.y) {
      inputFields[i].active = true;
      inputFields[i].filled = true;
    } else {
      inputFields[i].active = false;
    }
  }
  
}

void keyPressed() {
  
  for (int i=3; i>=0; i--) {
    if (inputFields[i].active) {
      if (key == 8 && inputFields[i].userText != "") {
        inputFields[i].userText = inputFields[i].userText.substring(0, inputFields[i].userText.length()-1);
      } else if (key == '\n' || key == '\t') {
        inputFields[i].active = false;
        if (i < inputFields.length-1) {
          inputFields[i+1].active = true;
          inputFields[i+1].filled = true;
        }
      } else if (key != CODED) {
        inputFields[i].userText = inputFields[i].userText + key;
      }
    }
  }
  
}
